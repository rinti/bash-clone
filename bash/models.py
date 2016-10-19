from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField

from .managers import QuoteQuerySet


class Quote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quote = models.TextField()
    submited = models.DateField(auto_now_add=True)
    score = models.IntegerField(default=0)
    voters = ArrayField(models.GenericIPAddressField(), default=[], blank=True, null=True)

    objects = QuoteQuerySet.as_manager()

    def __str__(self):
        quote = self.quote[:30] + '...' if len(self.quote) > 30 else self.quote
        return '{date}: {quote}'.format(
            date=str(self.submited),
            quote=quote
        )
