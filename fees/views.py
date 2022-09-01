from django.shortcuts import render
# Create your views here.
def fees_django(request):
    cname='Django'
    duration='4 months'
    seats=10
    django_details={'nm':cname,'du':duration,'st':seats}
    return render(request,'fees/feesone.html',django_details)
def fees_python(request):
    cname='Python'
    duration='4 months'
    seats=10
    django_details={'nm':cname,'du':duration,'st':seats}
    return render(request,'fees/feestwo.html',django_details)