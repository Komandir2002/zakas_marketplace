from django.urls import path
from . import views


urlpatterns = [
    path('mp/', views.MarketplaceListView.as_view(),name="shows_all_marketplace"),
    path('mp/<int:id>/', views.MarketplaceDetailView.as_view(),name="shows_marketplace_detail"),
    path("mp_add/", views.MarketplaceCreatedateView.as_view(), name="marketplace_add"),
    path(
        "mp/<int:id>/up/", views.MarketplaceUpdateView.as_view(), name="marketplace_update"
    ),
    path(
        "mp/<int:id>/del/", views.MarketplaceDeleteView.as_view(), name="marketplace_delete"
    ),
]