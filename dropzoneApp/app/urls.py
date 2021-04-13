from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from app import views


urlpatterns = [
   #path('',views.home,name='home')
   path('',views.MainView.as_view(),name='home'),
   path('upload',views.file_upload_view,name='upload')
]


if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

