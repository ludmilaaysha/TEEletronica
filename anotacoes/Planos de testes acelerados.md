É preciso ter controle sobre a confiabilidade dos produtos que se oferece para que os custos de garantia, por exemplo, não sejam prejudiciais para a empresa.

**Livro Acelerated Testings**

## HALT (High Accelerated Life Testing)
- Tabela FMEA: lista cada tipo de falha que um problema pode ter
	- Visa a identificar modos de falhas do produto
	- Para cada modo listado, há parâmetro como criticidade, unidades envolvidas na variável, valores que indicam a falha, probabilidade de ocorrência da falha, capacidade de observação da falha e como se desenvolve o sistema para evitar a falha
- Parâmetro de vida (horas, concentração química, etc)
- Quanto maior a vida útil, maior a qualidade do produto
- Visa uma única falha por vez

Confiabilidade: $R(t_0) = \int_{t_0}^\infty f(x) \, dx$, em que $f(x)$ é baseada na exponencial $(\theta)$ e na função Weibull $(p, \theta)$

Método da máxima verossimilhança é possível ser aplicado com a Weibull para chegar à densidade de probabilidade (visto no capítulo 4 do livro recomendado pelo professor)

### Técnicas de desenvolvimento
- Desenvolvimento por desempenho: desenvolver um produto para melhorá-lo cada vez mais. Nesse grupo, a falha não é bem-vinda
- Pró-falha: pensa que, para mitigar falhas, é preciso falhar muitas vezes, pois assim se conhece o modo de falha e maneiras de evitá-la.
	- Ex.: uso de cooler para reduzir de forma externa o aumento de temperatura da placa
		- Foram feitos diversos testes para concluir que o aumento de temperatura afetava no funcionamento da máquina e foi feita uma análise de custo-benefício para concluir que seria melhor incluir um dispositivo de resfriamento, e não mudar os materiais

- Para controlar se aquela falha foi eliminada, é analisado o parâmetro de confiabilidade na vida útil $R(t_0)$

O objetivo do teste acelerado é fazer o teste mais confiável possível da forma mais rápida possível.
- Por exemplo, se se quer testar a vida útil de um teste por 100h, é possível realizar os testes em 20h aumentando carga, pressão, etc, para garantir que a mesma falha está sendo vista.

## HASS (High Accelerated Scream Scenario)
Aumento agressivo da carga e condição de operação
- Ex.: deixar um caminhão rodando sem parar, com carga e velocidade controlados para entender a velocidade de degradação do veículo
❗Pesquisar sobre HASS relacionado à indústria de Software (o que seria similar a esse teste na indústria)

- Esse teste visa a entender quais são as falhas, quais, quando ocorrem e como.
- Pode complementar o HALT

### 📖Leituras
Accelerated Testing: capítulo 1, capítulo 2

## Confiabilidade
- Quando se tem um processo, para o qual se tem entradas e saídas, no CEP se analisa as saídas em amostras.
- Em testes, esse processo são os testes, e as saídas determinam a vida útil do produto
- Os itens são colocados em condição de operação durante aquele tempo determinado para mensurar sua vida útil.

#### Weibull
A função de confiabilidade Weibull é dada por $R(t) = e^{-(t/\theta)^{\beta}}$
Se a análise da confiabilidade com a função Weibull para o tempo $t_0$ for maior ou igual a 0,95, então a confiabilidade é ideal

#### Demonstração da Confiabilidade
Pode ser feita com base nas amostras que se obtém. O livro apresenta alguns métodos dessa demonstração
- Bogey Testing (falha 0)
- Bayesian Testing (falha 0)
- Bayesian Testing (falha permitida)

- Podem ser testados os itens antes de serem vendidos, mas sua vida útil é testada sem que o item seja quebrado. Este é um teste de demonstração.
- Se um item falha, não se trabalha mais com falha 0, e sim com permissão de falhas. Se esse item é descartado, é quebrado o princípio de aleatoriedade da amostra, o que não pode acontecer.

#### Critérios do teste de demonstração de confiabilidade
- $T$: Tempo do teste
- Critério de falha
	- um item foi testado por 100h e falhou na hora 101, ele passou no teste, pois dentro daquele critério ele passou no teste
- $n$: Quantidade de itens
- $r$: Permissão de falhas

### Bogey Testing
Utiliza o HALT, que é utilizado para reduzir o modo de falha
###### Requisitos
- Distribuição binomial: falha ou sucesso. O item passou ou não passou no teste.
- $t > T$: tempo de vida tem que ser maior que o tempo do teste
- $T = t_0$: tempo de vida tem que ser igual ao tempo de teste

**Distribuição binomial**
$$p(x, n, p) = \binom{n}{x}p^{x}(1-p)^{n-x}$$
em que:
- $p$: probabilidade de sucesso
- $n$: quantidade de itens
- $x$: quantidade de sucessos

![[Pasted image 20250117134416.png]]

Por exemplo, para definir o vendedor do produto em um workshop, deve-se analisar a probabilidade de sucesso de cada vendedor

Supondo um teste com n itens, são permitidas, inicialmente, 0 falhas. Nesse caso, $x=n$, pois supõe-se que todos os itens têm sucesso
$$p(x,n,p)=p(x,n,R(t_0))=R^{n}(t_0)$$
em que 
- $p(x,n,p)$ é a probabilidade de sucesso no teste ($\alpha$) 
- $R^{n}(t_0)$ é a confiabilidade do item
- $n$ é a qtd de itens

Geramos, através disso, a quantidade de itens que se precisa para realização do teste e garantir a taxa de confiabilidade para determinada produção
$$n = \frac{ln(\alpha)}{lnR(t_0)}$$
em que:
- $\alpha = R(t_0)$
- $ln \alpha = n ln(R(t_0))$

**Ex.: quantidade de itens para teste de para-brisas para demonstrar 99% de confiabilidade com confidência de 2 milhões de ciclos de operação. Quantos motores devem ser testados para 2 mil ciclos sem falha para atender a esses requisitos?**
$$\frac{ln(1-0.9)}{ln0.99} = 229.1$$
Como atestar a confiabilidade para 2 milhões de ciclos testando 500 ciclos, por exemplo?

área de confidência e área de segurança na distribuição normal?

❗Pesquisar o equivalente ao "Bogey Test" na indústria de software


#
29/01/2025

#### Relembrando:
## Bogey Testing
$n = \frac{ln(\alpha)}{lnR}$
em que 
- $n$ é a quantidade de itens
- $\alpha$ é o fator de segurança
- $R$ é a confiabilidade a ser demonstrada

## Bayesian Testing
- Adoção de uma f.d.p. $Weibol(\beta, \theta)$
- Adotar: $\beta$

$$R(t) = e^{-(\frac{t}{\theta})^\beta}$$
$$ln(R(t)) = -\Big(\frac{t}{\theta}\Big)^\beta$$
$$\Big[-ln(R(t))\Big]^{\frac{1}{\beta}} = \frac{t}{\theta}$$
$$R(t_0) = 0,95\%$$
$$\theta = \Bigg[\frac{t_0^{\beta}}{\big[-ln(R(t_0))\big]}\Bigg]^{1/\beta}$$
$$t = t_0\Big[\frac{n_\beta}{n}\Big]^{1/\beta}$$
$$t/t_0=\Big(\frac{n_\beta}{n}\Big)^{1/\beta}$$
$$n/n_\beta=\Big(\frac{t_0}{t}\Big)^{\beta}$$
Se, durante um teste falha zero e, no meio do teste, o item falha, há algumas opções
1. Retornar o item ao desenvolvimento
2. Solicitar nova amostra de $n$ itens com uma nova bancada rodando como se fosse o mesmo teste, respeitando as mesmas condições, aleatoriedade e tempo. Porém, a amostra inicial passa a compreender a nova quantidade de itens também.
3. Continuar com a mesma amostra inicial e aceita a falha. Contudo, isso tem um risco muito alto. Para isso precisa acreditar muito no seu produto e projeto e admitir que a falha ocorreu por um infortúnio.

⚠️Método da máxima verossimilhança?

### Teste com falha permitida

#### Weibol
$$\theta = \Bigg[\frac{2\sum_{i=1}^{\hat{}
} t_i^\beta}{X^{2}_{\alpha,d}}\Bigg]$$
$$\hat{\theta}$$

### Resolver problema p/ sexta-feira 31/01
Um custo envolve tanto o custo das horas-máquina (T: pondera sobre o tempo) quanto o preço do item (n: quantidade de amostras)
$C_m = T . C_H + n . C_I$

Desejamos saber qual o valor ótimo de $n$