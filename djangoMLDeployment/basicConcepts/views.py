# from django.shortcuts import render
# from .forms import image_form
# from .models import image_model

# # Create your views here.
# def Welcome(request):
# 	print("function called")
# 	context = {}
# 	if request.method == "POST":
# 		form = image_form(request.POST, request.FILES)
# 		if form.is_valid():
# 			#name = form.cleaned_data.get("name")
# 			img = form.cleaned_data.get("previewImage")
# 			obj = image_model.objects.create(
# 								#title = name, 
# 								img = img
# 								)
# 			obj.save()
# 			print(obj)
# 	else:
# 		form = image_form()
# 	context['form']= form
# 	return render(request, "index.html", context)

# def User(request):
# 	#image=request.POST['img']
# 	#name=request.POST['name']
# 	#print(name)
#     #img=model.predict()
 
# 	print(request)
# 	return render(request,'user.html')

from django.shortcuts import render, redirect
from django.conf import settings
from .models import Image
import os

def Welcome(request):
    if request.method == 'POST':
        image_file = request.FILES['image'] if 'image' in request.FILES else None
        if image_file:
            img = Image(image=image_file)
            img.save()
            request.session['image_id'] = img.id  # Save image id to session
            return redirect('User')
    return render(request, 'index.html')

def User(request):
    image_id = request.session.get('image_id')
    if image_id:
        image = Image.objects.get(id=image_id)  
        image_url = image.image.url
        
        return render(request, 'user.html', {'image_url': image_url})
    return render(request, 'user.html', {'image_url': None})


