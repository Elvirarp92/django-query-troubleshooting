from django.db import models
from contacts.models import Contact, ContactSubtype


class LegalFileContactRole(models.Model):
    contact = models.ForeignKey(
        Contact, on_delete=models.DO_NOTHING, blank=True, related_name='legal_file_contact')
    subtype = models.ForeignKey(ContactSubtype, on_delete=models.DO_NOTHING,
                                related_name='legal_file_contact_role', null=True)


class LegalFile(models.Model):
    code = models.CharField(max_length=25)
    description = models.CharField(max_length=255)
    contactrole = models.ManyToManyField(
        LegalFileContactRole, blank=True, related_name='contactroles')
