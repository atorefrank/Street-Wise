from django.shortcuts import render
from django.views.generic.base import View

from image_recognition.forms import DetectImageForm
from image 


class InterpretImageView(View):

	template_name = "index.html"

	def get(self, request):
		return render(request, self.template_name)

	def post(self, request):
		return render(request, self.template_name)