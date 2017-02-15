from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import PostForm
# Create your views here.



def login_home(request):
	if request.method =='GET':

		form = PostForm(request.POST)

		if form.is_valid():
			return render(request,"forms.html",{})
		

	else:		
		return render(request,"second.html",{})



	 
		
		
	
	

	

