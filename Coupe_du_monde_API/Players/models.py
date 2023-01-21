from django.db import models
import uuid
from Teams.models import Teams

class Players(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=80, null=False, blank=False)
    goals = models.CharField(max_length=80, null=False, blank=False)
    # team = models.ForeignKey(Teams,on_delete=models.PROTECT, null=False, blank=False, related_name='name')


