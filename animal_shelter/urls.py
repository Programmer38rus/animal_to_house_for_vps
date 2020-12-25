# from django.contrib import admin
from django.urls import path
# Импортируем Class-base view
from .views import PetsList, PetsDetailView, KindList, AboutUs, Map, index, kind_list, pet_detail

#Модули для МЕДИА файлов
from django.conf import settings
from django.conf.urls.static import static

app_name = "animal_shelter"

urlpatterns = [
    # path('', PetsList.as_view()),
    path('', index, name='index'),
    # path('<int:pk>', PetsDetailView.as_view(), name='pet-detail'),
    path('<int:pk>', pet_detail, name='pet-detail'),
    # path('k/<str:kind>', KindList.as_view(), name='finder_by_kind'),
    path('k/<str:kind>', kind_list, name='finder_by_kind'),
    path('about/', AboutUs.as_view()),
    path('map/', Map.as_view(), name='map'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

