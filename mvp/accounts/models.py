import uuid

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        verbose_name='ID do usuário', primary_key=True, default=uuid.uuid4,
        editable=False
    )
    name = models.CharField('nome', max_length=255)
    email = models.EmailField('e-mail', unique=True)
    is_superuser = models.BooleanField('administrador', default=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField('ativo', default=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    modified_at = models.DateTimeField('modificado em', auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
    
    def __str__(self):
        return self.name


class Advertiser(User):

    phone = models.CharField('telefone', max_length=14, unique=True)

    class Meta:
        verbose_name = 'Anunciante'
        verbose_name_plural = 'Anunciantes'

    def save(self, *args, **kwargs):
        self.is_superuser = False
        super().save(*args, **kwargs)