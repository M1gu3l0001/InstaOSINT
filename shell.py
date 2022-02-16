def goto(linenum):
    global line
    line = linenum
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
from getpass import getpass
from datetime import datetime

class globaluser:
    user_username = input("[InstaOSINT] Insira o seu nome de usuário: ")
    if (user_username == ''):
        print("O nome de usuário não pode ser vazio")
        exit()  
    user_password = getpass('[InstaOSINT] Insira a sua senha: ')

for i in range(0,10):

    print('1. SEGUIR OS FOLLOWERS DE UM TARGET\n')

    print('2. DEIXAR DE SEGUIR TODOS AS PESSOAS QUE EU SIGO QUE NÃO ME SEGUEM DE VOLTA\n')

    print('3. Pegar o email e nº de telefone de um usuário\n')

    print('4. Pegar o email e nº de telefone dos seguidores de um usuário\n')

    print('99. Sair do Programa\n')


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
        twofacode = input('[InstaOsint] Coloque o código de 2 fatores (se tiver):')
        users_amount = input('Digite quantos seguidores de -> ' + target + ' <- você quer seguir:')


        session = InstaPy(username= user_username, password = user_password, twofacode = twofacode, headless_browser= False)

        session.login()
        session.follow_user_followers(usernames= target, amount= 17, sleep_delay= 600)
        session.end()
    
    if (choice == 2):
            user_username = globaluser.user_username
            if (user_username == ''):
                print('[InstaOsint] O nome de usuário nao pode ser vazio')
                continue
            user_password = globaluser.user_password
            twofacode = input('[InstaOsint] Coloque o código de 2 fatores (se tiver):')
            nonFollowers_amount = input('[InstaOsint] Coloque a quantidade de pessoas que você segue mas não seguem de volta que deseja deixar de seguir:')
            
            session = InstaPy(username= user_username, password = user_password, twofacode = twofacode, headless_browser= False)
    
            session.login()
            session.unfollow_users(amount= nonFollowers_amount, nonFollowers= True, unfollow_after= 0, sleep_delay= 600)
            session.end()

    if (choice == 3):
        class emailpassword:
            user_username = globaluser.user_username
            user_password = globaluser.user_password
            target_username = input('[InstaOsint] Coloque o nome do usuario que você deseja pegar email/telefone:')
        

            if not os.path.exists("cookie.json"):
                class getcookie:
                    link = 'https://www.instagram.com/accounts/login/'
                    login_url = 'https://www.instagram.com/accounts/login/ajax/'

                    time = int(datetime.now().timestamp())

                    payload = {'username': user_username,'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:' + user_password,'queryParams': {},'optIntoOneTap': 'false'}
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
        response = requests.get('https://www.instagram.com/' + emailpassword.target_username + '/?__a=1', cookies=data1)
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
            f.write(emailpassword.target_username + " - " + phone + " - " + email + "\n")
            
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
    class bruh:
        for i in data['users']:
            print(i['pk'])
        with open("fwersid.txt", "w")as f:
            f.write(str(i['pk']))

            # In construction








    if (choice == 99):
        print('Saindo...')
        print('Developed by M1gu3l0001')
        os.remove('cookie.json')
        os.remove('response.json')
        os.remove('response2.json')
        exit()
    else:
        print('Opção Inválida')
