from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title

class AboutImage(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name="images")
    image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return f"Image for {self.about.title}"