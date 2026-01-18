import time
from utils.driver_factory import get_driver
from pages.cadastro_tinta_page import CadastroTintaPage

# ================= SETUP =================
# Inicializa o navegador e abre a página
driver = get_driver()
pagina = CadastroTintaPage(driver)
pagina.abrir_pagina()

# ================= TESTES NEGATIVOS =================
# Cada cenário valida regras de negócio ou validações obrigatórias

testes_negativos = [

    # Teste 1:
    # Valida comportamento quando NENHUM select obrigatório é selecionado
    {
        "nome": "Teste",
        "tipo": "",
        "cor": "",
        "acabamento": "",
        "quantidade": 10,
        "validade": "31-12-2029",
        "condicao": "nova"
    },

    # Teste 2:
    # Valida quando apenas o select "tipo" é preenchido
    {
        "nome": "Teste",
        "tipo": "Acrilica",
        "cor": "",
        "acabamento": "",
        "quantidade": 10,
        "validade": "31-12-2029",
        "condicao": "nova"
    },

    # Teste 3:
    # Valida campo obrigatório "nome" vazio
    {
        "nome": "",
        "tipo": "Acrilica",
        "cor": "",
        "acabamento": "",
        "quantidade": 10,
        "validade": "31-12-2029",
        "condicao": "nova"
    },

    # Teste 4:
    # Valida ausência do select "acabamento"
    {
        "nome": "Teste",
        "tipo": "Acrilica",
        "cor": "azul",
        "acabamento": "",
        "quantidade": 10,
        "validade": "31-12-2029",
        "condicao": "nova"
    },

    # Teste 5:
    # Valida regra de negócio: quantidade não pode ser zero
    {
        "nome": "Teste",
        "tipo": "Acrilica",
        "cor": "azul",
        "acabamento": "fosco",
        "quantidade": 0,
        "validade": "31-12-2029",
        "condicao": "nova"
    },

    # Teste 6:
    # Valida data inválida no campo "validade"
    {
        "nome": "Teste",
        "tipo": "Acrilica",
        "cor": "azul",
        "acabamento": "fosco",
        "quantidade": 10,
        "validade": "2029-02-31",
        "condicao": "nova"
    },
]

print("=== TESTES NEGATIVOS ===")

for i, teste in enumerate(testes_negativos, 1):
    pagina.preencher_formulario_completo(teste)
    pagina.enviar_formulario()
    time.sleep(1)

    # ===== Feedback do sistema =====
    # Mensagem exibida pelo frontend/backend
    feedback = pagina.obter_feedback()
    print(f"\nTeste negativo {i} - Feedback sistema: {feedback}")

    # ===== Validação HTML5 dos selects =====
    # Captura mensagens nativas do navegador (required)

    msg_tipo = pagina.obter_mensagem_validacao_select(pagina.TIPO)
    if msg_tipo:
        print(f"Teste negativo {i} - Validação select 'tipo': {msg_tipo}")

    msg_cor = pagina.obter_mensagem_validacao_select(pagina.COR)
    if msg_cor:
        print(f"Teste negativo {i} - Validação select 'cor': {msg_cor}")

    msg_acabamento = pagina.obter_mensagem_validacao_select(pagina.ACABAMENTO)
    if msg_acabamento:
        print(f"Teste negativo {i} - Validação select 'acabamento': {msg_acabamento}")

# ================= TESTE POSITIVO =================
# Valida fluxo completo com TODOS os campos válidos

teste_positivo = {
    "nome": "Leandro Pinheiro",
    "tipo": "Acrilica",
    "cor": "azul",
    "acabamento": "fosco",
    "quantidade": 15,
    "validade": "31-12-2029",
    "condicao": "nova"
}

print("\n=== TESTE POSITIVO ===")

pagina.preencher_formulario_completo(teste_positivo)
pagina.enviar_formulario()
time.sleep(1)

# Mensagem de sucesso
feedback = pagina.obter_feedback()
print(f"Teste positivo - Feedback sistema: {feedback}")

# Encerra o navegador
driver.quit()
