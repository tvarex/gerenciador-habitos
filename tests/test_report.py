"""
Testes para os relatórios e gráficos.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import pytest
from report import gerar_grafico_mensal
from database import init_db
from habit import adicionar_habito, registrar_habito
import os

def test_gerar_grafico(limpar_banco):
    """Testa se o gráfico é gerado sem erros"""
    adicionar_habito("Teste")
    registrar_habito("Teste")
    
    # Gera o gráfico
    gerar_grafico_mensal("Teste", "teste_grafico.png")
    
    # Verifica se o arquivo foi criado
    assert os.path.exists("teste_grafico.png")
    
    # Limpa o arquivo depois
    os.remove("teste_grafico.png")