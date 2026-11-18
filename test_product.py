from product import format_product_details


def test_product_id():
    result = format_product_details(101, "Wireless Mouse", 5, 25.50)
    assert "Product ID : 101" in result


def test_product_name():
    result = format_product_details(101, "Wireless Mouse", 5, 25.50)
    assert "Name       : Wireless Mouse" in result


def test_product_quantity():
    result = format_product_details(101, "Wireless Mouse", 5, 25.50)
    assert "Quantity   : 5" in result


def test_product_price():
    result = format_product_details(101, "Wireless Mouse", 5, 25.50)
    assert "Price      : $25.50" in result


def test_complete_product_details():
    expected = (
        "Product Details:\n"
        "-----------------\n"
        "Product ID : 101\n"
        "Name       : Wireless Mouse\n"
        "Quantity   : 5\n"
        "Price      : $25.50"
    )

    assert format_product_details(101, "Wireless Mouse", 5, 25.50) == expected