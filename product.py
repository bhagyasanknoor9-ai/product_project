def format_product_details(product_id: int | str, name: str, quantity: int, price: float) -> str:
    """Accepts product details and returns a well-formatted string."""
    return (
        f"Product Details:\n"
        f"-----------------\n"
        f"Product ID : {product_id}\n"
        f"Name       : {name}\n"
        f"Quantity   : {quantity}\n"
        f"Price      : ${price:.2f}"
    )


if __name__ == "__main__":
    print(format_product_details(101, "Wireless Mouse", 5, 25.50))