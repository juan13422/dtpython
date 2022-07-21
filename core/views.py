from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import logging
from django.core.files.storage import FileSystemStorage

# Create your views here.

def index(request):
    
    return render(request,"core/index.html")

@csrf_exempt
def ruteo(request):
    print(request.method)
    print(request.headers)
    print(request.POST)
    Usr = request.POST['inputUsuario']
    print("inputUsuario >>" + request.POST['inputUsuario'])
    print("inputUsuario >>" + Usr.lower())
    print("inputPassword >>"+request.POST['inputPassword'])
    logging.info("inputPassword >>{}", request.POST['inputPassword'])
    if Usr.lower() == "na25228@citi.com":
        html_file = "core/dtproto_main.html"
    else:
        print("MULTI ROL")
    return render(request,html_file)

@csrf_exempt
def inbox(request):
    return render(request, "core/dtap_inbox.html")

@csrf_exempt
def upload(request):
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        print(uploaded_file.content_type)
        fs=FileSystemStorage()
        nombre = fs._save(uploaded_file.name,uploaded_file)

        url = fs.url(nombre)
        print(url)

    return render(request,"core/upload.html")

