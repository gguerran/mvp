from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

from mvp.accounts.models import Advertiser
from mvp.demand.views import (
    Demand, DemandSerializer,SetFinishedDemandSerializer, DemandViewSet
)

factory = APIRequestFactory()


class DemandViewsTest(TestCase):
    def setUp(self):
        self.advertiser = Advertiser.objects.create(
            name="usuário teste", email='test@test.com', phone='(00)00000-0000'
        )
        self.advertiser.set_password('#pass123')
        self.advertiser.save()
        self.demand = Demand.objects.create(
            description="demanda teste", state='PI', city='Corrente',
            district='centro', street='rua 17', number=15, status='Aberta',
            advertiser=self.advertiser
        )
        self.demand.save()
        self.demand2 = Demand.objects.create(
            description="demanda teste", state='PI', city='Corrente',
            district='centro', street='rua 17', number=15, status='Aberta',
            advertiser=self.advertiser
        )
        self.demand2.save()
        self.demand3 = Demand.objects.create(
            description="demanda teste", state='PI', city='Corrente',
            district='centro', street='rua 17', number=15, status='Finalizada',
            advertiser=self.advertiser
        )
        self.demand3.save()

    def test_create(self):
        data = {
            'description': "demanda teste", 'state': 'PI', 'city': 'Corrente',
            'district': 'centro', 'street': 'rua 17', 'number': 15,
            'status': 'Aberta',
        }
        request = factory.post('api/v1/demand/', data)
        force_authenticate(request, user=self.advertiser)
        view = DemandViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all(self):
        request = factory.get('api/v1/demand/')
        force_authenticate(request, user=self.advertiser)
        view = DemandViewSet.as_view({'get': 'list'})
        response = view(request)
        demands = Demand.objects.all()
        serializer = DemandSerializer(demands, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_demand(self):
        request = factory.get('api/v1/demand/',)
        force_authenticate(request, user=self.advertiser)
        view = DemandViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=self.demand.id)
        demand = Demand.objects.get(pk=self.demand.id)
        serializer = DemandSerializer(demand)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update(self):
        data = {
            'description': "demanda teste", 'state': 'PI', 'city': 'Corrente',
            'district': 'centro', 'street': 'rua 17', 'number': 15,
            'status': 'Aberta',
        }
        request = factory.post('api/v1/demand/', data)
        force_authenticate(request, user=self.advertiser)
        view = DemandViewSet.as_view({'post': 'update'})
        response = view(request, pk=self.demand2.id)
        demand = Demand.objects.get(pk=self.demand2.id)
        serializer = DemandSerializer(demand)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_ok(self):
        data = {
            'status': 'Finalizada',
        }
        request = factory.patch('api/v1/demand/', data)
        force_authenticate(request, user=self.advertiser)
        view = DemandViewSet.as_view({'patch': 'partial_update'})
        response = view(request, pk=self.demand2.id)
        demand = Demand.objects.get(pk=self.demand2.id)
        serializer = SetFinishedDemandSerializer(demand)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_for_open(self):
        data = {
            'status': 'Aberta',
        }
        request = factory.patch('api/v1/demand/', data)
        force_authenticate(request, user=self.advertiser)
        view = DemandViewSet.as_view({'patch': 'partial_update'})
        response = view(request, pk=self.demand3.id)
        self.assertEqual(
            str(response.data[0]),
            'A demanda já estava finalizada, você não pode reabri-la.'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_partial_update_has_open(self):
        data = {
            'status': 'Aberta',
        }
        request = factory.patch('api/v1/demand/', data)
        force_authenticate(request, user=self.advertiser)
        view = DemandViewSet.as_view({'patch': 'partial_update'})
        response = view(request, pk=self.demand2.id)
        self.assertEqual(str(response.data[0]), 'A demanda já estava aberta.')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_partial_update_has_finished(self):
        data = {
            'status': 'Finalizada',
        }
        request = factory.patch('api/v1/demand/', data)
        force_authenticate(request, user=self.advertiser)
        view = DemandViewSet.as_view({'patch': 'partial_update'})
        response = view(request, pk=self.demand3.id)
        demand = Demand.objects.get(pk=self.demand3.id)
        self.assertEqual(
            str(response.data[0]), 'A demanda já estava finalizada'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete(self):
        request = factory.delete('api/v1/demand/',)
        force_authenticate(request, user=self.advertiser)
        view = DemandViewSet.as_view({"delete": "destroy"})
        response = view(request, pk=self.demand3.id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)