from django.urls import path
from .views import analyze_seo

urlpatterns = [
    path('analyze/', analyze_seo),
]
