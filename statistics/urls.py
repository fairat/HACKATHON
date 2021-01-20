from django.conf.urls import url
from . import views

urlpatterns = [  # api модулей и параметров открытия объектов в PRO-S
    url(r'^azs/get_all/$',  views.get_all_azs),
    url(r'^statistics/get_years/$',  views.get_years),
    url(r'^statistics/get_months/$',  views.get_months),
    url(r'^statistics/get_days/$',  views.get_days),
    url(r'^buyer/get_years/$',  views.buyer_years),
    url(r'^buyer/get_months/$',  views.buyer_months),
    url(r'^buyer/get_days/$',  views.buyer_days),
    url(r'^buyer/graph/$',  views.buyer_graph),
]
