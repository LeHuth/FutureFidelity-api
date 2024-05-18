from django.urls import path
from rest_framework.routers import DefaultRouter

from music.views import MusicListView, VinylDetailView, StreamAudioView

router = DefaultRouter()

#router.register('vinyls', MusicListView, basename='vinyls')

urlpatterns = (
        [
            path('vinyls/get/<slug:id>', VinylDetailView.as_view(), name='vinyls'),
            path('vinyls/all', MusicListView.as_view({'get': 'list'}), name='vinyls'),
            path('stream-audio/<int:track_id>', StreamAudioView.as_view(), name='stream_audio')

        ] + router.urls)
