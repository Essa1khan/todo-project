from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # serve the todo app at the project root and also under /todo/ for compatibility
    path('', include('todo.urls')),
    path('todo/', include('todo.urls')),
]