# strings.py

texto = input("Digite um texto: ")

print("\n🔤 Texto em maiúsculas:", texto.upper())
print("🔡 Texto em minúsculas:", texto.lower())
print("🔢 Quantidade de caracteres:", len(texto))
print("🔁 Texto invertido:", texto[::-1])

# Remover espaços e verificar palíndromo
texto_sem_espacos = texto.replace(" ", "").lower()
print("❓ É um palíndromo?", texto_sem_espacos == texto_sem_espacos[::-1])
