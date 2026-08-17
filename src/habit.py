import sqlite3
from database import get_connection  # <-- COM O PONTO!
from datetime import datetime, timedelta

def adicionar_habito(nome: str) -> bool:
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO habitos (nome, criado_em) VALUES (?, ?)",
                (nome, datetime.now().isoformat())
            )
            conn.commit()
            return True
    except sqlite3.IntegrityError:
        return False

def registrar_habito(nome: str) -> bool:
    hoje = datetime.now().date().isoformat()
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM habitos WHERE nome = ?", (nome,))
        resultado = cursor.fetchone()
        if not resultado:
            return False
        habit_id = resultado[0]
        try:
            cursor.execute(
                "INSERT INTO registros (habit_id, data) VALUES (?, ?)",
                (habit_id, hoje)
            )
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

def calcular_streak(nome: str) -> int:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT data FROM registros r
            JOIN habitos h ON h.id = r.habit_id
            WHERE h.nome = ?
            ORDER BY data DESC
        """, (nome,))
        registros = cursor.fetchall()
        if not registros:
            return 0
        ultima_data = datetime.fromisoformat(registros[0][0]).date()
        hoje = datetime.now().date()
        if (hoje - ultima_data).days > 1:
            return 0
        streak = 0
        data_esperada = hoje
        for registro in registros:
            data_reg = datetime.fromisoformat(registro[0]).date()
            if data_reg == data_esperada:
                streak += 1
                data_esperada -= timedelta(days=1)
            else:
                break
        return streak

def listar_habitos() -> list:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT nome FROM habitos ORDER BY nome")
        habitos = cursor.fetchall()
    resultado = []
    for (nome,) in habitos:
        streak = calcular_streak(nome)
        resultado.append({"nome": nome, "streak": streak})
    return resultado