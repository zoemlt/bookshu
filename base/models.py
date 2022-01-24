from django.db import models

# Create your models here.
class Space(models.Model):
    # host =
    # topic =
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # members =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
