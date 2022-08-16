from src.dataaccess import document as document_data_access, image as image_data_access
from src.config.enum import STATUS


class Finalizer(object):
    def __init__(self, name):
        self.name = name

    @staticmethod
    async def run():
        while True:
            next_files = await document_data_access.fetch_by_status(STATUS["OCR"])
            if len(next_files) <= 0:
                continue
            next_file = next_files[0]
            images = await image_data_access.fetch_by_file_key(next_file.fileKey)
            result = ""
            for image in images:
                result = result + " " + image.result
                image.status = STATUS["FINISHED"]
                _ = await image_data_access.update(image)

            next_file.status = STATUS["FINISHED"]
            next_file.result = result
            _ = await document_data_access.update(next_file)
