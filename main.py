import flet as ft
from app import App

def main(page: ft.Page):
    page.title = "Garbage Classifier"
    page.padding = 20
    
    try:
        new_app = App()
        page.add(new_app)
    except Exception as e:
        print(e)

    page.update()


if __name__ == "__main__":
    ft.app(target=main)