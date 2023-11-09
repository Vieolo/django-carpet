# Python
import json

# Django
from django.http.response import HttpResponse

# Third Party
from typing import Optional


class NotLoggedResponse(HttpResponse):

    def __init__(self):
        super().__init__(json.dumps({'result': 'not logged'}), status=401)

class APIResponse(HttpResponse):

    def __init__(self, response, request, status=200):
        if request.token is not None and request.token != '':
            super().__init__(json.dumps(response, default=str), content_type='application/json', status=status)
        else:
            super().__init__(json.dumps(response, default=str), status=status)


class NotAllowedResponse(HttpResponse):

    def __init__(self, reason: Optional[str] = None):
        super().__init__(json.dumps({'result': 'not allowed', 'reason': reason or ""}), status=405)

