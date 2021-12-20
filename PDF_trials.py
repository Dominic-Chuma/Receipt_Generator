from fpdf import FPDF

class PDF(FPDF):
    #pass
    def header(self):
        self.set_font('helvetica','B',20) # Set Font
        self.cell(50) # Set Padding..
        self.cell(100,10,'Payment Invoice',border = True, ln = True, align = 'C') # Set Receipt title
        self.ln(40) # Give some space after the Title

    def footer(self):
        self.set_y(-15)# Set Position of the footer.
        self.set_font('helvetica','I',7) # Set Font
        self.cell(0,10,f'Page {self.page_no()}', align = 'C')



##pdf = PDF('mm',orientation = 'P', format = 'A4')
pdf = PDF('P','mm','A4')

# create FPDF Object

#pdf = FPDF('P','mm','Letter')
qa = "BlaBlaBla"
na = 'Another Address'
pdf.add_page()
pdf.set_font('helvetica','B',16)
pdf.cell(40,20,'Name :')

pdf.set_font('helvetica','U',16)
pdf.cell(130,20,qa,ln = True)

pdf.set_font('helvetica','B',16)
pdf.cell(40,20,'Address :')

pdf.set_font('helvetica','U',16)
pdf.cell(130,20,qa,ln = True)

pdf.set_font('helvetica','B',16)
pdf.cell(40,20,'Phone :')

pdf.set_font('helvetica','U',16)
pdf.cell(130,20,'23568t4379p',ln = True)

pdf.set_font('helvetica','B',16)
pdf.cell(40,20,'Total Amount :')

pdf.set_font('helvetica','U',16)
pdf.cell(130,20,'30000',ln = True)

pdf.add_page()
pdf.set_font('helvetica','',16)
##
pdf.cell(50,40,'Hello World!')

pdf.add_page()
pdf.set_font('helvetica','',16)
##
pdf.cell(50,40,'Hello World!')

pdf.output('pdf_1.pdf')


