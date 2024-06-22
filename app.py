import flet as ft
from model import load_image

class App(ft.Column):
    """Main class for representing"""
    def __init__(self, page):
        super().__init__()
        self.page = page
        # Title
        self.title = ft.Text("Welcome to Garbage Classifier App", size=40, expand=True, text_align=ft.TextAlign.CENTER)
        
        # Image picker
        self.file_picker = ft.FilePicker(on_result=self.on_dialog_result)
        self.button_picker = ft.IconButton(icon=ft.icons.UPLOAD_FILE, on_click=self.upload_file, adaptive=True, scale=1.5, tooltip="Load image")
        self.text_file = ft.Text(value="", size=25, text_align=ft.TextAlign.CENTER, no_wrap=False)

        # Image
        self.image = ft.Image(src="images/", fit=ft.ImageFit.CONTAIN, width=400, height=400, expand=True)
        self.image_path = ""
        # Prediction 
        self.predict_btn = ft.TextButton(text="Predict", disabled=True, visible=False, scale=1.5, adaptive=True, on_click=self.on_predict)

        self.predict_text = ft.Text(value="", size=30)
        self.predict_ring_load = ft.ProgressRing(visible=False)
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
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        controls=[
                            self.predict_text,
                            self.predict_ring_load
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
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
            # Image string path
            self.image_path = e.files[0].path
    
            self.image.src = e.files[0].path
            self.text_file.value = e.files[0].name
            self.image.update()
            self.text_file.update()
            # Set prediction text to empty
            self.predict_text.value = ""
            self.predict_text.update()

            # Predict button set visible
            self.predict_btn.visible = True
            self.predict_btn.disabled = False
            self.predict_btn.update()
        except Exception as e:
            print(e)
            self.display_error_message("Can't open the file")
    
    def check_loading_prediction(self):
        """Check if the prediction is loading -> shows ring"""
        if self.predict_text.value == "":
            self.predict_ring_load.visible = True
        else:
            self.predict_ring_load.visible= False
        self.predict_ring_load.update()

    def on_predict(self, e):
        """Prediction"""
        try:
            # Check to show ring loading
            self.check_loading_prediction()
            self.predict_text.value = f"This is {load_image(self.image_path)} garbage"
            self.predict_text.update()
            # Make visible loading to False
            self.check_loading_prediction()

        except Exception as e:
            print("Error model", e)
            self.predict_ring_load.value = ""
            self.predict_ring_load.update()
            self.display_error_message("Can't predict. Please, try again.")

    def display_error_message(self, message):
        """Displaying error on the page"""
        dialog = ft.AlertDialog(title=ft.Text(message))
        self.page.overlay.append(dialog)
        dialog.open = True
        self.page.update()