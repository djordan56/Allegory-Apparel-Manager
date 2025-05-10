"""
Utility functions for validation and exit
"""

def validate_price(price):
    """Check if price is a valid float greater than 0."""
    try:
        return float(price) > 0
    except ValueError:
        return False

def validate_size(size):
    """Check if size is one of the allowed sizes."""
    return size.upper() in ["S", "M", "L", "XL"]

def exit_app(root):
    """Exit the application."""
    root.destroy()
