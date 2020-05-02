from django.urls import path
from webapp import views

urlpatterns = [
    path('myAPI/', views.UserList.as_view(), name='API')
]