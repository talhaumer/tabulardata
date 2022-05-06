from django.urls import path

from user.views import frontpage, signup, login_request, logout_request

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name='logout'),
]
