from django.shortcuts import render
from django.views.generic.base import View

from image_recognition.forms import DetectImageForm
from image_detector import detect_image


class InterpretImageView(View):

	template_name = "index.html"

	def get(self, request):

        #create a form object
        form = DetectImageForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = DetectImageForm(request.POST)
        image = None
        if form.is_valid():
            image = detect_image(form.data['image'])

        return render(request, self.template_name, {'form': form, 'image':image})