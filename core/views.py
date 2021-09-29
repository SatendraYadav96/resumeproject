from django.shortcuts import render


# Create your views here.


def home(request):
    context = {'home': 'active'}
    return render(request, 'core/home.html', context)


def contact(request):
    # if request.method == "POST":
        # yourname = request.POST.get('yourname')
        # youremail = request.POST.get('youremail')
        # yoursubject = request.POST.get('yoursubject')
        # yourmessage = request.POST.get('yourmessage')

        # contact = contact(yourname=yourname, youremail=youremail,
                        #   yoursubject=yoursubject, yourmessage=yourmessage)
        # contact.save()
        # message.success(request, 'Your message has been sent!)
    context = {'contact': 'active'}
    return render(request, 'core/contact.html', context)
