from fpdf import FPDF

pdf = FPDF(orientation='P', unit='pt', format='A4')

pdf.add_page()

pdf.image('tiger.jpeg', w=80, h=50, x=50)

pdf.set_font(family='Times',style='B',size=24)
pdf.cell(w=0,h=50,txt="[Company Name]",align='C', ln=1)

pdf.set_font(family='Times',style='B',size=9)
pdf.cell(w=0,h=50,txt="Address, City, State Zipcode | Phone # | email address",align='C',ln=1)

# pdf.line(pdf.get_x,pdf.get_y,110, pdf.get_y)

pdf.set_font(family='Times',style='B',size=15)
pdf.cell(w=0,h=50,txt="Heading")
pdf.ln(40)

text= """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam egestas erat nec neque porttitor placerat. 
Fusce vitae risus non augue ornare euismod. Nulla id turpis laoreet, faucibus urna eu, imperdiet tellus. Duis scelerisque iaculis semper. Curabitur sed dolor id ligula finibus congue nec vel est. 
Donec ut sem augue. Praesent auctor nulla eu semper venenatis. Proin eu lacinia est. Vestibulum pharetra turpis ut ipsum porta tincidunt. 
Duis justo nunc, egestas ultricies iaculis eu, fermentum id velit. Suspendisse ut nisl vitae justo euismod auctor. """
pdf.set_font(family='Times',size=12)
pdf.multi_cell(w=0,h=15,txt=text)


pdf.set_font(family='Times',size=10, style='B')
pdf.cell(w=60,h=15,txt="Category: ")

pdf.set_font(family='Times',size=10)
pdf.cell(w=100,h=15,txt="Information",ln=1)

pdf.set_font(family='Times',style='B',size=15)
pdf.cell(w=0,h=50,txt="Heading2")
pdf.ln(40)

text= """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam egestas erat nec neque porttitor placerat. 
Fusce vitae risus non augue ornare euismod. Nulla id turpis laoreet, faucibus urna eu, imperdiet tellus. Duis scelerisque iaculis semper. Curabitur sed dolor id ligula finibus congue nec vel est. 
Donec ut sem augue. Praesent auctor nulla eu semper venenatis. Proin eu lacinia est. Vestibulum pharetra turpis ut ipsum porta tincidunt. 
Duis justo nunc, egestas ultricies iaculis eu, fermentum id velit. Suspendisse ut nisl vitae justo euismod auctor. """
pdf.set_font(family='Times',size=12)
pdf.multi_cell(w=0,h=15,txt=text)


pdf.set_font(family='Times',style='B',size=15)
pdf.cell(w=0,h=50,txt="Heading3")
pdf.ln(40)

text= """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam egestas erat nec neque porttitor placerat. 
Fusce vitae risus non augue ornare euismod. Nulla id turpis laoreet, faucibus urna eu, imperdiet tellus. Duis scelerisque iaculis semper. Curabitur sed dolor id ligula finibus congue nec vel est. 
Donec ut sem augue. Praesent auctor nulla eu semper venenatis. Proin eu lacinia est. Vestibulum pharetra turpis ut ipsum porta tincidunt. 
Duis justo nunc, egestas ultricies iaculis eu, fermentum id velit. Suspendisse ut nisl vitae justo euismod auctor. 

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam egestas erat nec neque porttitor placerat. 
Fusce vitae risus non augue ornare euismod. Nulla id turpis laoreet, faucibus urna eu, imperdiet tellus. Duis scelerisque iaculis semper. Curabitur sed dolor id ligula finibus congue nec vel est. 
Donec ut sem augue. Praesent auctor nulla eu semper venenatis. Proin eu lacinia est. Vestibulum pharetra turpis ut ipsum porta tincidunt. 
Duis justo nunc, egestas ultricies iaculis eu, fermentum id velit. Suspendisse ut nisl vitae justo euismod auctor. """
pdf.set_font(family='Times',size=12)
pdf.multi_cell(w=0,h=15,txt=text)

pdf.output('output.pdf')