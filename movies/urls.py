from django.urls import path, include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'rate', views.RateMovieViewSet, basename='rate_movie')


urlpatterns = [
    path('get/', views.GetMovies.as_view()),
    path('view/', include(router.urls)),

]