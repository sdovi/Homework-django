from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.macbro, name='btn3'),
    path('macbrotwo', views.macbrotwo, name='btn4', ),
    path('macmac', views.macmac, name='btn5', ),
    path('maciphone', views.maciphone, name='btn6', ),
    path('macipad', views.macipad, name='btn7', ),
    path('macwatch', views.macwatch, name='btn8', ),
    path('macairpods', views.macair, name='btn10', ),
    path('macwatchmenu', views.macwatchmenu, name='btn11', ),
    path('maciphonemenu', views.maciphonemenu, name='btn12', ),
    path('macaksesuar', views.macaksesuar, name='btn13', ),
    path('macakustika', views.macakustika, name='btn14', ),
    path('macphone', views.macphone, name='btn15', ),
    path('macsamsung', views.macsamsung, name='btn17', )
    
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
