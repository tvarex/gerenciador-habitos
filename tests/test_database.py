"""
Testes específicos para o banco de dados.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import pytest
from database import init_db, get_connection
import sqlite3

def test_init_db_cria_tabelas():
    """Testa se o banco cria as tabelas corretamente"""
    init_db()
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tabelas = [row[0] for row in cursor.fetchall()]
        assert "habitos" in tabelas
        assert "registros" in tabelas

def test_db_path_correto():
    """Testa se o caminho do banco está correto"""
    from database import DB_PATH
    assert DB_PATH.name == "habitos.db"
    assert DB_PATH.parent.name == "data"