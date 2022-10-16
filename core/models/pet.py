from django.db import models

class Pet(models.Model):
    age = models.IntegerField(blank=True, null=True)
    display_name = models.CharField(max_length=25)
    description = models.TextField()
    avatar = models.FileField()
    # Gender choices
    MALE = "M"
    FEMALE = "F"
    GENDER_CHOICES = [
        (MALE, "Male"),
        (MALE, "Female"),
    ]
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default=MALE,
    ) 

    def __str__(self) -> str:
        return str(self.display_name)