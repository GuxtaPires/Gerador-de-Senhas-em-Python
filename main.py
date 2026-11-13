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

# Solicitando o tamanho da senha ao usuário
tamanho = int(input("\nQuantos caracteres sua senha deve ter? "))
# Gerando a senha
senha = ""

for i in range(tamanho):
    senha += secrets.choice(caracteres)

# Exibindo o resultado
print(f"\nSua senha gerada foi: {senha}")