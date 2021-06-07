from django.core.management import BaseCommand, CommandError
from django.db import transaction
from contacts.factories import ContactFactory, ContactSubtypeFactory
from legalfiles.factories import LegalFileFactory, LegalFileContactRoleFactory
from contacts.models import Contact, ContactSubtype
from legalfiles.models import LegalFile, LegalFileContactRole

from faker import Faker


class Command(BaseCommand):
    help = "Populate the database with sample data. Generates legal files, contact roles, contacts and contact subtypes."

    def add_arguments(self, parser):
        parser.add_argument(
            '--clean',
            help='Wipe existing data from the DB before loading fixtures.',
            action='store_true',
            default=False
        )

        parser.add_argument(
            '--number',
            help='Specify number of entries generated.',
            type=int,
            default=1
        )


    def _clean_db(self):
        for model in (Contact, ContactSubtype, LegalFile, LegalFileContactRole):
            model.objects.all().delete()

    def _load_fixtures(self, number):
        for x in range (0, number-1):
            contactrole1 = LegalFileContactRoleFactory.create()
            LegalFileFactory.create(contactrole=[contactrole1])

    def handle(self, *args, **options):
        try:
            with transaction.atomic():
                if options['clean']:
                    self._clean_db()
                    self.stdout.write('Database cleaned. On to populating...')

                number = options.get('number')
                self._load_fixtures(number)
                self.stdout.write('Population finished.')

        except Exception as e:
            raise CommandError(
                f"{e}\n\nTransaction was not committed due to the above exception.")
