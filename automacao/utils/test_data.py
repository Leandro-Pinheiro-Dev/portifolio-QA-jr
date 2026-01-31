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
            "condicao": "nova"
        }
    ]


def teste_positivo():
    return {
        "nome": "Tinta Premium",
        "tipo": "Latex",
        "cor": "azul",
        "acabamento": "fosco",
        "quantidade": 20,
        "validade": "2026-12-31",
        "condicao": "nova"
    }
