import re

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

from userform.models import User


def user_form(request):
    return  render(request, 'userforms.html')


def mob_validation(mob):
    mob = str(mob)
    pattern = re.fullmatch('(0|91)?[6-9][0-9]{9}', mob)
    return pattern

def form_information(request):
    name = request.POST.get('Nm')
    dob = request.POST.get('Date')
    email = request.POST.get('mail')
    mobile = request.POST.get('Phone')

    if mob_validation(mobile) is None:
        print("Enter valid mobile number")
    else:
        try:
            data = User(name=name, date_of_birth=dob, email=email, phone_number=mobile)
            data.save()
        except Exception as msg:
            return HttpResponse(msg)
        else:
            send_mail(
                'Form is submitted successfully',
                f'''Hii! {name},
                    your form is submitted successfully''',
                'arpit78007@gmail.com',
                [email],
                fail_silently=False,
            )
        data = {

            'name': name,
            'DOB': dob,
            'Number': mobile,
            'email': email
        }
        return render(request, 'submitted.html', data)



