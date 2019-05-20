from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Appointment
from django.shortcuts import get_object_or_404, render
from django.core.mail import EmailMessage

def appointment(request):
  if request.method == 'POST':
    listing_id = request.POST['listing_id']
    listing = request.POST['listing']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    time = request.POST['time']
    date = request.POST['date']
    user_id = request.POST['user_id']
    realtor_email = request.POST['realtor_email']

    #  Check if user has made inquiry already
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Appointment.objects.all().filter(listing_id=listing_id, user_id=user_id)
      if has_contacted:
        messages.error(request, 'You have already made an inquiry for this listing')
        return redirect('/doctor/')

    contact = Appointment(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone,time=time,date=date, user_id=user_id )

    contact.save()


    # send_mail(
    #   'Property Listing Inquiry',
    #   'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
    #   'rajr97555@gmail.com',
    #   [realtor_email, 'rajr97555@gmail.com'],
    #   fail_silently=False
    # )
# message1 = ('Subject here', 'Here is the message', 'from@example.com', ['first@example.com', 'other@example.com'])
# message2 = ('Another Subject', 'Here is another message', 'from@example.com', ['second@test.com'])
# send_mass_mail((message1, message2), fail_silently=False)
#msg_html = render_to_string(template_name, context)
    email = EmailMessage('Paitent Enquiry',
     '<html><body>'
     '<h1 style="text-align:center">DOCTOR ON CALL </h1><hr>'
     '<h2 style="color: green;"> Hello, '+ listing + 
     '</h2><strong><h3>Here is Paitent Details</h3><h4>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Name: '
     + name + '<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Email: ' + email  +'<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Phone Number: ' + phone +
      '</h4><h3>User Message:</h3><h4>&nbsp; '+time+
    '</h4><br> Thanks & Regards <br>'+ name +
    '</strong></body> </html>'
    , to=[realtor_email,'rajr971111@gmail.com'])
    email.content_subtype = "html"
    email.send()

  

    messages.success(request, 'Your request has been submitted, A Doctor  will get back to you ASAP')
    return redirect('/doctor/')


def appointment_details(request, pk):
  contact = get_object_or_404(Appointment, pk=pk)

  context = {
    'contact': contact
  }

  return render(request, 'accounts/details.html', context)
