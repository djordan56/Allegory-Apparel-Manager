"""
Second window for managing product data
"""

import tkinter as tk
from tkinter import messagebox
import os
from utils import validate_price, validate_size

def open_product_window(parent):
    top = tk.Toplevel(parent)
    top.title("Add Product")
    top.geometry("600x700")

    # Form Fields
    tk.Label(top, text="Product Name:").pack()
    name_entry = tk.Entry(top)
    name_entry.pack()

    tk.Label(top, text="Size (S, M, L, XL):").pack()
    size_entry = tk.Entry(top)
    size_entry.pack()

    tk.Label(top, text="Price:").pack()
    price_entry = tk.Entry(top)
    price_entry.pack()

    # Add Product Logic
    def add_product():
        name = name_entry.get().strip()
        size = size_entry.get().strip()
        price = price_entry.get().strip()

        if not name or not size or not price:
            messagebox.showerror("Input Error", "All fields are required.")
            return
        if not validate_size(size):
            messagebox.showerror("Input Error", "Size must be S, M, L, or XL.")
            return
        if not validate_price(price):
            messagebox.showerror("Input Error", "Price must be a number greater than 0.")
            return

        messagebox.showinfo("Success", f"Product '{name}' added successfully!")

    tk.Button(top, text="Submit", command=add_product).pack(pady=10)
    tk.Button(top, text="Close", command=top.destroy).pack()

    # --- Display Jeans Images ---
    image_path = os.path.join("assets", "images")

    jeans_blue_img = tk.PhotoImage(file=os.path.join(image_path, "jeans_blue.png"))
    jeans_blue_label = tk.Label(top, image=jeans_blue_img)
    jeans_blue_label.image = jeans_blue_img
    jeans_blue_label.pack()
    tk.Label(top, text="Blue Allegory Jeans").pack()

    jeans_black_img = tk.PhotoImage(file=os.path.join(image_path, "jeans_black.png"))
    jeans_black_label = tk.Label(top, image=jeans_black_img)
    jeans_black_label.image = jeans_black_img
    jeans_black_label.pack()
    tk.Label(top, text="Black Allegory Jeans").pack()
