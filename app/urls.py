from django.urls import path
from app import views
urlpatterns = [
    path('edata/',views.empinfo),
]
