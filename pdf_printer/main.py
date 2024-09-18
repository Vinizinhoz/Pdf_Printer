import flet as ft
import tkinter as tk
import pyautogui as gui
from tkinter import filedialog
from sistema import programa_print


def main(page: ft.Page):
    listaprint = []
    global sistema_brabo
    sistema_brabo = programa_print()
    page.title = "PDF Printer - Logistica"
    page.window.width = 300
    page.window.height = 100
    page.vertical_alignment = "center"

    def home(e):
        contagem_prints = ft.Text(value=str(len(listaprint)))
        botao_print = ft.TextButton("Tirar Print", on_click=printou)
        botao_pdf = ft.TextButton("Salvar PDF", on_click=atualizou)
        page.clean()
        page.add(
            ft.Column([
                ft.Row([ contagem_prints, botao_print, botao_pdf], alignment=ft.MainAxisAlignment.CENTER)
            ])
        )
        page.update()

    def reiniciar(e):
        sistema_brabo.apaga_prints()
        sistema_brabo.limpa_lista()
        page.clean()
        confirma_reinicio = ft.TextButton("Sim", on_click=home)
        page.add(
        ft.Column([
            ft.Text(value="Quer mesmo reiniciar?", text_align=ft.TextAlign.CENTER),
            ft.Row([confirma_reinicio], alignment=ft.MainAxisAlignment.CENTER)
        ])
        )   
        page.update()

    def printou(e):
        gui.click(542,314)
        
        nomess = sistema_brabo.tirar_print()
        sistema_brabo.salva_lista(nomess)
        contagem_prints = ft.Text(value=str(sistema_brabo.conta_lista()))
        page.clean()
        page.add(
        ft.Column([
            ft.Row([ contagem_prints, botao_print, botao_pdf], alignment=ft.MainAxisAlignment.CENTER)
        ])
        )   
        page.update()
        

    def atualizou(e):
        page.vertical_alignment = "center"
        page.window.width = 300
        page.window.height = 150
        page.clean()
        page.add(
        ft.Column([
            inserir_nome,
            ft.Row([ reiniciar, botao_pdf_salvou], alignment=ft.MainAxisAlignment.CENTER)
        ])
        )
        
    def salvou(e):
        locale = filedialog.askdirectory(title="Selecione a pasta para salvar o arquivo")
        sistema_brabo.salvar_em_pdf(inserir_nome.value, locale)
        page.clean()
        page.add(
        ft.Column([
            ft.Text(value="DOCUMENTO SALVO", text_align=ft.TextAlign.CENTER, color=ft.colors.RED),
            inserir_nome,
            ft.Row([ reiniciar, botao_pdf_salvou], alignment=ft.MainAxisAlignment.CENTER)
        ])
        )
        page.update()
        

    
    confirma_reinicio = ft.TextButton("Sim", on_click=home, style=ft.ButtonStyle(color=ft.colors.AMBER))
    reiniciar = ft.TextButton("Reiniciar", on_click=reiniciar, style=ft.ButtonStyle(color=ft.colors.AMBER))
    contagem_prints = ft.Text(value=str(len(listaprint)), color=ft.colors.AMBER)
    inserir_nome = ft.TextField(label="Insira o nome do pdf", text_align=ft.TextAlign.CENTER, border_color=ft.colors.AMBER)
    botao_print = ft.TextButton("Tirar Print", on_click=printou, style=ft.ButtonStyle(color=ft.colors.AMBER))
    botao_pdf = ft.TextButton("Salvar PDF", on_click=atualizou, style=ft.ButtonStyle(color=ft.colors.AMBER))
    botao_pdf_salvou = ft.TextButton("Salvar PDF", on_click=salvou, style=ft.ButtonStyle(color=ft.colors.AMBER))

    page.add(
        ft.Column([
            ft.Row([ contagem_prints, botao_print, botao_pdf], alignment=ft.MainAxisAlignment.CENTER)
        ])
    )
    page.update()



ft.app(main)
