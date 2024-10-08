from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('view_details/<int:recipe_id>/<str:recipe_type>/', views.view_details, name='view_details'),
    path('nonveg/', views.NonVegView, name='nonveg'),
    path('veg/', views.VegView, name='veg'),
    path('nonveg_curries/', views.NonVegCurries, name='nonveg_curries'),
    path('veg_curries/', views.VegCurries, name='veg_curries'),
    path('search/',views.search_view, name='search'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
