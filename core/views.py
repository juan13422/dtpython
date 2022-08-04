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
        # Data Stewaerwww
        html_file = "core/dtproto_main.html"
    else:   #Data owner
        if Usr.lower() == "do@citi.com":
            html_file = "core/dtproto_do_empty.html"
        else:
            # Lineage
            if Usr.lower() == "lineage@citi.com":
                html_file = "core/dtproto_lineage.html"
            else:
                html_file = "core/index.html"
                
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

@csrf_exempt
def do_ini(request):
    html_file = "core/dtproto_do_empty.html"
    return render(request, html_file)
@csrf_exempt
def do_full(request):
    html_file = "core/dtproto_do.html"
    return render(request, html_file)


@csrf_exempt
def do_dropzone(request):
    html_file = "core/dtproto_do_dz.html"
    return render(request, html_file)

@csrf_exempt
def lineage(request):
    html_file = "core/dtproto_lineage.html"
    return render(request, html_file)


@csrf_exempt
def main(request):
    html_file = "core/dtproto_main.html"
    return render(request, html_file)

@csrf_exempt
def felix(request):
    html_file = "core/prototipo_ntr.html"
    return render(request, html_file)

@csrf_exempt
def do_full_test(request):
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        print(uploaded_file.content_type)
        fs=FileSystemStorage()
        nombre = fs._save(uploaded_file.name,uploaded_file)

        url = fs.url(nombre)
        print(url)

    html_file = "core/dt_dropzone_test.html.html"
    return render(request, html_file)


@csrf_exempt
def alex(request):
    html_file = "core/dtap_inbox_alex.html"
    return render(request, html_file)
