from django.urls import path
from ai_web.views import index

urlpatterns = [
    path("list/", index)
]
