from django.db import models

# Create your models here.
class blogPost(models.Model):
    id =models.AutoField
    title = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    category = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to="images/", default="")
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    


class mainedits(models.Model):
    title_of_the_site =models.CharField(max_length=200, unique=True, default="")
    site_image = models.ImageField(upload_to="images/", default="")
    def __str__(self):
        return self.title_of_the_site
