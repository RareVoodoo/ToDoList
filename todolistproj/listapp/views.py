from django.shortcuts import render, redirect
from .models import Record 
from .forms import ListForm
# Create your views here.


def project_list(request):
	form = ListForm(request.POST)
	template_name = 'index.html'
	item_list = Record.objects.all()
	item_count = Record.objects.count()
	ctx = {
		"item_list":item_list,
		"item_count":item_count,
	}
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return render(request,template_name,ctx)
		else:
			return render(request,template_name,ctx)

	else:
		return render(request,template_name,ctx)


def delete(request, record_id):
	item = Record.objects.get(pk=record_id)
	item.delete()
	return redirect('main')


def done(request, record_id):
	item = Record.objects.get(pk=record_id)
	item.done = True
	item.save()
	return redirect('main')
		

def undone(request, record_id):
	item = Record.objects.get(pk=record_id)
	item.done = False
	item.save()
	return redirect('main')