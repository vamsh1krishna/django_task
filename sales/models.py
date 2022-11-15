from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category

class Products(models.Model):
    regions=(
        ("North","North"),
        ("South","South"),
        ("East","East"),
        ("West","West")
    )
    region = models.CharField(choices=regions,max_length=5)
    city = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    product = models.CharField(max_length=255)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10,decimal_places=2)
    ordered_date = models.DateField(auto_now_add=True)


# Create your models here.
