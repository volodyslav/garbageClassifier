import flet as ft
from app import App

def main(page: ft.Page):
    page.title = "Garbage Classifier"
    
    new_app = App()

    page.add(new_app)
    page.update()


if __name__ == "__main__":
    ft.app(target=main)