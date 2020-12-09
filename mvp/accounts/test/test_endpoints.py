from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

from mvp.accounts.views import (
    Advertiser, AdvertiserSerializer, CreateAdvertiserSerializer,
    UpdatePassAdvertiserSerializer, AdvertiserViewSet
)

factory = APIRequestFactory()


class AdvertiserViewsTest(TestCase):
    def setUp(self):
        self.advertiser = Advertiser.objects.create(
            name="usuário teste", email='test@test.com', phone='(00)00000-0000'
        )
        self.advertiser.set_password('#pass123')
        self.advertiser.save()
        self.advertiser2 = Advertiser.objects.create(
            name="usuário teste", email='test2@test.com', phone='(22)00000-0000'
        )
        self.advertiser2.set_password('#pass123')
        self.advertiser2.save()
        self.advertiser3 = Advertiser.objects.create(
            name="usuário teste", email='test3@test.com', phone='(33)00000-0000'
        )
        self.advertiser3.set_password('#pass123')
        self.advertiser3.save()

    def test_create_ok(self):
        data = {
            'name':"usuário teste", 'email':'test4@test.com',
            'phone':'(44)00000-0000', 'password1': '#pass123',
            'password2': '#pass123',
        }
        request = factory.post('api/v1/advertiser/', data)
        view = AdvertiserViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_pass_not_equals(self):
        data = {
            'name':"usuário teste", 'email':'test5@test.com',
            'phone':'(55)00000-0000', 'password1': '#pass123',
            'password2': '#pass1234', 

        }
        request = factory.post('api/v1/advertiser/', data)
        view = AdvertiserViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(str(response.data[0]), 'As senhas não conferem')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all(self):
        request = factory.get('api/v1/advertiser/')
        force_authenticate(request, user=self.advertiser)
        view = AdvertiserViewSet.as_view({'get': 'list'})
        response = view(request)
        advertisers = Advertiser.objects.filter(id=self.advertiser.id)
        serializer = AdvertiserSerializer(advertisers, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_advertiser(self):
        request = factory.get('api/v1/advertiser/',)
        force_authenticate(request, user=self.advertiser)
        view = AdvertiserViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=self.advertiser.id)
        advertiser = Advertiser.objects.get(pk=self.advertiser.id)
        serializer = AdvertiserSerializer(advertiser)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update(self):
        data = {
            'name':"usuário teste", 'email':'test6@test.com',
            'phone':'(44)00000-0002',
        }
        request = factory.post('api/v1/advertiser/', data)
        force_authenticate(request, user=self.advertiser)
        view = AdvertiserViewSet.as_view({'post': 'update'})
        response = view(request, pk=self.advertiser.id)
        advertiser = Advertiser.objects.get(pk=self.advertiser.id)
        serializer = AdvertiserSerializer(advertiser)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_ok(self):
        data = {
            'last_pass': '#pass123', 'password': '#pass1234',
            'password2': '#pass1234', 
        }
        request = factory.patch('api/v1/advertiser/', data)
        force_authenticate(request, user=self.advertiser)
        view = AdvertiserViewSet.as_view({'patch': 'partial_update'})
        response = view(request, pk=self.advertiser.id)
        advertiser = Advertiser.objects.get(id=self.advertiser.id)
        serializer = UpdatePassAdvertiserSerializer(advertiser)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update_last_pass_no_match(self):
        data = {
            'last_pass': '#pass12356', 'password': '#pass1234',
            'password2': '#pass1234', 
        }
        request = factory.patch('api/v1/advertiser/', data)
        force_authenticate(request, user=self.advertiser3)
        view = AdvertiserViewSet.as_view({'patch': 'partial_update'})
        response = view(request, pk=self.advertiser3.id)
        self.assertEqual(str(response.data[0]), 'Antiga senha inválida')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_partial_update_new_pass_no_match(self):
        data = {
            'last_pass': '#pass123', 'password': '#pass1234',
            'password2': '#pass1235', 
        }
        request = factory.patch('api/v1/advertiser/', data)
        force_authenticate(request, user=self.advertiser3)
        view = AdvertiserViewSet.as_view({'patch': 'partial_update'})
        response = view(request, pk=self.advertiser3.id)
        self.assertEqual(str(response.data[0]), 'As senhas não conferem')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)