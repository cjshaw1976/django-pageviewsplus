from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist


class HitCount(models.Model):
	try:
		created = models.DateTimeField(_('Created'), auto_now_add=True, editable=False)
		modified = models.DateTimeField(_('Modified'), auto_now=True, editable=False)
		url = models.CharField(_('URL'), max_length=2000)
		hits = models.PositiveIntegerField(_('Hits'), default=0)

	except ObjectDoesNotExist:
		print("problem with pageviewsplus hitcount table")


	class Meta:
		ordering = ('-created', '-modified')
		get_latest_by = 'created'


class AllRecords(models.Model):
	try:
		created = models.DateTimeField(_('Created'), auto_now_add=True, editable=False)
		modified = models.DateTimeField(_('Modified'), auto_now=True, editable=False)
		url = models.CharField(_('URL'), max_length=2000)
		ip = models.GenericIPAddressField(_('IP'))
		browser = models.CharField(_('Browser'), blank=True, max_length=128)
		os = models.CharField(_('OS'), blank=True, max_length=128)
		device = models.CharField(_('Device'), blank=True, max_length=128)
		count = models.PositiveIntegerField(_('Count'), default=0)

	except ObjectDoesNotExist:
		print("problem with pageviewsplus allrecords table")


	class Meta:
		ordering = ('-created', '-modified')
		get_latest_by = 'created'
