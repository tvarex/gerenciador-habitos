@echo off
title Testes - Gerenciador de Habitos
color 0E
echo ==================================================
echo   EXECUTANDO TESTES
echo ==================================================
echo.
py -m pytest tests\ -v
echo.
echo ==================================================
echo.
echo Pressione qualquer tecla para sair...
pause >nul
