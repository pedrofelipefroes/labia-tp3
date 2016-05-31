**CENTRO FEDERAL DE EDUCAÇÃO TECNOLÓGICA DE MINAS GERAIS**

**ENGENHARIA DE COMPUTAÇÃO**

**LABORATÓRIO DE INTELIGÊNCIA ARTIFICIAL**

**Prof. Flávio Cruzeiro**

**2016-1**

#### TP3: Algoritmo Genético Aplicado ao Problema do Passeio do Cavalo
**por Pedro Felipe Froes e Saulo Antunes**

======

O problema do passeio do cavalo consiste em codificar um algoritmo que encontre um caminho em um tabuleiro de xadrez pelo qual a peça do Cavalo passe por todas as suas casas, passando apenas uma única vez por cada uma delas. No xadrez, o Cavalo faz um movimento em _L_ a partir de sua posição inicial, pulando sobre quaisquer outras pessoas até o final do movimento.

Uma maneira recorrente para a solução do problema do Cavalo é a utilização de algoritmos de força bruta, através de _backtracking_. Existem aproximadamente 4x10<sup>51</sup> sequências de movimentos possíveis em um tabuleiro 8x8, porém esses algoritmos tornam-se ineficientes à medida que o tamanho do tabuleiro aumenta.

Para tentar resolver o problema, será implementado um algoritmo genético contemplando as operações de cruzamento, mutação e seleção a fim de gerar populações até encontrar uma solução adequada. Serão apresentados comparativos em relação ao número de casas do tabuleiro e o 

##### Codificação do problema

Falar sobre como a população foi codificada, sobre as operações de cross e de mutação, sobre a função objetivo (qtidade de movimentos)

##### Resultados

Colar resultados para as populações de diferentes tamanhos

##### Análise

Analisar com o gráfico, desvio padrão, média, falar sobre o crescimento exponencial

##### Conclusão

Falar sobre o quão randômico é

##### Referências

Referências aqui