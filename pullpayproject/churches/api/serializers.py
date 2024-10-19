from rest_framework.serializers import ModelSerializer
from ..models import User

class PostSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = ('user_first_name', 'user_last_name', 'email', 'phone_number', 'address', "payment_method", 'churches')