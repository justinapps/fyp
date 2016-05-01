from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm
# Create your views here.
from django.core.mail import send_mail
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.shortcuts import redirect



"""
if form.is_valid():
	subject = form.cleaned_data['subject']
	message = form.cleaned_data['message']
	sender = form.cleaned_data['sender']
	cc_myself = form.cleaned_data['cc_myself']

	recipients = ['Justinas.Ulevicius2@mail.dcu.ie']
	if cc_myself:
		recipients.append(sender)

	send_mail(subject, message, sender, recipients)
	return HttpResponseRedirect('/thanks/')
"""

def contact(request):

	form_class = ContactForm

	if request.method == 'POST':
		form = form_class(data=request.POST)

		if form.is_valid():
			contact_name = request.POST.get('contact_name', '')
			contact_email = request.POST.get('contact_email', '')
			form_content = request.POST.get('form_content', '')
			
			template = get_template('contact_template.txt')
			context = Context({
				'contact_name': contact_name,
				'contact_email': contact_email,
				'form_content': form_content,
			})

			content = template.render(context)

			email = EmailMessage(
				"New contact form submission",
				content,
				"Your website" + '',
				['Justinas.Ulevicius2@mail.dcu.ie'],
				headers = {'Reply-To': contact_email }
			)

			email.send()
			return redirect('contact')


	return render(request, 'contact/contact.html', {
		'form': form_class,
		})
