from django.db import models
from taggit.managers import TaggableManager
from core.models import TimeStampedModel


class Topic(TimeStampedModel):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000, null=True, blank=True)
    tags = TaggableManager()

