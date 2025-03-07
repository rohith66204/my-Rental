from django.db import models
from django.contrib.auth.models import AbstractUser

class Rent(models.Model):
    fullname = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.IntegerField()
    desired = models.DateField()
    message = models.CharField(max_length=255)

class buy(models.Model):
    fullname = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.CharField(max_length=50)

class sigin(AbstractUser):
    phone = models.CharField(max_length=15, unique=True, blank=True, null=True)

HOUSE_TYPE_CHOICES = [
    ("single_family", "Single Family House"),
    ("villa", "Villa"),
    ("farmhouse", "Farmhouse"),
    ("land", "Land"),
    ("apartment", "Apartment"),
    ("condo", "Condo"),
    ("townhouse", "Townhouse"),
    ("bungalow", "Bungalow"),
    ("duplex", "Duplex"),
    ("penthouse", "Penthouse"),
    ("studio", "Studio"),
    ("cottage", "Cottage"),
    ("mansion", "Mansion"),
]


class sell(models.Model):
    user = models.ForeignKey(sigin, on_delete=models.CASCADE)
    housename = models.CharField(max_length=30)
    price = models.IntegerField()
    bedrooms = models.IntegerField(default=1, null=True, blank=True)
    bathrooms = models.IntegerField(default=1, null=True, blank=True)
    location = models.CharField(max_length=30)
    square_feet = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=1255, null=True, blank=True)

    house_type = models.CharField(max_length=50, choices=HOUSE_TYPE_CHOICES)

    property_history = models.TextField(null=True, blank=True)
    
    # New field for built year
    built_year = models.IntegerField(null=True, blank=True, verbose_name="Built Year")

    image = models.ImageField(upload_to='images/')
    outside_image = models.ImageField(upload_to='houses/other_images/', null=True, blank=True)
    livingroom_image = models.ImageField(upload_to='houses/other_images/', null=True, blank=True)
    bedroom_image = models.ImageField(upload_to='houses/other_images/', null=True, blank=True)
    kitchen_image = models.ImageField(upload_to='houses/other_images/', null=True, blank=True)
    bathroom_image = models.ImageField(upload_to='houses/other_images/', null=True, blank=True)
    additional_image1 = models.ImageField(upload_to='houses/other_images/', null=True, blank=True)
    additional_image2 = models.ImageField(upload_to='houses/other_images/', null=True, blank=True)

    def __str__(self):
        return self.housename
    

class Saved(models.Model):
    user = models.ForeignKey('sigin', on_delete=models.CASCADE)
    house = models.ForeignKey('sell', on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('user', 'house') 

class PropertyUsage(models.Model):
    house = models.ForeignKey(sell, on_delete=models.CASCADE, related_name='usage_history')
    user = models.CharField(max_length=100, verbose_name="User Name")
    starting_year = models.IntegerField(verbose_name="Starting Year")
    ending_year = models.IntegerField(verbose_name="Ending Year")
    price = models.IntegerField(verbose_name="Price Paid")

    def __str__(self):
        return f"{self.user} ({self.starting_year}-{self.ending_year}) - ${self.price}"
    


# admin
# models.py (add this to the end)
class AgentInquiry(models.Model):
    house = models.ForeignKey(sell, on_delete=models.CASCADE, related_name='inquiries')
    seller = models.ForeignKey(sigin, on_delete=models.CASCADE, related_name='inquiries')
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry for {self.house.housename} by {self.name}"