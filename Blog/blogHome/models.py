from django.db import models

# Create your models here.


class ArticulosBlog(models.Model):
    """Model definition for MODELNAME."""
    title_blog = models.CharField(max_length = 250)
    articule_url = models.SlugField()
    body = models.TextField()
    data_create = models.DateField(auto_now_add=True)
    article_modificado = models.DateField(auto_now=True)
    imagen_article = models.FileField(upload_to='blog/articles', max_length = 100)


    class Meta:
        """Meta definition for MODELNAME."""
        verbose_name = 'ArticulosBlog'
        verbose_name_plural = 'ArticulosBlogs'

    # def __str__(self):
    #     """Unicode representation of MODELNAME."""
    #     pass
