@echo off
title Limpar Dados - Gerenciador de Habitos
color 0C

echo ==================================================
echo   LIMPANDO DADOS
echo ==================================================
echo.
echo [ATENCAO] Isso vai apagar TODOS os seus habitos!
echo.

set /p confirmacao="Digite 'SIM' para confirmar: "

if not "%confirmacao%"=="SIM" (
    echo Operacao cancelada.
    pause >nul
    exit /b
)

python -c "import sqlite3; conn = sqlite3.connect('data/habitos.db'); conn.execute('DELETE FROM registros'); conn.execute('DELETE FROM habitos'); conn.commit(); conn.close(); print('[OK] Dados removidos com sucesso!')"

echo.
echo Pressione qualquer tecla para sair...
pause >nul