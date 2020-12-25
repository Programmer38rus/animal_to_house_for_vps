from django.apps import AppConfig


class AnimalShelterConfig(AppConfig):
    name = 'animal_shelter'

    def ready(self):
        import animal_shelter.signals
