from fpdf import FPDF
import pandas as pd
   

class PDFGenerator:
     """
     A class to generate a lined PDF notebook from a list of topics.

     This class handles the creation of pages, addition of headers, footers,
     and lines to produce a structured PDF file.
     """
     def __init__(self):
          """Initializes the PDFGenerator and the underlying FPDF object."""
          self.pdf = FPDF(orientation="portrait", unit="mm",format="A4")
          self.pdf.set_auto_page_break(auto=False, margin=0)
               
     def set_header(self,text):
          """
          Sets the main header for a topic page.

          Args:
               text (str): The topic title to display in the header.
          """          
          self.pdf.set_text_color(0, 0, 0)
          self.pdf.set_font(family="Times",style="B" ,size=24)
          self.pdf.cell(w=0, h=12, txt=text, align="L", ln=1)
          self.pdf.line(10, 21, 200, 21)

     def set_footer(self,text):
          """
          Sets the footer on the bottom right of the current page.

          Args:
               text (str): The topic title to display in the footer.
          """
          self.pdf.ln(273)
          self.pdf.set_font(family="Times",style="I" ,size=8)
          self.pdf.set_text_color(0, 0, 0)
          self.pdf.cell(w=0, h=10, txt=text, align="R")
               
     def add_lines(self):
          """Draws horizontal lines across the full height of the page."""
          for i in range(31, 291,10):
               self.pdf.line(10, i, 200, i)
               
     def add_topic_pg(self, topic):
          """
          Adds a main page for a new topic, including header, footer, and lines.

          Args:
               topic (str): The name of the topic for the page.
          """
          self.pdf.add_page()
          self.set_header(topic)
          self.set_footer(topic)
          self.add_lines()
          
     def add_extra_pg(self,topic):
          """
          Adds a supplementary page for a topic, including footer and lines.

          This method is used for pages that follow the main topic page.

          Args:
               topic (str): The name of the topic for the page's footer.
          """
          self.pdf.add_page()
          self.set_footer(topic)
          self.add_lines()

     def output(self, file_name):
          """
          Saves the generated PDF to a file.

          Args:
               file_name (str): The path and name for the output PDF file.
          """
          self.pdf.output(file_name)