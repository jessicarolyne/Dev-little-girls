from django.db import models

# Create your models here.

from django.db import models
from django.db.models import permalink

# Create your models here.

class Site(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    url = models.SlugField(max_length=100, unique=True)
    corpo = models.TextField()


    def __unicode__(self):
        return '%s' % self.titulo

    @permalink
    def get_url_absoluta(self):
        return ('ver_cursos', None, { 'slug': self.url })

