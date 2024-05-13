## Se solicita crear un programa para leer direcciones de correo electrónico y verificar
## si representan una dirección válida. Por ejemplo usuario@dominio.com.ar. Para que
## una dirección sea considerada válida el nombre de usuario debe poseer solamente
## caracteres alfanuméricos, la dirección contener un solo carácter @, el dominio debe
## tener al menos un carácter y tiene que finalizar con .com o .com.ar. ##
def verificador_emails(email):
    usuario, arroba, dominio = email.partition("@")
    chequeo_usuario = usuario.isalnum()
    chequeo_arroba = "@" in email
    if chequeo_arroba:
        dominio_com = dominio.endswith(".com")
        dominio_com_ar = dominio.endswith(".com.ar")
        chequeo_dominio = dominio_com or dominio_com_ar
    else:
        chequeo_dominio = False
    direccion_valida = chequeo_usuario and chequeo_arroba and chequeo_dominio
    if direccion_valida == True:
        return "Su Dirección de Correo Electronico Se ha validado con exito"
    else:
        return "Su dirección de correo electronico No se ha podido Validar correctamente"

mail = input("Por favor ingrese su dirección de Correo Electronico: ")
chequeo = verificador_emails(mail)
print("-" * 148)
print()
print(chequeo)
print()
print("-" * 148)