from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from joblib import load

# Create your models here.
GENDER = ((0, "Female"), (1, "Male"))


class Data(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(13), MaxValueValidator(19)], null=True
    )
    height = models.PositiveIntegerField(null=True)
    sex = models.PositiveIntegerField(choices=GENDER, null=True)
    prediction = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ml_model = load("models\\model.joblib")
        self.prediction = ml_model.predict([[self.age, self.height, self.sex]])
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return str(self.name)
