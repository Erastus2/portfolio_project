from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from .forms import ContactForm
from django.conf import settings
from .models import ContactMessage

def contact_view(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
         # Get data from form
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message_content = form.cleaned_data['message']
            subject_content = form.cleaned_data.get('subject', 'Contact Form Submission')

            # Save to database
            ContactMessage.objects.create(
                name=name,
                email=email,
                message=message_content
            )
            email_message = EmailMessage(
                subject=f"{subject_content} from {name}",
                body=message_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.DEFAULT_FROM_EMAIL],
                headers={'Reply-To': email}  # sets reply-to for older Django versions
            )
            email_message.send(fail_silently=False)

            return redirect('contacts:contact_success')  # optional success page

    return render(request, 'contacts/contact.html', {'form': form})


def contact_success(request):
    """
    Shows the success page after form submission.
    """
    return render(request, 'contacts/contact_success.html')