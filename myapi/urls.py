# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('page', views.home, name="home"), # A path for an html page
    path('page/<int:id>',views.user, name="user"),
    path('pdf',views.pdfGEN,name="pdfGEN"),
]