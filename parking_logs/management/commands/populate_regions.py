from django.core.management.base import BaseCommand
from parking_logs.models.models import Region


class Command(BaseCommand):
    help = 'Populates the database with default regions if they do not exist'

    def handle(self, *args, **kwargs):
        # Check if there are already regions in the database
        if Region.objects.exists():
            self.stdout.write(
                self.style.SUCCESS("Regions are already populated."))
        else:
            # List of default region names
            regions = ["A", "B", "C", "D", "E", "F", "G"]
            for region_name in regions:
                Region.objects.create(name=region_name)
            self.stdout.write(
                self.style.SUCCESS("Successfully populated default regions."))
