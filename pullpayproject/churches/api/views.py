#brams Junk
from ..models import Church, User
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


#End BramJunk