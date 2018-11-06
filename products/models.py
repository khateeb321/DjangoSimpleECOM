from django.db import models

CATEGORY_CHOICES = (
    ('1', 'Fruit'),
    ('2', 'Vegetable'),
    ('3', 'Other'),
)

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default=1)
    image = models.ImageField(upload_to='images')
    uploadedBy = models.CharField(blank=True, max_length=254, default='admin')

    def __str__(self):
        return str(self.image)
