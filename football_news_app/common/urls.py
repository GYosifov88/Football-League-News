from django.urls import path
# from django.conf.urls.static import static
# from django.conf import settings

from football_news_app.common.views import index, show_contact_details

urlpatterns = (
    path('', index, name='index'),
    path('contacts/', show_contact_details, name='contacts'),
)

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)