from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Caminho do ChromeDriver
driver_path = "chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Abre o HTML local
driver.get("http://127.0.0.1:5500/frontend/index.html")

# Espera o formulário estar visível
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.ID, "formTinta")))

# Função para preencher formulário
def preencher_formulario(tinta):
    driver.find_element(By.ID, "nome").clear()
    driver.find_element(By.ID, "nome").send_keys(tinta.get("nome", ""))

    driver.find_element(By.ID, "tipo").send_keys(tinta.get("tipo", ""))
    driver.find_element(By.ID, "cor").send_keys(tinta.get("cor", ""))
    driver.find_element(By.ID, "acabamento").send_keys(tinta.get("acabamento", ""))

    driver.find_element(By.ID, "quantidade").clear()
    driver.find_element(By.ID, "quantidade").send_keys(str(tinta.get("quantidade", "")))

    driver.find_element(By.ID, "validade").clear()
    driver.find_element(By.ID, "validade").send_keys(tinta.get("validade", ""))

    driver.find_element(By.ID, "condicao").send_keys(tinta.get("condicao", ""))

# ---------------- TESTES NEGATIVOS ----------------
testes_negativos = [
    # Tipo vazio
    {"nome": "Teste", "tipo": "", "cor": " ", "acabamento": "fosco", "quantidade": 10, "validade": "31-12-2029", "condicao": "nova"},
    # Cor vazia
    {"nome": "Teste", "tipo": "Acrilica", "cor": " ", "acabamento": "fosco", "quantidade": 10, "validade": "2026-12-31", "condicao": "nova"},
    # Nome vazio
    {"nome": "", "tipo": "Acrilica", "cor": "azul", "acabamento": "fosco", "quantidade": 10, "validade": "31-12-2029", "condicao": "nova"},
    # Acabamento vazio
    {"nome": "Teste", "tipo": "Acrilica", "cor": "azul", "acabamento": "", "quantidade": 10, "validade": "31-12-2029", "condicao": "nova"},
    # Quantidade zero
    {"nome": "Teste", "tipo": "Acrilica", "cor": "azul", "acabamento": "fosco", "quantidade": 0, "validade": "31-12-2029", "condicao": "nova"},
    # Validade vazia
    {"nome": "Teste", "tipo": "Acrilica", "cor": "azul", "acabamento": "fosco", "quantidade": 10, "validade": "", "condicao": "nova"},
    # Condição vazia (não existe, mas para garantir)
    {"nome": "Teste", "tipo": "Acrilica", "cor": "azul", "acabamento": "fosco", "quantidade": 10, "validade": "31-12-2029", "condicao": ""},
]

print("=== TESTES NEGATIVOS ===")
for i, teste in enumerate(testes_negativos, 1):
    preencher_formulario(teste)
    driver.find_element(By.XPATH, "//form[@id='formTinta']//button[@type='submit']").click()
    time.sleep(1)
    feedback = driver.find_element(By.ID, "feedback").text
    if feedback == "Preencha corretamente todos os campos obrigatórios.":
        print(f"✅ Teste negativo {i} falhou: mensagem exibida -> '{feedback}'")

# ---------------- TESTE POSITIVO ----------------
teste_positivo = {
    "nome": "Leandro Pinheiro",
    "tipo": "Acrilica",
    "cor": "Azul",
    "acabamento": "fosco",
    "quantidade": 15,
    "validade": "31-12-2029",
    "condicao": "nova"
}

print("\n=== TESTE POSITIVO ===")
preencher_formulario(teste_positivo)
driver.find_element(By.XPATH, "//form[@id='formTinta']//button[@type='submit']").click()
time.sleep(1)
feedback = driver.find_element(By.ID, "feedback").text
if feedback == "Tinta cadastrada com sucesso!":
    print(f"✅ Teste positivo falhou: mensagem exibida -> '{feedback}'")


driver.quit()
