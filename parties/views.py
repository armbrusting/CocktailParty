from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404

from parties.models import Party

def index(request):
    latest_party_list = Party.objects.all()
    context = {'latest_party_list': latest_party_list}
    return render(request, 'party/index.html', context)

def detail(request, party_id):
    party = get_object_or_404(Party, pk=party_id)
    return render(request, 'party/detail.html', {'party': party})

def cocktails(request, party_id):
    return HttpResponse("You're looking at the cocktails of party %s." %
            party_id)

#def vote(request, poll_id):
#    return HttpResponse("You're voting on poll %s." % poll_id)
