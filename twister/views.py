from django.views import generic
from django.urls import reverse_lazy

from .models import Domain


class IndexView(generic.ListView):
    template_name = 'twister/index.html'
    context_object_name = 'recent_domains'

    def get_queryset(self):
        """Return recently twisted domains."""
        # create a list of the most recent domains
        recent_domains = [domain for domain in Domain.objects.all()]
        # reverse the list of recent domains
        recent_domains.reverse()
        return recent_domains


class TwistView(generic.edit.CreateView):
    model = Domain
    fields = ['domain_name']

    def get_success_url(self):
        return reverse_lazy('twister:domain', args=(self.object.domain_name,))


class DomainView(generic.DetailView):
    model = Domain
    template_name = 'twister/domain_details.html'

    def get_context_data(self, **kwargs):
        context = super(DomainView, self).get_context_data(**kwargs)
        context['domain'] = Domain.objects.filter(domain_name=self.object.domain_name)[0]
        return context
