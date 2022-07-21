from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def wizard(request):
    return render(request, "core/dtap_wizard.html")

@csrf_exempt
def send(request):
    return render(request, "core/dtap_ltp_send.html")
