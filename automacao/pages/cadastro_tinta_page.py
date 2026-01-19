from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CadastroTintaPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ===== LOCATORS =====
    NOME = (By.ID, "nome")
    TIPO = (By.ID, "tipo")
    COR = (By.ID, "cor")
    ACABAMENTO = (By.ID, "acabamento")
    QUANTIDADE = (By.ID, "quantidade")
    VALIDADE = (By.ID, "validade")
    CONDICAO = (By.ID, "condicao")
    BOTAO_SUBMIT = (By.XPATH, "//form[@id='formTinta']//button[@type='submit']")
    FEEDBACK = (By.ID, "feedback")

    # ===== AÇÕES =====
    def abrir_pagina(self):
        self.driver.get("http://127.0.0.1:5500/frontend/index.html")
        self.wait.until(EC.visibility_of_element_located(self.NOME))

    def preencher_nome(self, valor):
        campo = self.driver.find_element(*self.NOME)
        campo.clear()
        campo.send_keys(valor)

    def preencher_select(self, locator, valor):
        self.driver.find_element(*locator).send_keys(valor)

    def preencher_quantidade(self, valor):
        campo = self.driver.find_element(*self.QUANTIDADE)
        campo.clear()
        campo.send_keys(str(valor))

    def preencher_validade(self, valor):
        campo = self.driver.find_element(*self.VALIDADE)
        campo.clear()
        campo.send_keys(valor)

    def enviar_formulario(self):
        self.driver.find_element(*self.BOTAO_SUBMIT).click()

    def obter_feedback(self):
        return self.driver.find_element(*self.FEEDBACK).text

    def preencher_formulario_completo(self, dados):
        self.preencher_nome(dados.get("nome", ""))
        self.preencher_select(self.TIPO, dados.get("tipo", ""))
        self.preencher_select(self.COR, dados.get("cor", ""))
        self.preencher_select(self.ACABAMENTO, dados.get("acabamento", ""))
        self.preencher_quantidade(dados.get("quantidade", ""))
        self.preencher_validade(dados.get("validade", ""))
        self.preencher_select(self.CONDICAO, dados.get("condicao", ""))

    def obter_mensagem_validacao(self, locator):
        elemento = self.driver.find_element(*locator)
        return self.driver.execute_script(
            "return arguments[0].validationMessage;", elemento
        )
