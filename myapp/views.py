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
        print(str(self.request)[61])
        return Music_Albums.objects.filter(musician_id=int(str(self.request)[-3])).order_by("price")

# class MusicianList(generics.ListCreateAPIView):
#     queryset = Musicians.objects.all()
#     serializer_class = MusiciansSerializer
#
#     # def list(self, request):
#     #     # Note the use of `get_queryset()` instead of `self.queryset`
#     #     queryset = self.get_queryset()
#     #     serializer = MusiciansSerializer(queryset, many=True)
#     #     if Musicians.objects.filter(name="Rakesh Shoo").exists():
#     #         return Response(serializer.data)
#     #     return Response("not a user")
#
#
# class Music_AlbumsList(generics.ListCreateAPIView):
#     queryset = Music_Albums.objects.all()
#     serializer_class = Music_AlbumsSerializer
#
#
# class MusiciansUpdateAPIView(generics.RetrieveUpdateAPIView):
#     queryset = Musicians.objects.all()
#     serializer_class = MusiciansUpdateSerialier
#     lookup_field = 'id'
#
#     def get_object(self):
#         id = self.kwargs["id"]
#         return get_object_or_404(Musicians, id=id)
#
#     def post(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#
# class Music_AlbumsUpdateAPIView(generics.RetrieveUpdateAPIView):
#     queryset = Music_Albums.objects.all()
#     serializer_class = Music_AlbumsUpdateSerialier
#     lookup_field = 'id'
#
#     def get_object(self):
#         id = self.kwargs["id"]
#         return get_object_or_404(Music_Albums, id=id)
#
#     def post(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
