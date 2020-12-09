from datetime import datetime

from django.test import TestCase

from mvp.accounts.models import Advertiser
from mvp.demand.models import Demand


class DemandTest(TestCase):

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

    def test_create(self):
        self.assertTrue(Demand.objects.exists())
    
    def test_str(self):
        self.assertEqual('demanda teste', str(self.demand))

    def test_description_cannot_be_blank(self):
        field = Demand._meta.get_field('description')
        self.assertFalse(field.blank)

    def test_description_cannot_be_null(self):
        field = Demand._meta.get_field('description')
        self.assertFalse(field.null)

    def test_state_cannot_be_blank(self):
        field = Demand._meta.get_field('state')
        self.assertFalse(field.blank)

    def test_state_cannot_be_null(self):
        field = Demand._meta.get_field('state')
        self.assertFalse(field.null)

    def test_city_cannot_be_blank(self):
        field = Demand._meta.get_field('city')
        self.assertFalse(field.blank)

    def test_city_cannot_be_null(self):
        field = Demand._meta.get_field('city')
        self.assertFalse(field.null)

    def test_district_cannot_be_blank(self):
        field = Demand._meta.get_field('district')
        self.assertFalse(field.blank)

    def test_district_cannot_be_null(self):
        field = Demand._meta.get_field('district')
        self.assertFalse(field.null)

    def test_street_cannot_be_blank(self):
        field = Demand._meta.get_field('street')
        self.assertFalse(field.blank)

    def test_street_cannot_be_null(self):
        field = Demand._meta.get_field('street')
        self.assertFalse(field.null)

    def test_number_cannot_be_blank(self):
        field = Demand._meta.get_field('number')
        self.assertFalse(field.blank)

    def test_number_cannot_be_null(self):
        field = Demand._meta.get_field('number')
        self.assertFalse(field.null)

    def test_email_cannot_be_blank(self):
        field = Demand._meta.get_field('email')
        self.assertFalse(field.blank)

    def test_email_cannot_be_null(self):
        field = Demand._meta.get_field('email')
        self.assertFalse(field.null)

    def test_phone_cannot_be_blank(self):
        field = Demand._meta.get_field('phone')
        self.assertFalse(field.blank)

    def test_phone_cannot_be_null(self):
        field = Demand._meta.get_field('phone')
        self.assertFalse(field.null)

    def test_status_cannot_be_blank(self):
        field = Demand._meta.get_field('status')
        self.assertFalse(field.blank)

    def test_status_cannot_be_null(self):
        field = Demand._meta.get_field('status')
        self.assertFalse(field.null)

    def test_advertiser_cannot_be_blank(self):
        field = Demand._meta.get_field('advertiser')
        self.assertFalse(field.blank)

    def test_advertiser_cannot_be_null(self):
        field = Demand._meta.get_field('advertiser')
        self.assertFalse(field.null)

    def test_description(self):
        self.assertEquals(self.demand.description, 'demanda teste')

    def test_state(self):
        self.assertEquals(self.demand.state, 'PI')

    def test_city(self):
        self.assertEquals(self.demand.city, 'Corrente')

    def test_district(self):
        self.assertEquals(self.demand.district, 'centro')

    def test_street(self):
        self.assertEquals(self.demand.street, 'rua 17')

    def test_number(self):
        self.assertEquals(self.demand.number, 15)

    def test_status(self):
        self.assertEquals(self.demand.status, 'Aberta')

    def test_advertiser(self):
        self.assertEquals(self.demand.advertiser, self.advertiser)

    def test_email(self):
        self.assertEquals(self.demand.email, self.advertiser.email)

    def test_phone(self):
        self.assertEquals(self.demand.phone, self.advertiser.phone)

    def test_created_at(self):
        self.assertIsInstance(self.demand.created_at, datetime)

    def test_modified_at(self):
        self.assertIsInstance(self.demand.modified_at, datetime)