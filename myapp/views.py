from django.shortcuts import render

# Create your views here.
from .tasks import add
from .models import Sample

def index_view(request):
	context = dict()
	if request.method == "POST":
		a = request.POST.get('a')
		b = request.POST.get('b')
		result = add.apply_async((a, b))
		context['result'] = result
	return render(request, 'index.html', context)