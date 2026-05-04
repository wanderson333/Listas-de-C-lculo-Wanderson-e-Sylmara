import numpy as np

# Universidade Federal de Pernambuco (UFPE)
# Disciplina: Complementos de Cálculo Numérico
# Professor: Marcos Henrique
# Alunos: Wanderson Walisson Tavares dos Santos / Sylmara ALves do Nascimento
# Atividade 3

def newton(f, df, p0, tol=1e-4, max_iter=100, return_p2=False):
    p_prev = p0
    for i in range(1, max_iter + 1):
        deriv = df(p_prev)
        if deriv == 0:
            return f"Erro: Derivada nula na iteração {i}"
        
        p = p_prev - f(p_prev)/deriv
        
        if return_p2 and i == 2:
            return p
            
        if abs(p - p_prev) < tol:
            return p, i
            
        p_prev = p
    return p, max_iter

def secante(f, p0, p1, tol=1e-4, max_iter=100, return_p3=False):
    for i in range(2, max_iter + 2):
        if f(p1) - f(p0) == 0:
            return "Erro: Divisão por zero"
            
        p = p1 - f(p1) * (p1 - p0) / (f(p1) - f(p0))
        
        if return_p3 and i == 3:
            return p
            
        if abs(p - p1) < tol:
            return p
            
        p0 = p1
        p1 = p
    return p

def falsa_posicao(f, p0, p1, tol=1e-4, max_iter=100, return_p3=False):
    q0 = f(p0)
    q1 = f(p1)
    
    if q0 * q1 > 0:
        return "Erro: f(p0) e f(p1) devem ter sinais opostos"
        
    for i in range(2, max_iter + 2):
        p = p1 - q1 * (p1 - p0) / (q1 - q0)
        
        if return_p3 and i == 3:
            return p
            
        q = f(p)
        if abs(p - p1) < tol or q == 0:
            return p
            
        if q * q1 < 0:
            p0 = p1
            q0 = q1
        p1 = p
        q1 = q
    return p

print("Resolução da Atividade III")
print()

# Questão 1
print("Questão 1")
f1 = lambda x: x**2 - 6
df1 = lambda x: 2*x
print(f"p2 usando Newton: {newton(f1, df1, 1.0, return_p2=True)}")
print()

# Questão 2
print("Questão 2")
f2 = lambda x: -x**3 - np.cos(x)
df2 = lambda x: -3*x**2 + np.sin(x)
print(f"p2 usando Newton: {newton(f2, df2, -1.0, return_p2=True)}")
# Se p0 = 0, a derivada df2(0) = -3(0)^2 + sin(0) = 0. Divisão por zero!
print("Nota: Não podemos usar p0 = 0 pois f'(0) = 0, causando divisão por zero.")
print()

# Questão 3
print("Questão 3")
p3_sec = secante(f1, 3.0, 2.0, return_p3=True)
p3_fp = falsa_posicao(f1, 3.0, 2.0, return_p3=True)
raiz_6 = np.sqrt(6)
print(f"a) p3 (Secante): {p3_sec}")
print(f"b) p3 (Falsa Posição): {p3_fp}")
print(f"c) Valor real de raiz de 6: {raiz_6}")
melhor = "Secante" if abs(p3_sec - raiz_6) < abs(p3_fp - raiz_6) else "Falsa Posição"
print(f"O resultado mais próximo é o do método da {melhor}.")
print()

# Questão 4
print("Questão 4")
p3_sec_q4 = secante(f2, -1.0, 0.0, return_p3=True)
p3_fp_q4 = falsa_posicao(f2, -1.0, 0.0, return_p3=True)
print(f"a) p3 (Secante): {p3_sec_q4}")
print(f"b) p3 (Falsa Posição): {p3_fp_q4}")
print()

# Questão 5
print("Questão 5 (Tolerância 10^-4)")
f5a = lambda x: x**3 - 2*x**2 - 5
df5a = lambda x: 3*x**2 - 4*x
print(f"a) {newton(f5a, df5a, 2.5, tol=1e-4)[0]:.5f}") # Chute médio do intervalo [1,4]

f5b = lambda x: x**3 + 3*x**2 - 1
df5b = lambda x: 3*x**2 + 6*x
print(f"b) {newton(f5b, df5b, -2.5, tol=1e-4)[0]:.5f}")

f5c = lambda x: x - np.cos(x)
df5c = lambda x: 1 + np.sin(x)
print(f"c) {newton(f5c, df5c, 0.8, tol=1e-4)[0]:.5f}")

f5d = lambda x: x - 0.8 - 0.2*np.sin(x)
df5d = lambda x: 1 - 0.2*np.cos(x)
print(f"d) {newton(f5d, df5d, 0.8, tol=1e-4)[0]:.5f}")
print()

# Questão 6
print("Questão 6 (Tolerância 10^-5)")
# Letra A
f6a = lambda x: np.exp(x) + 2**(-x) + 2*np.cos(x) - 6
df6a = lambda x: np.exp(x) - (2**(-x))*np.log(2) - 2*np.sin(x)
print(f"a) {newton(f6a, df6a, 1.5, tol=1e-5)[0]:.6f}")

# Letra B
f6b = lambda x: np.log(x - 1) + np.cos(x - 1)
df6b = lambda x: 1/(x - 1) - np.sin(x - 1)
print(f"b) {newton(f6b, df6b, 1.5, tol=1e-5)[0]:.6f}")

# Letra C
f6c = lambda x: 2*x*np.cos(2*x) - (x - 2)**2
df6c = lambda x: 2*np.cos(2*x) - 4*x*np.sin(2*x) - 2*(x - 2)
print(f"c) Raiz em [2,3]: {newton(f6c, df6c, 2.5, tol=1e-5)[0]:.6f}")
print(f"c) Raiz em [3,4]: {newton(f6c, df6c, 3.5, tol=1e-5)[0]:.6f}")

# Letra D
f6d = lambda x: (x - 2)**2 - np.log(x)
df6d = lambda x: 2*(x - 2) - 1/x
print(f"d) Raiz em [1,2]: {newton(f6d, df6d, 1.5, tol=1e-5)[0]:.6f}")
print(f"d) Raiz em [e,4]: {newton(f6d, df6d, 3.0, tol=1e-5)[0]:.6f}")

# Letra E
f6e = lambda x: np.exp(x) - 3*x**2
df6e = lambda x: np.exp(x) - 6*x
print(f"e) Raiz em [0,1]: {newton(f6e, df6e, 0.5, tol=1e-5)[0]:.6f}")
print(f"e) Raiz em [3,5]: {newton(f6e, df6e, 4.0, tol=1e-5)[0]:.6f}")

# Letra F
f6f = lambda x: np.sin(x) - np.exp(-x)
df6f = lambda x: np.cos(x) + np.exp(-x)
print(f"f) Raiz em [0,1]: {newton(f6f, df6f, 0.5, tol=1e-5)[0]:.6f}")
print(f"f) Raiz em [3,4]: {newton(f6f, df6f, 3.5, tol=1e-5)[0]:.6f}")
print(f"f) Raiz em [6,7]: {newton(f6f, df6f, 6.5, tol=1e-5)[0]:.6f}")
print()

# Questão 7
print("Questão 7")
f7 = lambda x: 4*x**2 - np.exp(x) - np.exp(-x)
df7 = lambda x: 8*x - np.exp(x) + np.exp(-x)
chutes_q7 = [-10, -5, -3, -1, 0, 1, 3, 5, 10]
for p0 in chutes_q7:
    # Newton pode dar overflow com exponenciais grandes, usamos try-except
    try:
        raiz, iters = newton(f7, df7, p0, tol=1e-5)
        print(f"p0 = {p0:3d} -> Raiz: {raiz:.5f} (em {iters} iterações)")
    except OverflowError:
        print(f"p0 = {p0:3d} -> Erro: Overflow")
print()

# Questão 8
print("Questão 8")
f8 = lambda x: x**2 - 10*np.cos(x)
df8 = lambda x: 2*x + 10*np.sin(x)
chutes_q8 = [-100, -50, -25, 25, 50, 100]
for p0 in chutes_q8:
    raiz, iters = newton(f8, df8, p0, tol=1e-5)
    print(f"p0 = {p0:4d} -> Raiz: {raiz:.5f} (em {iters} iterações)")
print()

# Questão 9
print("Questão 9")
f9 = lambda x: np.log(x**2 + 1) - np.exp(0.4*x)*np.cos(np.pi * x)
df9 = lambda x: (2*x)/(x**2 + 1) - 0.4*np.exp(0.4*x)*np.cos(np.pi * x) + np.pi*np.exp(0.4*x)*np.sin(np.pi * x)

print(f"a) Único zero negativo: {newton(f9, df9, -0.5, tol=1e-6)[0]:.6f}")
print("b) 4 menores zeros positivos:")
for chute in [0.5, 1.5, 2.5, 3.5]:
    print(f"   {newton(f9, df9, chute, tol=1e-6)[0]:.6f}")
print("c) Aproximação razoável para o enésimo zero: p0 = n - 0.5")
print(f"d) 25º menor zero positivo (chute 24.5): {newton(f9, df9, 24.5, tol=1e-6)[0]:.6f}")
print()

# Questão 10
print("Questão 10")
f10 = lambda x: 0.5 + 0.25*x**2 - x*np.sin(x) - 0.5*np.cos(2*x)
df10 = lambda x: 0.5*x - (np.sin(x) + x*np.cos(x)) + np.sin(2*x)

p0_10a = np.pi / 2
raiz10a, iters10a = newton(f10, df10, p0_10a, tol=1e-5)
print(f"Para p0 = pi/2, Raiz: {raiz10a:.5f} (Iterações: {iters10a})")

p0_10b = 5 * np.pi
raiz10b, iters10b = newton(f10, df10, p0_10b, tol=1e-5)
print(f"Para p0 = 5pi, Raiz: {raiz10b:.5f} (Iterações: {iters10b})")

p0_10c = 10 * np.pi
raiz10c, iters10c = newton(f10, df10, p0_10c, tol=1e-5)
print(f"Para p0 = 10pi, Raiz: {raiz10c:.5f} (Iterações: {iters10c})")