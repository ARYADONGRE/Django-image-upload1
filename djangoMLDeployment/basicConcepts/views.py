from django.shortcuts import render
from .forms import image_form
from .models import image_model

# Create your views here.
def Welcome(request):
	print("function called")
	context = {}
	if request.method == "POST":
		form = image_form(request.POST, request.FILES)
		if form.is_valid():
			#name = form.cleaned_data.get("name")
			img = form.cleaned_data.get("previewImage")
			obj = image_model.objects.create(
								#title = name, 
								img = img
								)
			obj.save()
			print(obj)
	else:
		form = image_form()
	context['form']= form
	return render(request, "index.html", context)

def User(request):
	#image=request.POST['img']
	#name=request.POST['name']
	#print(name)
    #img=model.predict()
 
	print(request)
	return render(request,'user.html')
