from django.db import models




class Marketplace(models.Model):
    image = models.ImageField()
    material = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = models.TextField()
    provider = models.CharField(max_length=100)
    contact = models.PositiveIntegerField(max_length=100)



    def __str__(self):
        return self.material