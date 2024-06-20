import flet as ft
import os

class App(ft.Column):
    """Main class for representing"""
    def __init__(self):
        super().__init__()
        # Title
        self.title = ft.Text("Welcome to Garbage Classifier App", size=30, expand=True, text_align=ft.TextAlign.CENTER)
        
        # Image picker
        self.file_picker = ft.FilePicker(on_result=self.on_dialog_result)
        self.button_picker = ft.TextButton("Load image", icon=ft.icons.UPLOAD_FILE, on_click=self.upload_file, adaptive=True, scale=1.5, width=200, tooltip="Load image")

        
        self.image = ft.Image(src="images/image2.jpg", fit=ft.ImageFit.CONTAIN, width=400, height=400, expand=True)

        # Representation in the page
        self.controls = [
                    ft.Row(
                        controls=[
                            self.title,
                        ]
                    ),
                    ft.Row(
                        controls=[
                            self.file_picker,
                            self.button_picker
                        ],
                        alignment=ft.CrossAxisAlignment.CENTER,
                        expand_loose=True,
                    ),
                    ft.Row(
                        controls=[
                            self.image
                        ],
                        alignment=ft.CrossAxisAlignment.CENTER,
                    )
                ]
    
    def upload_file(self, e):
        self.file_picker.pick_files()
        self.file_picker.update()

    def on_dialog_result(self, e: ft.FilePickerResultEvent):
        print("Selected files:", e.files)
        print("Selected file or directory:", e.path)

    
