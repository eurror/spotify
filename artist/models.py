from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
