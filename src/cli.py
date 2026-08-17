"""
Interface de Linha de Comando para o Gerenciador de Habitos

"""
import sys
import os
from pathlib import Path
from report import gerar_grafico_mensal, gerar_grafico_semanal, gerar_relatorio_completo

# Adiciona a pasta src ao path para importar os modulos
sys.path.insert(0, str(Path(__file__).parent))

from database import init_db
from habit import adicionar_habito, registrar_habito, calcular_streak, listar_habitos


def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_banner():
    """Mostra o banner do programa"""
    print("=" * 50)
    print("  GERENCIADOR DE HABITOS v1.0")
    print("=" * 50)

def comando_graph(nome: str):
    """Gera um grafico dos ultimos 30 dias de um habito"""
    salvar = input("[INFO] Salvar grafico como imagem? (s/N): ")
    
    if salvar.lower() == 's':
        nome_arquivo = f"grafico_{nome.replace(' ', '_')}.png"
        gerar_grafico_mensal(nome, nome_arquivo)
    else:
        print("[INFO] Abrindo grafico na tela...")
        print("[INFO] Feche a janela do grafico para continuar.")
        gerar_grafico_mensal(nome)


def comando_graph_semanal(nome: str):
    """Gera um grafico dos ultimos 7 dias de um habito"""
    salvar = input("[INFO] Salvar grafico como imagem? (s/N): ")
    
    if salvar.lower() == 's':
        nome_arquivo = f"grafico_semanal_{nome.replace(' ', '_')}.png"
        gerar_grafico_semanal(nome, nome_arquivo)
    else:
        print("[INFO] Abrindo grafico na tela...")
        print("[INFO] Feche a janela do grafico para continuar.")
        gerar_grafico_semanal(nome)


def comando_relatorio():
    """Gera um relatorio com todos os habitos"""
    salvar = input("[INFO] Salvar relatorio como imagem? (s/N): ")
    
    if salvar.lower() == 's':
        gerar_relatorio_completo("relatorio_habitos.png")
    else:
        print("[INFO] Abrindo relatorio na tela...")
        print("[INFO] Feche a janela do grafico para continuar.")
        gerar_relatorio_completo()
        
def mostrar_ajuda():
    """Mostra os comandos disponiveis"""
    print("""
COMANDOS DISPONIVEIS:

  add "NOME"        Adiciona um novo habito
  check "NOME"      Registra que voce fez o habito HOJE
  list              Lista todos os habitos com streaks
  streak "NOME"     Mostra o streak atual de um habito
  graph "NOME"      Mostra grafico dos ultimos 30 dias
  graphsem "NOME"   Mostra grafico dos ultimos 7 dias
  relatorio         Mostra grafico com todos os habitos
  delete "NOME"     Remove um habito (e todos os registros)
  reset             Remove TODOS os habitos e registros (cuidado!)
  help              Mostra esta mensagem de ajuda
  exit              Sai do programa

EXEMPLOS:
  add Estudar Python
  check Estudar Python
  list
  streak Estudar Python
  graph Estudar Python
  graphsem Estudar Python
  relatorio
  delete Estudar Python
  reset
  help
  exit
""")


def comando_add(nome: str):
    """Adiciona um novo habito"""
    if adicionar_habito(nome):
        print(f"[OK] Habito '{nome}' adicionado com sucesso!")
    else:
        print(f"[ERRO] Habito '{nome}' ja existe.")


def comando_check(nome: str):
    """Registra um habito feito hoje"""
    if registrar_habito(nome):
        streak = calcular_streak(nome)
        print(f"[OK] Habito '{nome}' registrado hoje!")
        print(f"[INFO] Streak atual: {streak} dia(s) seguido(s)!")
        
        # Mostra mensagem motivacional (sem emojis)
        if streak >= 100:
            print("[FANTÁSTICO] Voce esta ha 100 dias consistente!")
        elif streak >= 30:
            print("[EXCELENTE] Voce esta ha 1 mes consistente!")
        elif streak >= 7:
            print("[PARABENS] Voce esta ha 1 semana consistente!")
    else:
        print(f"[ERRO] Falha ao registrar. Habito nao existe ou ja foi registrado hoje.")


def comando_list():
    """Lista todos os habitos com seus streaks"""
    habitos = listar_habitos()
    
    if not habitos:
        print("[INFO] Nenhum habito cadastrado.")
        print("       Use 'add NOME' para adicionar um habito.")
        return
    
    # Ordena por streak (maior primeiro)
    habitos.sort(key=lambda x: x["streak"], reverse=True)
    
    print("\n" + "-" * 60)
    print(f"{'STATUS':<10} {'HABITO':<35} {'STREAK':<15}")
    print("-" * 60)
    
    for hab in habitos:
        # Escolhe o simbolo baseado no streak
        if hab["streak"] >= 30:
            simbolo = "[*]"
        elif hab["streak"] >= 7:
            simbolo = "[+]"
        elif hab["streak"] >= 3:
            simbolo = "[!]"
        elif hab["streak"] > 0:
            simbolo = "[v]"
        else:
            simbolo = "[ ]"
        
        # Formata o streak
        if hab["streak"] > 0:
            streak_texto = f"{hab['streak']} dia(s)"
        else:
            streak_texto = "nunca"
        
        print(f"{simbolo:<10} {hab['nome'][:34]:<35} {streak_texto:<15}")
    
    print("-" * 60)
    
    # Estatisticas
    total_habitos = len(habitos)
    total_streaks = sum(hab["streak"] for hab in habitos)
    media_streak = total_streaks / total_habitos if total_habitos > 0 else 0
    
    print(f"\nESTATISTICAS:")
    print(f"  Total de habitos: {total_habitos}")
    print(f"  Total de streaks: {total_streaks}")
    print(f"  Media de streak: {media_streak:.1f} dia(s)")
    
    if habitos:
        print(f"  Habito mais forte: {habitos[0]['nome']} ({habitos[0]['streak']} dia(s))")


def comando_streak(nome: str):
    """Mostra o streak de um habito especifico"""
    streak = calcular_streak(nome)
    
    if streak > 0:
        # Mensagem personalizada (sem emojis)
        if streak == 1:
            msg = "Voce comecou hoje! Continue assim!"
        elif streak < 7:
            msg = f"Bom comeco! Sao {streak} dia(s) seguido(s)!"
        elif streak < 30:
            msg = f"Otimo! Voce esta ha {streak} dia(s) seguido(s)!"
        elif streak < 100:
            msg = f"INCRIVEL! {streak} dia(s) seguido(s)! Voce e uma maquina!"
        else:
            msg = f"FANTASTICO! {streak} dia(s) seguido(s)! Voce e um exemplo!"
        
        print(f"[INFO] Streak de '{nome}': {streak} dia(s) seguido(s)!")
        print(f"       {msg}")
    else:
        print(f"[INFO] '{nome}' nao tem streak ativo.")
        print(f"       Registre hoje com: check {nome}")


def comando_delete(nome: str):
    """Remove um habito e todos os seus registros"""
    confirmacao = input(f"[ATENCAO] Tem certeza que quer deletar '{nome}'? (s/N): ")
    
    if confirmacao.lower() != 's':
        print("[OK] Operacao cancelada.")
        return
    
    from database import get_connection
    
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM habitos WHERE nome = ?", (nome,))
        if cursor.rowcount > 0:
            conn.commit()
            print(f"[OK] Habito '{nome}' removido com sucesso!")
        else:
            print(f"[ERRO] Habito '{nome}' nao encontrado.")


def comando_reset():
    """Remove TODOS os habitos e registros"""
    confirmacao = input("[ATENCAO] TEM CERTEZA? Isso vai apagar TODOS os seus habitos! (digite 'SIM' para confirmar): ")
    
    if confirmacao != "SIM":
        print("[OK] Operacao cancelada.")
        return
    
    from database import get_connection
    
    with get_connection() as conn:
        conn.execute("DELETE FROM registros")
        conn.execute("DELETE FROM habitos")
        conn.commit()
    
    print("[OK] Todos os habitos foram removidos com sucesso!")


def modo_interativo():
    """Modo interativo - usuario digita comandos um por um"""
    limpar_tela()
    mostrar_banner()
    print("\n[INFO] Digite 'help' para ver os comandos disponiveis")
    print("       Digite 'exit' para sair\n")
    
    while True:
        try:
            # Le o comando do usuario
            comando_input = input("> ").strip()
            
            if not comando_input:
                continue
            
            # Divide o comando
            partes = comando_input.split(' ', 1)
            comando = partes[0].lower()
            
            # Pega o argumento (se houver)
            argumento = partes[1] if len(partes) > 1 else ""
            
            # Processa o comando
            if comando == "exit":
                print("[OK] Saindo...")
                break
            
            elif comando == "help":
                mostrar_ajuda()

            elif comando == "graph":
                if not argumento:
                    print("[ERRO] Use: graph 'NOME DO HABITO'")
                else:
                    comando_graph(argumento)

            elif comando == "graphsem":
                if not argumento:
                    print("[ERRO] Use: graphsem 'NOME DO HABITO'")
                else:
                    comando_graph_semanal(argumento)

            elif comando == "relatorio":
                comando_relatorio()
                        
            elif comando == "add":
                if not argumento:
                    print("[ERRO] Use: add 'NOME DO HABITO'")
                else:
                    comando_add(argumento)
            
            elif comando == "check":
                if not argumento:
                    print("[ERRO] Use: check 'NOME DO HABITO'")
                else:
                    comando_check(argumento)
            
            elif comando == "list":
                comando_list()
            
            elif comando == "streak":
                if not argumento:
                    print("[ERRO] Use: streak 'NOME DO HABITO'")
                else:
                    comando_streak(argumento)
            
            elif comando == "delete":
                if not argumento:
                    print("[ERRO] Use: delete 'NOME DO HABITO'")
                else:
                    comando_delete(argumento)
            
            elif comando == "reset":
                comando_reset()
            
            else:
                print(f"[ERRO] Comando '{comando}' nao reconhecido.")
                print("       Digite 'help' para ver os comandos disponiveis.")
            
            print()  # Linha em branco para organizar
        
        except KeyboardInterrupt:
            print("\n[OK] Saindo...")
            break
        except Exception as e:
            print(f"[ERRO] Ocorreu um erro: {e}")


def modo_direto():
    """Modo direto - executa um unico comando passado como argumento"""
    if len(sys.argv) < 2:
        mostrar_ajuda()
        return
    
    comando = sys.argv[1].lower()
    
    # Inicializa o banco
    init_db()
    
    if comando == "add":
        if len(sys.argv) < 3:
            print("[ERRO] Use: py src/cli.py add 'NOME DO HABITO'")
            return
        nome = " ".join(sys.argv[2:])
        comando_add(nome)
    
    elif comando == "check":
        if len(sys.argv) < 3:
            print("[ERRO] Use: py src/cli.py check 'NOME DO HABITO'")
            return
        nome = " ".join(sys.argv[2:])
        comando_check(nome)
    elif comando == "graph":
        if len(sys.argv) < 3:
            print("[ERRO] Use: py src/cli.py graph 'NOME DO HABITO'")
            return
        nome = " ".join(sys.argv[2:])
        comando_graph(nome)

    elif comando == "graphsem":
        if len(sys.argv) < 3:
            print("[ERRO] Use: py src/cli.py graphsem 'NOME DO HABITO'")
            return
        nome = " ".join(sys.argv[2:])
        comando_graph_semanal(nome)

    elif comando == "relatorio":
        comando_relatorio()
        
    elif comando == "list":
        comando_list()
    
    elif comando == "streak":
        if len(sys.argv) < 3:
            print("[ERRO] Use: py src/cli.py streak 'NOME DO HABITO'")
            return
        nome = " ".join(sys.argv[2:])
        comando_streak(nome)
    
    elif comando == "delete":
        if len(sys.argv) < 3:
            print("[ERRO] Use: py src/cli.py delete 'NOME DO HABITO'")
            return
        nome = " ".join(sys.argv[2:])
        comando_delete(nome)
    
    elif comando == "reset":
        comando_reset()
    
    elif comando in ["help", "--help", "-h"]:
        mostrar_ajuda()
    
    else:
        print(f"[ERRO] Comando '{comando}' nao reconhecido.")
        mostrar_ajuda()


if __name__ == "__main__":
    # Se tiver argumentos, executa modo direto
    if len(sys.argv) > 1:
        modo_direto()
    else:
        # Senao, entra no modo interativo
        modo_interativo()