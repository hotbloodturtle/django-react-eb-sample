from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alive', lambda request: HttpResponse("I'm alive...")),
]

urlpatterns += [
    re_path(r'^(?P<path>.*)$', TemplateView.as_view(template_name='index.html')),
]
