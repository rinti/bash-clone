from django.db import models


class QuoteQuerySet(models.QuerySet):

    def from_user(self, user):
        if type(user) == str:
          return self.filter(user__username=user)
        return self.filter(user=user)
