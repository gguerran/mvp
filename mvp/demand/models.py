import uuid

from django.db import models

from mvp.demand.utils import FINALIZATION_STATUS_CHOICES, STATE_CHOICES


class Demand(models.Model):
    id = models.UUIDField(
        verbose_name='ID da demanda', primary_key=True, default=uuid.uuid4,
        editable=False
    )
    description = models.CharField('descrição', max_length=255)
    state = models.CharField('estado', max_length=2, choices=STATE_CHOICES)
    city = models.CharField('cidade', max_length=70)
    district = models.CharField('bairro', max_length=70)
    street = models.CharField('rua', max_length=100)
    number = models.PositiveIntegerField('número')
    email = models.EmailField('e-mail')
    phone = models.CharField('telefone', max_length=14)
    status = models.CharField(
        'status de finalização', choices=FINALIZATION_STATUS_CHOICES,
        max_length=10
    )
    advertiser = models.ForeignKey(
        'accounts.Advertiser', verbose_name='anunciante',
        on_delete=models.PROTECT
    )
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    modified_at = models.DateTimeField('modificado em', auto_now=True)

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        self.email = self.advertiser.email
        self.phone = self.advertiser.phone
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "demanda"
        verbose_name_plural = "demandas"