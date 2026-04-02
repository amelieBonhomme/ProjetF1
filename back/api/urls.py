from rest_framework import routers
from .views import (
    NflUserViewSet, EquipeViewSet,
    CommentaireViewSet, FavorisViewSet
)
from django.urls import path
from .views import LoginView, RegisterView

router = routers.DefaultRouter()
router.register('users', NflUserViewSet)
router.register('equipes', EquipeViewSet)
router.register('commentaires', CommentaireViewSet)
router.register('favoris', FavorisViewSet)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]
