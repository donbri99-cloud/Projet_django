from django.db import models

# Create your models here.

class article(models.Model):
    
    


    """
        str est surcharge
        meta = c'est les info apropos des models
        migration:
            --py manage.py makemigrations
            --py manage.py migrate
    """
class articles(models.Model):
    
    name = models.CharField(max_length = 150,)
    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    status= models.CharField(max_length=50, verbose_name="Statut")
    
    description = models.TextField(blank=True, verbose_name="Description")
    
    #image = models.ImageField(upload_to="products/", blank=True, null=True, verbose_name="Image / Icone")
    
    # id : table Category
    #articles = models.ForeignKey(articles, on_delete=models.CASCADE, related_name="products", verbose_name="Category")
    
    class Meta:
        verbose_name = "article"
        verbose_name_plural = "articles"
    
    def __str__(self):
         return self.name