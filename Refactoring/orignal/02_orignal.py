def process_order(order):
    if order["payment_type"] == "credit_card":
        card_number = order["card_number"]
        expiration_date = order["expiration_date"]
        card_security_code = order["card_security_code"]

        if len(card_number) != 16:
            raise ValueError("Invalid card number")
        if not expiration_date:
            raise ValueError("Expiration date is missing")
        if len(card_security_code) != 3:
            raise ValueError("Invalid card security code")

        print("Processing credit card payment...")
        print(f"Card number: {card_number}, Expiration date: {expiration_date}")

    elif order["payment_type"] == "paypal":
        paypal_email = order["paypal_email"]

        if not paypal_email:
            raise ValueError("PayPal email is missing")

        print("Processing PayPal payment...")
        print(f"PayPal email: {paypal_email}")

    else:
        print("Invalid payment type")

    if order["shipping_address"] == "":
        raise ValueError("Shipping address is missing")

    print(f"Shipping to: {order['shipping_address']}")

    if order["quantity"] <= 0:
        raise ValueError("Quantity must be greater than zero")

    print(f"Quantity: {order['quantity']}")

    total_price = order["price"] * order["quantity"]
    print(f"Total price: {total_price}")

    print("Order processed successfully!")


# Example usage:
order = {
    "payment_type": "credit_card",
    "card_number": "1234567812345678",
    "expiration_date": "12/24",
    "card_security_code": "123",
    "shipping_address": "123 Main St",
    "quantity": 2,
    "price": 100.0
}

process_order(order)