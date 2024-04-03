# Case - Cancelamento de Clientes
![image](https://github.com/JadsonDS/cancelamento_clientes/blob/main/logo.jpg)


# 1. Problema de negócio
O CEO recém contratado de uma renomada empresa com mais de 800 mil clientes. Recentemente a empresa percebeu que da sua base total de clientes, a maioria são clientes inativos, ou seja, que já cancelaram o serviço.

Precisando melhorar seus resultados ela quer conseguir entender os principais motivos desses cancelamentos e quais as ações mais eficientes para reduzir esse número.
. Ele nos pediu então para criarmos um dashboard utilizando alguns dados históricos, onde o mesmo poderia acompanhar e responder algumas importantes questões para o negócio.

# 2. Premissas assumidas para a análise
  1. O objetivo é tratar essa base de dados, para que possamos analisar de forma eficiente e fazer algumas análises úteis para a empresa.     
  2. Sendo uma delas, cancelamentos e parâmetro. Verificar o motivo dos cancelamentos e tentar diminuir esse parâmetro.

# 3. Estratégia da solução
O painel estratégico foi desenvolvido utilizando as métricas que refletem as principais visões do modelo de negócio da empresa:

# 4. Principais insights  
Dos 800 mil clientes cadastrados na plataforma, A proporção de clientes que estão cancelando o serviço é de aproximadamente 56.71% das assinaturas. 

Em relação a duração do contrato temos uma divisão quase igual entre os planos anual 40,20% e trimestral 40,20%, mas o plano mensal já fica atrás com quase 20%, 
verificando as informações geral de cada plano é possível notar que os clientes do plano Mensal, possuem uma média de cancelamento igual a 1, ou seja, praticamente todos os clientes que utilizam esse plano fizeram o cancelamento do serviço.
Removendo o contrato mensal a proporção de cancelamento vai para 46,05%.

Verificando a informação geral de cada assinatura temos praticamente a mesma quantidade em cada uma das assinaturas, ou seja, temos praticamente 1/3 em cada assinatura.

Analizando os gráficos verificamos que Dias de Atraso e Ligações ao Call Center, representa que clientes com mais de 20 dias de atraso cancelam suas assinaturas e que clientes com mais de 20 dias de atraso cancelam suas assinaturas.
Analisando apenas os dois gráficos indicados, nós podemos manter na tabela as ligações ao call center que são menores do que 5, e manter as informações onde os dias de atraso são menores do que 0.

Removendo as informações dessas duas colunas temos a proporção de clientes que estão cancelando o serviço após a remoção passou de 50% para 18,40% de cancelamento.

# 5 O produto final do projeto:
Um dashboard iterativo hospedado em cloud que está disponível para acesso de qualquer dispositivo com conexão à internet. Para acessá-los basta clicar no link a seguir: https://cancelamentoclientes.streamlit.app/

# 6 Conclusão
Este projeto teve como objetivo a criação de um dashboard iterativo para auxiliar o CEO da empresa na tomada de decisões, de maneira simples e rápida. 

Começamos o problema com um taxa de cancelamento de 56,71%. Após o primeiro tratamento conseguimos diminuir um pouco e atingimos 46,05%. No final com ajuda dos gráficos conseguimos ajustar nossa base de dados e chegamos ao percentual de 18,40% em cancelamentos.

Em relação as ligações ao call center por exemplo, a empresa pode verificar onde melhorar para resolver o problema evitando que as ligações sejam mais altas, e resolver o problema dos dias de atraso ligando para o cliente ou até mesmo ofercer desconto nos planos anuais e trimestrais.

Projeto desse tipo temos que conversar com o responsável tanto para verificar o que é possível fazer quanto para definir uma meta.

# 7 Próximo passos
1 Cada parte da nossa análise é fundamental para chegarmos no resultado que queremos. Nessa empresa já seria um avanço muito grande sair de 56% cancelamentos para 18% não é mesmo. 
Claro que podemos aprofundar mais as análises e diminuir ainda mais esse percentual, mas por motivos óbvios nunca vamos chegar em 0% de cancelamentos.

2 Por isso é muito importante analisar os dados e verificar a viabilidade e não só pensar em chegar a 0% de cancelamentos, pois isso será impossível. 
Precisamos fazer isso de forma correta e eficiente, poderíamos ter determinado que até 20% seria um percentual ideal melhor 50%.

3 É muito importante falar sobre viabilidade, pois certas análises podem não fazer sentido. Valor gasto por exemplo, se fosse apenas para obter um número no final poderíamos eliminar todos os cancelamentos da base de dados, com isso teríamos 0% de cancelamentos, mas não faria nenhum sentido. 
Por isso é importante analisar com calma e verificar se de fato é viável fazer esses ajustes.




