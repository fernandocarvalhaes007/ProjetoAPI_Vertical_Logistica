import json
from atributos import parse_line

def process_order_line(input_line, users):
    user_id, name, order_id, product_id, value, date = parse_line(input_line)

    if user_id not in users:
        users[user_id] = {
            "user_id": user_id,
            "name": name,
            "orders": {}
        }

    if order_id not in users[user_id]["orders"]:
        users[user_id]["orders"][order_id] = {
            "order_id": order_id,
            "total": 0,
            "date": date,
            "products": {}
        }

    if product_id not in users[user_id]["orders"][order_id]["products"]:
        users[user_id]["orders"][order_id]["products"][product_id] = {
            "product_id": product_id,
            "value": 0
        }

    users[user_id]["orders"][order_id]["products"][product_id]["value"] += value
    users[user_id]["orders"][order_id]["total"] += value

def process_upload_data(file_lines):
    users = {}

    for input_line in file_lines:
        try:
            process_order_line(input_line, users)
        except Exception as e:
            print(f"Erro ao processar a linha do pedido: {e}")

    output_data = []
    for user in users.values():
        user_orders = list(user["orders"].values())
        for order in user_orders:
            order["total"] = f"R$ {order['total']:.2f}".replace('.', ',')
            order["products"] = list(order["products"].values())
            for product in order["products"]:
                product["value"] = f"R$ {product['value']:.2f}".replace('.', ',')
        user["orders"] = user_orders
        output_data.append(user)

    return json.dumps(output_data, indent=2)