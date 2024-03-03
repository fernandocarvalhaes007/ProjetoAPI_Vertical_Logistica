from datetime import datetime

def parse_line(line):
    
        user_id = int(line[:10].strip())
        name = line[10:55].strip()
        order_id = int(line[55:65].strip())
        product_id = int(line[65:75].strip())
        value = float(line[75:87].strip())
        date_str = line[87:95].strip()
        date = convert_to_date(date_str)

        return user_id, name, order_id, product_id, value, date

def convert_to_date(date_str):
    return datetime.strptime(date_str, '%Y%m%d').strftime('%d/%m/%Y') if date_str else None