<dl>
<p><strong>
CENTRO FEDERAL DE EDUCAÇÃO TECNOLÓGICA DE MINAS GERAIS<br>
ENGENHARIA DE COMPUTAÇÃO<br>
LABORATÓRIO DE INTELIGÊNCIA ARTIFICIAL<br>
Prof. Flávio Cruzeiro<br>

<p>2016-1</p>
</strong></p>
</dl>

### TP3: Algoritmo Genético aplicado ao problema do Passeio do Cavalo
**por Pedro Felipe Froes e Saulo Antunes**

---

O problema do Passeio do Cavalo consiste em codificar um algoritmo que encontre um caminho em um tabuleiro de xadrez pelo qual a peça do Cavalo passe por todas as suas casas, passando apenas uma única vez por cada uma delas. No xadrez, o Cavalo faz um movimento em _L_ a partir de sua posição inicial, pulando sobre quaisquer outras pessoas até o final do movimento.

Uma maneira recorrente para a solução do problema do Cavalo é a utilização de algoritmos de força bruta, através de _backtracking_. Existem aproximadamente 4x10<sup>51</sup> sequências de movimentos possíveis em um tabuleiro 8x8, porém esses algoritmos tornam-se ineficientes à medida que o tamanho do tabuleiro aumenta.

Para tentar resolver o problema, foi implementado um Algoritmo Genético contemplando as operações de pareamento, cruzamento, mutação e seleção através de uma função objetivo a fim de gerar populações até encontrar uma solução adequada. Posteriormente, foram feitas análises de resultados para diversos tamanhos de tabuleiros (5x5, 8x8, 16x16, etc.), considerando os valores da melhor e pior solução de cada geração, além mostrar a média e o desvio padrão para 30 execuções.

#### Codificação do problema

O algoritmo foi construído em cima de três parâmetros principais: o número de gerações (determina a quantidade de vezes que o algoritmo será executado), o tamanho da população (número de indíviduos a cada população) e o tamanho do tabuleiro. Cada indivíduo foi codificado na forma de um `Game`, cujos atributos são:
* `moves`, a quantidade de movimentos realizada até o momento;
* `path`, o caminho do indivíduo pelo tabuleiro;
* `table`, cria um tabuleiro de prioridade de movimentos;
* `position`, sua posição inicial;
* `table[x][y]`, sua tabela de posições visitadas no tabuleiro.

Um dos princípais atributos do indivíduo é seu tabuleiro de prioridade de movimentos. Cada indvíduo possui um tabuleiro com tamanho equivalente ao tabuleiro do problema, onde cada casa possui um valor de prioridade randômico definido entre 0 e 10. Para escolher qual será sua próxima casa a ser visitada, o indivíduo seleciona primeiramente aquelas cujo movimento é válido (ou seja, correspondem ao _L_ do Cavalo), e posteriormente a casa de maior prioridade analisada primeiro. Ambas decisões são realizadas através dos métodos `nextMoves` e `getBestMove`, respectivamente.

![Escolha do movimento do Cavalo](img/makemove.png)

_Figura 1: Escolha do movimento do Cavalo._

A figura acima exemplifica o processo de decisão do próximo movimento de um indivíduo, mostrando seu tabuleiro de prioridades. No tabuleiro da esquerda, o Cavalo se encontra inicialmente na posição `(0,0)` (em verde), e os movimentos possíveis obtidos através do `nextMoves` são representados em laranja. Cabe ao `getBestMove` analisar qual a casa de maior prioridade dentre as selecionadas previamente - no caso, a posição `(3,2)` é selecionada, e a quantidade de movimentos `moves` é incrementada em 1. Na figura da direita, o Cavalo encontra-se na posição seguinte (em verde), e as possíveis posições são mostradas também em laranja. É válido reparar que sua posição anterior, `(0,0)`, não é um movimento possível, pois está já presente na tabela de posições visitadas pelo indivíduo.

O processo descrito no parágrafo acima é implementado no método `play`, e executado até o indíviduo não obter nenhum movimento possível em sua lista de `nextMoves`, parando de incrementar `moves`. Entretanto, esse processo é influenciado pelas operações inerentes aos Algoritmos Genéticos: seleção, pareamento, _crossover_ e mutação, descritas a seguir.

###### Implementação do Algoritmo Genético

Com o processo de decisão de movimentos codificado, é possível iniciar, de fato, a implementação do Algoritmo Genético para a resolução do problema. Para exemplificar como foi realizada sua codificação, será descrito todo o processo de uma iteração do algoritmo para uma população de tamanho 30.

Inicialmente, 30 indíviduos são gerados, cada um com um tabuleiro de prioridades gerado de maneira aleatória. Cada indivíduo executa um jogo (método `play`), e ao final de cada jogo, o número de movimentos alcançados é armazenado na variável `moves` de cada um deles.

A operação de **seleção** é implementada no método `getBestGame` e verificará qual indivíduo possui o maior valor de `moves` dentre os 30. Ou seja, a **função objetivo** desse algoritmo é baseada em qual indivíduo consegue realizar o maior caminho pelo tabuleiro. Para fins de análise de resultados, há também um método que, diferentemente do anterior, armazena o pior jogo.

O **pareamento** é então aplicado à população, de modo que o indivíduo 1 é pareado com o 15, o 2 com 16, o 3 com 17, e assim por diante até parear o indivíduo 14 com o 30. Agora pareados, ocorre a operação de **_crossover_**, mostrada na figura a seguir.

![Crossover](img/crossover.png)

_Figura 2: Operação de_ crossover_._

O _crossover_ dos indivíduos a direita gera outros dois indivíduos _filhos_ a esquerda, ambos possuindo características mescladas dos seus _pais_. A operação de _crossver_ se dá mesclando o tabuleiro de prioridades de ambos indivíduos, gerando assim dois novos indivíduos com dois novos tabuleiros de prioridade. Ao final dessa etapa, a população será dobrada.

A **mutação** tem uma chance aleatória de ocorrer sobre os indivíduos da população. O indivíduo afetado por ela tem algum valor de seu tabuleiro de prioridade alterado randomicamente, conforme mostrado na figura abaixo.

![Mutação](img/mutation.png)
_Figura 3: Operação de mutação_

Na Figura 3, a posição `(4,4)` do tabuleiro de prioridades de um indivíduo é selecionada aleatoriamente, e tem seu valor alterado de 7 para 1 também de forma aleatória.

Após todas as operações anteriores, dos 60 indivíduos da população, 30 são selecionados de forma aleatória, formando uma nova população. Entretanto, foi decidido aplicar o elitismo e garantiu-se que o melhor jogo da população anterior esteja presente na nova população. Portanto, o indivíduo oriundo do método `getBestGame` estará presente na próxima iteração do algoritmo.

O algoritmo vai iterar até um número de gerações previamente determinado. Em sua última geração, o problema pode ou não ter sido resolvido, mostrando o melhor e pior indivíduo de cada população.

#### Análise dos resultados

O algoritmo pode ser executado considerando diferentes números de gerações, tamanhos de tabuleiros e populações. Inicialmente, considerou-se o número de gerações como 30, e executou-se o algoritmo em um tabuleiro 8x8, obtendo o resultado a seguir:

![Passeio do Cavalo em um tabuleiro 8x8](img/data1.png)

_Figura 4: Aplicação do algoritmo em um tabuleiro 8x8, com os melhores indivíduos em roxo e os piores em azul._

Através do resultado acima, pode-se perceber algumas características do algoritmo:
* Para essa execução do algoritmo, ele não consegue encontrar uma solução para o problema, porém chega próximo a uma com um indivíduo com 62 movimentos.
* Apesar de não encontrar a solução, é perceptível que a população tende a melhorar a cada geração. Enquanto os valores dos melhores jogos só aumentam, os valores dos piores tem um comportamento mais variável. Isso se deve à habilidade dos piores indivíduos da geração `n` de poderem ir para a geração `n+1`, além de não haver garantia que as operações de _crossover_ e mutação sempre gerem indivíduos melhores que na geração anterior. Entrentanto, é perceptível que ainda há uma leve tendência de melhora nos piores indivíduos, com a primeira geração tendo um `worstGame` de 13, e a trigésima de 26.
* A melhora dos melhores indivíduos ocorre de maneira quase exponencial: no começo do algoritmo há uma taxa de melhoria mais rápida do valor de `bestGame`, que vai diminuindo até a última geração.

Três fatores são determinantes na análise do sucesso do algoritmo: o número de gerações, o tamanho da população e a randomicidade de cada execução. Para um tabuleiro 8x8, 30 mostrou-se um valor pequeno como número de gerações quanto para o tamanho de uma população. Além disso, executando o algoritmo novamente, a resposta será diferente da representada anteriormente. De fato, a cada execução, a chance de que as resposta do algoritmo seja equivalente à anterior é mínima, dado que os tabuleiros de prioridades para cada indivíduo, bem como as operações de mutação, têm natureza aleatória. Portanto, aumentando o número de indvíduos e de gerações, aumenta-se também a chance de que um dos indivíduos contribua aleatoriamente para encontrar a solução do problema.

A seguir, foram executado 30 vezes o algoritmo ainda para o tabuleiro 8x8, com cada execução considerando 30 gerações e aumentando a população para 60 indivíduos. Uma análise gráfica das 30 execuções é mostrada a seguir, com o melhor e pior jogo da trigésima execução para cada uma das 30 execuções sendo comparados.

![30 execuções para um tabuleiro 8x8 e população 60](img/data2.png)

_Figura 5: 30 execuções em um tabuleiro 8x8, melhor e pior jogo de cada execução são mostrados em roxo e azul, respectivamente._



Colar resultados para as populações de diferentes tamanhos

#### Análise

Analisar com o gráfico, desvio padrão, média, falar sobre o crescimento exponencial

#### Conclusão

Falar sobre o quão randômico é

#### Referências

* [Passeio do Cavalo na Wikipedia](https://en.wikipedia.org/wiki/Knight%27s_tour "Knight's Tour")
* [Artigo sobre a aplicação do Algoritmo Genético no problema do Passeio do Cavalo](http://citeseerx.ist.psu.edu/viewdoc/download?rep=rep1&type=pdf&doi=10.1.1.115.3709)
