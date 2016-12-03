from django.conf.urls import url

from views import InterpretImageView

urlpatterns = [
	url(r'^', InterpretImageView.as_view(), name='index'),
]