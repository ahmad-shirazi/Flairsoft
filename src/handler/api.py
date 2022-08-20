from src.dataaccess.document import fetch_by_file_key, insert
from src.config.enum import STATUS, BUCKET_NAMES
from src.config.file import TEMP_FOLDER
from src.util.google_cloud import upload_file
from src.util.misc import Document

import asyncio


async def _search(keys):
    result = dict()
    docs = await fetch_by_file_key(keys[0])
    result["req_status"] = "ok"
    if len(docs) <= 0:
        result["req_status"] = "bad_req"
    else:
        doc = docs[0]
        result["result"] = doc.result
    return result


def search(key):
    event_loop = asyncio.get_event_loop()
    res = event_loop.run_until_complete(_search(key))
    return res


async def _get_status(keys):
    result = dict()
    docs = await fetch_by_file_key(keys[0])
    result["req_status"] = "ok"
    if len(docs) <= 0:
        result["req_status"] = "bad_req"
    else:
        doc = docs[0]
        result["status"] = doc.status
    return result


def get_status(key):
    event_loop = asyncio.get_event_loop()
    res = event_loop.run_until_complete(_get_status(key))
    return res


async def _post_data(file_key, filename, full_body):
    print("amin")
    url = TEMP_FOLDER + BUCKET_NAMES["UNPROCESSED"] + "/" + filename
    with open(url, 'wb') as f:
        f.write(full_body)
    print("aaaa")
    upload_file(name=filename, bucket_name=BUCKET_NAMES["UNPROCESSED"], filename=url)
    doc = Document(file_key=file_key, original_name=filename, original_bucket_name=BUCKET_NAMES["UNPROCESSED"],
                   status=STATUS["UNPROCESSED"], document_id=10)
    res = await insert(doc)
    return res


def post_data(file_key, filename, full_body):
    event_loop = asyncio.get_event_loop()
    res = event_loop.run_until_complete(_post_data(file_key, filename, full_body))
    return res
