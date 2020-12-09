from mvp.accounts.permissions import IsAuthenticatedOrWriteOnly
from mvp.accounts.serializers import (
    Advertiser, AdvertiserSerializer, CreateAdvertiserSerializer,
    UpdatePassAdvertiserSerializer
)
from mvp.accounts.utils import NewModelViewSet


class AdvertiserViewSet(NewModelViewSet):

    permission_classes = [IsAuthenticatedOrWriteOnly]
    serializer_class = AdvertiserSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateAdvertiserSerializer
        if self.action == 'partial_update':
            return UpdatePassAdvertiserSerializer
        return AdvertiserSerializer

    def get_queryset(self):
        return Advertiser.objects.filter(id=self.request.user.id)