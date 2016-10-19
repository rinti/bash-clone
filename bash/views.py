from django.contrib.auth.models import User
from django.http import HttpResponseForbidden, JsonResponse
from django.views.generic import ListView

from .models import Quote
from .utils import get_ip


class HomeView(ListView):
    queryset = Quote.objects.order_by('?')[:10]
    template_name = 'home.html'


class TopListView(ListView):
    template_name = 'top.html'

    def get_queryset(self):
        return Quote.objects.order_by('-score')[50:100]


class UserListView(ListView):
    template_name = 'top.html'
    paginate_by = 10

    def get_queryset(self):
        return Quote.objects.from_user(
            int(self.kwargs.get('pk'))
        ).order_by('-score')

    def get_context_data(self):
        context = super().get_context_data()
        context.update({
            'user': User.objects.get(pk=self.kwargs.get('pk'))
        })
        return context


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
