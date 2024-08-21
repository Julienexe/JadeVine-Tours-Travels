from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150)
    imageUrl = models.CharField(max_length=250)
    description = models.TextField(default="Description", null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=100)
    imageUrl = models.CharField(max_length=250)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name="places")
    description = models.TextField()
    price = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Testimonial(models.Model):
    class Gender(models.TextChoices):
        MALE = "male","male"
        FEMALE = "female","female"

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="testimonials")
    country = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    gender= models.CharField(max_length=10,choices=Gender.choices)

    testimonial = models.TextField()

    def __str__(self) -> str:
        return self.name