from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, UserLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', TaskList.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('task-update/<int:pk>/n', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/n', TaskDelete.as_view(), name='task-delete'),

    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register')

]