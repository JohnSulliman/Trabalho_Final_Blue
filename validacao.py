#--------------------------------------------Usuários-------------------------------------------------------------

def valida_usuario(nome_completo, CPF):
    if len(nome_completo) == 0:
        return False

    if len(CPF) != 14:
        return False

    else:
        return True

#---------------------------------------------Gêneros-------------------------------------------------------------

def valida_genero(nome):
    if len(nome) == 0:
        return False

    else:
        return True

#---------------------------------------------Diretores-----------------------------------------------------------

