from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse

from recruitment.models import Application
from recruitment.forms import ApplicationForm

# Create your views here.
def status(request):
	return render(request, 'recruitment/status.html')
	
def apply(request):
	template = loader.get_template('recruitment/apply.html')
	application_form = ApplicationForm()
	context = RequestContext(request, {
		'application_form': application_form
	})
	return HttpResponse(template.render(context))
	
def process_application(request):
	if request.method == 'POST':
		print request.META['REMOTE_ADDR']
		af = ApplicationForm(request.POST)
		if af.is_valid():
			a = af.save(commit=False)
			a.header = a.character_name + " " + str(a.level) + " " + a.race + " " + a.xclass
			a.save()
			af.save_m2m()
			return HttpResponseRedirect(reverse('recruitment:applications'))
	return render(request, 'recruitment/apply.html', { 'application_form': af })
	
def applications(request):
	applications_list = Application.objects.all().order_by('-date')
	if not request.user.is_authenticated():
		for a in applications_list:
			a.name = 'Login required'
			a.email = 'Login required'
	template = loader.get_template('recruitment/applications.html')
	context = RequestContext(request, {
		'applications': applications_list,
	})
	return HttpResponse(template.render(context))