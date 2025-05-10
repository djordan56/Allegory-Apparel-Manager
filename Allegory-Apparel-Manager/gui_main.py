"""
Main GUI window for Allegory Apparel Manager
"""

import tkinter as tk
import os
from gui_product import open_product_window
from utils import exit_app

def open_main_window():
    root = tk.Tk()
    root.title("Allegory Apparel Manager")
    root.geometry("800x800")

    # Welcome Label
    tk.Label(root, text="Welcome to Allegory Apparel Manager!", font=("Helvetica", 16)).pack(pady=20)

    # Navigation Buttons
    tk.Button(root, text="Manage Products", command=lambda: open_product_window(root)).pack(pady=10)
    tk.Button(root, text="Exit", command=lambda: exit_app(root)).pack(pady=10)

    # --- Display product images ---
    image_path = os.path.join("assets", "images")

    # Sweatshirt
    sweatshirt_img = tk.PhotoImage(file=os.path.join(image_path, "sweatshirt_black.png"))
    sweatshirt_label = tk.Label(root, image=sweatshirt_img)
    sweatshirt_label.image = sweatshirt_img  # prevent garbage collection
    sweatshirt_label.pack()
    tk.Label(root, text="Black Allegory Sweatshirt").pack()

    # White Shirt
    shirt_img = tk.PhotoImage(file=os.path.join(image_path, "shirt_white.png"))
    shirt_label = tk.Label(root, image=shirt_img)
    shirt_label.image = shirt_img
    shirt_label.pack()
    tk.Label(root, text="White Allegory Shirt").pack()

    # Blue Jeans
    jeans_blue_img = tk.PhotoImage(file=os.path.join(image_path, "jeans_blue.png"))
    jeans_blue_label = tk.Label(root, image=jeans_blue_img)
    jeans_blue_label.image = jeans_blue_img
    jeans_blue_label.pack()
    tk.Label(root, text="Blue Allegory Jeans").pack()

    # Black Jeans
    jeans_black_img = tk.PhotoImage(file=os.path.join(image_path, "jeans_black.png"))
    jeans_black_label = tk.Label(root, image=jeans_black_img)
    jeans_black_label.image = jeans_black_img
    jeans_black_label.pack()
    tk.Label(root, text="Black Allegory Jeans").pack()

    root.mainloop()

if __name__ == "__main__":
    open_main_window()
