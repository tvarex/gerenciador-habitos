@echo off
title Atualizar - Gerenciador de Habitos
color 0E
echo ==================================================
echo   ATUALIZANDO PROJETO
echo ==================================================
echo.
echo [1/2] Baixando atualizacoes do GitHub...
git pull
echo.
echo [2/2] Atualizando dependencias...
py -m pip install -r requirements.txt --upgrade
echo.
echo [OK] Atualizacao concluida!
echo.
pause >nul
