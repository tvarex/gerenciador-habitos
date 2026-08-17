@echo off
title Instalador - Gerenciador de Habitos
color 0A

echo ==================================================
echo   GERENCIADOR DE HABITOS - INSTALADOR
echo ==================================================
echo.

echo [1/5] Verificando Python...

REM Tenta encontrar Python de varias formas
set PYTHON_CMD=

REM Tenta comando 'py' (Python Launcher do Windows)
py --version >nul 2>&1
if not errorlevel 1 (
    set PYTHON_CMD=py
    echo [OK] Python encontrado! (via 'py')
    py --version
    goto :python_encontrado
)

REM Tenta comando 'python'
python --version >nul 2>&1
if not errorlevel 1 (
    set PYTHON_CMD=python
    echo [OK] Python encontrado! (via 'python')
    python --version
    goto :python_encontrado
)

REM Tenta comando 'python3'
python3 --version >nul 2>&1
if not errorlevel 1 (
    set PYTHON_CMD=python3
    echo [OK] Python encontrado! (via 'python3')
    python3 --version
    goto :python_encontrado
)

REM Se chegou aqui, Python nao foi encontrado
echo [ERRO] Python nao encontrado!
echo.
echo Por favor, instale o Python:
echo 1. Acesse: https://www.python.org/downloads/
echo 2. Baixe e instale o Python
echo 3. MARQUE a opcao "Add Python to PATH"
echo 4. Reinicie o computador
echo.
echo Pressione qualquer tecla para sair...
pause >nul
exit /b 1

:python_encontrado
echo.
echo [2/5] Verificando pip...
%PYTHON_CMD% -m pip --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Pip nao encontrado! Instalando...
    %PYTHON_CMD% -m ensurepip --upgrade
)
echo [OK] Pip disponivel!
echo.

echo [3/5] Instalando dependencias...
echo Isso pode levar alguns minutos...
echo.
%PYTHON_CMD% -m pip install -r requirements.txt
if errorlevel 1 (
    echo [ERRO] Falha ao instalar dependencias!
    echo Tente executar como Administrador.
    pause >nul
    exit /b 1
)
echo [OK] Dependencias instaladas!
echo.

echo [4/5] Criando atalhos...
echo.

REM Criar habitos.bat (usando py que sempre funciona no Windows)
echo Criando 'habitos.bat'...
(
echo @echo off
echo title Gerenciador de Habitos
echo color 0A
echo py src\cli.py %%*
) > habitos.bat

echo Criando 'testar.bat'...
(
echo @echo off
echo title Testes - Gerenciador de Habitos
echo color 0E
echo echo ==================================================
echo echo   EXECUTANDO TESTES
echo echo ==================================================
echo echo.
echo py -m pytest tests\ -v
echo echo.
echo echo ==================================================
echo echo.
echo echo Pressione qualquer tecla para sair...
echo pause ^>nul
) > testar.bat

echo Criando 'limpar.bat'...
(
echo @echo off
echo title Limpar Dados - Gerenciador de Habitos
echo color 0C
echo echo ==================================================
echo echo   LIMPANDO DADOS
echo echo ==================================================
echo echo.
echo echo [ATENCAO] Isso vai apagar TODOS os seus habitos!
echo echo.
echo set /p confirmacao="Digite 'SIM' para confirmar: "
echo if not "%%confirmacao%%"=="SIM" (
echo     echo Operacao cancelada.
echo     pause ^>nul
echo     exit /b
echo )
echo py -c "import sqlite3; conn = sqlite3.connect('data/habitos.db'); conn.execute('DELETE FROM registros'); conn.execute('DELETE FROM habitos'); conn.commit(); conn.close(); print('[OK] Dados removidos com sucesso!')"
echo echo.
echo pause ^>nul
) > limpar.bat

echo Criando 'atualizar.bat'...
(
echo @echo off
echo title Atualizar - Gerenciador de Habitos
echo color 0E
echo echo ==================================================
echo echo   ATUALIZANDO PROJETO
echo echo ==================================================
echo echo.
echo echo [1/2] Baixando atualizacoes do GitHub...
echo git pull
echo echo.
echo echo [2/2] Atualizando dependencias...
echo py -m pip install -r requirements.txt --upgrade
echo echo.
echo echo [OK] Atualizacao concluida!
echo echo.
echo pause ^>nul
) > atualizar.bat

echo [OK] Atalhos criados!
echo.

echo [5/5] Configuracao concluida!
echo.
echo ==================================================
echo   INSTALACAO CONCLUIDA COM SUCESSO!
echo ==================================================
echo.
echo Para usar o programa:
echo   1. Execute: habitos.bat
echo   2. Ou digite: py src\cli.py
echo.
echo Para rodar os testes:
echo   Execute: testar.bat
echo.
echo Para limpar os dados:
echo   Execute: limpar.bat
echo.
echo Para atualizar o projeto:
echo   Execute: atualizar.bat
echo.
echo ==================================================
echo.
pause