from src.util.google_cloud import get_gcs_url, get_text
from src.dataaccess import document as document_data_access, image as image_data_access
from src.config.enum import STATUS, BUCKET_NAMES
from src.util.name_setter import get_random_name


# todo amin
def get_ocr(file_name, bucket_name, destination_file_name, destination_bucket_name):
    source_url = get_gcs_url(bucket_name, file_name)
    destination_url = get_gcs_url(destination_bucket_name, destination_file_name)
    return get_text(source_url, destination_url)


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
                name = get_random_name(15) + ".json"
                bucket_name = BUCKET_NAMES["OCR"]
                image.noiseRemovedBucketName = bucket_name
                image.noiseRemovedName = name
                text = get_ocr(image.noiseRemovedName, image.noiseRemovedBucketName)
                image.result = text
                image.status = STATUS["OCR"]
                _ = await image_data_access.insert_and_update(image, "update")

            next_file.status = STATUS["OCR"]
            _ = await document_data_access.insert_and_update(next_file, "update")


noise_removal = NoiseRemoval("noise")
noise_removal.run()
