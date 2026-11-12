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

# Definindo o tamanho da senha
tamanho = 12

# Gerando a senha
senha = ""

for i in range(tamanho):
    senha += secrets.choice(caracteres)

# Exibindo o resultado
print(f"\nSua senha gerada foi: {senha}")