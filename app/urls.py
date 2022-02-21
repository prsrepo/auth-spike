from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('krmaps', views.krmap_list),
    path('krmaps/<pk>', views.krmap_detail),
    path('oauth2/url', views.get_autheticate_url),
    path('oauth2/callback', views.handle_callback),
    path('navigate/search/recent', views.recent_files)
]
