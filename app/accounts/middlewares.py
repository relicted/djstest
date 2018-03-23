import json
import sys
from urllib.parse import urlparse

from django.http import HttpResponsePermanentRedirect
from django.conf import settings

from app.accounts import models


def dumps(value):
    return json.dumps(value, default=lambda o: None)


def save(request, response):

    if not request.user.is_anonymous:
        user = request.user
    else:
        user = None

    meta = request.META.copy()
    meta.pop('QUERY_STRING', None)
    meta.pop('HTTP_COOKIE', None)
    remote_addr_fwd = None

    if 'HTTP_X_FORWARDED_FOR' in meta:
        remote_addr_fwd = meta['HTTP_X_FORWARDED_FOR'].split(",")[0].strip()
        if remote_addr_fwd == meta['HTTP_X_FORWARDED_FOR']:
            meta.pop('HTTP_X_FORWARDED_FOR')

    post = None

    uri = request.build_absolute_uri()
    if request.POST and uri != '/login/':
        post = dumps(request.POST)
        print(post)

    models.WebRequest.objects.create(
        host=request.get_host(),
        path=request.path,
        method=request.method,
        uri=request.build_absolute_uri(),
        status_code=response.status_code,
        user_agent=meta.pop('HTTP_USER_AGENT', None),
        remote_addr=meta.pop('REMOTE_ADDR', None),
        remote_addr_fwd=remote_addr_fwd,
        meta=None if not meta else dumps(meta),
        cookies=None if not request.COOKIES else dumps(request.COOKIES),
        get=None if not request.GET else dumps(request.GET),
        post=post,
        is_secure=request.is_secure(),
        is_ajax=request.is_ajax(),
        user=user
    )


def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        if request.path.endswith('/favicon.ico'):
            print('1111111')
            return response

        if type(
                response) == HttpResponsePermanentRedirect and settings.APPEND_SLASH:
            new_location = response.get('location', None)
            content_length = response.get('content-length', None)
            print('222222222')

            if new_location and content_length is '0':
                new_parsed = urlparse(new_location)

                old = (
                    ('http', 'https')[request.is_secure()], request.get_host(),
                    '{0}/'.format(request.path), request.META['QUERY_STRING'])
                new = (new_parsed.scheme, new_parsed.netloc, new_parsed.path,
                       new_parsed.query)
                print('3333333333')
                if old == new:
                    return response
        try:
            save(request, response)
        except Exception as e:
            print(sys.stderr, "Error saving request log", e)
        return response

    return middleware
