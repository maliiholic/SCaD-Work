def validate_credit_card(order_data):
    card_number = order_data.get("card_number", "")
    expiration_date = order_data.get("expiration_date", "")
    card_security_code = order_data.get("card_security_code", "")

    # Adding assertion to check card number length
    assert len(card_number) == 16, "Card number must be 16 digits"

    assert expiration_date, "Expiration date is missing"
    assert len(card_security_code) == 3, "Card security code must be 3 digits"

    print("Processing credit card payment...")
    print(f"Card number: {card_number}, Expiration date: {expiration_date}")


def validate_paypal(order_data):
    paypal_email = order_data.get("paypal_email", "")

    # Adding assertion to check if paypal_email is present
    assert paypal_email, "PayPal email is missing"

    print("Processing PayPal payment...")
    print(f"PayPal email: {paypal_email}")


def validate_shipping(order_data):
    shipping_address = order_data.get("shipping_address", "")

    # Adding assertion to check if shipping address is present
    assert shipping_address, "Shipping address is missing"

    print(f"Shipping to: {order_data['shipping_address']}")


def validate_quantity_and_calculate(order_data):
    quantity = order_data.get("quantity", 0)
    price = order_data.get("price", 0.0)

    # Adding assertion to check if quantity is greater than zero
    assert quantity > 0, "Quantity must be greater than zero"

    total_price = quantity * price
    print(f"Quantity: {quantity}")
    print(f"Total price: {total_price}")
    return total_price


def process_order(order_data):
    payment_type = order_data.get("payment_type", "")

    # Checking if the payment type is either credit card or paypal
    assert payment_type in ["credit_card", "paypal"], "Invalid payment type"

    if payment_type == "credit_card":
        validate_credit_card(order_data)
    elif payment_type == "paypal":
        validate_paypal(order_data)

    validate_shipping(order_data)
    validate_quantity_and_calculate(order_data)

    print("Order processed successfully!")
