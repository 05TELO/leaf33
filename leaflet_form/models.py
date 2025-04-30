from django.db import models


class AreaCollection(models.Model):
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Areas from {self.created_at}"

    @property
    def areas(self):
        return self.data
