# urls.py
from django.urls import path
from .views import PassListView, PassCreateView, PassDeleteView, get_decrypted_password

urlpatterns = [
    path("", PassListView.as_view(), name="pass_list"),
    path("create/", PassCreateView.as_view(), name="pass_create"),
    path("delete/<int:pk>/", PassDeleteView.as_view(), name="pass_delete"),
    path("decrypt/", get_decrypted_password, name="decrypt_password")
]