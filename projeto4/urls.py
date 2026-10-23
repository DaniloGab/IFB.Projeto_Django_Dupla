from django.contrib import admin          
from django.urls import path, include    
from rest_framework.routers import DefaultRouter  
from cinemateca.views import FilmesViewSet, GenerosViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'generos', GenerosViewSet)
router.register(r'filmes', FilmesViewSet)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/', include(router.urls)),
   path('api/token/', obtain_auth_token),
]