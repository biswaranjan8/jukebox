from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from myapp.serializers import MusiciansSerializer, Music_AlbumsSerializer, MusiciansUpdateSerialier, \
    Music_AlbumsUpdateSerialier
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser
from .models import Musicians, Music_Albums


# Musicians (create,list show, update, delete, retrieve)
class MusiciansViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = MusiciansSerializer
    queryset = Musicians.objects.all()


# Music Album (create,list show, update, delete, retrive)
class Music_AlbumsViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = Music_AlbumsSerializer
    queryset = Music_Albums.objects.all()


class MusicAlbumRetrieve(generics.ListAPIView):
    serializer_class = Music_AlbumsSerializer

    def get_queryset(self):
        return Music_Albums.objects.all().order_by("date_of_release")


class MusicAlbumFilterPrice(generics.ListAPIView):
    serializer_class = Music_AlbumsSerializer

    def get_queryset(self):
        i = ""
        c = 61
        j = ""
        while (j != "/"):
            j = str(self.request)[c]
            i += str(self.request)[c]
            c += 1
        id = i.replace("/", "")
        return Music_Albums.objects.filter(musician_id=id).order_by("price")


######################## Generic type view  ##########################

class MusicAlbumFilter(generics.ListAPIView):
    serializer_class = Music_AlbumsSerializer


    def get_queryset(self):
        i = ""
        c = 55
        j = ""
        while (j != "/"):
            j = str(self.request)[c]
            i += str(self.request)[c]
            c += 1
        name = i.replace("%20", " ")
        name = name.replace("/","")
        return Music_Albums.objects.filter(album_name=name).order_by("musician__name")