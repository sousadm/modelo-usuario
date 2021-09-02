import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Usuario(AbstractUser):

    uuid = models.UUIDField(_("User UUID"), editable=False, default=uuid.uuid4)
    celular = models.CharField('Celular', max_length=20, null=True, blank=True)
    is_consulta = models.BooleanField('Desenvolvimento', blank=True, default=False)

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
        verbose_name = _("usuario")
        verbose_name_plural = _("usuarios")
        db_table = "usuario"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("usuario_detail", kwargs={"pk": self.pk})
