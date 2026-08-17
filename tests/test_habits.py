"""
Testes para o gerenciador de hábitos.
"""
import sys
from pathlib import Path

# Adiciona a pasta src ao PATH do Python
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import pytest
from database import init_db, get_connection
from habit import adicionar_habito, registrar_habito, calcular_streak, listar_habitos


@pytest.fixture
def limpar_banco():
    """Limpa o banco antes e depois de cada teste"""
    init_db()
    with get_connection() as conn:
        conn.execute("DELETE FROM registros")
        conn.execute("DELETE FROM habitos")
        conn.commit()
    
    yield  # O teste roda aqui
    
    with get_connection() as conn:
        conn.execute("DELETE FROM registros")
        conn.execute("DELETE FROM habitos")
        conn.commit()


def test_adicionar_habito(limpar_banco):
    """Testa adicionar hábitos"""
    assert adicionar_habito("Estudar") == True
    assert adicionar_habito("Estudar") == False  # Já existe


def test_registrar_habito(limpar_banco):
    """Testa registrar um hábito"""
    adicionar_habito("Exercitar")
    assert registrar_habito("Exercitar") == True
    assert registrar_habito("Exercitar") == False  # Já registrou hoje
    assert registrar_habito("Inexistente") == False  # Hábito não existe


def test_calcular_streak(limpar_banco):
    """Testa o cálculo do streak"""
    adicionar_habito("Ler")
    assert calcular_streak("Ler") == 0  # Sem registros
    
    registrar_habito("Ler")
    assert calcular_streak("Ler") == 1  # Um dia


def test_listar_habitos(limpar_banco):
    """Testa a listagem de hábitos"""
    adicionar_habito("A")
    adicionar_habito("B")
    adicionar_habito("C")
    
    lista = listar_habitos()
    assert len(lista) == 3
    nomes = [h["nome"] for h in lista]
    assert "A" in nomes
    assert "B" in nomes
    assert "C" in nomes