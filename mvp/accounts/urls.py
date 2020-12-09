from rest_framework import routers
from django.urls import path, include

from mvp.accounts import views

app_name = 'accounts'

router = routers.DefaultRouter()

router.register(
    '', views.AdvertiserViewSet, basename='accounts'
)

urlpatterns = [
    path('', include(router.urls)),
]