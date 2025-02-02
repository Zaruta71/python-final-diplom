from django.dispatch import receiver
from easy_thumbnails.signals import saved_file

from .tasks import generate_thumbnails


@receiver(saved_file)
def generate_thumbnails_async(sender, fieldfile, **kwargs):
    generate_thumbnails.delay(
        class_path="{}.{}".format(sender.__module__, sender.__name__),
        pk=fieldfile.instance.pk,
        field=fieldfile.field.name,
    )
