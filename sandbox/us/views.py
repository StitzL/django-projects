from django.shortcuts import render_to_response, get_object_or_404, redirect
import random, string, json, requests
from us.models import Urls
from django.http import JsonResponse
from django.template.context_processors import csrf
from django.core.urlresolvers import reverse, NoReverseMatch

def index(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('us/index.html', c)

def redirect_original(request, short_id):
	url = get_object_or_404(Urls, pk=short_id) 
	url.counter += 1
	url.save()
	return redirect(url.long_url, permanent=True) # permanent redirect might mean our statistics are off, but okay

def shorten_url(request):
	url = request.POST.get("url", '') 
	if (url == ''):
		return JsonResponse({'error': "No URL given"})

	# check if this is already an shortened url. in this case, do not handle it, but simply return
	end_of_url = url[-4:]
	try:
		if (url.startswith(request.build_absolute_uri(reverse('us:redirectoriginal', args=[end_of_url])))):
			if (is_existing_short_code(end_of_url)):
				return JsonResponse({'url':url})
			return JsonResponse({'error': 'Invalid URL {0}'.format(url)})
	except NoReverseMatch:
		# nothing found, as expected
		pass
		
		
	# url was given, now try out whether it exists
	try:
		requests.head(url).raise_for_status()
	except Exception as e:
		return JsonResponse({'error': "Retrieving URL was impossible: {0}".format(e)})
		
	try:
		# try to reuse existing url
		existing_url = Urls.objects.get(long_url=url)
		short_id = existing_url.short_id
	except (Urls.DoesNotExist):
		# no existing url found, create a new entry
		short_id = get_short_code()
		b = Urls(long_url=url, short_id=short_id)
		b.save()

	return JsonResponse({'url':request.build_absolute_uri(reverse('us:redirectoriginal', args=[short_id]))})
	
def preview_redirect(request, short_id):
	#todo implement preview.
	pass

def get_short_code():
	length = 4
	char = string.ascii_uppercase + string.digits + string.ascii_lowercase
	# if the randomly generated short_id is used then generate next
	while True:
		short_id = ''.join(random.choice(char) for x in range(length))
		try:
			Urls.objects.get(pk=short_id)
		except (Urls.DoesNotExist):
			return short_id

def is_existing_short_code(short_id):
	try:
		Urls.objects.get(pk=short_id)
		return True
	except (Urls.DoesNotExist):
		return False
