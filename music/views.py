import os
import re
from django.utils.http import http_date
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.generics import RetrieveAPIView
from music.models import Vinyl, Track
from music.serializers import VinylListSerializer, VinylDetailSerializer, TrackSerializer
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Default chunk size for streaming audio
DEFAULT_CHUNK_SIZE = 262144  # 256 KB


class MusicListView(ViewSet):
    """
    A viewset for viewing a list of all vinyl records.
    """
    queryset = Vinyl.objects.all()
    serializer_class = VinylListSerializer

    def list(self, request):
        """
        Returns a list of all vinyl records.
        """
        vinyls = self.queryset
        return Response(self.serializer_class(vinyls, many=True).data)


class VinylDetailView(RetrieveAPIView):
    """
    A view for viewing the details of a single vinyl record.
    """
    queryset = Vinyl.objects.all()
    serializer_class = VinylDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def retrieve(self, request, *args, **kwargs):
        """
        Returns the details of a single vinyl record.
        """
        return super().retrieve(request, *args, **kwargs)


class StreamAudioView(RetrieveAPIView):
    """
    A view for streaming audio tracks.
    """
    queryset = Track.objects.all()
    lookup_field = 'track_id'
    lookup_url_kwarg = 'track_id'
    serializer_class = TrackSerializer

    def retrieve(self, request, *args, **kwargs):
        """
        Streams an audio track. Supports range requests for efficient streaming.
        """
        track_id = kwargs.get('track_id')
        track = get_object_or_404(Track, id=track_id)
        file_path = track.audio.path

        file_size = os.path.getsize(file_path)
        range_header = request.headers.get('Range')
        if not range_header:
            return HttpResponse(
                open(file_path, 'rb').read(),
                content_type='audio/mpeg',
                status=200,
                headers={
                    'Content-Length': str(file_size),
                    'Content-Disposition': f'inline; filename="{track.name}"'
                }
            )

        range_match = re.match(r'bytes=(\d+)-(\d*)', range_header)
        if not range_match:
            return HttpResponse(status=400)

        first_byte, last_byte = range_match.groups()
        first_byte = int(first_byte)
        if last_byte:
            last_byte = int(last_byte)
        else:
            last_byte = first_byte + DEFAULT_CHUNK_SIZE - 1
            if last_byte >= file_size:
                last_byte = file_size - 1

        length = last_byte - first_byte + 1

        with open(file_path, 'rb') as f:
            f.seek(first_byte)
            data = f.read(length)

        response = HttpResponse(
            data,
            content_type='audio/mpeg',
            status=206
        )
        response['Content-Range'] = f'bytes {first_byte}-{last_byte}/{file_size}'
        response['Accept-Ranges'] = 'bytes'
        response['Content-Length'] = str(length)
        response['Content-Disposition'] = f'inline; filename="{track.name}"'
        response['Cache-Control'] = 'no-cache'

        return response
