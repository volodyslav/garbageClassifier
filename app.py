import flet as ft

class App(ft.Column):
    def __init__(self):
        super().__init__()
        self.title = ft.Text("Welcome to Garbage Classifier App", size=30, expand=True, text_align=ft.TextAlign.CENTER)
        self.controls = [
            ft.Row(
                controls=[
                    self.title,
                ]
            )
        ]

    
    

    
