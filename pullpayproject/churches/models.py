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

PAYMENT_TYPE_CHOICES = [
    ("VISA", "Visa"),
    ("MASTERCARD", "Mastercard"),
    ("DISCOVER", "Discover"),
    ("AMEX", "Amex"),
    ("NONE", "None"),
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

    def __str__(self):
        return self.church_name_text


class Campus(models.Model):
    campus_name_text = models.CharField(max_length=200)
    size_int = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],  # Ensures the integer is non-negative
    )
    churches = models.ForeignKey(
        Church, on_delete=models.CASCADE, related_name="campus"
    )


class User(models.Model):
    user_first_name = models.CharField(max_length=200)
    user_last_name = models.CharField(max_length=200)
    email = models.EmailField(
        max_length=254, unique=True
    )  # Adds an email field with validation
    phone_number = models.CharField(
        max_length=15, blank=True, null=True
    )  # Adds a phone number field
    address = models.CharField(
        max_length=500, blank=True, null=True
    )  # Optional address field
    payment_method = models.CharField(
        max_length=200,
        choices=PAYMENT_TYPE_CHOICES,
        default="NONE",  # Ensure default is one of the choices
    )
    # Many-to-Many relationship with Church
    churches = models.ManyToManyField(Church, related_name="user")

    def __str__(self):
        return f"{self.user_first_name} {self.user_last_name}"
