
from utils import get_data, get_filtered_data, get_last_values, get_formatted_data

data_1 = []


def main():
    operations_link = 'https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1676391093154&signature=mul2kqNNZ3whe5_K8dXpLchmAwDZndty52Zq-Z_Cnq0&downloadName=operations.json'
    FILTERED_EMPTY_FROM = True
    COUNT_LAST_VALUES = 5

    data, info = get.data(operations_link)
    if not data:
        exit(info)
    else:
        print(info)

    new_data = get_filtered_data(new_data, filtered_empty_form=FILTERED_EMPTY_FROM)
    new_data = get_last_values(new_data, COUNT_LAST_VALUES)
    new_data = get_formatted_data(new_data)


    print('INFO: Вывод данных:')
    for row in new_data:
        print(row, end='\n\n')


if __name__ == '__main__':
    main()