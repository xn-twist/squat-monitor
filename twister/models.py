from django.db import models


class Domain(models.Model):
    domain_name = models.CharField(max_length=40, primary_key=True)

    def __str__(self):
        return self.domain_name
