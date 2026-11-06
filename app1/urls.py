from django.urls import path

from app1.views import aboutus, contactus, delete, home, mark_complete, todolist, create, edit

urlpatterns = [
    # path('home/', home),
    # path('aboutus/', aboutus),
    # path('contactus/', contactus),
    path('todolist/', todolist),
    path('todolist/create/', create),
    path('todolist/<id>/mark/', mark_complete),
    path('todolist/<id>/', edit),
    path('todolist/<id>/delete/', delete),
]