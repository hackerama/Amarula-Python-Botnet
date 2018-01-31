# Amarula IRC Botnet v1.0
<h4> Abacatch Version </h4>

Keylloger feito em **Python 2.7** *(written in Python 2.7)* <br>
Testado em: **Windows 10** *(tested on)*<br>
Escrito por: **Carlos Néri Correia** *(coded by)* <br>
Versão: **1.0** *(version)*

## Funções *(features)*
- Captura de teclas digitadas pelo cliente em tempo real *(real-time keylogging)* <br>
- Armazenamento local de logs *(local storage)* <br> 
- Envio de logs para servidor remoto *(send logs to remote server)*<br>
- Persistência *(persistence)*<br>

## Instalação *(install)*
    $ pip install requests
    $ pip install pypiwin32

**Download pyHook**
https://sourceforge.net/projects/pyhook/

## Configuração *(setup)*
**VARIÁVEIS:** *(variables)* <br>

***ldir*** *(sets local directory, dropping directory)*<br>
Diretório local, onde será salvo o arquivo de log. <br>
Diretório para o qual o .exe se copia para ser executado em persistência quando a máquina reiniciar. 

***urlUpload*** *(Upload page on remote server)*<br>
Página de upload no servidor remoto, para a função de envio remoto. <br>
Será criado um arquivo *capt-(nome do PC).txt* na mesma pasta de upload.php, no servidor.  

**COMPILAR** *(compile)*

    $ pyinstaller -w WinService.py --onefile
    

mail me: hackerama@protonmail.com

