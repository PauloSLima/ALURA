Usuario_correto = 'paulo'
senha_correta = '2008'

Usuario = input('Digite nome de usuario: \n')
senha = input('digite a senha: \n')

if Usuario == Usuario_correto and senha == senha_correta:
    print('login bem sucedido')

else:
    print('login invalido. Tente novamente.')