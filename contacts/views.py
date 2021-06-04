from rest_framework import viewsets
from .models import Contact, ContactSubtype
from .serializers import ContactSerializer, ContactSubtypeSerializer


class ContactViewSet(viewsets.ModelViewSet):
    model = Contact
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ContactSubtypeViewSet(viewsets.ModelViewSet):
    model = ContactSubtype
    serializer_class = ContactSubtypeSerializer
    queryset = ContactSubtype.objects.all()
