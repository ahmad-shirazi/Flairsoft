from src.dataaccess.document import fetch_by_file_key

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


def post_data(key):
    pass
