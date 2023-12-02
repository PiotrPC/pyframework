from django.urls import path
from ai_web.views import index
from ai_web.views import kontakt
from ai_web.views import regulamin

urlpatterns = [
    path("Glowna/", index),
    path("Kontakt/", kontakt),
    path("Regulamin/", regulamin),
]
