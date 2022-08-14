from src.util.google_cloud import get_file
from src.dataaccess import document as document_data_access, image as image_data_access
from src.config.enum import STATUS


def get_ocr(file_obj):
    return file_obj


class NoiseRemoval(object):
    def __init__(self, name):
        self.name = name

    @staticmethod
    async def run():
        while True:
            next_files = await document_data_access.fetch_by_status(STATUS["REMOVED_NOISE"])
            if len(next_files) <= 0:
                continue
            next_file = next_files[0]
            images = await image_data_access.fetch_by_file_key(next_file.fileKey)
            for image in images:
                file_obj = get_file(name=image.noiseRemovedName, bucket_name=image.noiseRemovedBucketName)
                text = get_ocr(file_obj)
                image.result = text
                image.status = STATUS["OCR"]
                _ = await image_data_access.insert_and_update(image, "update")

            next_file.status = STATUS["OCR"]
            _ = await document_data_access.insert_and_update(next_file, "update")


noise_removal = NoiseRemoval("noise")
noise_removal.run()
