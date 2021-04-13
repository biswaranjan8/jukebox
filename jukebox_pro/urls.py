from django.contrib import admin
from django.urls import path
from myapp import views

from myapp.views import MusiciansViewSet, Music_AlbumsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'musician', MusiciansViewSet, basename='musician')
router.register(r'musician_album', Music_AlbumsViewSet, basename='musician_album')
urlpatterns = router.urls


####################
#   musician_album list => url "musician_album" request(get)
#   musician_album Retrieve=> url "musician_album/(musician_album-id)" request(get)
#   musician_album Create => url "/musician_album/" request(post) data_fields("musician","album_name","genre","price","description")
#   musician_album_Update => url "musician_album/(musician_album-id)/" request(put) data_fields("musician","album_name","genre","price","description")
#   musician_album_Delete => url "musician_album/(musician_album-id)/" request(delete)

#   Musician list => url "musician" request(get)
#   Musician Retrieve=> url "musician/(musician-id)" request(get)
#   Musician Create => url "/musician/" request(post) data_fields("name","musician_type")
#   Musician_Update => url "musician/(musician-id)/" request(put) data_fields("name","musician_type")
#   Musician_Delete => url "musician/(musician-id)/" request(delete)

#  List Of Music Album Sorted By date release ascending
#              url => "musicalbum_retrieve/" request(get)

# List Of Music Album for a specific musician sorted by price ascending
#              url => "musician_filter_price/(musician-id)/" request(get)

# List of Musician for specific music album sorted by Musician name ascending
#              url => "musician_filter/(album-name)/"  request(get)
####################

urlpatterns += [
    path('admin/', admin.site.urls),
    path('musicalbum_retrieve/', views.MusicAlbumRetrieve.as_view(), name='musicalbum_retrieve'),
    path('musician_filter_price/<int:id>/', views.MusicAlbumFilterPrice.as_view(), name='MusicAlbumFilterPrice'),
    path('musician_filter/<str:name>/', views.MusicAlbumFilter.as_view(), name='MusicAlbumFilter'),
]

