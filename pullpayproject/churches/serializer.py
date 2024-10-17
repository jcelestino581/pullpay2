from rest_framework import serializers
from .models import *


class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Church
        fields = ["church_name_text", "size_int", "church_type_text"]
