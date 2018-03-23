from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.store.urls', namespace='store')),
    path('', include('app.accounts.urls', namespace='accounts')),

    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
]


if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
