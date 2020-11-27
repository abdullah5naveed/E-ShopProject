from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)


    @staticmethod
    def get_all_categories():
        return Category.objects.all()


    def __str__(self):
        return self.name




class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0)
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=150, default="")
    image = models.ImageField(upload_to="media/product/img/")

    @staticmethod
    def get_all_products():
        return Product.objects.all()


