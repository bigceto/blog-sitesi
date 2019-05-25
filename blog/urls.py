from django.urls import path
from blog.views import post_list,post_update,post_delete,post_create,sanatcilar

urlpatterns = [
    path('list', post_list),
    path('create/', post_create),
    path('delete/', post_delete),
    path('update/', post_update),
    path('sanatcilar/(?P<sayi>[0-9a-z]+)/',sanatcilar)

]

