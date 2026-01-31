from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class CadastroTintaPage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "http://127.0.0.1:5500/frontend/index.html"

        self.NOME = (By.ID, "nome")
        self.TIPO = (By.ID, "tipo")
        self.COR = (By.ID, "cor")
        self.ACABAMENTO = (By.ID, "acabamento")
        self.CONDICAO = (By.ID, "condicao")
        self.QUANTIDADE = (By.ID, "quantidade")
        self.VALIDADE = (By.ID, "validade")

        self.BOTAO = (By.ID, "btnCadastrar")

    def abrir_pagina(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.NOME)
        )

    def limpar_formulario(self):
        # Apenas inputs de texto/numero/data
        for campo in [self.NOME, self.QUANTIDADE, self.VALIDADE]:
            el = self.driver.find_element(*campo)
            el.send_keys(Keys.CONTROL, "a")
            el.send_keys(Keys.DELETE)

        # NÃO limpar selects (option disabled causa erro)

    def preencher_formulario_completo(self, dados):
        self.limpar_formulario()

        if "nome" in dados:
            self.driver.find_element(*self.NOME).send_keys(dados["nome"])

        if "tipo" in dados:
            Select(self.driver.find_element(*self.TIPO)) \
                .select_by_value(dados["tipo"])

        if "cor" in dados:
            Select(self.driver.find_element(*self.COR)) \
                .select_by_value(dados["cor"])

        if "acabamento" in dados:
            Select(self.driver.find_element(*self.ACABAMENTO)) \
                .select_by_value(dados["acabamento"])

        if "condicao" in dados:
            Select(self.driver.find_element(*self.CONDICAO)) \
                .select_by_value(dados["condicao"])

        if "quantidade" in dados:
            self.driver.find_element(*self.QUANTIDADE) \
                .send_keys(str(dados["quantidade"]))

        if "validade" in dados:
            self.driver.find_element(*self.VALIDADE) \
                .send_keys(dados["validade"])

    def enviar_formulario(self):
        self.driver.find_element(*self.BOTAO).click()

    def obter_mensagem_validacao(self, campo):
        elemento = self.driver.find_element(*campo)
        return self.driver.execute_script(
            "return arguments[0].validationMessage;", elemento
 )

    def obter_feedback(self):
        try:
            elemento = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "feedback"))
            )
            return elemento.text.strip()
        except:
            return "Nenhum feedback exibido"

    
