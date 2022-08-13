from google.cloud import storage


def upload_file(name, bucket_name, file_obj):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(name)

    blob.upload_from_file(file_obj)

    print(
        f"File uploaded to {name}."
    )


def get_file(name, bucket_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(name)

    file_obj = None
    blob.download_to_file(file_obj)

    return file_obj
