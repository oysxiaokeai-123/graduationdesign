
from django.contrib import admin
from django.urls import path, include
from .views import start

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),

    path('',start),

    path('Login/',include('Login.urls')),
    
    path('Register/',include('Register.urls')),
    
    path('search/',include('SearchApp.urls')),

    path('studentinfo/',include('StudentInfo.urls')),

    path('insertgoods/',include('Insertgoods.urls')),

    path('modifyInfo/',include('ModifyInfo.urls')),
 
    path('modifyGoods/',include('ModifyGoods.urls')),

    path('itemInfo/',include('itemInfo.urls')),
    
    path('showInfo/',include('ShowInfo.urls')),

    path('messages/',include('messages.urls')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
