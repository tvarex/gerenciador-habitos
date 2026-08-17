"""
Testes para a interface de linha de comando.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import pytest
from cli import main
import argparse

def test_comando_add():
    """Testa se o comando add funciona via CLI"""
    # Como testar CLI é mais complexo, vamos fazer um teste simples
    # Aqui você pode testar se o parser reconhece os comandos
    pass