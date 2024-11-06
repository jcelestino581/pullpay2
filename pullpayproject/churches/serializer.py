from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()


class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Church
        fields = ["church_name_text", "size_int", "church_type_text"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "user_first_name",
            "user_last_name",
            "email",
            "phone_number",
            "address",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user
