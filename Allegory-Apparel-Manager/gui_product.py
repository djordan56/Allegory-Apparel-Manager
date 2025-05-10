"""
Second window for managing product data
"""

try:
    import tkinter as tk
    from tkinter import messagebox
    import os
    from utils import validate_price, validate_size

    # Constants
    WINDOW_TITLE = "Add Product"
    WINDOW_SIZE = "600x700"
    IMAGE_PATH = os.path.join("assets", "images")

    def open_product_window(parent):
        top = tk.Toplevel(parent)
        top.title(WINDOW_TITLE)
        top.geometry(WINDOW_SIZE)

        # --- Form Fields ---
        entries = {}
        fields = [
            ("Product Name:", "name"),
            ("Size (S, M, L, XL):", "size"),
            ("Price:", "price")
        ]

        for label_text, key in fields:
            tk.Label(top, text=label_text).pack()
            entry = tk.Entry(top)
            entry.pack()
            entries[key] = entry

        def add_product():
            name = entries["name"].get().strip()
            size = entries["size"].get().strip()
            price = entries["price"].get().strip()

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

        # --- Display Jeans Images Using Loop ---
        jeans_images = [
            ("jeans_blue.png", "Blue Allegory Jeans"),
            ("jeans_black.png", "Black Allegory Jeans")
        ]

        for filename, alt_text in jeans_images:
            try:
                img = tk.PhotoImage(file=os.path.join(IMAGE_PATH, filename))
                label = tk.Label(top, image=img)
                label.image = img
                label.pack()
                tk.Label(top, text=alt_text).pack()
            except Exception as e:
                tk.Label(top, text=f"Failed to load: {filename}").pack()

except ModuleNotFoundError as e:
    print("This environment does not support tkinter or it is not installed.")
    print(f"Error: {e}")
except Exception as e:
    print("An unexpected error occurred.")
    print(f"Error: {e}")
