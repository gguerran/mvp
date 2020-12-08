from datetime import datetime

from django.test import TestCase

from mvp.accounts.models import User, Advertiser


class UserTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            name="usuário teste", email='test@test.com'
        )
        self.user.save()

    def test_create(self):
        self.assertTrue(User.objects.exists())
    
    def test_str(self):
        self.assertEqual('usuário teste', str(self.user))

    def test_name_cannot_be_blank(self):
        field = User._meta.get_field('name')
        self.assertFalse(field.blank)

    def test_name_cannot_be_null(self):
        field = User._meta.get_field('name')
        self.assertFalse(field.null)

    def test_email_cannot_be_null(self):
        field = User._meta.get_field('email')
        self.assertFalse(field.null)
    
    def test_email_cannot_be_blank(self):
        field = User._meta.get_field('email')
        self.assertFalse(field.blank)

    def test_name(self):
        self.assertEquals(self.user.name, 'usuário teste')

    def test_email(self):
        self.assertEquals(self.user.email, 'test@test.com')

    def test_is_active(self):
        self.assertEquals(self.user.is_active, True)

    def test_is_staff(self):
        self.assertEquals(self.user.is_staff, True)

    def test_is_superuser(self):
        self.assertEquals(self.user.is_superuser, True)

    def test_created_at(self):
        self.assertIsInstance(self.user.created_at, datetime)

    def test_modified_at(self):
        self.assertIsInstance(self.user.modified_at, datetime)


class AdvertiserTest(TestCase):

    def setUp(self):
        self.advertiser = Advertiser.objects.create(
            name="usuário teste", email='test@test.com', phone='(00)00000-0000'
        )
        self.advertiser.save()

    def test_create(self):
        self.assertTrue(Advertiser.objects.exists())
    
    def test_str(self):
        self.assertEqual('usuário teste', str(self.advertiser))

    def test_name_cannot_be_blank(self):
        field = Advertiser._meta.get_field('name')
        self.assertFalse(field.blank)
    
    def test_name_cannot_be_null(self):
        field = Advertiser._meta.get_field('name')
        self.assertFalse(field.null)

    def test_email_cannot_be_null(self):
        field = Advertiser._meta.get_field('email')
        self.assertFalse(field.null)
    
    def test_email_cannot_be_blank(self):
        field = Advertiser._meta.get_field('email')
        self.assertFalse(field.blank)

    def test_phone_cannot_be_null(self):
        field = Advertiser._meta.get_field('phone')
        self.assertFalse(field.null)
    
    def test_phone_cannot_be_blank(self):
        field = Advertiser._meta.get_field('phone')
        self.assertFalse(field.blank)

    def test_name(self):
        self.assertEquals(self.advertiser.name, 'usuário teste')

    def test_email(self):
        self.assertEquals(self.advertiser.email, 'test@test.com')

    def test_phone(self):
        self.assertEquals(self.advertiser.phone, '(00)00000-0000')

    def test_is_active(self):
        self.assertEquals(self.advertiser.is_active, True)

    def test_is_staff(self):
        self.assertEquals(self.advertiser.is_staff, True)

    def test_is_superuser(self):
        self.assertEquals(self.advertiser.is_superuser, False)

    def test_created_at(self):
        self.assertIsInstance(self.advertiser.created_at, datetime)

    def test_modified_at(self):
        self.assertIsInstance(self.advertiser.modified_at, datetime)