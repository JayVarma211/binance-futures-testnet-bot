import logging


def create_order(client, symbol, side, order_type, quantity, price=None):
    params = {
        "symbol": symbol.upper(),
        "side": side,
        "type": order_type,
        "quantity": quantity
    }

    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    logging.info(f"Placing order with params: {params}")

    response = client.place_order(params)

    logging.info(f"Order response: {response}")

    return response
def create_stop_limit_order(client, symbol, side, quantity, stop_price, price):
    params = {
        "symbol": symbol.upper(),
        "side": side,
        "type": "STOP",
        "quantity": quantity,
        "price": price,
        "stopPrice": stop_price,
        "timeInForce": "GTC"
    }

    return client.place_order(params)