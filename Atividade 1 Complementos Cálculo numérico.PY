import numpy as np
import matplotlib.pyplot as plt


# Disciplina: Complementos de Cálculo Numérico
# Professor: Marcos Henrique
# Alunos: Wanderson Walisson Tavares dos Santos / Sylmara ALves do Nascimento
# Atividade I 


def bissecao(f, a, b, tol=1e-4, max_iter=100, return_p3=False):
    """
    Função genérica para o Método da Bisseção.
    Retorna a raiz aproximada ou a iteração p3 se solicitado.
    """
    if f(a) * f(b) > 0:
        return "Erro: f(a) e f(b) têm o mesmo sinal (não há garantia de raiz no intervalo)."
    
    p = a
    for i in range(1, max_iter + 1):
        p = (a + b) / 2.0
        
        # Parada específica para a Questão 2
        if return_p3 and i == 3:
            return p
            
        # Critério de parada: raiz exata encontrada ou tolerância atingida
        if f(p) == 0 or (b - a) / 2.0 < tol:
            return p
            
        if f(a) * f(p) > 0:
            a = p
        else:
            b = p
            
    return p

print("="*50)
print("RESOLUÇÃO DA ATIVIDADE I - CÁLCULO NUMÉRICO")
print("="*50)

# --- Questão 1 ---
print("\n--- Questão 1 ---")
f1 = lambda x: np.sqrt(x) - np.cos(x)
# Tolerância não informada, assumindo 10^-4
print(f"Raiz em [0, 1]: {bissecao(f1, 0, 1):.5f}")

# --- Questão 2 ---
print("\n--- Questão 2 ---")
f2 = lambda x: 3 * (x + 1) * (x - 0.5) * (x - 1)
print(f"a) p3 em [-2, 1.5]: {bissecao(f2, -2, 1.5, return_p3=True)}")
print(f"b) p3 em [-1.25, 2.5]: {bissecao(f2, -1.25, 2.5, return_p3=True)}")

# --- Questão 3 ---
print("\n--- Questão 3 ---")
f3 = lambda x: x**3 - 7*x**2 + 14*x - 6
tol3 = 1e-2
print(f"a) Raiz em [0, 1]: {bissecao(f3, 0, 1, tol=tol3):.5f}")
print(f"b) Raiz em [1, 3.2]: {bissecao(f3, 1, 3.2, tol=tol3):.5f}")
print(f"c) Raiz em [3.2, 4]: {bissecao(f3, 3.2, 4, tol=tol3):.5f}")

# --- Questão 4 ---
print("\n--- Questão 4 ---")
f4 = lambda x: x**4 - 2*x**3 - 4*x**2 + 4*x + 4
tol4 = 1e-2
print(f"a) Raiz em [-2, -1]: {bissecao(f4, -2, -1, tol=tol4):.5f}")
print(f"b) Raiz em [0, 2]: {bissecao(f4, 0, 2, tol=tol4):.5f}")
print(f"c) Raiz em [2, 3]: {bissecao(f4, 2, 3, tol=tol4):.5f}")
print(f"d) Raiz em [-1, 0]: {bissecao(f4, -1, 0, tol=tol4):.5f}")

# --- Questão 5 ---
print("\n--- Questão 5 ---")
# Tolerâncias não informadas, assumindo 10^-4
f5a = lambda x: x - 2**(-x)
f5b = lambda x: np.exp(x) - x**2 + 3*x - 2
f5c = lambda x: 2*x*np.cos(2*x) - (x + 1)**2
f5d = lambda x: x*np.cos(x) - 2*x**2 + 3*x - 1

print(f"a) Raiz em [0, 1]: {bissecao(f5a, 0, 1):.5f}")
print(f"b) Raiz em [0, 1]: {bissecao(f5b, 0, 1):.5f}")
print(f"c) Raiz em [-3, -2]: {bissecao(f5c, -3, -2):.5f}")
print(f"c) Raiz em [-1, 0]: {bissecao(f5c, -1, 0):.5f}")
print(f"d) Raiz em [0.2, 0.3]: {bissecao(f5d, 0.2, 0.3):.5f}")
print(f"d) Raiz em [1.2, 1.3]: {bissecao(f5d, 1.2, 1.3):.5f}")

# --- Questão 6 ---
print("\n--- Questão 6 ---")
tol6 = 1e-5
f6a = lambda x: 3*x - np.exp(x)
f6b = lambda x: 2*x + 3*np.cos(x) - np.exp(x)
f6c = lambda x: x**2 - 4*x + 4 - np.log(x)
f6d = lambda x: x + 1 - 2*np.sin(np.pi * x)

print(f"a) Raiz em [1, 2]: {bissecao(f6a, 1, 2, tol=tol6)}")
print(f"b) Raiz em [0, 1]: {bissecao(f6b, 0, 1, tol=tol6)}")
print(f"c) Raiz em [1, 2]: {bissecao(f6c, 1, 2, tol=tol6)}")
print(f"c) Raiz em [2, 4]: {bissecao(f6c, 2, 4, tol=tol6)}")
print(f"d) Raiz em [0, 0.5]: {bissecao(f6d, 0, 0.5, tol=tol6)}")
print(f"d) Raiz em [0.5, 1]: {bissecao(f6d, 0.5, 1, tol=tol6)}")


# Questões com Gráficos (7 a 10)

print("\n--- Questões 7 a 10 (Resultados e Gráficos) ---")
print("Feche a janela do gráfico atual para gerar o próximo e continuar a execução.")

# Questão 7
f7 = lambda x: x - 2*np.sin(x)
raiz7 = bissecao(f7, 1, 2, tol=1e-5) # O primeiro valor positivo está próximo a 1.9
print(f"Q7 b) Primeiro valor positivo de x: {raiz7}")

x_val = np.linspace(0, 3, 100)
plt.figure()
plt.plot(x_val, x_val, label='y = x')
plt.plot(x_val, 2*np.sin(x_val), label='y = 2*sen(x)')
plt.title('Questão 7')
plt.grid(True); plt.legend()
plt.show()

# Questão 8
f8 = lambda x: x - np.tan(x)
# O primeiro valor positivo onde x = tan(x) está entre 4.0 e 4.6 (aprox 4.49)
raiz8 = bissecao(f8, 4.0, 4.6, tol=1e-5)
print(f"Q8 b) Primeiro valor positivo de x: {raiz8}")

x_val = np.linspace(3, 5, 100)
plt.figure()
plt.plot(x_val, x_val, label='y = x')
plt.plot(x_val, np.tan(x_val), label='y = tan(x)')
plt.ylim(-10, 10) # Limitando o eixo y por causa da assíntota da tangente
plt.title('Questão 8')
plt.grid(True); plt.legend()
plt.show()

# Questão 9
f9 = lambda x: (np.exp(x) - 2) - np.cos(np.exp(x) - 2)
raiz9 = bissecao(f9, 0.5, 1.5, tol=1e-5)
print(f"Q9 b) Aproximação em [0.5, 1.5]: {raiz9}")

x_val = np.linspace(0.5, 1.5, 100)
plt.figure()
plt.plot(x_val, np.exp(x_val) - 2, label='y = e^x - 2')
plt.plot(x_val, np.cos(np.exp(x_val) - 2), label='y = cos(e^x - 2)')
plt.title('Questão 9')
plt.grid(True); plt.legend()
plt.show()

# Questão 10
f10 = lambda x: (x**2 - 1) - np.exp(1 - x**2)
raiz10 = bissecao(f10, -2, 0, tol=1e-3)
print(f"Q10 b) Aproximação em [-2, 0]: {raiz10}")

x_val = np.linspace(-2, 0, 100)
plt.figure()
plt.plot(x_val, x_val**2 - 1, label='y = x^2 - 1')
plt.plot(x_val, np.exp(1 - x_val**2), label='y = e^(1-x^2)')
plt.title('Questão 10')
plt.grid(True); plt.legend()
plt.show()

# --- Questão 11 e 12 ---
print("\n--- Questões 11 e 12 ---")
# Para descobrir para qual zero converge, basta aplicar o método aos intervalos
f11 = lambda x: (x + 2)*(x + 1)*x*((x - 1)**3)*(x - 2)
print("Questão 11 - Converge para as raízes:")
print(f"a) [-3, 1]: {bissecao(f11, -3, 1)}")
print(f"b) [-2.5, 3]: {bissecao(f11, -2.5, 3)}")
print(f"c) [-1.75, 1.5]: {bissecao(f11, -1.75, 1.5)}")
print(f"d) [-1.5, 1.75]: {bissecao(f11, -1.5, 1.75)}")

f12 = lambda x: (x + 2)*((x + 1)**2)*x*((x - 1)**3)*(x - 2)
print("\nQuestão 12 - Converge para as raízes:")
print(f"a) [-1.5, 2.5]: {bissecao(f12, -1.5, 2.5)}")
print(f"b) [-0.5, 2.4]: {bissecao(f12, -0.5, 2.4)}")
print(f"c) [-0.5, 3]: {bissecao(f12, -0.5, 3)}")
print(f"d) [-3, -0.5]: {bissecao(f12, -3, -0.5)}")

# --- Questão 13 e 14 ---
print("\n--- Questões 13 e 14 ---")
f13 = lambda x: x**3 - 25
# 2^3 = 8 e 3^3 = 27, logo a raiz está em [2, 3]
print(f"Questão 13: Aproximação de raiz cúbica de 25: {bissecao(f13, 2, 3, tol=1e-4):.5f}")

f14 = lambda x: x**2 - 3
# 1^2 = 1 e 2^2 = 4, logo a raiz está em [1, 2]
print(f"Questão 14: Aproximação de raiz quadrada de 3: {bissecao(f14, 1, 2, tol=1e-4):.5f}")