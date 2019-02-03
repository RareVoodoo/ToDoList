from django.conf.urls import url,include
from . import views
urlpatterns = [

	url(r'^$',views.project_list,name='main'),
	url(r'^del/(?P<record_id>[\w]+)/$',views.delete, name='delete')
]