import json

from django.views import generic
from django.urls import reverse_lazy
from xn_twist import XNTwist

from .models import Domain


class IndexView(generic.ListView):
    template_name = 'twister/index.html'
    context_object_name = 'recent_domains'

    def get_queryset(self):
        """Return recently twisted domains."""
        if str(self.request.user) != 'AnonymousUser':
            recent_domains = [domain for domain in Domain.objects.filter(users__in=[self.request.user])]
            # create a list of the most recent domains
            # recent_domains = [domain for domain in Domain.objects.all()]
            # reverse the list of recent domains
            recent_domains.reverse()
        else:
            recent_domains = None

        return recent_domains


class TwistView(generic.edit.CreateView):
    model = Domain
    fields = ['domain_name']

    def get_success_url(self):
        # record the user who created the domain
        self.object.users.add(self.request.user)
        # twist the domain
        xn = XNTwist()
        self.object.spun_data = json.JSONEncoder().encode(xn.twist(self.object.domain_name))
        return reverse_lazy('twister:domain', args=(self.object.id,))


class DomainView(generic.DetailView):
    model = Domain
    template_name = 'twister/domain_details.html'

    def get_context_data(self, **kwargs):
        context = super(DomainView, self).get_context_data(**kwargs)
        context['domain'] = Domain.objects.filter(domain_name=self.object.domain_name)[0]
        return context
