import requests


def get_exchange_rate():
    # Получаем курс рубля к тугрику
    url = "https://api.exchangerate-api.com/v4/latest/RUB"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['rates']['MNT']  # Получаем курс к монгольскому тугрику
    else:
        print("Ошибка при получении данных о курсе валют.")
        return None


def convert_rub_to_mnt(rub_amount, exchange_rate):
    return rub_amount * exchange_rate


def main():
    rub_amount = float(input("Введите сумму в рублях: "))

    exchange_rate = get_exchange_rate()
    if exchange_rate:
        mnt_amount = convert_rub_to_mnt(rub_amount, exchange_rate)
        print(f"{rub_amount} рублей равны {mnt_amount:.2f} монгольских тугриков (по курсу {exchange_rate:.2f}).")


if __name__ == "__main__":
    main()