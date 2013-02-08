from django.http import HttpResponse
from django.template import Context, loader

from parties.models import Party

def index(request):
    latest_party_list = Party.objects.all
    template = loader.get_template('index.html')
    context = Context({
        'latest_party_list': latest_party_list,
    })
    return HttpResponse(template.render(context))

def detail(request, party_id):
    return HttpResponse("You're looking at party %s." % party_id)

def cocktails(request, party_id):
    return HttpResponse("You're looking at the cocktails of party %s." %
            party_id)

#def vote(request, poll_id):
#    return HttpResponse("You're voting on poll %s." % poll_id)
