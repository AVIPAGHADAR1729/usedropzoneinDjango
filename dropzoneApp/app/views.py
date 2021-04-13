from django.shortcuts import render,HttpResponse

# Create your views here.

# def home(request):
# 	return render(request, 'app/home.html',{})


# first time use class base view


from django.views.generic import TemplateView
from app.models import MyUpload


class MainView(TemplateView):
	template_name = 'app/home.html'



def file_upload_view(request):
	# print(request.FILES)
	if request.method == 'POST':
		file = request.FILES['file']
		# print(file)
		# check = file.name.endswith('.png')
		# print(check)
		MyUpload.objects.create(upload=file)



		
	return HttpResponse('upload Success')