
Repositório criado para entregar as nossas resoluções das listas de Complementos de Cálculo Numérico (Prof. Marcos Henrique).

(Wanderson Walisson Tavares dos Santos / Sylmara Alves do Nascimento

Todo o código foi feito em Python, com a ideia de criar funções genéricas para reaproveitar nos exercícios das listas em vez de copiar e colar código repetido.

## Estrutura dos Arquivos

* **resolucao_lista1.py**: Exercícios sobre o Método da Bisseção. O script resolve as raízes e também gera os gráficos pedidos nas questões 7 a 10.
* **resolucao_lista2.py**: Exercícios sobre Iteração de Ponto Fixo. Implementei blocos de "try/except" para mostrar exatamente quais funções $g(x)$ falham (por divisão por zero ou raiz negativa) e quais chegam na raiz.
* **resolucao_lista3.py**: Implementação dos métodos de Newton, Secante e Falsa Posição.

## Dependências (Como rodar)

Para rodar os scripts, usei o padrão do mercado para matemática em Python: `numpy` (para lidar com raízes, logaritmos e trigonometria) e `matplotlib` (para plotar os gráficos). 

Se o senhor precisar instalar no seu PC, é só rodar:
`pip install numpy matplotlib`

Depois, basta executar os arquivos no terminal, por exemplo:
`python resolucao_lista1.py`

## Respostas Teóricas e Justificativas

As demonstrações algébricas maiores (como a Questão 1 e 9 da Lista 2) eu fiz no papel/caderno para facilitar o desenvolvimento matemático. Abaixo estão as justificativas teóricas e análises pedidas na Lista 3, baseadas no comportamento dos scripts:

**Lista 3 - Questão 2: Poderíamos utilizar p0 = 0?**
Não tem como. A fórmula de Newton divide o valor pela derivada da função. Como $f(x) = -x^3 - \cos(x)$, a nossa derivada é $f'(x) = -3x^2 + \sin(x)$. Se a gente tentar rodar com $p_0 = 0$, a derivada dá exatamente zero, gerando um erro de divisão por zero logo na primeira iteração do laço.

**Lista 3 - Questão 3: Qual método chegou mais perto de raiz de 6?**
O método da Secante teve um desempenho melhor e mais rápido. O método da Falsa Posição é seguro porque a raiz fica presa no intervalo, mas para essa função específica ele foi mais lento porque um dos limites do intervalo "estacionou".

**Lista 3 - Questão 9c: Aproximação inicial para o enésimo menor zero**
Observando a função $f(x) = \ln(x^2+1) - e^{0.4x}\cos(\pi x)$, dá pra notar que a exponencial $e^{0.4x}$ cresce muito rápido. Para a função inteira dar zero, o $\cos(\pi x)$ precisa ser muito próximo de zero. O cosseno zera em $\pi/2$, $3\pi/2$, $5\pi/2$ (ou seja, quando $x$ é $0.5$, $1.5$, $2.5$...). Logo, o melhor chute inicial para o enésimo zero é usar a regra $p_0 = n - 0.5$.

**Lista 3 - Questão 10: Por que o resultado não parece normal pro método de Newton?**
O método de Newton é conhecido por ser muito rápido (convergência quadrática). Só que rodando o script dessa questão, ele precisou de muitas iterações para chegar na precisão de $10^{-5}$. Isso acontece porque estamos lidando com uma raiz múltipla (o gráfico da função "raspa" no eixo x). Em raízes múltiplas, a derivada tende a zero junto com a função, o que estraga a velocidade do Newton e faz ele ficar lento (convergência linear).
