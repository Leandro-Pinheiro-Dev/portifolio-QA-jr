from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CadastroTintaPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ===== Locators =====
    NOME = (By.ID, "nome")
    TIPO = (By.ID, "tipo")
    COR = (By.ID, "cor")
    ACABAMENTO = (By.ID, "acabamento")
    QUANTIDADE = (By.ID, "quantidade")
    VALIDADE = (By.ID, "validade")
    CONDICAO = (By.ID, "condicao")
    BOTAO_SUBMIT = (By.XPATH, "//form[@id='formTinta']//button[@type='submit']")
    FEEDBACK = (By.ID, "feedback")

    # ===== Ações =====
    def abrir_pagina(self):
        # Abre a página de cadastro de tinta
        self.driver.get("http://127.0.0.1:5500/frontend/index.html")
        self.wait.until(EC.visibility_of_element_located(self.NOME))

    def preencher_nome(self, nome):
        campo = self.driver.find_element(*self.NOME)
        campo.clear()
        campo.send_keys(nome)

    def preencher_tipo(self, tipo):
        self.driver.find_element(*self.TIPO).send_keys(tipo)

    def preencher_cor(self, cor):
        self.driver.find_element(*self.COR).send_keys(cor)

    def preencher_acabamento(self, acabamento):
        self.driver.find_element(*self.ACABAMENTO).send_keys(acabamento)

    def preencher_quantidade(self, quantidade):
        campo = self.driver.find_element(*self.QUANTIDADE)
        campo.clear()
        campo.send_keys(str(quantidade))

    def preencher_validade(self, validade):
        campo = self.driver.find_element(*self.VALIDADE)
        campo.clear()
        campo.send_keys(validade)

    def preencher_condicao(self, condicao):
        self.driver.find_element(*self.CONDICAO).send_keys(condicao)

    def enviar_formulario(self):
        self.driver.find_element(*self.BOTAO_SUBMIT).click()

    def obter_feedback(self):
        # Captura mensagem exibida pelo sistema (frontend/backend)
        return self.driver.find_element(*self.FEEDBACK).text

    def preencher_formulario_completo(self, dados):
        # Preenche todos os campos do formulário
        self.preencher_nome(dados.get("nome", ""))
        self.preencher_tipo(dados.get("tipo", ""))
        self.preencher_cor(dados.get("cor", ""))
        self.preencher_acabamento(dados.get("acabamento", ""))
        self.preencher_quantidade(dados.get("quantidade", ""))
        self.preencher_validade(dados.get("validade", ""))
        self.preencher_condicao(dados.get("condicao", ""))

    def obter_mensagem_validacao_select(self, locator):
        """
        Retorna a mensagem de validação HTML5 (required)
        exibida pelo navegador para selects não preenchidos
        """
        elemento = self.driver.find_element(*locator)
        return self.driver.execute_script(
            "return arguments[0].validationMessage;", elemento
        )
