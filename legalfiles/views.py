from rest_framework import viewsets
from .models import LegalFile, LegalFileContactRole
from .serializers import LegalFileSerializer, LegalFileContactRoleSerializer


class LegalFileViewSet(viewsets.ModelViewSet):
    model = LegalFile
    serializer_class = LegalFileSerializer
    queryset = LegalFile.objects.all()


class LegalFileContactRoleViewSet(viewsets.ModelViewSet):
    model = LegalFileContactRole
    serializer_class = LegalFileContactRoleSerializer
    queryset = LegalFileContactRole.objects.all()
