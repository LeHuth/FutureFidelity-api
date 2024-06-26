from django.db import models

from products.models import Product


# Create your models here.

class Label(models.Model):
    name = models.CharField(max_length=100)
    founded = models.DateField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    label = models.ForeignKey(Label, related_name='artists', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


track_locations = (
    ('A1', 'A1'),
    ('A2', 'A2'),
    ('A3', 'A3'),
    ('A4', 'A4'),
    ('A5', 'A5'),
    ('B1', 'B1'),
    ('B2', 'B2'),
    ('B3', 'B3'),
    ('B4', 'B4'),
    ('B5', 'B5'),
    ('C1', 'C1'),
    ('C2', 'C2'),
    ('C3', 'C3'),
    ('C4', 'C4'),
    ('C5', 'C5'),
    ('D1', 'D1'),
    ('D2', 'D2'),
    ('D3', 'D3'),
    ('D4', 'D4'),
    ('D5', 'D5'),
)


class Track(models.Model):
    name = models.CharField(max_length=100)
    duration = models.TimeField()
    audio = models.FileField(upload_to='vinyls/tracks/', null=True, blank=True)
    vinyl = models.ForeignKey('Vinyl', related_name='tracks', on_delete=models.CASCADE)
    coverart = models.ImageField(upload_to='vinyls/tracks/coverart', null=True, blank=True)
    track_locations = models.CharField(max_length=2, choices=track_locations, null=True, blank=True)

    def __str__(self):
        return self.name + ' - ' + self.vinyl.artist.name


class Vinyl(Product):
    artist = models.ForeignKey(Artist, related_name='vinyls', on_delete=models.CASCADE)
    album = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, related_name='vinyls', on_delete=models.CASCADE)
    release_date = models.DateField()
    label = models.ForeignKey(Label, related_name='vinyls', on_delete=models.CASCADE)
    condition = models.CharField(max_length=100)
    speed = models.IntegerField()
    size = models.IntegerField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='vinyls/images/')

    def __str__(self):
        return f'{self.artist} - {self.album}'
