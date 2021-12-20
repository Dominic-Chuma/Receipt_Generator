from django.shortcuts import render,get_object_or_404

# Changes begin here....
from rest_framework import viewsets
from .serializers import HeroSerializer
from .models import Hero
# Some more Importations
from django.http import FileResponse,HttpResponse, request
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

from .models import Hero


# user_profile = ""
user_ID = 0


# Create your views here.
class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

# Define a view function that takes a request & renders a page (home.html)
#    which is located in the templates folder
def home(request):
    return render(request, 'new/home.html', {}) 

# Define a user function that picks a poarticular user
def user(request, id):
    global user_ID
    user_ID = id
    # user_profile = Hero.objects.get(get_object_or_404(Hero,pk=id))
    user_profile = get_object_or_404(Hero,pk=id)
    # user_address = Hero.objects.all().filter(name=user_profile)
    list_profile = str(user_profile).split("|")
    
    return render(request,'new/user.html', {'user':list_profile})
    # return render(request,'new/user.html')
    
# Define a user function that picks a poarticular user
def new_user(request, id):
    #
    # user_profile = Hero.objects.get(get_object_or_404(Hero,pk=id))
    user_profile = get_object_or_404(Hero,pk=id)
    # user_address = Hero.objects.all().filter(name=user_profile)
    list_profile = str(user_profile).split("|")
    
    return list_profile
    
    
def pdfGEN(request):
    # Function Call.....
    new_list = new_user(request,user_ID)
    print(new_list)
    # Create Bytestream buffer
    buf = io.BytesIO()
    # Create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # Create Text Object
    textob =  c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica",14)
    # Trials
    lines = ["Hey Line 1","Hey Line 2"]
    # Loop through obtained Model data
    for line in new_list:
        textob.textLine(line)
    
    c.drawText(textob)
    c.showPage()
    c.drawText(textob)
    c.showPage()
    c.drawText(textob)
    c.showPage()
    c.drawText(textob)
    c.showPage()
    c.drawText(textob)
    c.showPage()
    c.drawText(textob)
    c.showPage()
    c.drawText(textob)
    c.showPage()
    c.drawText(textob)
    c.showPage()
    c.drawText(textob)
    c.showPage()
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    
    # Prepare the PDF file name
    striped = new_list[0].split(": ")
    print(striped)
    file_name = striped[1]
    
    return FileResponse(buf, as_attachment=True, filename=file_name + ".pdf")
    