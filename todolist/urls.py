from django.urls import path, include
from . import views
from todolist.views import *
# TODO: Implement Routings Here

app_name= 'todolist'

urlpatterns= [
   path('', todolist, name="todolist"),
   path('login/', login_user, name="login_user"),
   path('register/', register, name="register"),
   path('logout/', logout_user, name="logout"),
   path('create-task/', create_task, name="create_task"),
   path('json/', show_json, name="show_json"),
   path('add/', create_ajax, name='create_ajax'),
]