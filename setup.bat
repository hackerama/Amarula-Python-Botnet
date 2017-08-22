@echo off
mkdir %AppData%\Amarula
echo Copiando arquivos para diretorio de execução.
copy amarula.exe %AppData%\Amarula
cd %AppData%\Amarula\
echo Iniciando arquivo:
start %AppData%\Amarula\amarula.exe
REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "My App" /t REG_SZ /F /D "%AppData%\Amarula\Amarula.exe"
exit