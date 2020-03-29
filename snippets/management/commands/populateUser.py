import datetime
import random

from django.core.management.base import BaseCommand

from snippets.models import User,Activity


class Command(BaseCommand):
    help = "Save randomly generated User record values."

    def get_date(self):
        # Naively generating a random date
        day = random.randint(1, 28)
        month = random.randint(1, 12)
        year = random.randint(2014, 2020)
        return datetime.date(year, month, day)

    def handle(self, *args, **options):
        records = []
        for _ in range(100):
            kwargs = {
                'NId': self.get_date(),
                'closing_record': random.randint(1, 1000)
            }
            record = StockRecord(**kwargs)
            records.append(record)
        StockRecord.objects.bulk_create(records)
        self.stdout.write(self.style.SUCCESS('Stock records saved successfully.'))
