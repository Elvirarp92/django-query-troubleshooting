from rest_framework import viewsets
from .models import LegalFile, LegalFileContactRole
from .serializers import LegalFileSerializer, LegalFileContactRoleSerializer


class LegalFileViewSet(viewsets.ModelViewSet):
    model = LegalFile
    serializer_class = LegalFileSerializer
    queryset = LegalFile.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.serializer_class.setup_eager_loading(queryset)
        return queryset


class LegalFileContactRoleViewSet(viewsets.ModelViewSet):
    model = LegalFileContactRole
    serializer_class = LegalFileContactRoleSerializer
    queryset = LegalFileContactRole.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.serializer_class.setup_eager_loading(queryset)
        return queryset