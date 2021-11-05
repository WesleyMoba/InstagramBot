from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys



class InstagramBot:
    def __init__(self):  #Abrir o Firefox e definir senha
        self.navegador = webdriver.Firefox()
        self.navegador.AddArgument ("--headless")
        self.email = 'mobbenalvo1@gmail.com'
        self.senha = '25252425w'
        self.navegador.get('http://www.instagram.com') #Abrir o Site do Instagram
    def login(self):
        emailLogar = self.navegador.find_element_by_name('username')
        emailLogar.send_keys(self.email) 
        senhaLogar = self.navegador.find_element_by_name('password')
        senhaLogar.send_keys(self.senha)
        #Achar os elementos, e digitar a senha
        time.sleep(2)
        botaoLogar = self.navegador.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div').click()
    def seguir(self):
        self.conta_seguir = 'https://www.instagram.com/sigo_de_volta/' #Link para comecar a seguir pessoas
        self.contasEntradas = [] #Lista criada Para armazenar os perfis que voce entro
        time.sleep(4) 
        self.navegador.get(self.conta_seguir) 
        self.SeguirUsuarioNumero = 1
        seguir = 0
        while seguir < 100:
            contaAtual = self.navegador.current_url #Pegar o link da conta atual
            try:
                if contaAtual not in self.contasEntradas: #Caso a conta Atual nao tenha sido aberta ainda, executar isso
                    if self.SeguirUsuarioNumero > 5: #Se o numero do usuario a ser seguido for menor doq 5
                        self.seguidoresDoUsuario = 1 #Redefinimos o valor
                    time.sleep(2)
                    self.seguidoresDoUsuario = self.navegador.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
                    self.seguidoresDoUsuario.click()
                    time.sleep(3)
                    self.entrarNoPerfil = self.navegador.find_element_by_xpath(f'/html/body/div[6]/div/div/div[2]/ul/div/li[{self.SeguirUsuarioNumero}]/div/div[2]/div[1]/div/div/span/a')
                    self.entrarNoPerfil.click()    #Seguir o usuario na lista de seguidores de acordo com o valor da variavel "SeguirUsuarioNumero"
                    time.sleep(2)
                    BotaoSeguir = self.navegador.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button')
                    BotaoSeguir.click()
                    print('Seguiu')
                    seguir += 1
                    self.contasEntradas.append(contaAtual) #Adicionar o link para a lista de contas já entrada.
                else: #Se nao tratar o erro
                    self.tratarErros()
            except: #Caso a conta seja privada tratar o erro tb
                self.tratarErros()
    def tratarErros(self):
        try:
            self.SeguirUsuarioNumero += 1 #Adicionar um a variavel para nao repetir a msm pessoa.
            self.navegador.get(self.contasEntradas[-1])  #Voltar a pagina anterior
            self.contasEntradas.pop() #Excluir esta pagina para no operador logico
        except:
            print('Falha')
bot = InstagramBot() #Inicia tudo que está no __init__
bot.login() #Logar o usuario
bot.seguir() #Segue as pessoas