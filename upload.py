from google.cloud import storage


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    bucket_name = "ocrinpu"
    # The path to your file to upload
    source_file_name = "/Users/ahmadshirazi/Desktop/FlairSoft/FlairSoft/Documents/00000231.PDF"
    # The ID of your GCS object
    destination_blob_name = "00000231.PDF"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )


upload_blob("", "", "")