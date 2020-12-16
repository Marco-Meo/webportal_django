from faq.models import Faq
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import FaqSerializer


class FaqViewSet(viewsets.ModelViewSet):
    serializer_class = FaqSerializer
    queryset = Faq.objects.all().order_by('-id')
    permission_classes = [permissions.IsAuthenticated]