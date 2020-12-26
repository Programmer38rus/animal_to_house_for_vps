from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Pet, Kind
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
)
from django.core.cache import cache
import os


class PetsList(ListView):
    model = Pet
    template_name = 'animal_shelter/index.html'

    # context_object_name = 'Pets'

    def get_context_data(self, *, object_list=None, **kwargs):
        pets = super(PetsList, self).get_context_data(**kwargs)

        if cache.get('kind') is None:
            cache.set('kind', Kind.objects.all())

        pets['kind'] = cache.get('kind')

        return pets


# / показывает всех животных на главной странице
def index(request):
    # if not cache.get('Pets'):
    #     cache.set('Pets', Pet.objects.all())
    #
    # if cache.get('kind') is None:
    #     cache.set('kind', Kind.objects.all())

    # context = {
    #     'kind': cache.get('kind'),
    #     'Pets': cache.get('Pets')
    # }
    context = {
        'kind': Kind.objects.all(),
        'Pets': Pet.objects.all()
    }
    return render(request, 'animal_shelter/index.html', context)


class KindList(ListView):
    model = Pet
    template_name = 'animal_shelter/index.html'

    def get_context_data(self, **kwargs):
        pets = super().get_context_data(**kwargs)
        name_kind = self.kwargs['kind'].title()

        kind = Kind.objects.filter(name=name_kind).values()

        for id in kind:
            pets['Pets'] = Pet.objects.filter(kind=id['id'])

        if cache.get('kind') is None:
            cache.set('kind', Kind.objects.all())

        # pets['kind'] = Kind.objects.all()
        pets['kind'] = cache.get('kind')
        return pets


def kind_list(request, **kwargs):
    if not cache.get('Pets'):
        cache.set('Pets', Pet.objects.all().select_related())

    if cache.get('kind') is None:
        cache.set('kind', Kind.objects.all().select_related())

    name_kind = kwargs['kind'].title()
    kind = cache.get('kind').filter(name=name_kind).values()[0]

    context = {
        'kind': cache.get('kind'),
        'Pets': cache.get('Pets').filter(kind=kind['id'])
    }
    return render(request, 'animal_shelter/index.html', context)


class PetsDetailView(DetailView):
    model = Pet
    template_name = 'animal_shelter/details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if cache.get('kind') is None:
            cache.set('kind', Kind.objects.all())

        context['kind'] = cache.get('kind')
        return context


def pet_detail(request, **kwargs):
    if not cache.get('Pets'):
        cache.set('Pets', Pet.objects.all().select_related())

    if cache.get('kind') is None:
        cache.set('kind', Kind.objects.all().select_related())

    object = cache.get('Pets').filter(id=kwargs['pk']).first()

    context = {
        'kind': cache.get('kind'),
        'object': object,
    }

    return render(request, 'animal_shelter/details.html', context)


class AboutUs(TemplateView):
    template_name = 'animal_shelter/about.html'


class Map(TemplateView):
    template_name = 'animal_shelter/map.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['map'] = True
        return context


@csrf_exempt
def push(request):
    os.system('sudo git pull origin master && sudo systemctl restart gunicorn')
    return HttpResponse(f"{request} - это ответ")
