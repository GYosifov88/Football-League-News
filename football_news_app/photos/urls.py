from django.urls import path, include

from football_news_app.photos.views import add_photo, details_photo, edit_photo, delete_photo, like_photo, PhotoListView

urlpatterns = (
    path('', PhotoListView.as_view(), name='show photos'),
    path('add/', add_photo, name='add photo'),
    path('<int:pk>/', include([
        path('', details_photo, name='details photo'),
        path('edit/', edit_photo, name='edit photo'),
        path('delete/', delete_photo, name='delete photo'),
    ])),
    path('like/<int:photo_id>/', like_photo, name='like photo'),
)