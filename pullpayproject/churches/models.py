from django.db import models
from django.core.validators import MinValueValidator

# Define choices before the model
CHURCH_TYPE_CHOICES = [
    ("BAPTIST", "Baptist"),
    ("CATHOLIC", "Catholic"),
    ("METHODIST", "Methodist"),
    ("PRESBYTERIAN", "Presbyterian"),
    ("NON_DENOMINATIONAL", "Non-Denominational"),
    # Add more choices as needed
]


class Church(models.Model):
    church_name_text = models.CharField(max_length=200)
    size_int = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],  # Ensures the integer is non-negative
    )
    church_type_text = models.CharField(
        max_length=200,
        choices=CHURCH_TYPE_CHOICES,
        default="NON_DENOMINATIONAL",  # Ensure default is one of the choices
    )
