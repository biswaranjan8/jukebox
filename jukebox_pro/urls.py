from django.contrib import admin
from django.urls import path
from myapp import views

from myapp.views import MusiciansViewSet, Music_AlbumsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'musician', MusiciansViewSet, basename='musician')
router.register(r'musician_album', Music_AlbumsViewSet, basename='musician_album')
urlpatterns = router.urls

# OR
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('musicians/', views.MusicianList.as_view(), name='musicians'),
#     path('musician_album/', views.Music_AlbumsList.as_view(), name='musician_album'),
#     path('update/<int:id>/', views.MusiciansUpdateAPIView.as_view(), name='MusiciansUpdateAPIView'),
#     path('update_album/<int:id>/', views.Music_AlbumsUpdateAPIView.as_view(), name='Music_AlbumsUpdateAPIView'),
# ]

####################
#   Musician list => url "musician" request(get)
#   Musician Retrieve=> url "musician/id" request(get)
#   Musician Create => url "musician" request(post) data_fields("name","musician_type")
#   Musician_Update => url "musician/id/" request(put) data_fields("name","musician_type")
#   Musician_Delete => url "musician/id/" request(delete)
####################

urlpatterns += [
    path('admin/', admin.site.urls),
    path('musicalbum_retrieve/', views.MusicAlbumRetrieve.as_view(), name='musicalbum_retrieve'),
    path('musician_filter_price/<int:id>', views.MusicAlbumFilterPrice.as_view(), name='MusicAlbumFilterPrice'),
]

