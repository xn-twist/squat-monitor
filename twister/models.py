import uuid

from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models


class Domain(models.Model):
    domain_name = models.CharField(max_length=40)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    users = models.ManyToManyField(User)
    date_spun = models.DateField(auto_now=True)
    spun_data = JSONField(blank=True, null=True)

    def __str__(self):
        return self.domain_name
