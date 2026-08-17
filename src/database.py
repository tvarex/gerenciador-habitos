import sqlite3
from pathlib import Path

# Pega a RAIZ do projeto (sobe um nível de src/)
ROOT_DIR = Path(__file__).parent.parent
DB_PATH = ROOT_DIR / "data" / "habitos.db"

def get_connection():
    """Cria a conexão com o banco"""
    DB_PATH.parent.mkdir(exist_ok=True)
    return sqlite3.connect(DB_PATH)

def init_db():
    """Cria as tabelas se não existirem"""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS habitos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT UNIQUE NOT NULL,
                criado_em TEXT NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS registros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                habit_id INTEGER NOT NULL,
                data TEXT NOT NULL,
                FOREIGN KEY (habit_id) REFERENCES habitos (id) ON DELETE CASCADE,
                UNIQUE(habit_id, data)
            )
        """)
        conn.commit()