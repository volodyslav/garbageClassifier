import flet as ft
from model import load_image

class App(ft.Column):
    """Main class for representing"""
    def __init__(self):
        super().__init__()
        # Title
        self.title = ft.Text("Welcome to Garbage Classifier App", size=40, expand=True, text_align=ft.TextAlign.CENTER)
        
        # Image picker
        self.file_picker = ft.FilePicker(on_result=self.on_dialog_result)
        self.button_picker = ft.IconButton(icon=ft.icons.UPLOAD_FILE, on_click=self.upload_file, adaptive=True, scale=1.5, tooltip="Load image")
        self.text_file = ft.Text(value="image2.jpg", size=25, text_align=ft.TextAlign.CENTER, no_wrap=False)

        # Image
        self.image = ft.Image(src="images/image2.jpg", fit=ft.ImageFit.CONTAIN, width=400, height=400, expand=True)

        # Prediction 
        self.predict_btn = ft.TextButton(text="Predict", scale=1.5, adaptive=True, on_click=self.on_predict)
        self.predict_text = ft.Text(value="", size=30)

        # Representation on the page
        self.controls = [
                    # Title row
                    ft.Row(
                        controls=[
                            self.title,
                        ],
                    ),
                    # Image picker and name
                    ft.Row(
                        controls=[
                            self.file_picker,
                            self.button_picker,
                            self.text_file
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                        height=50
                    ),
                    # Image
                    ft.Row(
                        controls=[
                            self.image
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20
                    ),
                    # Predictions
                    ft.Row(
                        controls=[
                            self.predict_btn,
                            self.predict_text
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20
                    )
                ]
    
    def upload_file(self, e):
        """Upload image, checks formats"""
        self.file_picker.pick_files(file_type=ft.FilePickerFileType.IMAGE,allowed_extensions=["jpg", "png", "jfif"])
        self.file_picker.update()

    def on_dialog_result(self, e: ft.FilePickerResultEvent):
        """Change image's source and text file"""
        try:
            print("Selected files:", e.files[0].path)
            self.image.src = e.files[0].path
            self.text_file.value = e.files[0].name
            self.image.update()
            self.text_file.update()
            # Set prediction text to empty
            self.predict_text.value = ""
            self.predict_text.update()
        except Exception as e:
            print(e)
    
    def on_predict(self, e):
        """Prediction"""
        try:
            self.predict_text.value = f"This is {load_image(self.image.src)}"
            self.predict_text.update()
        except Exception as e:
            print(e)
    