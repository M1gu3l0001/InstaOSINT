def goto(linenum):
    global line
    line = linenum
from contextlib import suppress
import os
clear = lambda: os.system('clear')
clear()
print("\n")
print("\n")
import src.asciiart as asciiart
from instapy import InstaPy
print(asciiart.ascii_art)
import re
import requests
import json
import configparser
import instaloader
from getpass import getpass
from datetime import datetime
def getCookie():
        link = 'https://www.instagram.com/accounts/login/'
        login_url = 'https://www.instagram.com/accounts/login/ajax/'

        time = int(datetime.now().timestamp())

        payload = {'username': globaluser.user_username,'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:' + globaluser.user_password,'queryParams': {},'optIntoOneTap': 'false'}
        with requests.Session() as s:
            r = s.get(link)
            csrf = re.findall(r"csrf_token\":\"(.*?)\"",r.text)[0]
            r = s.post(login_url,data=payload,headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": "https://www.instagram.com/accounts/login/",
                "x-csrftoken":csrf
            })
            with open("cookie.json", "w") as f:
                f.write((str(s.cookies.get_dict()).replace("'", '"')))
class globaluser:
    config = configparser.ConfigParser(interpolation=None)
    config.read("config.ini")
    username = config['Config']['username']
    password = config['Config']['password']
    
    user_username = username
    if (user_username == ''):
        print("The username can't be empty")
        exit()  
    user_password = password

def main():
    if os.getenv('LANG') == 'en_US.UTF-8':
        for i in range(0,1):
            print('1. Follow the followers of a target\n')
            print('2. Unfollow the users that dont follow me back\n')
            print('3. Fetch the email and number phone of a user\n')
            print('4. Fetch the email and number phone of followers of a user\n')
            print('5. Remove Inative Followers\n')
            print('99. Exit\n')

            choice = int(input('Choice One:\n'))

        if (choice == 1):

            target = input('[InstaOsint] put the @ username(example: idk123):')
            print('\n')

            if (target == ''):
                print("[InstaOsint] the @ of the user can't be empyt\n")
                main()
                
            

            user_username = globaluser.user_username

            if (user_username == ''):
                print("[InstaOsint] The username can't be empty\n")
                main()
            

            user_password = globaluser.user_password
            users_amount = input('type how many followers of -> ' + target + ' <- you want to follow:')


            session = InstaPy(username= user_username, password = user_password, headless_browser= False)

            session.login()
            session.follow_user_followers(usernames= target, amount= 17, sleep_delay= 600)
            session.end()
    
            if (choice == 2):
                    user_username = globaluser.user_username
                    if (user_username == ''):
                        print("[InstaOsint] The username can't be empty\n")
                        main()

                    user_password = globaluser.user_password
                    nonFollowers_amount = input('[InstaOsint] Put the amount of users that dont follow you back that you want to unfollow: ')

                    session = InstaPy(username= user_username, password = user_password, headless_browser= False)

                    session.login()
                    session.unfollow_users(amount= nonFollowers_amount, nonFollowers= True, unfollow_after= 0, sleep_delay= 600)
                    session.end()

    if (choice == 3):
        class emailphone:
            user_username = globaluser.user_username
            user_password = globaluser.user_password
            target_username = input('[InstaOsint] put the username that you want to fetch the email and number phone:')
        

        if os.path.exists("cookie.json"):
            os.remove("cookie.json")
            getCookie()
        else:
            getCookie()

        clear = lambda: os.system('clear')
        if os.path.exists("response.json"):
            os.remove("response.json")
        else:
            print("")
        
        if os.path.exists("response2.json"):
            os.remove("response2.json")
        else:
            print("")
        f1 = open('cookie.json')
        data1 = json.load(f1)
        response = requests.get(' https://i.instagram.com/api/v1/users/web_profile_info/?username=' + emailphone.target_username, cookies=data1, headers={'x-ig-app-id': '1217981644879628'})
        print(response.url)
        print(response.status_code)
        print(response.text)
        open("response.json", "w").write(json.dumps(response.json(), indent=4))
        f = open('response.json')
        data = json.load(f)
        id = data["data"]["user"]["id"]
        url = "https://i.instagram.com/api/v1/users/" + id + "/info/"
        print(url)
        response2 = requests.get(url, cookies=data1, headers={"x-ig-app-id": "1217981644879628"})
        print(response2.status_code)
        print(response2.headers)
        print(response2.text)
        with open("response2.json", "w") as f:
            f.write(json.dumps(response2.json(), indent=4))
        f2 = open('response2.json')
        data2 = json.load(f2)
        phone = data2["user"]["contact_phone_number"]
        if (phone == None):
            print("[InstaOsint] Failed to fetch the number phone")
        email = data2["user"]["public_email"]
        if (email == None):
            print("[InstaOsint] Failed to fetch the email")
        clear()
        print(phone)
        print(email)

        with open("result.txt", "a") as f:
            f.write(emailphone.target_username + " - " + phone + " - " + email + "\n")
            
        print("results saved in the file with the name 'result.txt'! \n")
        main()

    if (choice == 4):
        class bemailpassword:
            user_username = globaluser.user_username
            user_password = globaluser.user_password
            target_username = input('[InstaOsint] put the username that you want to fetch email and number phone from followers:')
        if os.path.exists('fwersid.txt'):
            os.remove('fwersid.txt')
        if os.path.exists("cookie.json"):
            os.remove("cookie.json")
        else:
            getCookie()
        cookie = json.load(open('cookie.json'))
        response = requests.get('https://i.instagram.com/api/v1/users/web_profile_info/?username=' + bemailpassword.target_username, cookies=cookie, headers={"x-ig-app-id": "1217981644879628"})
        with open("response.json", "w") as f:
            f.write(response.text)
        f = open('response.json')
        data = json.load(f)
        id = data["data"]["user"]["id"]
        
        
        response = requests.get('https://i.instagram.com/api/v1/friendships/'+ id + '/followers/', cookies=cookie, headers={"x-ig-app-id": "1217981644879628"})
        print(response.url)
        open("responsefollower.json", "w").write(json.dumps(response.json(), indent=4))
        rf = open('responsefollower.json')
        data = json.load(rf)
        for i in data['users']:
            print(i['pk'])
            open("fwersid.txt", "a").write(str(i['pk']) + "\n")

        f1 = open('cookie.json') #user credentials
        data1 = json.load(f1) 
        f2 = open('response2.json')
        data2 = json.load(f2)
         # read all lines at once
        iddata = open("fwersid.txt").readlines()
        for i in iddata:
            url = "https://i.instagram.com/api/v1/users/" + str(i).strip() + "/info/"
            print("idData -> " + str(iddata))
            print("URL -> " + url)
            response2 = requests.get(url, cookies=cookie, headers={"x-ig-app-id": "1217981644879628"})
            print(response2.status_code)
            print(response2.headers)
            with open("response2.json", "w") as f:
                f.write(response2.text)
            with suppress(KeyError):
                if data2["user"]["contact_phone_number"] in data2:
                    fwersphone = data2["user"]["contact_phone_number"]
            with suppress(KeyError):  
                if data2["user"]["public_email"] in data2:
                    fwersemail = data2["user"]["public_email"]

            fwersusername = data2["user"]["username"]

            with suppress(NameError):
                with open ("fwersresult.txt", "a") as f:
                    f.write(fwersusername + " - " + fwersphone + " - " + fwersemail + "\n")
            with suppress(NameError):
                print(fwersphone)
                print(fwersemail)
                print(fwersusername)
  
        print("file saved with name 'fwersresult.txt'")
        main()

    if (choice == 5):
        print("wow")
        accountName = globaluser.username
        if os.path.exists("followers.txt"):
            os.remove("followers.txt")
        else:
            print("")

        L = instaloader.Instaloader()
        
        #Login or load session
        username = "m1gu3l0001"
        password = "M1gu3lPC@#wowidk"
        L.login(username, password)  # (login)
        
        #Obtain profile metadata
        profile = instaloader.Profile.from_username(L.context, accountName)
        
        follow_list = []
        
        for followee in profile.get_followers():
            follow_list.append(followee.userid)
            open('followersId.json', 'w').write(str({"followerId": follow_list} ).replace("'", '"'))
            print(follow_list)
        followersId = open('followersId.json', 'r').read()
        print(followersId["followerId"][0])
        main()
    if (choice == 99):
        print('Leaving...')
        print('Developed by M1gu3l0001')
        os.remove('cookie.json')
        os.remove('response.json')
        os.remove('response2.json')
        os.remove("followersId.json")
        exit()
    else:
        print('Invalid option')
        main()
main()