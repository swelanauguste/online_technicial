from django.db import models


class Form(models.Model):
    form = models.CharField(max_length=50, unique=True)
    doc = models.FileField(upload_to="forms")
    
    def __str__(self):
        return self.form
