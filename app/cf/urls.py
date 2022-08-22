from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("users.urls", namespace="users")),
    path("overtime/", include("overtime.urls", namespace="overtime")),
    path('accounts/', include('allauth.urls')),
    path("meals/", include("meals.urls", namespace="meals")),
    path("forms/", include("forms.urls", namespace="forms")),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
