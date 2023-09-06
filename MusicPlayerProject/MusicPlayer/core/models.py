from django.db import models


class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    
    class Meta:
        abstract = True