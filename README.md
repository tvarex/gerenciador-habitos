<div align="center">

# 🎯 habit-tracker

*Sua jornada de consistência começa aqui*

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/Tests-100%25-brightgreen)](https://github.com/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

</div>

---

## 💡 Sobre

Um **gerenciador de hábitos** minimalista para quem quer:

- 🔥 Manter streaks (sequência de dias)
- 📊 Visualizar progresso com gráficos
- 🎯 Alcançar metas consistentemente

Sem distrações. Sem firulas. **Apenas dados**.

---

## 🚀 Começando

### 1. Clone o repositório

```bash
git clone https://github.com/tvarex/habit-tracker.git
cd habit-tracker

2. Instale

Windows:
bash

setup.bat

Linux/Mac:
bash

pip install -r requirements.txt

3. Use

Windows:
bash

habitos.bat

Linux/Mac:
bash

python src/cli.py

📖 Guia Rápido
bash

# Crie um hábito
> add "Meditar"

# Registre hoje
> check "Meditar"

# Veja seu progresso
> list

# Visualize gráficos
> graph "Meditar"

# Veja relatório completo
> relatorio

# Saia
> exit

📊 Exemplo de saída
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

📋 Comandos Disponíveis
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
📊 Gráficos

O sistema gera gráficos automáticos para visualizar seu progresso:

    Gráfico de 30 dias: Visão mensal dos seus hábitos

    Gráfico de 7 dias: Acompanhamento semanal

    Relatório completo: Comparação entre todos os hábitos

As cores são intuitivas:

    ✅ Verde: Dia que você fez o hábito

    ❌ Vermelho: Dia que você não fez

🧪 Testes

Qualidade é prioridade. O projeto inclui 10 testes automatizados.
Rodar os testes

Windows:
bash

testar.bat

Linux/Mac:
bash

pytest tests/ -v

Resultado esperado
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

Cobertura de código
bash

pytest tests/ --cov=src

🗂️ Estrutura do Projeto
text

📂 habit-tracker/
├── 📂 src/                    # Código fonte
│   ├── 📄 __init__.py
│   ├── 📄 database.py         # Banco de dados SQLite
│   ├── 📄 habit.py            # Lógica dos hábitos
│   ├── 📄 report.py           # Gráficos e relatórios
│   └── 📄 cli.py              # Interface de linha de comando
├── 📂 tests/                  # Testes automatizados
│   ├── 📄 __init__.py
│   ├── 📄 test_habits.py
│   └── 📄 test_sistema_completo.py
├── 📂 data/                   # Banco de dados
│   └── 📄 habitos.db
├── 📄 requirements.txt        # Dependências
├── 📄 setup.bat              # Instalador Windows
├── 📄 habitos.bat            # Atalho principal
├── 📄 testar.bat             # Atalho para testes
├── 📄 limpar.bat             # Limpar dados
├── 📄 atualizar.bat          # Atualizar projeto
└── 📄 README.md              # Este arquivo

🛠️ Tecnologias
Tecnologia	Para quê
Python 3.8+	Linguagem principal
SQLite	Banco de dados local (leve e rápido)
Matplotlib	Geração de gráficos
Pytest	Testes automatizados
Argparse	Interface de linha de comando
🚀 Próximas Melhorias

Ideias para o futuro:

    □

    Exportar dados para CSV
    □

    Dashboard web com Streamlit
    □

    Notificações por e-mail
    □

    Versão para Linux/Mac
    □

    App mobile (React Native)
    □

    Sincronização com nuvem

🤝 Como Contribuir

Contribuições são sempre bem-vindas!

    Faça um fork do projeto

    Crie sua branch (git checkout -b feature/AmazingFeature)

    Commit suas mudanças (git commit -m 'Add some AmazingFeature')

    Push para a branch (git push origin feature/AmazingFeature)

    Abra um Pull Request

📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
👤 Autor

Gustavo Tavares da Silva

https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white
https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white
https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white
⭐ Agradecimentos

Obrigado por usar o habit-tracker!

Se este projeto te ajudou de alguma forma, considere deixar uma estrela ⭐ no GitHub!
<div align="center">

Feito com Python
</div> ```