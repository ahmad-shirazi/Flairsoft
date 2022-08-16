from src.util.google_cloud import upload_file, get_file
from src.dataaccess import document as document_data_access, image as image_data_access
from src.config.enum import STATUS, BUCKET_NAMES
from src.config.file import TEMP_FOLDER
from src.util.name_setter import get_random_name


# todo ahmad
def remove_noise(file_url):
    return file_url


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
                base_url = TEMP_FOLDER + BUCKET_NAMES["CONVERTED"] + "/"
                destination_url = base_url + image.name
                file_obj = get_file(name=image.name, bucket_name=image.bucketName, destination_url=destination_url)
                removed_noise_file_obj = remove_noise(file_obj)
                name = get_random_name(15) + ".png"
                bucket_name = BUCKET_NAMES["REMOVED_NOISE"]
                image.noiseRemovedBucketName = bucket_name
                image.noiseRemovedName = name
                image.status = STATUS["REMOVED_NOISE"]
                upload_file(name, bucket_name, removed_noise_file_obj)
                _ = await image_data_access.update(image)

            next_file.status = STATUS["REMOVED_NOISE"]
            _ = await document_data_access.update(next_file)
