from django.db import models

# Create your models here.


class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# 1. Muchos a uno  (ForeignKey)
class ArticulosBlog(models.Model):
    """Model definition for MODELNAME."""
    title_blog = models.CharField(max_length = 250)
    articule_url = models.SlugField()
    body = models.TextField()
    data_create = models.DateField(auto_now_add=True)
    article_modificado = models.DateField(auto_now=True)
    imagen_article = models.FileField(upload_to='blog/articles', max_length = 100)
    reporter = models.ForeignKey(Reporter, verbose_name="Reportero", on_delete=models.CASCADE, null=True)

    class Meta:
        """Meta definition for MODELNAME."""
        verbose_name = 'ArticulosBlog'
        verbose_name_plural = 'ArticulosBlogs'

    # def __str__(self):
    #     """Unicode representation of MODELNAME."""
    #     pass





# Relaciones fundamentales en las tablas de la DB
# 1. Muchos a uno  (ForeigKey)
# 2. Muhos a muchos (MoretoMore)
# 3 Uno a uno (OnetoOne)



# 3 Uno a uno (OnetoOne)
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.name} the place"


class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return f'the restaurant {self.place.name}'


class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s the waiter at %s" % (self.name, self.restaurant)





# 2. Muhos a muchos (MoretoMore)
class Publication(models.Model):
    title = models.CharField(max_length=30)
    descripcion = models.TextField()
    data_create = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Newsletter(models.Model):
    newsletter = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.newsletter