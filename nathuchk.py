import urllib.request
import json
import os
import time
import mashina
import base
import banner
COLOR_CODE = {
    "RESET": "\033[0m",
    "UNDERLINE": "\033[04m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[93m",
    "RED": "\033[31m",
    "CYAN": "\033[36m",
    "BOLD": "\033[01m",
    "PINK": "\033[95m",
    "URL_L": "\033[36m",
    "LI_G": "\033[92m",
    "F_CL": "\033[0m",
    "DARK": "\033[90m",
}

print(banner.banner)

select = input(f'{COLOR_CODE["CYAN"]}Выберите пункт: ')

if select == '1':
    getIP = input(f'{COLOR_CODE["YELLOW"]}[+] Введите IP ')
    url = "https://ipinfo.io/" + getIP + "/json"
    try:
        getInfo = urllib.request.urlopen(url)
    except:
        print("\nIp не найдено!\n")
    infoList = json.load(getInfo)
    def whoisIPinfo(ip):
        try:
            myComand = "whois " + getIP
            whoisInfo = os.popen(myComand).read()
            return whoisInfo
        except:
            return "\n Ошибка \n"
    print("IP: ", infoList["ip"])
    print("Город: ", infoList["city"])
    print("Регион: ", infoList["region"])
    print("Страна: ", infoList["country"])
    print("Провайдер: ", infoList["hostname"])
    print("Координаты: ", infoList["loc"])
    print("Временная зона: ", infoList["timezone"])
    print("Индекс: ", infoList["postal"])
    print("Орг: ", infoList["org"])
    time.sleep(1)
    print('')
if select == '3':
    print('Для пробива перейдите в бота:')
    print(mashina.bot)
if select == '4':
    print(base.base)
if select == '2':
    username = input("Введите юсернейм: ")
    print("Проверьте эти ссылки: ")
    print("телеграмм: https://t.me/" + username)
    print("Вконтакте: https://vk.com/" + username)
    print("Одноклассники: https://ok.ru/" + username)
    print("Github: https://github.com/" + username)
    print(" ")
    print("Поиск в яндексе: ")
    print("https://yandex.ru/search/?text=" + username)
if select == '6':
    exit()