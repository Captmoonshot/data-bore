from django.shortcuts import render


def home(request):
	template_name = 'hello_world.html'
	context = {

	}
	return render(request, template_name, context)


