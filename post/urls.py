from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.VacancyListView.as_view(),name="shows_all_vacancy"),
    path('posts/<int:id>/', views.VacancyDetailView.as_view(),name="shows_vacancy_detail"),
    path("add_post/", views.VacancyCreatedateView.as_view(), name="book_add"),
    path(
        "posts/<int:id>/update/", views.VacancyUpdateView.as_view(), name="book_update"
    ),
    path(
        "posts/<int:id>/delete/", views.VacancyDeleteView.as_view(), name="book_delete"
    ),
]