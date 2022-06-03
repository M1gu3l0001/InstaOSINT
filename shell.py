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
from getpass import getpass
from datetime import datetime
class globaluser:

    config = configparser.ConfigParser(interpolation=None)
    config.read("config.ini")
    username = config['Config']['username']
    password = config['Config']['password']
    if os.getenv('LANG') == 'pt_BR.UTF-8':
        
        user_username = username
        if (user_username == ''):
            print("O nome de usuário não pode ser vazio")
            exit()  
        user_password = password
    if os.getenv('LANG') == 'en_US.UTF-8':
            
            user_username = username
            if (user_username == ''):
                print("The username can't be empty")
                exit()  
            user_password = password

if os.getenv('LANG') == 'en_US.UTF-8':
    for i in range(0,1):
        print('1. Follow the followers of a target\n')
        print('2. Unfollow the users that dont follow me back\n')
        print('3. Fetch the email and number phone of a user\n')
        print('4. Fetch the email and number phone of followers of a user\n')
        print('99. Exit\n')

        choice = int(input('Choice One:\n'))

        if (choice == 1):

            target = input('[InstaOsint] put the @ username(example: idk123):')
            print('\n')

            if (target == ''):
                print("[InstaOsint] the @ of the user can't be empyt\n")
                continue
                
            

            user_username = globaluser.user_username

            if (user_username == ''):
                print("[InstaOsint] The username can't be empty\n")
                continue
            

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
                        continue

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
        

            if not os.path.exists("cookie.json"):
                class getcookie:
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
                        print(r.status_code)
                        print(r.url)
                        print(r.text)

                        print(s.cookies)
                        print(r.headers)


        

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
        response = requests.get('https://www.instagram.com/' + emailphone.target_username + '/?__a=1', cookies=data1)
        with open("response.json", "w") as f:
            f.write(response.text)
        f = open('response.json')
        data = json.load(f)
        id = data["graphql"]["user"]["id"]
        url = "https://i.instagram.com/api/v1/users/" + id + "/info/"
        print(url)
        response2 = requests.get(url, cookies=data1, headers={"x-ig-app-id": "936619743392459"})
        print(response2.status_code)
        print(response2.headers)
        with open("response2.json", "w") as f:
            f.write(response2.text)
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
            
        print("file saved with the name ""result.txt""")

    if (choice == 4):
        class bemailpassword:
            user_username = globaluser.user_username
            user_password = globaluser.user_password
            target_username = input('[InstaOsint] put the username that you want to fetch email and number phone from followers:')
        if os.path.exists('fwersid.txt'):
            os.remove('fwersid.txt')
        if not os.path.exists("cookie.json"):
            class getcookie:
                link = 'https://www.instagram.com/accounts/login/'
                login_url = 'https://www.instagram.com/accounts/login/ajax/'
                time = int(datetime.now().timestamp())
                payload = {'username': bemailpassword.user_username,'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:' + bemailpassword.user_password,'queryParams': {},'optIntoOneTap': 'false'}
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
                    print(r.status_code)
                    print(r.url)
                    print(r.text)
                    print(s.cookies)
            
        
        cookie = json.load(open('cookie.json'))
        response = requests.get('https://www.instagram.com/' + bemailpassword.target_username + '/?__a=1', cookies=cookie, headers={"x-ig-app-id": "936619743392459"})
        with open("response.json", "w") as f:
            f.write(response.text)
        f = open('response.json')
        data = json.load(f)
        id = data["graphql"]["user"]["id"]
        
        
        response = requests.get('https://i.instagram.com/api/v1/friendships/'+ id + '/followers/', cookies=cookie, headers={"x-ig-app-id": "936619743392459"})
        print(response.url)
        with open("responsefollower.json", "w") as f:
                    f.write(response.text)
        rf = open('responsefollower.json')
        data = json.load(rf)
        for i in data['users']:
            print(i['pk'])
            with open("fwersid.txt", "a")as iddata:
                iddata.write(str(i['pk']) + "\n")

        f1 = open('cookie.json') #user credentials
        with open("fwersid.txt") as f:
            iddata = f.readlines() # read all lines at once
        data1 = json.load(f1) 
        f2 = open('response2.json')
        data2 = json.load(f2)
    class bruh:    
        for i in iddata:
                url = "https://i.instagram.com/api/v1/users/" + str(i).strip() + "/info/"
                print(iddata)
                print(url)
                response2 = requests.get(url, cookies=cookie, headers={"x-ig-app-id": "936619743392459"})
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




    if (choice == 99):
        print('Leaving...')
        print('Developed by M1gu3l0001')
        os.remove('cookie.json')
        os.remove('response.json')
        os.remove('response2.json')
        exit()
    else:
        print('Invalid option')

        
if os.getenv('LANG') == 'pt_BR.UTF-8':
    for i in range(0,10):
        print('1. SEGUIR OS FOLLOWERS DE UM TARGET\n')
        print('2. DEIXAR DE SEGUIR TODOS AS PESSOAS QUE EU SIGO QUE NÃO ME SEGUEM DE VOLTA\n')
        print('3. Pegar o email e nº de telefone de um usuário\n')
        print('4. Pegar o email e nº de telefone dos seguidores de um usuário\n')
        print('99. Sair do Programa\n')
        print(os.getenv('LANG'))

    
        choice = int(input('Escolha um:\n'))

        if (choice == 1):

            target = input('[InstaOsint] Coloque o @ do usuario(ex: fulano123):')
            print('\n')

            if (target == ''):
                print('[InstaOsint] O @ do usuario nao pode ser vazio\n')
                continue
                
            

            user_username = globaluser.user_username

            if (user_username == ''):
                print('[InstaOsint] O nome de usuário nao pode ser vazio')
                continue
            

            user_password = globaluser.user_password
            users_amount = input('Digite quantos seguidores de -> ' + target + ' <- você quer seguir:')


            session = InstaPy(username= user_username, password = user_password, headless_browser= False)

            session.login()
            session.follow_user_followers(usernames= target, amount= 17, sleep_delay= 600)
            session.end()
    
            if (choice == 2):
                    user_username = globaluser.user_username
                    if (user_username == ''):
                        print('[InstaOsint] O nome de usuário nao pode ser vazio')
                        continue

                    user_password = globaluser.user_password
                    nonFollowers_amount = input('[InstaOsint] Coloque a quantidade de pessoas que você segue mas não seguem de volta que deseja deixar de seguir:')

                    session = InstaPy(username= user_username, password = user_password, headless_browser= False)

                    session.login()
                    session.unfollow_users(amount= nonFollowers_amount, nonFollowers= True, unfollow_after= 0, sleep_delay= 600)
                    session.end()

    if (choice == 3):
        class emailphone:
            user_username = globaluser.user_username
            user_password = globaluser.user_password
            target_username = input('[InstaOsint] Coloque o nome do usuario que você deseja pegar email/telefone:')
        

            if not os.path.exists("cookie.json"):
                class getcookie:
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
                        print(r.status_code)
                        print(r.url)
                        print(r.text)

                        print(s.cookies)
                        print(r.headers)


        

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
        response = requests.get('https://www.instagram.com/' + emailphone.target_username + '/?__a=1', cookies=data1)
        with open("response.json", "w") as f:
            f.write(response.text)
        f = open('response.json')
        data = json.load(f)
        id = data["graphql"]["user"]["id"]
        url = "https://i.instagram.com/api/v1/users/" + id + "/info/"
        print(url)
        response2 = requests.get(url, cookies=data1, headers={"x-ig-app-id": "936619743392459"})
        print(response2.status_code)
        print(response2.headers)
        with open("response2.json", "w") as f:
            f.write(response2.text)
        f2 = open('response2.json')
        data2 = json.load(f2)
        phone = data2["user"]["contact_phone_number"]
        if (phone == None):
            print("[InstaOsint] Não foi possivel pegar o número de telefone")
        email = data2["user"]["public_email"]
        if (email == None):
            print("[InstaOsint] Não foi possivel pegar o email")
        clear()
        print(phone)
        print(email)

        with open("resultado.txt", "a") as f:
            f.write(emailphone.target_username + " - " + phone + " - " + email + "\n")
            
        print("arquivo salvo com o nome ""resultado.txt""")

    if (choice == 4):
        class bemailpassword:
            user_username = globaluser.user_username
            user_password = globaluser.user_password
            target_username = input('[InstaOsint] Coloque o nome do usuario que você deseja pegar email/telefone dos seguidores:')

        if not os.path.exists("cookie.json"):
            class getcookie:
                link = 'https://www.instagram.com/accounts/login/'
                login_url = 'https://www.instagram.com/accounts/login/ajax/'
                time = int(datetime.now().timestamp())
                payload = {'username': bemailpassword.user_username,'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:' + bemailpassword.user_password,'queryParams': {},'optIntoOneTap': 'false'}
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
                    print(r.status_code)
                    print(r.url)
                    print(r.text)
                    print(s.cookies)
            
        
        cookie = json.load(open('cookie.json'))
        response = requests.get('https://www.instagram.com/' + bemailpassword.target_username + '/?__a=1', cookies=cookie, headers={"x-ig-app-id": "936619743392459"})
        with open("response.json", "w") as f:
            f.write(response.text)
        f = open('response.json')
        data = json.load(f)
        id = data["graphql"]["user"]["id"]
        
        
        response = requests.get('https://i.instagram.com/api/v1/friendships/'+ id + '/followers/', cookies=cookie, headers={"x-ig-app-id": "936619743392459"})
        print(response.url)
        with open("responsefollower.json", "w") as f:
                    f.write(response.text)
        rf = open('responsefollower.json')
        data = json.load(rf)
        for i in data['users']:
            print(i['pk'])
        with open("fwersid.txt", "w")as iddata:
            iddata.write(str(i['pk']))

        f1 = open('cookie.json')
        iddata = json.load('fwersid.txt')
        data1 = json.load(f1)
        response = requests.get('https://www.instagram.com/' + iddata['pk'] + '/?__a=1', cookies=cookie)
        with open("response.json", "w") as f:
            f.write(response.text)
        f = open('response.json')
        data = json.load(f)
        id = data["graphql"]["user"]["id"]
        url = "https://i.instagram.com/api/v1/users/" + iddata['pk'] + "/info/"
        print(url)
        response2 = requests.get(url, cookies=cookie, headers={"x-ig-app-id": "936619743392459"})
        print(response2.status_code)
        print(response2.headers)
        with open("response2.json", "w") as f:
            f.write(response2.text)
        f2 = open('response2.json')
        data2 = json.load(f2)
        phone = data2["user"]["contact_phone_number"]
        if (phone == None):
            print("[InstaOsint] Não foi possivel pegar o número de telefone")
        email = data2["user"]["public_email"]
        if (email == None):
            print("[InstaOsint] Não foi possivel pegar o email")
        clear()
        print(phone)
        print(email)

        with open("resultado.txt", "a") as f:
            f.write(bemailpassword.target_username + " - " + phone + " - " + email + "\n")
            
        print("arquivo salvo com o nome ""resultado.txt""")

    if (choice == 99):
        print('Saindo...')
        print('Developed by M1gu3l0001')
        os.remove('cookie.json')
        os.remove('response.json')
        os.remove('response2.json')
        exit()
    else:
        print('Opção Inválida')

#line 500 bruh