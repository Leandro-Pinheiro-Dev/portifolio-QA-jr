import time
<<<<<<< HEAD
from utils.driver_factory import get_driver
=======
from utils.drivers_factory import get_driver
>>>>>>> 6b326bf4e390c6fda908a3a455147bfb601b7163
from pages.cadastro_tinta_page import CadastroTintaPage
from utils.test_data import testes_negativos, teste_positivo

driver = get_driver()
pagina = CadastroTintaPage(driver)
pagina.abrir_pagina()

print("=== TESTES NEGATIVOS ===")

for i, dados in enumerate(testes_negativos(), 1):
    pagina.preencher_formulario_completo(dados)
    pagina.enviar_formulario()
<<<<<<< HEAD

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

=======
    time.sleep(1)

    print(f"\nTeste negativo {i}")
    print("Feedback:", pagina.obter_feedback())

    for campo in [pagina.TIPO, pagina.COR, pagina.ACABAMENTO]:
        msg = pagina.obter_mensagem_validacao(campo)
        if msg:
            print("Validação HTML5:", msg)
>>>>>>> 6b326bf4e390c6fda908a3a455147bfb601b7163

print("\n=== TESTE POSITIVO ===")

pagina.preencher_formulario_completo(teste_positivo())
pagina.enviar_formulario()
time.sleep(1)

print("Feedback:", pagina.obter_feedback())

driver.quit()
