import http.client

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View


# Create your views here.

class VeichleView(View):
    def get(self, request, *args, **kwargs):
        res = HttpResponse(
            "ciao ciao ciao"
        )
        res.status_code = http.HTTPStatus.OK
        return res

    def options(self, request, *args, **kwargs):
        res = HttpResponse(
            headers={
                "pietro": "pazzo"
            }
        )
        return res
