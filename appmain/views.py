from django.shortcuts import render

# MAH VIEWS ALL DEM VIEWS VIEWS FROM THE SIX

def index(request):
	
	number = 6
	return render(request, 'index.html', {'number' : number, })
	# main view
	#return render(request, 'index.html')