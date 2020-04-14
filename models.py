from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length= 50)
    description = models.CharField(max_length=40)
    price = models.FloatField()
    discount = models.FloatField()
    category = models.CharField(max_length=20)
    created_at = models.DateField()
    product_image=models.ImageField(upload_to ='shopify/images',default = '')
    def __str__(self):
        return "%i : Name is %s,Description %s,Price %f,Discount %f,Category %s,created_at %s" %(self.id,self.name,self.description,self.price,self.discount,self.category,self.created_at)