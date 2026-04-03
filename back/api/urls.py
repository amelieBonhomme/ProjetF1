from rest_framework import routers
from .views import (
    f1UserViewSet, EquipeViewSet,CircuitViewSet,
    CommentaireViewSet, FavorisViewSet,
    LoginView, RegisterView
)
from django.urls import path, include

router = routers.DefaultRouter()
router.register('users', f1UserViewSet)
router.register('equipes', EquipeViewSet)
router.register('circuit', CircuitViewSet)
router.register('commentaires', CommentaireViewSet)
router.register('favoris', FavorisViewSet)

urlpatterns = [
    path('', include(router.urls)),   
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]
