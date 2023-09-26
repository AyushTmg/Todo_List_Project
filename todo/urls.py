
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path('',include('tasks.urls')),
]


admin.site.site_header='Todo List Admin'
admin.site.index_title='Admin page for managing the todo app'
admin.site.site_title='Admin page for Todo list'

