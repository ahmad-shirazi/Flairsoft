from src.util.db import executeval, fetch
from src.util.misc import Image
from src.util.time import get_current_time
from src.config.enum import TABLE_NAMES


async def _get_result(query):
    result = await fetch(query)
    return [Image(image_id=row['id'], file_key=row['fileKey'], name=row['name'],
                  bucket_name=row['bucketName'], number=row['number'], noise_removed_name=row['noiseRemovedName'],
                  noise_removed_bucket_name=row['noiseRemovedBucketName'], ocr_name=row['ocrName'],
                  ocr_bucket_name=row['ocrBucketName'], result=row['result'], status=row['status'],
                  created_at=row['createdAt'], updated_at=row['updatedAt'])
            for row in result]


async def insert_and_update(image_data, _type):
    model_name = TABLE_NAMES['image']
    if _type == "insert":
        image_data.createdAt = get_current_time()
    if _type == "update":
        image_data.updatedAt = get_current_time()

    field_names = ['fileKey', 'name', 'bucketName', 'number', 'noiseRemovedName', 'noiseRemovedBucketName',
                   'ocrName', 'ocrBucketName', 'result', 'status', 'createdAt', 'updatedAt']
    values_string = ','.join(['$' + str(idx + 1) for idx, _ in enumerate(field_names)])
    values = [getattr(image_data, field_name) for field_name in field_names]

    fields_string = ','.join(['"' + field + '"' for field in field_names])

    query = '''
        INSERT INTO "{model_name}" ({fields_string}) VALUES ({values_str})
        '''.format(
        model_name=model_name,
        fields_string=fields_string,
        values_str=values_string
    )
    await executeval(query, values)


async def fetch_by_file_key(file_key):
    model_name = TABLE_NAMES['image']
    query = '''SELECT  "id", "fileKey", "name", "bucketName", "number", "noiseRemovedName", "noiseRemovedBucketName",
    "ocrName", "ocrBucketName", "result", "status", "createdAt", "updatedAt"
    FROM "{model_name}"
    WHERE "fileKey" = '{file_key}'
    '''.format(file_key=file_key, model_name=model_name)

    result = await _get_result(query)
    return result


async def fetch_by_id(image_id):
    model_name = TABLE_NAMES['image']
    query = '''SELECT  "id", "fileKey", "name", "bucketName", "number", "noiseRemovedName", "noiseRemovedBucketName",
    "ocrName", "ocrBucketName", "result", "status", "createdAt", "updatedAt"
    FROM "{model_name}"
    WHERE "id" = '{image_id}'
    '''.format(image_id=image_id, model_name=model_name)

    result = await _get_result(query)
    return result


async def fetch_by_status(status):
    model_name = TABLE_NAMES['image']
    query = '''SELECT  "id", "fileKey", "name", "bucketName", "number", "noiseRemovedName", "noiseRemovedBucketName",
    "ocrName", "ocrBucketName", "result", "status", "createdAt", "updatedAt"
    FROM "{model_name}"
    WHERE "status" = '{status}'
    '''.format(status=status, model_name=model_name)

    result = await _get_result(query)
    return result

