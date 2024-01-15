from django.urls import path
from fizzbuzz import views


urlpatterns = [
    path("fizzbuzz/", views.fizzbuzz_list),
    path("fizzbuzz/<int:fizzbuzz_id>/", views.fizzbuzz_single)
]
