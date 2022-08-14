from src.util.google_cloud import upload_file, get_file
from src.dataaccess import document as document_data_access, image as image_data_access
from src.config.enum import STATUS, BUCKET_NAMES
from src.util.name_setter import get_random_name


# todo
def remove_noise(file_obj):
    return file_obj


class NoiseRemoval(object):
    def __init__(self, name):
        self.name = name

    @staticmethod
    async def run():
        while True:
            next_files = await document_data_access.fetch_by_status(STATUS["CONVERTED"])
            if len(next_files) <= 0:
                continue
            next_file = next_files[0]
            images = await image_data_access.fetch_by_file_key(next_file.fileKey)
            for image in images:
                file_obj = get_file(name=image.name, bucket_name=image.bucketName)
                removed_noise_file_obj = remove_noise(file_obj)
                name = get_random_name(15) + ".png"
                bucket_name = BUCKET_NAMES["REMOVED_NOISE"]
                image.noiseRemovedBucketName = bucket_name
                image.noiseRemovedName = name
                image.status = STATUS["REMOVED_NOISE"]
                upload_file(name, bucket_name, removed_noise_file_obj)
                _ = await image_data_access.insert_and_update(image, "update")

            next_file.status = STATUS["REMOVED_NOISE"]
            _ = await document_data_access.insert_and_update(next_file, "update")


noise_removal = NoiseRemoval("noise")
noise_removal.run()
