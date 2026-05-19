from django.contrib import admin
from django.urls import path, include

from main.views import (
    home,
    about,
    dashboard,
    guides,
    community,
    create_post,
    add_comment,
    phrases
)

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', home),

    path('about/', about),

    path('dashboard/', dashboard),

    path('guides/', guides),

    path('community/', community),

    path('community/create/', create_post),

    path(
        'community/comment/<int:post_id>/',
        add_comment
    ),

    path('phrases/', phrases),

    path('users/', include('users.urls')),
]