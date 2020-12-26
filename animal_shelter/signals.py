from django.db.models.signals import (
    post_save,
    post_delete,
    post_init,
    m2m_changed

)
from django.dispatch import receiver

from animal_shelter.models import Pet, Kind

from django.core.cache import cache

@receiver(post_save, sender=Pet)
def pet_save(sender, instance, **kwargs):
    cache.set('Pets', sender.objects.all().select_related())


@receiver(post_delete, sender=Pet)
def pet_delete(sender, **kwargs):
    cache.set('Pets', sender.objects.all().select_related())

# сигналы для видов животных
@receiver(post_save, sender=Kind)
def kind_save(sender, instance, **kwargs):
    cache.set('kind', sender.objects.all().select_related())


@receiver(post_delete, sender=Kind)
def kind_delete(sender, **kwargs):
    cache.set('kind', sender.objects.all().select_related())
