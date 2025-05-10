"""
Main GUI window for Allegory Apparel Manager
Note: This module requires a system with a GUI environment that supports tkinter.
If you're running in a headless or restricted environment (like some sandboxed interpreters),
this module will not work due to missing GUI support.
"""

try:
    import tkinter as tk
    import os
    from gui_product import open_product_window  # Imports function to open second window
    from utils import exit_app  # Import exit function with validation

    # Constants
    WINDOW_TITLE = "Allegory Apparel Manager"
    WINDOW_SIZE = "800x800"
    FONT_HEADER = ("Helvetica", 16)
    IMAGE_PATH = os.path.join("assets", "images")

    def open_main_window():
        root = tk.Tk()
        root.title(WINDOW_TITLE)
        root.geometry(WINDOW_SIZE)

        # Welcome Label
        tk.Label(root, text="Welcome to Allegory Apparel Manager!", font=FONT_HEADER).pack(pady=20)

        # Navigation Buttons
        tk.Button(root, text="Manage Products", command=lambda: handle_open_product(root)).pack(pady=10)
        tk.Button(root, text="Exit", command=lambda: handle_exit(root)).pack(pady=10)

        # --- Display product images using a loop ---
        products = [
            ("sweatshirt_black.png", "Black Allegory Sweatshirt"),
            ("shirt_white.png", "White Allegory Shirt"),
            ("jeans_blue.png", "Blue Allegory Jeans"),
            ("jeans_black.png", "Black Allegory Jeans")
        ]

        for filename, label_text in products:
            try:
                img = tk.PhotoImage(file=os.path.join(IMAGE_PATH, filename))
                img_label = tk.Label(root, image=img)
                img_label.image = img  # prevent garbage collection
                img_label.pack()
                tk.Label(root, text=label_text).pack()
            except Exception as e:
                tk.Label(root, text=f"Image load failed: {filename}").pack()

        root.mainloop()

    def handle_open_product(root):
        open_product_window(root)

    def handle_exit(root):
        exit_app(root)

    if __name__ == "__main__":
        open_main_window()

except ModuleNotFoundError as e:
    print("This environment does not support tkinter or it is not installed.")
    print(f"Error: {e}")
except Exception as e:
    print("An unexpected error occurred.")
    print(f"Error: {e}")
