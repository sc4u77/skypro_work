import requests
from datetime import datetime


def get_data(url):
    responce = requests.get(url)
    try:
        if responce.status_code == 200:
            return responce.json(), 'INFO: Данные получены успешно!\n'
        return None, f'ERROR: status_code: {status_code}\n'

    except requests.exceptoins.ConnectionError:
        return None, 'ERROR: Данные не получены (requests.exceptoins.ConnectionError)\n'
    except requests.exceptions.JSONDecodeError:
        return None, 'ERROR: Данные не получены (requests.exceptions.JSONDecodeError)\n'



def get_filtered_data(data, filtered_empty_from=False):
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    if filtered_empty_from:
        data = [x for x in data if 'from' in x]
    return data


def get_last_values(data, count_last_values):
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    data = data[:count_last_values]
    return data



def get_formatted_data(data):
    formatted_data = []
    for row in data:
        date = datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = row['description']
        sender = row['from'].split(-1)
        from_bill = f'{from_bill[:4]} {from_bill[4:6]}** **** {from_bill[-4:]}'
        from_info = ' '.join(sender)
        to = f'{row["to"].split()[0]} **{row["to"][-4:]}'
        operation_amount = f'{row["operationAmount"]["amount"]} {row["operationAmount"]["currency"]["name"]}'
        formatted_data.append(f"""\
{date} {description}
{from_info} {from_bill} -> {to}
{operation_amount}""")


    return formatted_data
