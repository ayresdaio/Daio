import math

def obter_float(mensagem):
    """Função auxiliar para garantir que o utilizador insere um número (float)."""
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                print("Por favor, insira um valor positivo.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def obter_int(mensagem):
    """Função auxiliar para garantir que o utilizador insere um número inteiro."""
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print("Por favor, insira um valor positivo.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

def calcular_juros():
    """
    Função principal para calcular o capital acumulado
    com base no tipo de juro e fórmulas fornecidas.
    """
    
    # Pedir os valores iniciais ao utilizador
    Ci = obter_float("Insira o valor do Capital Inicial (Ci) (€): ")
    
    # Pedir juro em percentagem (j) e calcular r
    j = obter_float("Insira o valor do juro em percentagem (j) (%): ")
    r = j / 100.0 # r = j/100
    
    print("\nTipos de juro disponíveis:")
    print("1. Juro Simples")
    print("2. Juro Composto")
    print("3. Juro Contínuo")
    
    while True:
        tipo_juro_input = input("Escolha o tipo de juro (1, 2, ou 3): ")
        
        # --- Cenário 1: Juro Simples ---
        if tipo_juro_input == '1':
            n = obter_int("Insira a duração em anos (n) para aplicar: ")
            Cn = Ci + Ci * r * n
            print(f"\n--- Resultado (Juro Simples) ---")
            print(f"Capital Acumulado (Cn): {Cn:.2f}€")
            break
            
        # --- Cenário 2: Juro Composto ---
        elif tipo_juro_input == '2':
            print("\nTipo de aplicação (capitalização K):")
            print("a. Anual (K=1)")
            print("b. Semestral (K=2)")
            print("c. Trimestral (K=4)")
            
            K = 0
            while True:
                tipo_aplicacao = input("Escolha o tipo de aplicação (a, b, ou c): ").lower()
                if tipo_aplicacao == 'a':
                    K = 1
                    break
                elif tipo_aplicacao == 'b':
                    K = 2
                    break
                elif tipo_aplicacao == 'c':
                    K = 4
                    break
                else:
                    print("Escolha inválida. Tente novamente.")
                    
            n = obter_int("Quantos anos (n) pretende aplicar os juros? ")
            Cn = Ci * math.pow((1 + r / K), n * K)
            print(f"\n--- Resultado (Juro Composto) ---")
            print(f"Capital Acumulado (Cn): {Cn:.2f}€")
            break

        # --- Cenário 3: Juro Contínuo ---
        elif tipo_juro_input == '3':
            n = obter_int("Insira a duração em anos (n) para aplicar: ")
            Cn = Ci * math.exp(n * r)
            print(f"\n--- Resultado (Juro Contínuo) ---")
            print(f"Capital Acumulado (Cn): {Cn:.2f}€")
            break
            
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

# --- Executar o programa (AQUI ESTÁ A MUDANÇA) ---
if __name__ == "__main__":
    
    # Este 'while True:' é a parte "do" do loop.
    # Ele vai continuar a executar para sempre...
    while True:
        
        # 1. Executa o cálculo (pelo menos uma vez)
        calcular_juros()
        
        # 2. Pergunta ao utilizador se quer continuar (a condição "while")
        print("\n" + "="*30)
        resposta = input("Deseja realizar um novo cálculo? (s/n): ").lower()
        
        # 3. Se a resposta não for 's', sai do loop com 'break'
        if resposta != 's':
            print("Obrigado por usar o programa. Adeus!")
            break
        
        # Se for 's', o loop volta ao início e chama calcular_juros() novamente.
        print("\n--- Novo Cálculo ---")