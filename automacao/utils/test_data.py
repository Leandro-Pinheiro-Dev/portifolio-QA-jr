def testes_negativos():
    return [
<<<<<<< HEAD
        # 1️⃣ Nenhum campo preenchido
        {},

        # 2️⃣ Somente tipo
        {
            "tipo": "Latex"
        },

        # 3️⃣ Tipo + cor
        {
            "tipo": "Latex",
            "cor": "azul"
        },

        # 4️⃣ Tipo + cor + acabamento
        {
            "tipo": "Latex",
            "cor": "azul",
            "acabamento": "fosco"
        },

        # 5️⃣ Nome + tipo + cor + acabamento
        {
            "nome": "Teste",
            "tipo": "Latex",
            "cor": "azul",
            "acabamento": "fosco"
        },

        # 6️⃣ Todos, mas quantidade inválida
        {
            "nome": "Teste",
            "tipo": "Latex",
            "cor": "azul",
            "acabamento": "fosco",
            "quantidade": -1,
            "validade": "2026-12-31",
=======
        {
            "nome": "Teste",
            "tipo": "",
            "cor": "",
            "acabamento": "",
            "quantidade": 10,
            "validade": "31-12-2029",
            "condicao": "nova"
        },
        {
            "nome": "Teste",
            "tipo": "Acrilica",
            "cor": "",
            "acabamento": "",
            "quantidade": 10,
            "validade": "31-12-2029",
            "condicao": "nova"
        },
        {
            "nome": "",
            "tipo": "Acrilica",
            "cor": "",
            "acabamento": "",
            "quantidade": 10,
            "validade": "31-12-2029",
            "condicao": "nova"
        },
        {
            "nome": "Teste",
            "tipo": "Acrilica",
            "cor": "azul",
            "acabamento": "",
            "quantidade": 10,
            "validade": "31-12-2029",
            "condicao": "nova"
        },
        {
            "nome": "Teste",
            "tipo": "Acrilica",
            "cor": "azul",
            "acabamento": "fosco",
            "quantidade": 0,
            "validade": "31-12-2029",
>>>>>>> 6b326bf4e390c6fda908a3a455147bfb601b7163
            "condicao": "nova"
        }
    ]

<<<<<<< HEAD

def teste_positivo():
    return {
        "nome": "Tinta Premium",
        "tipo": "Latex",
        "cor": "azul",
        "acabamento": "fosco",
        "quantidade": 20,
        "validade": "2026-12-31",
=======
def teste_positivo():
    return {
        "nome": "Leandro Pinheiro",
        "tipo": "Acrilica",
        "cor": "azul",
        "acabamento": "fosco",
        "quantidade": 15,
        "validade": "31-12-2029",
>>>>>>> 6b326bf4e390c6fda908a3a455147bfb601b7163
        "condicao": "nova"
    }
