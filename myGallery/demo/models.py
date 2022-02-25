from django.db import models
from django.utils.safestring import mark_safe 
from PIL import Image as Im                  # new

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='pics')

    def save(self):                        # new
        super().save()

        img = Im.open(self.photo.path)

        # resize it
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.photo.path)


    def image_tag(self):                     
        return mark_safe('<img src="/../../media/%s" width="150" height="150" />' % (self.photo))


