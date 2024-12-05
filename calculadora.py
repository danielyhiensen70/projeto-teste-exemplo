# Calculadora no terminal

def calcular():
    print("Calculadora")
    print("Digite 'sair' para encerrar.")
    
    while True:
        # Solicitar ao usuário a operação matemática
        expressao = input("Digite uma operação (ex: 2 + 3): ")

        # Condição de saída
        if expressao.lower() == "sair":
            print("Saindo da calculadora.")
            break
        
        try:
            # Avaliar a expressão inserida
            resultado = eval(expressao)
            print(f"Resultado: {resultado}")
        except Exception as e:
            print("Erro! Certifique-se de digitar a operação corretamente.")

# Rodar a calculadora
calcular()

