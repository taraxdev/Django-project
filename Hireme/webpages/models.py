from django.db import models

# Create your models here.
class Slider(models.Model):
    headline = models.CharField(max_length = 225)
    subtitle = models.CharField(max_length = 225)
    button_text = models.CharField(max_length = 225)
    photo = models.ImageField(upload_to = 'media/slider/%Y')
    created_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.headline