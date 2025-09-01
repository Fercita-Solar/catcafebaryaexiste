from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=100)
    image_file = models.ImageField(upload_to='imagenes/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
        return self.question

class AboutUs(models.Model):
    content = models.TextField()

    def __str__(self):
        return "About Us Content"