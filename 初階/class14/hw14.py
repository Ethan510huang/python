import pygame

from datetime import datetime


def standardize_date(input_date):
    date_format = ["%Y-%m-%d", "%d/%m/%Y", "%m-%d-%Y", "%Y/%m/%d"]

    for format in date_format:
        try:
            standardize_date = datetime.strptime(input_date, format)
            return standardize_date.strftime("%Y-%m-%d")
        except:
            continue

    pygame.init()
    pygame.mixer.music.load("Alarm.mp3")
    while True:
        pygame.mixer.music.play()
        print(
            "error error error emergency!!!!! error error error emergency!!!!! error error error emergency!!!!! error error error emergency!!!!! error error error emergency!!!!! error error error emergency!!!!! error error error emergency!!!!! error error error emergency!!!!! error error error emergency!!!!! error error error emergency!!!!! error error error emergency!!!!! error error error emergency!!!!! error error error emergency!!!!! error error error emergency!!!!! error error error emergency!!!!!"
        )
        while pygame.mixer.music.get_busy() == True:
            continue


print(standardize_date("2023-12-01"))
print(standardize_date("01/12/2023"))
print(standardize_date(""))
