from django.urls import path
from web import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
    path('edit/<int:id>/', views.edit_item, name='edit_item'),
    path('done/<int:id>/', views.item_done, name='item_done'),
]
