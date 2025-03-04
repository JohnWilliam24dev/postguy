@echo off
setlocal

:: Define o diretório onde o executável será instalado
set "INSTALL_DIR=%USERPROFILE%\AppData\Local\Programs\postguy"

:: Cria o diretório, se não existir
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

:: Copia o executável para o diretório
copy /Y "%~dp0postguy.exe" "%INSTALL_DIR%\"

:: Adiciona o diretório ao PATH do usuário, se ainda não estiver lá
setx PATH "%PATH%;%INSTALL_DIR%" /M

echo Postguy instalado com sucesso! Agora você pode usar o comando 'postguy' de qualquer lugar.
pause