from rest_framework import serializers
from .models import LegalFile, LegalFileContactRole
from contacts.serializers import ContactSerializer, ContactSubtypeSerializer


class LegalFileContactRoleSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    subtype = ContactSubtypeSerializer()

    class Meta:
        model = LegalFileContactRole
        fields = ('id', 'contact', 'subtype')


class LegalFileSerializer(serializers.ModelSerializer):
    contactrole = LegalFileContactRoleSerializer(many=True)

    class Meta:
        model = LegalFile
        fields = ('id', 'code', 'description', 'contactrole')
