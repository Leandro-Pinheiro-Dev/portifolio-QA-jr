def testes_negativos():
    return [

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

        # 5️⃣ Nome + tipo + cor + acabamento (sem quantidade e validade)
        {
            "nome": "Teste",
            "tipo": "Latex",
            "cor": "azul",
            "acabamento": "fosco"
        },

        # 6️⃣ Quantidade inválida (negativa)
        {
            "nome": "Teste",
            "tipo": "Latex",
            "cor": "azul",
            "acabamento": "fosco",
            "quantidade": -1,
            "validade": "2026-12-31",
            "condicao": "nova"
        },

        # 7️⃣ Tipo, cor e acabamento vazios
        {
            "nome": "Teste",
            "tipo": "",
            "cor": "",
            "acabamento": "",
            "quantidade": 10,
            "validade": "2029-12-31",
            "condicao": "nova"
        },

        # 8️⃣ Cor e acabamento vazios
        {
            "nome": "Teste",
            "tipo": "Acrilica",
            "cor": "",
            "acabamento": "",
            "quantidade": 10,
            "validade": "2029-12-31",
            "condicao": "nova"
        },

        # 9️⃣ Nome vazio
        {
            "nome": "",
            "tipo": "Acrilica",
            "cor": "azul",
            "acabamento": "fosco",
            "quantidade": 10,
            "validade": "2029-12-31",
            "condicao": "nova"
        },

        # 🔟 Quantidade zero (inválida)
        {
            "nome": "Teste",
            "tipo": "Acrilica",
            "cor": "azul",
            "acabamento": "fosco",
            "quantidade": 0,
            "validade": "2029-12-31",
            "condicao": "nova"
        }
    ]


def teste_positivo():
    return {
        "nome": "Tinta Premium",
        "tipo": "Acrilica",
        "cor": "azul",
        "acabamento": "fosco",
        "quantidade": 15,
        "validade": "2029-12-31",
        "condicao": "nova"
    }
