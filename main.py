from fpdf import FPDF
import pandas as pd
 

pdf = FPDF(orientation="portrait", unit="mm",format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():

     #set the header
     pdf.add_page()
     pdf.set_text_color(0, 0, 0)
     pdf.set_font(family="Times",style="B" ,size=24)
     pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
     pdf.line(10, 21, 200, 21)
     
     #add lines
     for i in range(31, 291,10):
          pdf.line(10, i, 200, i)
     
     # set the footer
     pdf.ln(265)
     pdf.set_font(family="Times",style="I" ,size=8)
     pdf.set_text_color(0, 0, 0)
     pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
     
     
     for i in range(row["Pages"] - 1):
          pdf.add_page()
          
          #add lines
          for j in range(31, 291,10):
               pdf.line(10, j, 200, j)
          
          # set the footer
          pdf.ln(273)
          pdf.set_font(family="Times",style="I" ,size=8)
          pdf.set_text_color(0, 0, 0)
          pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
     
pdf.output("output.pdf")