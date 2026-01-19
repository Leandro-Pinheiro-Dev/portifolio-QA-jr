def testes_negativos():
    return [
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
            "condicao": "nova"
        }
    ]

def teste_positivo():
    return {
        "nome": "Leandro Pinheiro",
        "tipo": "Acrilica",
        "cor": "azul",
        "acabamento": "fosco",
        "quantidade": 15,
        "validade": "31-12-2029",
        "condicao": "nova"
    }
