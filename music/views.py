from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.generics import RetrieveAPIView
from music.models import Vinyl
from music.serializers import VinylListSerializer, VinylDetailSerializer


# Create your views here.

class MusicListView(ViewSet):
    queryset = Vinyl.objects.all()
    serializer_class = VinylListSerializer

    def list(self, request):
        vinyls = self.queryset
        return Response(self.serializer_class(vinyls, many=True).data)


class VinylDetailView(RetrieveAPIView):
    queryset = Vinyl.objects.all()
    serializer_class = VinylDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
