from django.db import models
from django.core.exceptions import ValidationError


def validate_name(value):
    if len(value) < 3:  # Your conditions here
        raise ValidationError("Name Should be minimum 3 characters")


class Musicians(models.Model):
    name = models.CharField(max_length=50, validators=[validate_name])
    musician_type = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "musicians"


def validate_number(value):
    if value < 100 or value > 1000:  # Your conditions here
        raise ValidationError("Value must be in between 100 to 1000")


def validate_album_name(value):
    if len(value) < 5:  # Your conditions here
        raise ValidationError("Album Name Should be minimum 5 characters")


class Music_Albums(models.Model):
    musician = models.ForeignKey(Musicians, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=100, validators=[validate_album_name])
    date_of_release = models.DateField(auto_now_add=True)
    genre = models.CharField(max_length=30, blank=True, null=True)
    price = models.IntegerField(validators=[validate_number])
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.album_name

    class Meta:
        db_table = "music_albums"
