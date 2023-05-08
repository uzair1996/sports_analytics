from django.contrib import admin
from django.urls import path, include
from . import views
from .views_api import views_api
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.home,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    #path('home.html',views_api.images1,name='images1'),

    #path("home.html",views.home, name='home'),
    #path("series.html",views.series, name='series'),
    #path("matches.html",views.matches, name='matches'),
    #path("player.html",views.player, name='player'),
    path("about",views.about, name='about'),
   # path("project/",views.project, name='project'),
    path("contact/",views.contact, name='contact'),
    path("sets",views.movies, name='movies'),
    #path("fetch_html",views_api.my_view,name='my_view'),
    path("api/",views_api.MatchesListApiView.as_view(),name='MatchesListApiView'),
    path("project.html/",views_api.my_view2, name='my_view'),
    path("series/",views_api.my_view4, name='my_view4'),
    path("series/",views_api.my_view5, name='my_view5'),
    path("series/",views_api.my_view6, name='my_view6'),
    path("matches/",views_api.my_view4, name='my_view4'),
    path("tableau/",views.tableau, name='my_view4'),




   # path("player.html/",views_api.my_view4, name='player'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



