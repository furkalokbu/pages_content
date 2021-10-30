from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField

class Page(models.Model):

    url = models.CharField(_('url'), max_length=255)
    title = models.CharField(_('title'), max_length=255, blank=True)
    show_title = models.BooleanField(_('show title?'), default=True)
    enabled = models.BooleanField(_('enabled?'), default=True)
    content = RichTextField(_('content'), blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.url

    class Meta:
        verbose_name = _('page')
        verbose_name_plural = _('pages')
    