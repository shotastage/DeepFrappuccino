import os
import subprocess


frappuccino_data = {
    "white_snow_chocolate_frappuccino": {
        "title": "White Snow Chocolate Frappuccino",
        "title_jp": "ホワイト チョコレート スノー フラペチーノ",
        "size": "tall" 
    },
    "christmas_strawberry_cake_frappuccino": {
        "title": "Christmas Strawberry Cake Frappuccino",
        "title_jp": "クリスマス ストロベリー ケーキ フラペチーノ",
        "size": "tall" 
    },
}



def hiec_jpg():
    DIR = ""

    FILES = os.listdir(DIR)

    for f in FILES:
        command = 'sips --setProperty format jpeg ' + DIR + f +  ' --out ' + DIR + f.replace('.HEIC','.jpg')
        subprocess.call(command, shell=True)
