from rest_framework import routers
from django.urls import path, include

from mvp.demand import views

app_name = 'demand'

router = routers.DefaultRouter()

router.register(
    '', views.DemandViewSet, basename='demand'
)

urlpatterns = [
    path('', include(router.urls)),
]