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
        # Gerando a senha
        senha = ""

        for i in range(tamanho):
            senha += secrets.choice(caracteres)

        # Exibindo o resultado
        print(f"\nSua senha gerada foi: {senha}")

except ValueError:
    print("\nErro: você precisa digitar um número inteiro!")