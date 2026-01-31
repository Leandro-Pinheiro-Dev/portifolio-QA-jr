from selenium.webdriver.common.by import By
<<<<<<< HEAD
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
=======
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
>>>>>>> 6b326bf4e390c6fda908a3a455147bfb601b7163

class CadastroTintaPage:

    def __init__(self, driver):
        self.driver = driver
<<<<<<< HEAD
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

    
=======
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
>>>>>>> 6b326bf4e390c6fda908a3a455147bfb601b7163
