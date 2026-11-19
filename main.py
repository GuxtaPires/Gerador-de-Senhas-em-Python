import secrets
import string

print("================================")
print("       GERADOR DE SENHAS")
print("================================")

# Definindo os caracteres disponíveis
caracteres = (
    string.ascii_lowercase +
    string.ascii_uppercase +
    string.digits +
    string.punctuation
)

# Solicitando o tamanho da senha
try:
    tamanho = int(input("\nQuantos caracteres sua senha deve ter? "))

    # Validando o tamanho informado
    if tamanho < 1 or tamanho > 128:
        print("\nErro: escolha um tamanho entre 1 e 128.")

    else:
        # Perguntando quais caracteres utilizar
        usar_minusculas = input("Incluir letras minúsculas? (s/n): ").lower()
        usar_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower()
        usar_numeros = input("Incluir números? (s/n): ").lower()
        usar_simbolos = input("Incluir símbolos? (s/n): ").lower()

        # Criando o conjunto de caracteres
        caracteres = ""

        if usar_minusculas == "s":
            caracteres += string.ascii_lowercase

        if usar_maiusculas == "s":
            caracteres += string.ascii_uppercase

        if usar_numeros == "s":
            caracteres += string.digits

        if usar_simbolos == "s":
            caracteres += string.punctuation

        # Verificando se alguma categoria foi selecionada
        if caracteres == "":
            print("Erro: selecione pelo menos uma categoria!")

        else:
            # Gerando a senha
            senha = ""

            for i in range(tamanho):
                senha += secrets.choice(caracteres)

            print(f"\nSua senha gerada foi: {senha}")

except ValueError:
    print("\nErro: você precisa digitar um número inteiro!")  