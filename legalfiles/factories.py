import factory
from faker import Faker

from contacts.factories import ContactFactory, ContactSubtypeFactory
from .models import LegalFile, LegalFileContactRole

fake = Faker('es_ES')


class LegalFileContactRoleFactory(factory.django.DjangoModelFactory):
    contact = factory.SubFactory(ContactFactory)
    subtype = factory.SubFactory(ContactSubtypeFactory)

    class Meta:
        model = LegalFileContactRole


class LegalFileFactory(factory.django.DjangoModelFactory):
    code = fake.unique.pystr(max_chars=20)
    description = fake.sentence(nb_words=7)

    class Meta:
        model = LegalFile

    @factory.post_generation
    def contactrole(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for contactrole in extracted:
                self.contactrole.add(contactrole)
