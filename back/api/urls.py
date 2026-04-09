from rest_framework import routers
from .views import (
    f1UserViewSet, EquipeViewSet, CircuitViewSet,
    CommentaireViewSet, FavorisViewSet,PrefereViewSet,
    LoginView, RegisterView, get_favoris_user, toggle_favori, get_prefere_user, toggle_prefere, stats_sexe,get_commentaires,add_commentaire 
)
from django.urls import path, include

router = routers.DefaultRouter()
router.register('users', f1UserViewSet)
router.register('equipes', EquipeViewSet)
router.register('circuit', CircuitViewSet)
router.register('commentaires', CommentaireViewSet)

# ⭐ IMPORTANT : on change le nom ici
router.register('favoris-list', FavorisViewSet)
router.register('prefere-list', PrefereViewSet)

urlpatterns = [

    # ⭐ ROUTES PERSONNALISÉES
    path('favoris/toggle/', toggle_favori),
    path('favoris/<str:id_user>/', get_favoris_user),
    path('prefere/toggle/', toggle_prefere),
    path('prefere/<str:id_user>/', get_prefere_user),
    path('stats/sexe/', stats_sexe),
    path('commentaires/', get_commentaires),
    path('commentaires/add/', add_commentaire),


    # ⭐ ROUTES DU ROUTER
    path('', include(router.urls)),

    # ⭐ LOGIN / REGISTER
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]
