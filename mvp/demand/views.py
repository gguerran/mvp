from rest_framework import viewsets
from rest_framework import permissions

from mvp.accounts.models import Advertiser
from mvp.demand.serializers import (
    Demand, DemandSerializer, SetFinishedDemandSerializer
)


class DemandViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'partial_update':
            return SetFinishedDemandSerializer
        return DemandSerializer

    def perform_create(self, serializer):
        advertiser = Advertiser.objects.get(id=self.request.user.id)
        serializer.save(advertiser=advertiser)
    
    def get_queryset(self):
        advertiser = Advertiser.objects.get(id=self.request.user.id)
        return Demand.objects.filter(advertiser=advertiser)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = False
        return self.update(request, *args, **kwargs)
