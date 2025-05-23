import requests
import subprocess

# Получаем данные с API
url = "https://oiot.ru/api/v1/?id=YYYY&token=XXXXXXXXXXXXXXXXXXXXXXXXX"
response = requests.get(url)
data = response.json()

for item in data['result'].values():
    # ХВС — холодная вода (округляем вниз)
    counter_hvs = int(float(item['data'][0]['counter_2']))
    # ГВС — горячая вода (округляем вниз)
    counter_gvs = int(float(item['data'][0]['counter_1']))

    # Текст СМС по формату
    sms_text = f"ВОДА ДОБАВИТЬ {counter_hvs} {counter_gvs}"

    # Отправка СМС на 7377
    subprocess.run(["termux-sms-send", "-n", "7377", sms_text])
    print(f"СМС отправлено: {sms_text}")
