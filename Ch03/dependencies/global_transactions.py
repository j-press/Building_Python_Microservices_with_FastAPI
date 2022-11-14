from fastapi import Request
from uuid import uuid4

service_paths_log = dict()


def log_tranaction(request: Request):
    service_paths_log[uuid4()] = request.url.path
