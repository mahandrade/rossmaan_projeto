# Rossmann Stores
A Rossmann opera mais de 3.000 drogarias em 7 países europeus. Atualmente, os gerentes de loja da Rossmann têm a tarefa de prever suas vendas diárias com até seis semanas de antecedência. As vendas da loja são influenciadas por muitos fatores, incluindo promoções, competição, feriados escolares e estaduais, sazonalidade e localidade. Com milhares de gerentes individuais prevendo vendas com base em suas circunstâncias únicas, a precisão dos resultados pode ser bastante variada. Nesse sentido, o CFO pede a previsão de todas as lojas de forma antecipe a venda em até 6 semanas.

#Business Assumptions
As seguintes suposições foram feitas sobre o problema de negócio:

    Para lojas que não tinham informação de CompetitionDistance, assumiu-se que a distancia seria 2 vezes maior que a maior distancia de um competidor mais próximo.
    Como foi assumido que existe competidor mesmo que muito longe, caso não haja a data em que o competidor abriu ou dados em relação aos periodos promocionais, trabalhase-se com a data da loja pensando na premissa que algumas variáveis derivadas do tempo são extremamente importantes para representar um comportamento.
    Os dados de Customers sendo difíceis prever foi descartado, podendo ser escopo para outro projeto complementar á este.
    Os dias em que as loja estavam fechadas foram descartados.
    Só foram consideradas entradas em que o valores de Sales fossem superiores a 0.
