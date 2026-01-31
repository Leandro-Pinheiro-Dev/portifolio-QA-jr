import time
from utils.driver_factory import get_driver
from pages.cadastro_tinta_page import CadastroTintaPage
from utils.test_data import testes_negativos, teste_positivo

driver = get_driver()
pagina = CadastroTintaPage(driver)
pagina.abrir_pagina()

print("=== TESTES NEGATIVOS ===")

for i, dados in enumerate(testes_negativos(), 1):
    pagina.preencher_formulario_completo(dados)
    pagina.enviar_formulario()

    print(f"\nTeste negativo {i}")

    for campo in [
        pagina.NOME,
        pagina.TIPO,
        pagina.COR,
        pagina.ACABAMENTO,
        pagina.QUANTIDADE,
        pagina.VALIDADE,
        pagina.CONDICAO
    ]:
        msg = pagina.obter_mensagem_validacao(campo)
        if msg:
            print(f"Validação HTML5 ({campo[1]}):", msg)


print("\n=== TESTE POSITIVO ===")

pagina.preencher_formulario_completo(teste_positivo())
pagina.enviar_formulario()
time.sleep(1)

print("Feedback:", pagina.obter_feedback())

driver.quit()
