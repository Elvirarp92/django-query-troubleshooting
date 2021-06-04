from rest_framework import serializers
from .models import Contact, ContactSubtype


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'name', 'surname_1', 'surname_2')


class ContactSubtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSubtype
        fields = ('id', 'name')
