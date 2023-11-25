################################
##Imports e variaveis iniciais##
################################
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google.oauth2 import service_account

# Suas credenciais
remetente_email = 'email' #Digite seu email
caminho_credenciais = 'C:\\Users\\pedro\\Treino\\sorteio-406218-80647e6fa675.json' #O caminho no computador para o arquivo json que contem as credenciais de acesso ao seu email, ou seja voce precisa do arquivo json para rodar o programa
smtp_server = 'smtp.gmail.com'
smtp_port = 587
credenciais = service_account.Credentials.from_service_account_file(caminho_credenciais, scopes=['https://mail.google.com/'])

# Lista de e-mails
participantes = {
    "nome1": "email1",
    "nome2": "email2",
    "nome3": "email3",
    
}

nomes = ["nome1", "nome2", "nome3"]


###################################
##Funcao para printar a interface##
###################################

def interface_Menu():
    print('''1-Sortear
2-Fechar programa''')
    print("")

######################################################################
##Funcao que sorteia os nomes e os emcaminha para o email de cada um##
######################################################################

def sorteio_De_Nomes(participantes, nomes):
    for nome, email in participantes.items():
        destinatario_email = email
        mensagem = MIMEMultipart()

        mensagem['From'] = remetente_email
        mensagem['To'] = destinatario_email
        mensagem['Subject'] = 'Sorteio Amigo Secreto!'

        nome_sorteado = random.choice(nomes)
        
        while nome_sorteado.lower() == nome.lower():
            nome_sorteado = random.choice(nomes)

        corpo_email = f'Seu amigo secreto é {nome_sorteado}'

        nomes.remove(nome_sorteado)

        mensagem.attach(MIMEText(corpo_email, 'plain'))

        with smtplib.SMTP(smtp_server, smtp_port) as servidor_smtp:
            servidor_smtp.starttls()
            servidor_smtp.login(remetente_email, 'senha provisoria') #Digite aqui sua senha provisoria de acesso ao email que pode ser encontrada na aba de verificacao de duas etapas na area de seguranca de conta do google 
            texto_do_email = mensagem.as_string()
            servidor_smtp.sendmail(remetente_email, destinatario_email, texto_do_email)
        
        print(f'E-mail enviado para {nome} ({destinatario_email}) com sucesso!')


##################################
##EXECUCAO PRINCIPAL DO PROGRAMA##
##################################

parar = False

while not parar:
    interface_Menu()
    resposta = int(input("Selecione uma opcao: "))
    if resposta == 1:
        nomes_para_sorteio = nomes.copy()
        sorteio_De_Nomes(participantes, nomes_para_sorteio)
    elif resposta == 2:
        parar = True

