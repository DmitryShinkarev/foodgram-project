"""foodgram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import handler404, handler500, handler400
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_view
from django.urls import include, path

handler404 = 'recipes.views.page_not_found'
handler500 = 'recipes.views.server_error'
handler400 = 'recipes.views.page_bad_request'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('django.contrib.flatpages.urls')),
    path('auth/', include('users.urls')),
    path('auth/', include([
        path('login/', auth_view.LoginView.as_view(
            template_name='authForm.html'), name='login'),
        path('logout/', auth_view.LogoutView.as_view(
            template_name='logged_out.html'), name='logout'),
        path('password_change/', auth_view.PasswordChangeView.as_view(
            template_name='changePassword.html'), name='password_change'),
        path('password_change/done/',
             auth_view.PasswordChangeDoneView.as_view(
                template_name='password_change_done.html'
                ), name='password_change_done'),
        path('password_reset/',
             auth_view.PasswordResetView.as_view(
                template_name='resetPassword.html'
                ), name='password_reset'),
        path('reset/<uidb64>/<token>/',
             auth_view.PasswordResetConfirmView.as_view(
                template_name='password_reset_confirm.html'
                ), name='password_reset_confirm'),
        path('password_reset/done/',
             auth_view.PasswordResetDoneView.as_view(
                template_name='password_reset_done.html'
                ), name='password_reset_done'),
    ])),
    
    path('api/', include('api.urls')),
    
]

urlpatterns += [
    path('', include('recipes.urls')),
]

# urls for static and media
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )

# urls for debug-toolbar
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
