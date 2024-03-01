import json
from atributos import parse_line

def process_orders(input_file):
    users = {}
    with open(input_file, 'r') as file:
        for line in file:
            user_id, name, order_id, product_id, value, date = parse_line(line)
            
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

    output_data = []
    for user in users.values():
        user_orders = list(user["orders"].values())
        for order in user_orders:
            order["total"] = f"R$ {order['total']:.2f}".replace('.',',')
            order["products"] = list(order["products"].values())
            for product in order["products"]:
             product["value"] = f"R$ {product['value']:.2f}".replace('.', ',')
        user["orders"] = user_orders
        output_data.append(user)

    return output_data


def process_upload_data(file_path):
    input_files = [file_path]
    orders_data_list = []

    for i, input_file in enumerate(input_files):
        orders_data = process_orders(input_file)
        orders_data_list.append(orders_data)

        output_str = json.dumps(orders_data, indent=2)

    return output_str
