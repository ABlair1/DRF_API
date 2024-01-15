from django.contrib import admin
from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()

urlpatterns = [
    path("", include(router.urls)),
    path("", include("fizzbuzz.urls")),
    path("admin/", admin.site.urls),
]
urlpatterns += router.urls
