from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from local_users.views import CustomChangePasswordView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
    path("accounts/password/change",
         CustomChangePasswordView.as_view(), name="account_change_password"),
    path('allauth/', include('allauth.urls')),
    path('users/', include('local_users.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
