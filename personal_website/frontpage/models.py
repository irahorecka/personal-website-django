from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    bike_make = models.CharField(max_length=100)
    bike_make_url = models.CharField(max_length=256)
    bike_model = models.TextField()
    bike_img = models.ImageField(upload_to='bike_imgs/')  # currently not working...
    content = models.TextField()  
    date_posted = models.DateTimeField(default=timezone.now)  # don't call func yet
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.bike_make