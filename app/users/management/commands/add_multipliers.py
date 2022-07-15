from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from overtime.models import Multiplier


class Command(BaseCommand):
    help = "Add Multipliers"

    def handle(self, *args, **options):
        Multiplier.objects.get_or_create(multiplier=float(1.5))
        Multiplier.objects.get_or_create(multiplier=float(2.0))
        Multiplier.objects.get_or_create(multiplier=float(2.5))
        Multiplier.objects.get_or_create(multiplier=float(3.0))
