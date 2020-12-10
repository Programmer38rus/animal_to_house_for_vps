from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Pet, Kind
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
)
import os


# Create your views here.
class PetsList(ListView):
    model = Pet
    template_name = 'base.html'
    context_object_name = 'Pets'

    def get_context_data(self, *, object_list=None, **kwargs):
        pets = super(PetsList, self).get_context_data(**kwargs)

        pets['kind'] = Kind.objects.all()

        return pets

class KindList(ListView):
    model = Pet
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        pets = super().get_context_data(**kwargs)
        name_kind = self.kwargs['kind'].title()

        kind = Kind.objects.filter(name=name_kind).values()

        for id in kind:
            pets['Pets'] = Pet.objects.filter(kind=id['id'])

        pets['kind'] = Kind.objects.all()
        return pets


class PetsDetailView(DetailView):
    model = Pet
    template_name = 'base2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kind'] = Kind.objects.all()
        return context

class AboutUs(TemplateView):
    template_name = 'about.html'

class Map(TemplateView):
    template_name = 'map.html'

@csrf_exempt
def push(request):
    os.system('sudo git pull origin master')
    return HttpResponse(request)
