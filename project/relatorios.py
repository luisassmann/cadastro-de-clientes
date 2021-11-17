from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image

import webbrowser


class Relats():
    def printCliente(self):
        webbrowser.open("bin/cliente.pdf")

    def geradorRelatCliente(self):
        self.archivepdf = canvas.Canvas("bin/cliente.pdf")

        self.codigoRel = self.entryCodigo.get()
        self.nomeRel = self.entryNome.get()
        self.telefoneRel = self.entryTelefone.get()
        self.cidadeRel = self.entryCidade.get()

        # --- Título ---
        self.archivepdf.setFont("Helvetica-Bold", 24)
        self.archivepdf.drawString(200, 790, 'Ficha do Cliente')

        # --- Dados do Cliente ---
        self.archivepdf.setFont("Helvetica-Bold", 18)
        self.archivepdf.drawString(50, 700, 'Código: ')
        self.archivepdf.drawString(50, 670, 'Nome: ')
        self.archivepdf.drawString(50, 640, 'Telefone: ')
        self.archivepdf.drawString(50, 610, 'Cidade: ')

        self.archivepdf.setFont("Helvetica", 18)
        self.archivepdf.drawString(120, 700, self.codigoRel)
        self.archivepdf.drawString(110, 670, self.nomeRel)
        self.archivepdf.drawString(134, 640, self.telefoneRel)
        self.archivepdf.drawString(120, 610, self.cidadeRel)

        self.archivepdf.rect(20, 550, 550, 280, fill=False, stroke=True)

        self.archivepdf.showPage()
        self.archivepdf.save()
        self.printCliente()
