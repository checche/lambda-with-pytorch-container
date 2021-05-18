import base64
import cgi
import io
import json
import logging
import traceback
from typing import Any, Dict, List

from lib import prediction

logger = logging.getLogger(__name__)


def _get_parts(event) -> Dict[str, List[Any]]:
    """multipart/form-dataをパースする処理"""
    byte_body = base64.b64decode(event["body"])
    rfile = io.BytesIO(byte_body)
    content_type = event["headers"]["Content-Type"]
    _, parameters = cgi.parse_header(content_type)
    parameters["boundary"] = parameters["boundary"].encode("utf-8")
    parsed = cgi.parse_multipart(rfile, parameters)
    return parsed


def handler(event, context):
    """
    画像とその他のデータを含むmultipart/form-dataのリクエストから
    画像だけ取り出しResNet50で適当に処理して値を返す関数
    """
    try:
        data: Dict[str, List[Any]] = _get_parts(event)
    except Exception as e:
        # エラー時に雑に全部返す仕様
        logger.error(e.args)
        logger.error(list(traceback.TracebackException.from_exception(e).format()))
        return {
            "statusCode": 200,
            "body": json.dumps({"message": e.args}),
        }

    try:
        output = prediction.predict(data)
    except Exception as e:
        # エラー時に雑に全部返す仕様
        logger.error(e.args)
        logger.error(list(traceback.TracebackException.from_exception(e).format()))
        return {
            "statusCode": 200,
            "body": json.dumps(
                {
                    "message": e.args,
                }
            ),
        }

    return {"statusCode": 200, "body": json.dumps({"output": output})}
