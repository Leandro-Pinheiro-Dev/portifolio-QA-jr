
## 📘 Banco de Tintas — QA Jr Portfolio

### 🧾 Descrição

Este repositório contém o projeto **Banco de Tintas**, que inclui:

📌 Interface web para cadastro de tintas (frontend HTML/CSS/JS)
📌 Backend em Python (Flask) com persistência em banco de dados MySQL
📌 Scripts de automação de testes usando **Selenium WebDriver**
📌 Análise de testes manuais e automatizados com evidências e resultados

O objetivo é demonstrar habilidades de **testes manuais, automação e integração** entre frontend, backend e banco de dados.

---

## 🚀 Tecnologias Usadas

| Camada         | Tecnologia                             |
| -------------- | -------------------------------------- |
| Frontend       | HTML, CSS, JavaScript                  |
| Backend        | Python 3.11.x, Flask                      |
| Banco de Dados | MySQL                                  |
| Automação      | Selenium WebDriver                     |
| Ferramentas    | VS Code, ChromeDriver, MySQL Workbench |

---

## 🔧 Pré‑Requisitos

Antes de iniciar, verifique se você tem:

1. **Python 3.x** instalado
2. **MySQL Server e MySQL Workbench**
3. **Google Chrome** instalado
4. **ChromeDriver** compatível com sua versão do Chrome
5. Editor de código (ex.: **VS Code**)

---

## 🛠️ Configuração

### 💿 Banco de Dados

No **MySQL Workbench** ou terminal SQL, execute:

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

> Ajuste seu usuário/senha no arquivo de conexão do backend conforme necessário.

---

## 🧑‍💻 Rodando o Projeto

### 🔹 Backend (Flask)

1. Abra o terminal
2. Vá para a pasta `backend`:

```power shell
cd backend
```

3. Crie e ative ambiente virtual:

```power shell
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate
```

4. Instale dependências:

```power shell
pip install flask mysql‑connector‑python
```

5. Execute o servidor Flask:

```power shell
python app.py
```

O backend ficará disponível em:

```
http://127.0.0.1:5000
```

---

### 🔹 Frontend

Abra o arquivo:

```
http://127.0.0.1:5500/frontend/index.html
```

no navegador (ou use o Live Server do VS Code).

---

## 🧪 Testes Manuais

### 🚧 Cenários executados

✔ Campos obrigatórios bem preenchidos
✔ Tentativas com campos vazios
✔ Verificação de mensagem de erro
✔ Registro válido salvo no banco

Verifique diretamente no MySQL após um cadastro válido:

```sql
SELECT * FROM Tinta;
```

---

## 🤖 Automação com Selenium

### 💼 Instalação

Na pasta do seu projeto (mesmo ambiente que rodou o backend), instale Selenium:

```power shell
pip install selenium
```
---

### 🏃 Executando os testes

No terminal:

```power shell
cd backend
python app.py
```
```power shell
cd frontend
python automaizar_tintas.py
```
Ele vai executar:

✔ Casos negativos (campos obrigatórios vazios)
✔ Caso positivo (cadastro válido)

Veja os resultados no terminal e confirme no banco de dados.

---

## 📊 Análise de Testes

Você também encontra no repositório o arquivo:

📄 **Analise_Testes_Tinta.xlsx** – com tabela de resultados, entradas, feedbacks e verificação no banco.


---

## 👍 Considerações Finais

Esse projeto demonstra:

✔ Entendimento de formulários web
✔ Integração com banco de dados
✔ Testes manuais e automatizados
✔ Documentação clara do processo

