from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class sitedevlittlegirls(models.Model):
    nome_site = models.CharField(max_length=255)
    slug_site =  models.SlugField(max_length=255, unique=True) 
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField() 
    created = models.DateTimeField(auto_now_add=True)
    link_site = models.CharField(max_length=255)


# Slug é a url do site que ao clicar será encaminhado
# body = Descrição do site que está sendo indicado