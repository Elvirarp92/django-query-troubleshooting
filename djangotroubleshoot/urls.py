"""djangotroubleshoot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from rest_framework import routers
from contacts.views import ContactViewSet, ContactSubtypeViewSet
from legalfiles.views import LegalFileViewSet, LegalFileContactRoleViewSet

router = routers.DefaultRouter()

router.register(r'contacts', ContactViewSet, basename='contact')
router.register(r'contact_subtypes', ContactSubtypeViewSet,
                basename='contact-subtype')
router.register(r'legalfiles', LegalFileViewSet, basename='legalfile')
router.register(r'legalfile_contactroles',
                LegalFileContactRoleViewSet, basename='legalfile-contactrole')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'api/v1/', include((router.urls, 'api-v1'), namespace='api-v1'))
]
