from src.util.google_cloud import upload_file, get_file
from src.dataaccess import document as document_data_access, image as image_data_access
from src.config.enum import STATUS, BUCKET_NAMES
from src.util.misc import Image
from src.util.name_setter import get_random_name


# todo
def convert_pdf_to_images(file_obj):
    return []


def create_image_model(file_key, name, bucket_name, number, status):
    image = Image(image_id=None, file_key=file_key, name=name, bucket_name=bucket_name, number=number, status=status)
    return image


class Convertor(object):
    def __init__(self, name):
        self.name = name

    @staticmethod
    async def run():
        while True:
            next_files = await document_data_access.fetch_by_status(STATUS["UNPROCESSED"])
            if len(next_files) <= 0:
                continue
            next_file = next_files[0]
            file_obj = get_file(name=next_file.originalName, bucket_name=next_file.originalBucketName)
            images = convert_pdf_to_images(file_obj=file_obj)
            for i in range(len(images)):
                name = get_random_name(15) + ".png"
                bucket_name = BUCKET_NAMES["CONVERTED"]
                image = create_image_model(file_key=next_file.fileKey, name=name, bucket_name=bucket_name,
                                           number=i, status=STATUS["CONVERTED"])

                upload_file(name, bucket_name, images[i])
                _ = await image_data_access.insert_and_update(image, "insert")

            next_file.status = "CONVERTED"
            _ = await document_data_access.insert_and_update(next_file, "update")


convertor_obj = Convertor("first")
convertor_obj.run()
