"""
Relatorios e graficos para o Gerenciador de Habitos
"""
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from pathlib import Path
from database import get_connection


def gerar_grafico_mensal(nome: str, salvar_imagem: str = None):
    """
    Gera um grafico dos ultimos 30 dias para um habito.
    
    Args:
        nome: Nome do habito
        salvar_imagem: Caminho para salvar o grafico (opcional)
                      Se nao for especificado, mostra na tela
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        
        # Verifica se o habito existe
        cursor.execute("SELECT id FROM habitos WHERE nome = ?", (nome,))
        resultado = cursor.fetchone()
        if not resultado:
            print(f"[ERRO] Habito '{nome}' nao encontrado.")
            return
        
        habit_id = resultado[0]
        
        # Pega todos os registros dos ultimos 30 dias
        trinta_dias_atras = (datetime.now() - timedelta(days=30)).date().isoformat()
        cursor.execute("""
            SELECT data FROM registros
            WHERE habit_id = ? AND data >= ?
            ORDER BY data
        """, (habit_id, trinta_dias_atras))
        
        registros = {row[0] for row in cursor.fetchall()}  # Set para busca rapida
    
    # Cria a lista de dias dos ultimos 30 dias
    hoje = datetime.now().date()
    dias = [(hoje - timedelta(days=i)).strftime("%d/%m") for i in range(29, -1, -1)]
    datas_iso = [(hoje - timedelta(days=i)).isoformat() for i in range(29, -1, -1)]
    
    # Cria os valores (1 = fez, 0 = nao fez)
    valores = [1 if dia in registros else 0 for dia in datas_iso]
    
    # Cria o grafico
    fig, ax = plt.subplots(figsize=(14, 6))
    
    # Cores: verde para dias feitos, vermelho para nao feitos
    cores = ['#2ecc71' if v == 1 else '#e74c3c' for v in valores]
    
    # Barras
    barras = ax.bar(range(30), valores, color=cores, edgecolor='black', linewidth=0.5)
    
    # Personaliza o grafico
    ax.set_title(f'Ultimos 30 dias - {nome}', fontsize=16, fontweight='bold')
    ax.set_xlabel('Dias', fontsize=12)
    ax.set_ylabel('Fez o habito?', fontsize=12)
    
    # Configura os ticks do eixo X (mostra alguns dias para nao poluir)
    ax.set_xticks(range(0, 30, 5))
    ax.set_xticklabels([dias[i] for i in range(0, 30, 5)], rotation=45)
    
    # Configura os ticks do eixo Y (0 = Nao, 1 = Sim)
    ax.set_yticks([0, 1])
    ax.set_yticklabels(['Nao', 'Sim'])
    
    # Adiciona grade
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    # Adiciona uma linha horizontal no meio
    ax.axhline(y=0.5, color='gray', linestyle='-', alpha=0.2)
    
    # Adiciona o total de dias feitos
    total_feitos = sum(valores)
    percentual = (total_feitos / 30) * 100
    
    # Adiciona texto com estatisticas
    stats_text = f'Dias feitos: {total_feitos}/30 ({percentual:.1f}%)'
    ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, 
            fontsize=12, verticalalignment='top', 
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    # Ajusta o layout
    plt.tight_layout()
    
    # Salva ou mostra
    if salvar_imagem:
        # Garante que a pasta existe
        Path(salvar_imagem).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(salvar_imagem, dpi=150, bbox_inches='tight')
        print(f"[OK] Grafico salvo em: {salvar_imagem}")
        plt.close()
    else:
        plt.show()
    
    return fig


def gerar_grafico_semanal(nome: str, salvar_imagem: str = None):
    """
    Gera um grafico dos ultimos 7 dias para um habito.
    """
    with get_connection() as conn:
        cursor = conn.cursor()
        
        # Verifica se o habito existe
        cursor.execute("SELECT id FROM habitos WHERE nome = ?", (nome,))
        resultado = cursor.fetchone()
        if not resultado:
            print(f"[ERRO] Habito '{nome}' nao encontrado.")
            return
        
        habit_id = resultado[0]
        
        # Pega todos os registros dos ultimos 7 dias
        sete_dias_atras = (datetime.now() - timedelta(days=7)).date().isoformat()
        cursor.execute("""
            SELECT data FROM registros
            WHERE habit_id = ? AND data >= ?
            ORDER BY data
        """, (habit_id, sete_dias_atras))
        
        registros = {row[0] for row in cursor.fetchall()}
    
    # Cria a lista de dias dos ultimos 7 dias
    hoje = datetime.now().date()
    dias = [(hoje - timedelta(days=i)).strftime("%d/%m") for i in range(6, -1, -1)]
    datas_iso = [(hoje - timedelta(days=i)).isoformat() for i in range(6, -1, -1)]
    
    # Cria os valores
    valores = [1 if dia in registros else 0 for dia in datas_iso]
    
    # Cria o grafico
    fig, ax = plt.subplots(figsize=(10, 5))
    
    cores = ['#2ecc71' if v == 1 else '#e74c3c' for v in valores]
    barras = ax.bar(range(7), valores, color=cores, edgecolor='black', linewidth=0.5)
    
    ax.set_title(f'Ultimos 7 dias - {nome}', fontsize=16, fontweight='bold')
    ax.set_xlabel('Dias', fontsize=12)
    ax.set_ylabel('Fez o habito?', fontsize=12)
    
    ax.set_xticks(range(7))
    ax.set_xticklabels(dias, rotation=45)
    
    ax.set_yticks([0, 1])
    ax.set_yticklabels(['Nao', 'Sim'])
    
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.axhline(y=0.5, color='gray', linestyle='-', alpha=0.2)
    
    total_feitos = sum(valores)
    stats_text = f'Dias feitos: {total_feitos}/7'
    ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, 
            fontsize=12, verticalalignment='top', 
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    
    if salvar_imagem:
        Path(salvar_imagem).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(salvar_imagem, dpi=150, bbox_inches='tight')
        print(f"[OK] Grafico salvo em: {salvar_imagem}")
        plt.close()
    else:
        plt.show()
    
    return fig


def gerar_relatorio_completo(salvar_imagem: str = None):
    """
    Gera um relatorio completo com todos os habitos.
    """
    from habit import listar_habitos
    
    habitos = listar_habitos()
    
    if not habitos:
        print("[ERRO] Nenhum habito cadastrado.")
        return
    
    # Cria um grafico de barras mostrando todos os streaks
    fig, ax = plt.subplots(figsize=(12, 6))
    
    nomes = [hab['nome'][:20] for hab in habitos]
    streaks = [hab['streak'] for hab in habitos]
    
    # Ordena por streak (do maior para o menor)
    pares = sorted(zip(streaks, nomes), reverse=True)
    streaks, nomes = zip(*pares) if pares else ([], [])
    
    # Cores variadas
    cores = plt.cm.viridis([i/len(streaks) for i in range(len(streaks))])
    
    barras = ax.bar(range(len(nomes)), streaks, color=cores, edgecolor='black', linewidth=0.5)
    
    ax.set_title('Streak de Todos os Habitos', fontsize=16, fontweight='bold')
    ax.set_xlabel('Habitos', fontsize=12)
    ax.set_ylabel('Streak (dias consecutivos)', fontsize=12)
    
    ax.set_xticks(range(len(nomes)))
    ax.set_xticklabels(nomes, rotation=45, ha='right')
    
    # Adiciona valores acima das barras
    for i, (barra, streak) in enumerate(zip(barras, streaks)):
        if streak > 0:
            ax.text(barra.get_x() + barra.get_width()/2, barra.get_height() + 0.5,
                    str(streak), ha='center', va='bottom', fontsize=10, fontweight='bold')
        else:
            ax.text(barra.get_x() + barra.get_width()/2, barra.get_height() + 0.5,
                    'nunca', ha='center', va='bottom', fontsize=9, color='gray')
    
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_ylim(0, max(streaks) * 1.2 if streaks else 1)
    
    plt.tight_layout()
    
    if salvar_imagem:
        Path(salvar_imagem).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(salvar_imagem, dpi=150, bbox_inches='tight')
        print(f"[OK] Relatorio salvo em: {salvar_imagem}")
        plt.close()
    else:
        plt.show()
    
    return fig