from django.urls import path, include
from rest_framework import routers
from tutorial.quickstart import views

router = routers.DefaultRouter()

urlpatterns = [
    path('quick/', views.Quick.as_view()),
    path('', include(router.urls)),
]
