from home import views
from django.urls import re_path as url

urlpatterns =[
     url(r'^$',views.homepage1),
     url(r'^predict$',views.predict),
     url(r'^about$',views.about),
     url(r'^firstaid$',views.firstaid),
     url(r'^professionaltreatment$',views.pt),
     url(r'^img$',views.img),
     url(r'^hospregis$',views.hospregis),
     url(r'^hospital_from$',views.hospital_from),
     url(r'^hospital$',views.nearhospi),
     url(r'^city$',views.hospital_result),
     url(r'^get_city_from_coords$', views.get_city_from_coords, name='get_city_from_coords'),
     url(r'^me$',views.aboutus),
     url(r'^chatbot$', views.chatbot, name='chatbot'),
]