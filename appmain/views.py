from django.shortcuts import render

# MAH VIEWS ALL DEM VIEWS VIEWS FROM THE SIX

def index(request):

	# main view
	return render(request, 'index.html')