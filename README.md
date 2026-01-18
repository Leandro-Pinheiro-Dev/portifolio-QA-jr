# 📘 Banco de Tintas — QA Jr Portfolio

## 🧾 Descrição do Projeto

O **Banco de Tintas** é uma aplicação web desenvolvida com foco em **qualidade de software**, abrangendo **testes manuais e automação de testes** aplicados a um sistema real de cadastro de tintas.

O projeto foi estruturado seguindo boas práticas com destaque para o uso do **padrão Page Object Model (POM)** na automação com Selenium.

Este repositório tem como objetivo demonstrar competências técnicas em:

* Testes manuais
* Automação de testes
* Integração Frontend, Backend e Banco de Dados
* Organização e documentação de projetos de QA

---

## 🗂️ Estrutura do Projeto

A automação foi organizada seguindo o **Page Object Model**, separando responsabilidades de forma clara e escalável.

```
Banco-de-tintas/
│
├── automacao/
│   ├── pages/                 # Page Objects (mapeamento de telas)
│   │   └── cadastro_tinta_page.py
│   │
│   ├── tests/                 # Casos de teste automatizados
│   │   └── test_cadastro_tinta.py
│   │
│   ├── utils/                 # Utilitários (driver, configurações)
│   │   └── driver_factory.py
│   │
│   └── venv/                  # Ambiente virtual da automação
│
├── backend/
│   ├── app.py                 # Backend Flask
│   ├── venv/                  # Ambiente virtual do backend
│   └── __pycache__/
│
├── banco de dados/
│   └── schema.sql             # Script de criação do banco
│
├── front-end/
│   ├── index.html
│   ├── script.js
│   ├── styles.css
│   └── img/
│
├── chromedriver.exe
├── Analise_Testes_Tinta.xlsx
└── README.md
```

---

## 🧠 Padrão Page Object Model (POM)

A automação utiliza o **Page Object Model**, onde:

* Cada página da aplicação é representada por uma **classe**
* Elementos são mapeados por **locators**
* Ações e comportamentos ficam centralizados
* Os testes ficam mais limpos, legíveis e fáceis de manter

📌 Exemplo:

* `pages/cadastro_tinta_page.py` → representa a tela de cadastro
* `tests/test_cadastro_tinta.py` → contém apenas os cenários de teste

---

## 🚀 Tecnologias Utilizadas

| Camada            | Tecnologia                             |
| ----------------- | -------------------------------------- |
| Frontend          | HTML, CSS, JavaScript                  |
| Backend           | Python 3.11, Flask                     |
| Banco de Dados    | MySQL                                  |
| Automação         | Selenium WebDriver                     |
| Padrão de Projeto | Page Object Model (POM)                |
| Ferramentas       | VS Code, ChromeDriver, MySQL Workbench |

---

## 🔧 Pré-Requisitos

Antes de executar o projeto, certifique-se de ter instalado:

1. Python 3.x
2. MySQL Server e MySQL Workbench
3. Google Chrome
4. ChromeDriver compatível com o navegador
5. VS Code ou editor similar

---

## 💿 Configuração do Banco de Dados

Execute o script abaixo no MySQL:

```sql
CREATE DATABASE IF NOT EXISTS banco_tintas
CHARACTER SET utf8mb4
COLLATE utf8mb4_general_ci;

USE banco_tintas;

CREATE TABLE IF NOT EXISTS Tinta (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    tipo VARCHAR(100) NOT NULL,
    cor VARCHAR(50) NOT NULL,
    acabamento VARCHAR(50) NOT NULL,
    quantidade INT NOT NULL,
    validade DATE NOT NULL,
    condicao VARCHAR(50) NOT NULL
);
```

📌 Ajuste usuário e senha no backend conforme seu ambiente.

---

## ▶️ Executando a Aplicação

### 🔹 Backend (Flask)

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install flask mysql-connector-python
python app.py
```

Servidor disponível em:

```
http://127.0.0.1:5000
```

---

### 🔹 Frontend

Abra o arquivo:

```
front-end/index.html
```

Ou utilize o **Live Server** do VS Code.

---

## 🧪 Testes Manuais

### Cenários Validados

✔ Campos obrigatórios
✔ Validação de selects obrigatórios
✔ Mensagens de erro
✔ Registros inválidos
✔ Cadastro válido persistido no banco

Consulta no banco:

```sql
SELECT * FROM Tinta;
```

---

## 🤖 Automação de Testes (Selenium)

### 📦 Instalação

```bash
pip install selenium
```

---

### ▶️ Execução dos Testes Automatizados

Com o backend rodando:

```bash
cd automacao
python -m tests.test_cadastro_tinta
```

### Cenários Automatizados

✔ Testes negativos (validações de campos e selects obrigatórios)
✔ Teste positivo (cadastro válido)
✔ Captura de mensagens de feedback do sistema
✔ Impressão dos resultados no console

---

## 📊 Análise de Testes

O arquivo abaixo contém a análise consolidada:

📄 **Analise_Testes_Tinta.xlsx**

Inclui:

* Casos de teste
* Entradas
* Resultados esperados
* Resultados obtidos
* Evidências

---

## ✅ Considerações Finais

Este projeto demonstra:

✔ Aplicação prática do padrão Page Object Model
✔ Automação de testes com Selenium
✔ Validações funcionais e de regras de negócio
✔ Integração completa Frontend, Backend e Banco de Dados
✔ Organização e documentação voltadas para portfólio QA Jr

---

📌 **Autor:** Leandro Pinheiro
📌 **Objetivo:** Portfólio QA Júnior
