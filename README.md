# Gerenciador de Hábitos

Sistema completo para monitorar seus hábitos diários com streaks, gráficos e estatísticas.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Tests](https://img.shields.io/badge/tests-10%2F10-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)
![Windows](https://img.shields.io/badge/platform-Windows-blue)

## Sobre o Projeto

O **Gerenciador de Hábitos** é uma ferramenta de linha de comando (CLI) que ajuda você a:
- Criar e gerenciar hábitos diários
- Calcular streaks (sequência de dias consecutivos)
- Visualizar progresso com gráficos
- Acompanhar estatísticas detalhadas

## Funcionalidades

| Funcionalidade | Descrição |
|----------------|-----------|
| Adicionar | Crie novos hábitos facilmente |
| Registrar | Marque hábitos concluídos hoje |
| Streak | Acompanhe dias consecutivos |
| Listar | Visualize todos os hábitos com estatísticas |
| Gráficos | Veja seu progresso visualmente |
| Relatório | Análise completa de todos os hábitos |
| Deletar | Remova hábitos não desejados |
| Reset | Limpe todos os dados com segurança |

## Instalação

### Windows (Recomendado)

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/gerenciador-habitos.git
cd gerenciador-habitos

    Execute o instalador:

bash

setup.bat

    Pronto! Use o programa:

bash

habitos.bat

Linux / Mac

    Clone o repositório:

bash

git clone https://github.com/seu-usuario/gerenciador-habitos.git
cd gerenciador-habitos

    Instale as dependências:

bash

pip3 install -r requirements.txt

    Execute:

bash

python3 src/cli.py

Como Usar
Modo Interativo (Recomendado)
bash

habitos.bat

Digite os comandos interativamente:
text

> help        # Mostra todos os comandos
> add "Nome"  # Adiciona um hábito
> check "Nome" # Registra hábito hoje
> list        # Lista todos os hábitos
> graph "Nome" # Gera gráfico de 30 dias
> exit        # Sai do programa

Modo Direto
bash

# Adicionar hábito
habitos.bat add "Estudar Python"

# Registrar hoje
habitos.bat check "Estudar Python"

# Ver lista
habitos.bat list

# Ver streak específico
habitos.bat streak "Estudar Python"

# Gerar gráfico
habitos.bat graph "Estudar Python"

# Ver relatório completo
habitos.bat relatorio

Comandos Disponíveis
Comando	Descrição	Exemplo
add "NOME"	Adiciona novo hábito	add "Estudar"
check "NOME"	Registra hábito hoje	check "Estudar"
list	Lista todos os hábitos	list
streak "NOME"	Mostra streak do hábito	streak "Estudar"
graph "NOME"	Gráfico de 30 dias	graph "Estudar"
graphsem "NOME"	Gráfico de 7 dias	graphsem "Estudar"
relatorio	Relatório completo	relatorio
delete "NOME"	Remove um hábito	delete "Estudar"
reset	Remove todos os hábitos	reset
help	Mostra ajuda	help
exit	Sai do programa	exit
Exemplo de Uso
text

==================================================
  GERENCIADOR DE HABITOS v1.0
==================================================

> add Estudar Python
[OK] Habito 'Estudar Python' adicionado com sucesso!

> check Estudar Python
[OK] Habito 'Estudar Python' registrado hoje!
[INFO] Streak atual: 1 dia(s) seguido(s)!

> list
------------------------------------------------------------
STATUS     HABITO                               STREAK
------------------------------------------------------------
[v]        Estudar Python                       1 dia(s)
[ ]        Fazer Exercicios                     nunca
[ ]        Ler Livros                           nunca
------------------------------------------------------------

ESTATISTICAS:
  Total de habitos: 3
  Total de streaks: 1
  Media de streak: 0.3 dia(s)
  Habito mais forte: Estudar Python (1 dia(s))

Testes

O projeto inclui 10 testes automatizados.
Rodar os testes:
bash

testar.bat

Saída esperada:
text

============================= test session starts =============================
collected 10 items

tests/test_sistema_completo.py::test_01_criar_habitos PASSED
tests/test_sistema_completo.py::test_02_registrar_habitos PASSED
tests/test_sistema_completo.py::test_03_calcular_streak PASSED
tests/test_sistema_completo.py::test_04_listar_habitos_com_streak PASSED
tests/test_sistema_completo.py::test_05_fluxo_completo_usuario PASSED
tests/test_sistema_completo.py::test_06_resistencia_erros PASSED
tests/test_sistema_completo.py::test_07_desempenho_muitos_habitos PASSED
tests/test_sistema_completo.py::test_08_dados_persistem PASSED
tests/test_sistema_completo.py::test_09_habitos_independentes PASSED
tests/test_sistema_completo.py::test_10_relatorio_final PASSED

============================= 10 passed in 0.85s =============================

Estrutura do Projeto
text

gerenciador_habitos/
├── src/                    # Código fonte
│   ├── __init__.py
│   ├── database.py         # Banco de dados SQLite
│   ├── habit.py            # Lógica dos hábitos
│   ├── report.py           # Gráficos e relatórios
│   └── cli.py              # Interface de linha de comando
├── tests/                  # Testes automatizados
│   ├── __init__.py
│   ├── test_habits.py
│   └── test_sistema_completo.py
├── data/                   # Banco de dados
│   └── habitos.db
├── requirements.txt        # Dependências
├── setup.bat              # Instalador Windows
├── habitos.bat            # Atalho principal
├── testar.bat             # Atalho para testes
├── limpar.bat             # Limpar dados
├── atualizar.bat          # Atualizar projeto
└── README.md              # Documentação

Tecnologias Utilizadas

    Python 3.8+ - Linguagem principal

    SQLite - Banco de dados local

    Matplotlib - Geração de gráficos

    Pytest - Testes automatizados

    Argparse - Interface de linha de comando

Próximas Melhorias

    □

    Exportar dados para CSV/PDF
    □

    Notificações por e-mail
    □

    Dashboard web com Streamlit
    □

    Versão para Linux/Mac
    □

    Executável único (.exe)

Contribuição

    Faça um fork do projeto

    Crie uma branch: git checkout -b minha-feature

    Commit suas mudanças: git commit -m 'Adiciona nova feature'

    Push: git push origin minha-feature

    Abra um Pull Request

Licença

Este projeto está sob a licença MIT.
Desenvolvedor

Seu Nome - seu-email@gmail.com