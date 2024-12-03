from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.home,name='home'),
    path('register_user/',views.register_user,name='register'),
    path('register/', views.register_student, name='register_student'),
    path('list/', views.student_list, name='student_list'),
    path('edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('delete/<int:pk>/', views.delete_student, name='delete_student'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
