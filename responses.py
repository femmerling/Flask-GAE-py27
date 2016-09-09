from flask import Response
from flask import json

def api_response(
    status=200, payload=None, message='success',
    headers=None, mimetype='application/json'):
    status = int(status)
    data = json.dumps(payload)
    return Response(
        headers=headers,
        status=status,
        mimetype=mimetype,
        response=data)
