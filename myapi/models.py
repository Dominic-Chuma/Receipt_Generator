from django.db import models
# Begin code change from here
from django.core.signals import request_finished
from django.dispatch.dispatcher import receiver
from django.db.models.signals import pre_save,post_save
# from myapi.models import MyModel
# from .models import Hero
from fpdf import FPDF


# Create your models here.
class Hero(models.Model): # Creating a model class "Hero"
    name = models.CharField(max_length=60)
    # alias = models.CharField(max_length=60)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=60)
    total = models.CharField(max_length=60)
    
    # def __str__(self) -> str:
    #     return super().__str__()
    
    def __str__(self):
        return "Name: " + self.name +"|" +"Address: " + self.address + "|" + "Phone: " + self.phone + "|" + "Total Amount: " + self.total


name = Hero.name
address = Hero.address
phone = Hero.phone
total = Hero.total

# Create a pdf class
class PDF(FPDF):
    # pass
    def header(self):
        self.set_font('helvetica','B',20) # Set Font
        self.cell(50) # Set Padding..
        self.cell(100,10,'Payment Invoice',border = True, ln = True, align = 'C') # Set Receipt title
        self.ln(40) # Give some space after the Title

    def footer(self):
        self.set_y(-15)# Set Position of the footer.
        self.set_font('helvetica','I',7) # Set Font
        self.cell(0,10,f'Page {self.page_no()}', align = 'C')
    

# # A decorator that connects a sender(my_callback) to te signal (request_finished)
# @receiver(request_finished)
# Sender function definition
def my_callback(sender, **kwargs):
    print("Request Finished!")
    
# request_finished.connect(my_callback,dispatch_uid="GET /heroesHTTP/1.1 200")
request_finished.connect(my_callback)


# Try and make a sender function that does something
#    when the post_save signal is triggered......

@receiver(post_save, sender=Hero)

def print_pdf(sender, **kwargs):
    print("I nailed it!!.....")
    
    print(name)
    print(address)
    print(phone)
    print(total)
    
    # # Create PDFs
    # pdf = PDF('P','mm','A4')
    
    # # Page 1
    # pdf.add_page()
    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Name :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,name,ln = True)

    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Address :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,address,ln = True)

    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Phone :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,phone,ln = True)

    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Total Amount :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,total,ln = True)
    
    
    # # Page 2
    # pdf.add_page()
    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Name :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,name,ln = True)

    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Address :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,address,ln = True)

    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Phone :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,phone,ln = True)

    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Total Amount :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,total,ln = True)


    # # Page 3
    # pdf.add_page()
    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Name :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,name,ln = True)

    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Address :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,address,ln = True)

    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Phone :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,phone,ln = True)

    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Total Amount :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,total,ln = True)
    
    
    # # Page 4
    # pdf.add_page()
    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Name :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,name,ln = True)

    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Address :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,address,ln = True)

    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Phone :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,phone,ln = True)

    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Total Amount :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,total,ln = True)
    
    
    # # Page 5
    # pdf.add_page()
    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Name :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,name,ln = True)

    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Address :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,address,ln = True)

    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Phone :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,phone,ln = True)

    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Total Amount :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,total,ln = True)
    
    
    # # Page 6
    # pdf.add_page()
    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Name :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,name,ln = True)

    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Address :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,address,ln = True)

    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Phone :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,phone,ln = True)

    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Total Amount :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,total,ln = True)
    

    # # Page 7
    # pdf.add_page()
    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Name :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,name,ln = True)

    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Address :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,address,ln = True)

    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Phone :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,phone,ln = True)

    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Total Amount :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,total,ln = True)
    
    
    # # Page 8
    # pdf.add_page()
    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Name :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,name,ln = True)

    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Address :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,address,ln = True)

    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Phone :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,phone,ln = True)

    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Total Amount :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,total,ln = True)
    
    
    # # Page 9
    # pdf.add_page()
    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Name :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,name,ln = True)

    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Address :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,address,ln = True)

    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Phone :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,phone,ln = True)

    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Total Amount :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,total,ln = True)
    
    
    # # Page 10
    # pdf.add_page()
    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Name :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,name,ln = True)

    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Address :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,address,ln = True)

    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Phone :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,phone,ln = True)

    # pdf.set_font('helvetica','B',16)
    # pdf.cell(40,20,'Total Amount :')

    # pdf.set_font('helvetica','U',16)
    # pdf.cell(130,20,total,ln = True)
    
    # # Print Out The PDF
    # pdf.output(name + '.pdf')