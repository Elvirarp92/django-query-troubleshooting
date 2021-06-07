import factory
from faker import Faker
from .models import Contact, ContactSubtype

fake = Faker('es_ES')


class ContactFactory(factory.django.DjangoModelFactory):
    name = fake.first_name_nonbinary()
    surname_1 = fake.last_name()
    surname_2 = fake.last_name()

    class Meta:
        model = Contact


class ContactSubtypeFactory(factory.django.DjangoModelFactory):
    name = fake.unique.word()

    class Meta:
        model = ContactSubtype
