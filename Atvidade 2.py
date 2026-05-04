import numpy as np

# Universidade Federal de Pernambuco (UFPE) - BICT
# Disciplina: Complementos de Cálculo Numérico
# Professor: Marcos Henrique
# Alunos: Wanderson Walisson Tavares dos Santos / Sylmara ALves do Nascimento
# Atividade II - Método do Ponto Fixo (Iteração Linear)


def iteracao_ponto_fixo(g, p0, num_iters=4):
    """
    Realiza um número fixo de iterações e retorna o histórico.
    Útil para as questões 2, 3, 4, 5 e 6.
    """
    p = p0
    historico = []
    for i in range(1, num_iters + 1):
        try:
            p_next = g(p)
            # Checagem para evitar números complexos indesejados em raízes pares
            if isinstance(p_next, complex):
                historico.append(f"Erro na iteração {i}: Gerou número complexo.")
                break
            historico.append(p_next)
            p = p_next
        except ZeroDivisionError:
            historico.append(f"Erro na iteração {i}: Divisão por zero.")
            break
        except Exception as e:
            historico.append(f"Erro na iteração {i}: {e}")
            break
    return historico

def ponto_fixo_tolerancia(g, p0, tol=1e-2, max_iter=100):
    """
    Encontra o ponto fixo dada uma tolerância.
    Útil para as questões 7 a 12.
    """
    p = p0
    for i in range(1, max_iter + 1):
        p_next = g(p)
        if abs(p_next - p) < tol:
            return p_next, i
        p = p_next
    return p, max_iter

print("="*50)
print("RESOLUÇÃO DA ATIVIDADE II - PONTO FIXO")
print("="*50)

#  Questão 1 e 2 
# A questão 1 é de dedução algébrica (fazer no papel isolando o x).
# A questão 2 pede 4 iterações com p0 = 1.
print("\n--- Questão 2 ---")
p0_2 = 1.0
g1_q2 = lambda x: (3 + x - 2*x**2)**0.25 if (3 + x - 2*x**2) >= 0 else complex(-1, 1)
g2_q2 = lambda x: ((x + 3 - x**4) / 2)**0.5 if ((x + 3 - x**4) / 2) >= 0 else complex(-1, 1)
g3_q2 = lambda x: ((x + 3) / (x**2 + 2))**0.5
g4_q2 = lambda x: (3*x**4 + 2*x**2 + 3) / (4*x**3 + 4*x - 1)

print(f"a) g1: {iteracao_ponto_fixo(g1_q2, p0_2)}")
print(f"   g2: {iteracao_ponto_fixo(g2_q2, p0_2)}")
print(f"   g3: {iteracao_ponto_fixo(g3_q2, p0_2)}")
print(f"   g4: {iteracao_ponto_fixo(g4_q2, p0_2)}")
print("b) A função g4 converge muito mais rápido para a raiz (p ≈ 1.124).")

# Questão 3 
print("\n--- Questão 3 ---")
p0_3 = 0.5
g_3a = lambda x: 0.5 * (x**3 + 1)
g_3b = lambda x: (2/x) - (1/x**2)
g_3c = lambda x: np.sqrt(2 - 1/x) if (2 - 1/x) >= 0 else complex(-1, 1)
# Usando np.cbrt para calcular raiz cúbica de números negativos corretamente
g_3d = lambda x: -np.cbrt(1 - 2*x) 

print(f"a) {iteracao_ponto_fixo(g_3a, p0_3)}")
print(f"b) {iteracao_ponto_fixo(g_3b, p0_3)}")
print(f"c) {iteracao_ponto_fixo(g_3c, p0_3)}")
print(f"d) {iteracao_ponto_fixo(g_3d, p0_3)}")
print("Os métodos (a) e (d) parecem adequados no início, mas o método (c) quebra por raiz negativa e o (b) diverge.")

#  Questão 4 
print("\n--- Questão 4 ---")
p0_4 = 1.0
g_4a = lambda x: np.sqrt((2 - x**4)/3) if ((2 - x**4)/3) >= 0 else complex(-1,1)
g_4b = lambda x: (2 - 3*x**2)**0.25 if (2 - 3*x**2) >= 0 else complex(-1,1)
g_4c = lambda x: (2 - x**4) / (3*x)
g_4d = lambda x: np.cbrt((2 - 3*x**2)/x)

print(f"a) {iteracao_ponto_fixo(g_4a, p0_4)}")
print(f"b) {iteracao_ponto_fixo(g_4b, p0_4)}")
print(f"c) {iteracao_ponto_fixo(g_4c, p0_4)}")
print(f"d) {iteracao_ponto_fixo(g_4d, p0_4)}")

#  Questão 5 e 6 
print("\n--- Questão 5 e 6 ---")
print("Para as questões 5 e 6, calcularemos as iterações para analisar a convergência.")
p0_5 = 1.0
g_5a = lambda x: (20*x + 21/x**2) / 21
g_5b = lambda x: x - (x**3 - 21) / (3*x**2) # Fórmula de Newton (muito rápida)
g_5c = lambda x: x - (x**4 - 21*x) / (x**3 - 21)
g_5d = lambda x: np.sqrt(21/x)

print("Q5 (Cálculo de 21^(1/3)):")
print(f"a) {iteracao_ponto_fixo(g_5a, p0_5)}")
print(f"b) {iteracao_ponto_fixo(g_5b, p0_5)} -> Mais rápida (Newton)")
print(f"c) {iteracao_ponto_fixo(g_5c, p0_5)}")
print(f"d) {iteracao_ponto_fixo(g_5d, p0_5)}")

p0_6 = 1.0
g_6a = lambda x: x * (1 + (7 - x**5)/x**2)**3
g_6b = lambda x: x - (x**5 - 7)/x**2
g_6c = lambda x: x - (x**5 - 7)/(5*x**4) # Fórmula de Newton (muito rápida)
g_6d = lambda x: x - (x**5 - 7)/12

print("\nQ6 (Cálculo de 7^(1/5)):")
print(f"a) {iteracao_ponto_fixo(g_6a, p0_6)}")
print(f"b) {iteracao_ponto_fixo(g_6b, p0_6)}")
print(f"c) {iteracao_ponto_fixo(g_6c, p0_6)} -> Mais rápida (Newton)")
print(f"d) {iteracao_ponto_fixo(g_6d, p0_6)}")

#  Questão 7 e 8 
print("\n--- Questões 7 e 8 ---")
# Q7: x^4 - 3x^2 - 3 = 0 -> isolando x: x = (3x^2 + 3)^(1/4)
g_7 = lambda x: (3*x**2 + 3)**0.25
raiz7, iters7 = ponto_fixo_tolerancia(g_7, 1.0, tol=1e-2)
print(f"Q7) Raiz: {raiz7:.4f} (Iterações: {iters7})")

# Q8: x^3 - x - 1 = 0 -> isolando x: x = (x + 1)^(1/3)
g_8 = lambda x: np.cbrt(x + 1)
raiz8, iters8 = ponto_fixo_tolerancia(g_8, 1.0, tol=1e-2)
print(f"Q8) Raiz: {raiz8:.4f} (Iterações: {iters8})")

#  Questão 9 e 10 
print("\n--- Questões 9 e 10 ---")
g_9 = lambda x: x + 0.5 * np.sin(x / 2)
raiz9, iters9 = ponto_fixo_tolerancia(g_9, 1.0, tol=1e-2) # Chute inicial = 1
print(f"Q9) Raiz aprox: {raiz9:.4f} em {iters9} iterações. (Cálculo teórico de k feito no papel).")

g_10 = lambda x: 2**(-x)
raiz10, iters10 = ponto_fixo_tolerancia(g_10, 1.0, tol=1e-4) # Chute inicial = 1
print(f"Q10) Raiz aprox: {raiz10:.5f} em {iters10} iterações.")

#  Questão 11 e 12 
print("\n--- Questões 11 e 12 ---")
# Para garantir convergência, usamos a função de iteração baseada em Newton (p_n = x - f(x)/f'(x))
# Q11: f(x) = x^2 - 3 -> g(x) = x - (x^2 - 3)/(2x) = 0.5 * (x + 3/x)
g_11 = lambda x: 0.5 * (x + 3/x)
raiz11, iters11 = ponto_fixo_tolerancia(g_11, 1.5, tol=1e-4)
print(f"Q11) Aproximação de raiz de 3: {raiz11:.5f} (Iterações: {iters11})")

# Q12: f(x) = x^3 - 25 -> g(x) = x - (x^3 - 25)/(3x^2)
g_12 = lambda x: x - (x**3 - 25)/(3*x**2)
raiz12, iters12 = ponto_fixo_tolerancia(g_12, 2.5, tol=1e-4)
print(f"Q12) Aproximação de raiz cúbica de 25: {raiz12:.5f} (Iterações: {iters12})")