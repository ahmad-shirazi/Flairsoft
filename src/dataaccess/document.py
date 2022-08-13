from src.util.db import executeval, fetch
from src.util.misc import Document
from src.util.time import get_current_time
from src.config.enum import TABLE_NAMES


async def _get_result(query):
    result = await fetch(query)
    return [Document(document_id=row['id'], file_key=row['fileKey'], original_name=row['originalName'],
                     original_bucket_name=row['originalBucketName'], result=row['result'], status=row['status'],
                     created_at=row['createdAt'], updated_at=row['updatedAt'])
            for row in result]


async def insert_and_update(document_data, _type):
    model_name = TABLE_NAMES['document']
    if _type == "insert":
        document_data.createdAt = get_current_time()
    if _type == "update":
        document_data.updatedAt = get_current_time()

    field_names = ['fileKey', 'originalName', 'originalBucketName', 'result', 'status', 'createdAt', 'updatedAt']
    values_string = ','.join(['$' + str(idx + 1) for idx, _ in enumerate(field_names)])
    values = [getattr(document_data, field_name) for field_name in field_names]

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
    model_name = TABLE_NAMES['document']
    query = '''SELECT  "id", "fileKey", "originalName", "originalBucketName",
     "result", "status", "createdAt", "updatedAt"
    FROM "{model_name}"
    WHERE "fileKey" = '{file_key}'
    '''.format(file_key=file_key, model_name=model_name)

    result = await _get_result(query)
    return result


async def fetch_by_id(document_id):
    model_name = TABLE_NAMES['document']
    query = '''SELECT  "id", "fileKey", "originalName", "originalBucketName",
     "result", "status", "createdAt", "updatedAt"
    FROM "{model_name}"
    WHERE "id" = '{document_id}'
    '''.format(document_id=document_id, model_name=model_name)

    result = await _get_result(query)
    return result


async def fetch_by_status(status):
    model_name = TABLE_NAMES['document']
    query = '''SELECT  "id", "fileKey", "originalName", "originalBucketName",
     "result", "status", "createdAt", "updatedAt"
    FROM "{model_name}"
    WHERE "status" = '{status}'
    '''.format(status=status, model_name=model_name)

    result = await _get_result(query)
    return result

