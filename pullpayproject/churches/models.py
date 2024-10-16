from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
import uuid

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


class Administrator(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a regular user with the given email and password.
        """
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)

    def delete_model(self, request, obj):
        # Remove all related churches before deleting the user
        obj.churches.clear()  # Clear the ManyToMany relationship
        super().delete_model(request, obj)  # Proceed with the deletion of the user


class User(AbstractBaseUser, PermissionsMixin):
    user_first_name = models.CharField(max_length=200)
    user_last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, unique=True)  # Used as the username
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    payment_method = models.CharField(
        max_length=200,
        choices=PAYMENT_TYPE_CHOICES,
        default="NONE",
    )
    churches = models.ManyToManyField("Church", related_name="users")

    # Fields required by Django's authentication system
    is_active = models.BooleanField(default=True)  # To deactivate a user account
    is_staff = models.BooleanField(default=False)  # To allow access to the admin site
    date_joined = models.DateTimeField(auto_now_add=True)

    # Specify the email field as the username for authentication
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "user_first_name",
        "user_last_name",
    ]  # Fields that will be required when creating a superuser

    objects = Administrator()

    def __str__(self):
        return self.email  # What will be shown when printing or logging the user


class Transaction(models.Model):
    transaction_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    amount = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],  # Ensures the integer is non-negative
    )
    userKey = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Transaction ID: {self.transaction_id} by {self.userKey.user_first_name}: ${self.amount}"
