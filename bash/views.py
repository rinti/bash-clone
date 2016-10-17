from django.http import HttpResponseForbidden, JsonResponse
from django.views.generic import ListView

from .models import Quote
from .utils import get_ip


class HomeView(ListView):
    queryset = Quote.objects.order_by('?')[:10]
    template_name = 'home.html'


def vote(request, pk):
    vote = int(request.POST.get('vote'))
    quote = Quote.objects.get(pk=pk)
    ip = get_ip(request)

    if not vote or vote not in [1, -1] or ip in quote.voters:
      return HttpResponseForbidden()

    quote.score += vote
    quote.voters.append(ip)
    quote.save()

    return JsonResponse({'pk': quote.pk, 'score': quote.score})
