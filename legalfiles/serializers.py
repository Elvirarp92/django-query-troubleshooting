from rest_framework import serializers
from .models import LegalFile, LegalFileContactRole
from contacts.serializers import ContactSerializer, ContactSubtypeSerializer


class EagerLoadingMixin:
    @classmethod
    def setup_eager_loading(cls, queryset):
        if hasattr(cls, "SELECT_RELATED"):
            queryset = queryset.select_related(*cls.SELECT_RELATED)
        if hasattr(cls, "PREFETCH_RELATED"):
            queryset = queryset.prefetch_related(*cls.PREFETCH_RELATED)
        return queryset


class LegalFileContactRoleSerializer(serializers.ModelSerializer, EagerLoadingMixin):
    contact = ContactSerializer()
    subtype = ContactSubtypeSerializer()
    SELECT_RELATED = ('contact', 'subtype',)

    class Meta:
        model = LegalFileContactRole
        fields = ('id', 'contact', 'subtype')


class LegalFileSerializer(serializers.ModelSerializer, EagerLoadingMixin):
    contactrole = LegalFileContactRoleSerializer(many=True)
    PREFETCH_RELATED = ('contactrole__contact', 'contactrole__subtype')

    class Meta:
        model = LegalFile
        fields = ('id', 'code', 'description', 'contactrole')
