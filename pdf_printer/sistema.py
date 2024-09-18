import pyautogui
from PIL import Image
from fpdf import FPDF
import os
import time

class programa_print:
    def __init__(self):
        self.nome = 1
        self.listaprint = []

    def apaga_prints(self):
        try:
            for i in self.listaprint:
                os.remove(i)
        except:
            pass
    
    def limpa_lista(self):
        self.nome = 1
        self.listaprint = []

    def conta_lista(self):
        return len(self.listaprint)

    def salva_lista(self, nome):
        self.listaprint.append(nome)
        self.nome += 1

    def salvar_em_pdf(self, nomez, local):
        nome_pdf = str(nomez) + ".pdf"
        pdf = FPDF(orientation='L', unit='mm', format='A4')
        for imagem in self.listaprint:
            pdf.add_page()
            page_width = pdf.w 
            page_height = pdf.h -30
            pdf.image(imagem, x=0, y=0, w=page_width, h=page_height)
        pdf.output(f"{local}/{nome_pdf}")
        for i in self.listaprint:
            os.remove(i)

    def tirar_print(self):
        nome_image = f"{self.nome}.png"
        print_tela = pyautogui.screenshot()
        print_tela.save(f"{nome_image}")
        return nome_image


