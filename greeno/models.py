from django.db import models

from ckeditor.fields import RichTextField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Contact(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    email = models.EmailField(max_length=225, unique=True, null=True, blank=True)
    message = RichTextField(null=True, blank=True)
    phone = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"
    

class Gallery(BaseModel):
    image = models.ImageField(upload_to='gallery', null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.id}"
    

class OurWonderfulPlants(BaseModel):
    name = models.CharField(max_length=225, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='plants', null=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"
    