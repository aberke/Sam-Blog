# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.shortcuts import render_to_response, render

from models import Post, Header

from django import forms

def serve_index(request):
	return serve_index_page(request, 1)

def serve_index_page(request, i):
	page = int(i)
	posts = Post.objects.all().order_by('-date_posted') #('-date_posted') for most recent?
	last_page = len(posts)/10 + 1

	context = {'page': page, 'count': Post.objects.count(), 'last_page': last_page}
	context['pages'] = [i for i in range(1,last_page + 1)]
	context['posts'] = [posts[i] for i in range((page-1)*10, page*10) if i< len(posts)]

	header = list(Header.objects.all())
	if len(header) > 0:
		context['header'] = header.pop()

	return render(request, "index.html", context)

class SubmitMeForm(forms.Form):
    message = forms.CharField(label="Message")
    sender = forms.EmailField(label="Your Email")
    image_url = forms.URLField(label="link to that photo on imgur or elsewhere",required=False, initial="http://")
    #file = forms.FileField(required=False)


def serve_share(request):
    if request.method == 'POST': # If the form has been submitted...
        form = SubmitMeForm(request.POST, request.FILES) # A form bound to the POST data
        if form.is_valid():
		    sender = form.cleaned_data['sender']

		    message = 'Hey there, You got another post to your blog: \n \nmessage from '+str(sender)+': \n \n'+form.cleaned_data['message']

		    recipients = ['berke.alexandra@gmail.com']

		    if form.cleaned_data['image_url']:
		    	image_url = form.cleaned_data['image_url']
		    	message += '\n \nThis link was posted with it, but please only follow the link if you trust it unless I decide to update this with some nice security: '+str(image_url)
		    else:
		    	message += "\n\nThey didn't post a link with this message, do you want a link to be mandatory to send you a message?"

		    from django.core.mail import send_mail, EmailMessage

		    email = EmailMessage('Post from that blog', message, sender, recipients)
		    email.send()

		    return HttpResponseRedirect('/submitme_thanks/') # Redirect after POST
    else:
    	form = SubmitMeForm() # An unbound form
    context = {'form': form}

    header = list(Header.objects.all())
    if len(header) > 0:
    	context['header'] = header.pop()
    return render(request, 'share.html', context)

def serve_submitme_thanks(request):
	context = {}
	header = list(Header.objects.all())
	if len(header) > 0:
		context['header'] = header.pop()

	return render(request, 'share_thanks.html', context)



