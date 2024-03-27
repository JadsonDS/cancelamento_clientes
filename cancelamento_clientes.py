# ==================================================
# Bibliotecas Necessárias
# ==================================================
import pandas as pd
import plotly_express as px
import streamlit as st
import numpy as np
from PIL import Image

#-------------------------------------Início das Funções-----------------------------------

st.set_page_config(page_title='Cancelamento_Clientes', page_icon='❌', layout='wide') 

# ===================================================================
# 
# Import dataset, Limpando os dados e Remover a coluna Customer ID
# ===================================================================
df=pd.read_csv('cancelamentos.csv')
df=df.drop('CustomerID', axis=1)
df=df.dropna()
df=df.drop_duplicates()

# ==================================================
# Logo
# ==================================================
image=Image.open('logo.jpg')
st.sidebar.image(image, width=300)

# ==================================================
# Layout no Streamliy
# ==================================================
tab1, tab2, tab3, tab4=st.tabs(['🏠 Home', '🚫 Análises dos Cancelamentos', '📊 Análises Gráficas', '📈 Análises dos Gráficos'])

with tab1:
    with st.container():
        st.write('# Projeto de Análise de Cancelamento de Clientes- Dashbord')
       

    st.markdown(
    """
    ## - Análise da base de dados
    <span style="font-size:22px;">
    Vamos verificar as informações dos clientes e o percentual de cancelamento desses clientes. 
    O objetivo do projeto vai ser fazer análises para verificar onde temos os maiores cancelamentos e os motivos desses cancelamentos.
    Com isso vamos poder propor uma solução para diminuir essas quantidades de cancelamentos.<br>
    É importante fazer de fato uma análise de dados para que possa tirar conclusões utilizando os números como referência, sendo dentro de 
    uma empresa um passo muito importante essas análises de dados para tomadas de decisões.<br>
    Começamos com um percentual x de cancelamentos, mas ao longo da análise e tratamento dos dados, vamos notar que conseguimos reduzir drasticamente esse número só com essas análises.
    Então é uma solução que a empresa pode seguir para diminuir a quantidade de cancelamentos que está tendo.<br>
    Foi removido a coluna CustomerID da nossa base de dados, pois essa informação não é útil e não adiciona nada na nossa análise.
    É apenas o número do cliente, e não vai impactar nos resultados, por esse motivo podemos remover essas informações logo no início.</span>
    """,unsafe_allow_html=True)
    st.markdown('''___''')
    
    st.markdown(
    """
    ## - Informações da base de dados - Clientes
    <span style="font-size:22px;">
    <span style="font-weight:bold;">Idade:</span> <br>
    <span style="font-weight:bold;">Sexo:</span> Masculino e Feminino <br>
    <span style="font-weight:bold;">Tempo_como_cliente:</span> <br>
    <span style="font-weight:bold;">Frequencia_uso:</span> A frequência de uso desse cliente <br>
    <span style="font-weight:bold;">Ligacoes_callcenter:</span> Quantas vezes o cliente ligou ao Call Center da empresa <br>
    <span style="font-weight:bold;">Dias_atraso:</span> Dias em que o cliente esteve em atraso <br>
    <span style="font-weight:bold;">Assinatura:</span> O plano que o cliente possui <br>
    <span style="font-weight:bold;">Duracao_contrato:</span> Tempo de duração do contrato (Mensal, Trimestral e Anual) <br>
    <span style="font-weight:bold;">Total_gasto:</span> <br>
    <span style="font-weight:bold;">Meses_ultima_interação:</span> Meses desde a última interação do cliente <br>
    <span style="font-weight:bold;">Cancelou:</span> Se o cliente cancelou (1) ou não (0) sua assinatura
    </span>
    """,unsafe_allow_html=True)

           
with tab2:
    
    st.markdown('## - Análise Inicial dos Cancelamentos')
    
    with st.container(): 
        col1, col2,col3=st.columns([1, 1.3, 1])
        
        
        with col1:
            st.markdown('#### Quantas pessoas cancelaram e quantas não cancelaram')
            
            cancelou_counts=df['cancelou'].value_counts()
            st.write(cancelou_counts)
        
        with col2:
             st.markdown('#### Quantas pessoas cancelaram e quantas não cancelaram em percentual')
             
             cancelou_normalized=df['cancelou'].value_counts(normalize=True).map('{:.2%}'.format)
             st.write(cancelou_normalized)
              
              
    st.success(
    """
    ##### Visualizamos qual é a proporção de clientes que cancelaram e que continuam com a assinatura.

    **Contagem dos Dados:**
    - Clientes que cancelaram (1): X
    - Clientes que não cancelaram (0): Y

    **Visualização em Percentual:**
    - A proporção de clientes que estão cancelando o serviço é de aproximadamente 56.71% das assinaturas. Isso significa que mais da metade dos clientes estão cancelando o serviço.
    """)
             
    st.markdown('''___''') 
                
    st.markdown('## - Verificando o Cancelamento por Contrato')
    
    with st.container(): 
        col1, col2=st.columns([1, 2])
        
        
        with col1:
            st.markdown('#### Quantas pessoas cancelaram')
            
            dur_contr_counts=df['duracao_contrato'].value_counts()
            st.write(dur_contr_counts)
        
        with col2:
             st.markdown('#### Quantas pessoas cancelaram em percentual')
             
             dur_contr_perce=df['duracao_contrato'].value_counts(normalize=True).map('{:.2%}'.format)
             st.write(dur_contr_perce)

        st.success(
        """
        ##### Visualizamos qual é a proporção de clientes em relação a duração do contrato.

        **Contagem dos Dados:**
        - Annual - Anual: X
        - Quarterly - Trimestral: Y
        - Monthly - Mensal: z

        **Visualização em Percentual:**
        - É importante ver como está essa proporção para verificar se isso pode ser um fator que afeta diretamente o cancelamento do serviço. Temos uma divisão quase igual entre os planos anual e
        trimestral, mas o plano mensal já fica atrás com quase 20%. Vamos analisar as informações dos contratos para verificar como estão distribuídas e verificar se algum deles tem um percentual maior de cancelamento.
        """)      
             
    st.markdown('''___''') 
                
    st.markdown('## - Analisando as Informações dos Contratos')
    
    with st.container(): 
        st.markdown('#### Verificando a informação geral de cada plano') 
        
        dur_contr_mean=df.groupby('duracao_contrato').mean(numeric_only=True) 
        st.write(dur_contr_mean)
        
        st.success(
        """
        ##### Visualizamos qual é a proporção de clientes em relação ao contrato.

        **Sobre os Planos:**
        - Com as informações agrupadas, é possível notar que os clientes do plano Mensal, possuem uma média de cancelamento igual a 1,
        ou seja, praticamente todos os clientes que utilizam esse plano fizeram o cancelamento do serviço.
        Esse já é um ponto importante dentro da nossa análise, pois existe um plano dessa empresa, onde praticamente todos os clientes
        fazem o cancelamento do serviço.
        
        **Analisando o Contrato Mensal:**
        - sabendo que o contrato mensal é ruim para a empresa, nós podemos remover as informações desse contrato específico e continuar analisando.
        Aqui vale lembrar que nem sempre que encontrar algo que seja ruim na análise de dados retira e para por ali. A ideia é ir analisando até que chegue em um
        valor aceitável dentro do projeto. Então é importante definir esse “valor aceitável” ou o objetivo para não ficar trabalhando sem ter um ponto de parada.
        """)
    
    st.markdown('''___''') 
                
    st.markdown('## - Removendo o Contrato Mensal')
    
    with st.container(): 
        col1, col2,col3=st.columns([1, 1.3, 1])
        
        
        with col1:
            st.markdown('#### Quantas pessoas não cancelaram e quantas cancelaram')
            
            df=df[df['duracao_contrato']!='Monthly']
            cancelou_counts=df['cancelou'].value_counts()
            st.write(cancelou_counts)
        
        with col2:
             st.markdown('#### Quantas pessoas não cancelaram e quantas cancelaram em percentual')
             
             cancelou_normalized=df['cancelou'].value_counts(normalize=True).map('{:.2%}'.format)
             st.write(cancelou_normalized) 
                 
        
        st.success(
        """
        ##### Visualizamos qual é a proporção de clientes que cancelaram e que continuam com a assinatura.

        **Contagem dos Dados:**
        - Clientes que não cancelaram (0): Y
        - Clientes que cancelaram (1): X
        
        **Visualização em Percentual:**
        - A proporção de clientes que estão cancelando o serviço já caiu para 46.05% das assinaturas nessa análise, mas esse número
        ainda é muito alto.
        Então vamos continuar analisando para chegar em um valor aceitável de cancelamentos que não esteja perto dos 50%.
        """)
        
    st.markdown('''___''')
    
    st.markdown('## - Análise das Assinaturas')
    
    with st.container(): 
        col1, col2,col3=st.columns([1, 3, 1])
        
        
        with col1:
            st.markdown('#### Assinaturas')
            
            ass_counts=df['assinatura'].value_counts(normalize=True)
            st.write(ass_counts)
        
        with col2:
             st.markdown('#### Assinaturas em percentual')
             
             ass_perc=df['assinatura'].value_counts(normalize=True).map('{:.2%}'.format)
             st.write(ass_perc) 
                 
        with st.container():
            st.markdown('#### Verificando a informação geral de cada assinatura')
            ass_mean=df.groupby('assinatura').mean(numeric_only=True)
            st.write(ass_mean) 
             
        st.success(
        """
        ##### Visualizamos qual é a proporção de clientes por assinatura.

        **Na primeira Análise:**
        - Podemos verificar que temos praticamente a mesma quantidade em cada uma das assinaturas, ou seja, temos praticamente 1/3 em cada assinatura.
                
        **Na segunda Análise:**
        - Temos que os valores de cancelamento também são muito parecidos.
        - Não podemos excluir nenhuma informação, pois os dados são praticamente iguais. Isso quer dizer que vamos ter que ir mais fundo na nossa análise de dados
        """)
        
        st.markdown('''___''')
    
        st.info(
        """
        **Próximos Passos:**
        - Como a última análise não foi muito boa para poder verificar quais informações poderiam ser removidas, vamos criar alguns gráficos.
        pois dessa forma fica muito mais fácil visualizar os dados e obter as informações que de fato estão aumentando o número de cancelamentos na empresa.
        
        **Na Proxima aba 'Análises Gráficas' vamos vizualizar os gráficos.**
        """)
        
       
with tab3:
    with st.container():
        st.write('# Criação dos Gráficos')
        
        st.info('**Temos duas visualizações quem cancelou (1) e quem não cancelou (0).**')
        
        idade=px.histogram(df, x='idade', color='cancelou', title='Gráfico por Idade', color_discrete_sequence=['red', 'blue'])
        st.plotly_chart(idade, use_container_width=True)
        st.success("Podemos vizualizar que clientes com idade superior a 50 anos tendem a cancelar suas assinaturas.")
        st.markdown('''___''')
        
        
        sexo=px.histogram(df, x='sexo', color='cancelou', title='Gráfico por Sexo', color_discrete_sequence=['red', 'blue'])
        st.plotly_chart(sexo, use_container_width=True)
        st.success(
            """Podemos vizualizar que temos praticamente a mesma quantidade em cada uma das assinaturas, os valores de cancelamento também
            são muito parecidos. Não podemos excluir nenhuma informação, pois os dados são praticamente iguais.""")
        st.markdown('''___''')
           
           
        tempo_cliente=px.histogram(df, x='tempo_como_cliente', color='cancelou', title='Gráfico por Tempo como Cliente', color_discrete_sequence=['red', 'blue'])
        st.plotly_chart(tempo_cliente, use_container_width=True)
        st.success(
            """Podemos vizualizar que temos praticamente a mesma quantidade em cada uma das assinaturas.
            Não podemos excluir nenhuma informação, pois os dados são praticamente iguais.""")
        st.markdown('''___''')
        
        
        freq_uso=px.histogram(df, x='frequencia_uso', color='cancelou', title='Gráfico por Frequência de Uso', color_discrete_sequence=['red', 'blue'])
        st.plotly_chart(freq_uso, use_container_width=True)
        st.success(
            """Podemos vizualizar que temos praticamente a mesma quantidade em cada uma das assinaturas.
            Também não podemos excluir nenhuma informação, pois os dados são praticamente iguais.""")
        st.markdown('''___''')
        
        
        lig_call=px.histogram(df, x='ligacoes_callcenter', color='cancelou', title='Gráfico por Ligacões ao Call Center', color_discrete_sequence=['red', 'blue'])
        st.plotly_chart(lig_call, use_container_width=True)
        st.success("Podemos vizualizar que clientes com mais de 5 ligações ao call center cancelam suas assinaturas.")
        st.markdown('''___''')
        
        
        dias_atraso=px.histogram(df, x='dias_atraso', color='cancelou', title='Gráfico por Dias de Atraso', color_discrete_sequence=['red', 'blue'])
        st.plotly_chart(dias_atraso, use_container_width=True)
        st.success("Podemos vizualizar que clientes com mais de 20 dias de atraso cancelam suas assinaturas.")
        st.markdown('''___''')
        
        
        assinatura=px.histogram(df, x='assinatura', color='cancelou', title='Gráfico por Assinatura', color_discrete_sequence=['red', 'blue'])
        st.plotly_chart(assinatura, use_container_width=True)
        st.success(
        """Podemos vizualizar que temos praticamente a mesma quantidade em cada uma das assinaturas.
        Também não podemos excluir nenhuma informação, pois os dados são praticamente iguais.""")
        st.markdown('''___''')
         
          
        durac_cont=px.histogram(df, x='duracao_contrato', color='cancelou', title='Gráfico por Duracão do Contrato', color_discrete_sequence=['red', 'blue'])
        st.plotly_chart(durac_cont, use_container_width=True)
        st.success(
        """Podemos vizualizar que temos praticamente a mesma quantidade em cada uma das assinaturas.
        Também não podemos excluir nenhuma informação, pois os dados são praticamente iguais.""")
        st.markdown('''___''')
         
         
        total_gasto=px.histogram(df, x='total_gasto', color='cancelou', title='Gráfico por Total Gasto', color_discrete_sequence=['red', 'blue'])
        st.plotly_chart(total_gasto, use_container_width=True)
        st.success("Podemos vizualizar que clientes com gasto inferior a 500 cancelam suas assinaturas.")
        st.markdown('''___''')
         
         
        meses_ult_int=px.histogram(df, x='meses_ultima_interacao', color='cancelou', title='Gráfico por Meses de Ultima Interacão', color_discrete_sequence=['red', 'blue'])
        st.plotly_chart(meses_ult_int, use_container_width=True)
        st.success(
        """Podemos vizualizar que temos praticamente a mesma quantidade em cada uma das assinaturas.
        Também não podemos excluir nenhuma informação, pois os dados são praticamente iguais.""")
        st.markdown('''___''')
        
        
        cancelou=px.histogram(df, x='cancelou', color='cancelou', title='Gráfico por Cancelamento', color_discrete_sequence=['red', 'blue'])
        st.plotly_chart(cancelou, use_container_width=True)
        st.success("Podemos vizualizar que temos praticamente a mesma quantidade em cada uma das assinaturas.")
        st.markdown('''___''')  
               
        st.info("**Na Proxima aba 'Análies dos Gráficos' temos as Análises referente aos gráficos e conclusão.**")    


with tab4:
  
    st.write('# Análises referente aos Gráficos e Conclusão')
    
    with st.container():
        col1, col2=st.columns([1, 1])
        
        with col1:
             dias_atraso=px.histogram(df, x='dias_atraso', color='cancelou', title='Gráfico por Dias de Atraso', color_discrete_sequence=['red', 'blue'])
             st.plotly_chart(dias_atraso, use_container_width=True)
            
        with col2:
             lig_call=px.histogram(df, x='ligacoes_callcenter', color='cancelou', title='Gráfico por Ligacões ao Call Center', color_discrete_sequence=['red', 'blue'])
             st.plotly_chart(lig_call, use_container_width=True)    

        st.success(
        """
        ##### Analizando o gráfico de Dias de Atraso e Ligações ao Call Center.

        **No primeiro Gráfico:**
        - Nesse gráfico é possível notar que clientes com mais de 20 dias de atraso cancelam suas assinaturas.
                
        **No segundo Gráfico:**
        - Já nesse outro gráfico é possível notar que clientes com mais de 5 ligações ao call center cancelam suas assinaturas.
        """)
        st.info(
            """
            **Algumas Conclusões:**
        - Analisando apenas os dois gráficos indicados, nós podemos manter na tabela as ligações ao call center que são menores do que 5.
        - E manter as informações onde os dias de atraso são menores do que 0.
        - Com isso podemos visualizar a base de dados e fazer o cálculo novamente para verificar o percentual de cancelamento.
        """)
        
        st.markdown('''___''')
        
    with st.container():
        col1, col2,col3=st.columns([1, 1.3, 1])
         
        with col1:
            st.markdown('#### Quantas pessoas não cancelaram e quantas cancelaram')
            
        
            df=df[df['ligacoes_callcenter']<5]
            df=df[df['dias_atraso']<=20]
            
            cancelou_counts=df['cancelou'].value_counts()
            st.write(cancelou_counts)
        
        with col2:
             st.markdown('#### Quantas pessoas não cancelaram e quantas cancelaram em percentual')
             
             cancelou_normalized=df['cancelou'].value_counts(normalize=True).map('{:.2%}'.format)
             st.write(cancelou_normalized)
        
        st.success(
        """
        ##### Removendo as informações dessas duas colunas temos.
        
        **Contagem dos Dados:**
        - Clientes que não cancelaram (0): Y
        - Clientes que cancelaram (1): X
        

        **Visualização em Percentual:**
        - A proporção de clientes que estão cancelando o serviço após a remoção passou de 50% para 18,40% de cancelamento.
        """)
        
        st.markdown('''___''')

    with st.container():
        
        st.write('# Conclusão')
        
        st.markdown(
        """
        <span style="font-size:22px;">
        - Começamos o problema com um taxa de cancelamento de 56,71%. Após o primeiro tratamento conseguimos diminuir um pouco e atingimos 46,05%. 
        No final com ajuda dos gráficos conseguimos ajustar nossa base de dados e chegamos ao percentual de 18,40% em cancelamentos.<br><br>
        - Cada parte da nossa análise é fundamental para chegarmos no resultado que queremos. Nessa empresa já seria um avanço muito grande sair de 56% cancelamentos para 18% não é mesmo.
        Claro que podemos aprofundar mais as análises e diminuir ainda mais esse percentual, mas por motivos óbvios nunca vamos chegar em 0% de cancelamentos.<br><br>
        - Por isso é muito importante analisar os dados e verificar a viabilidade e não só pensar em chegar a 0% de cancelamentos, pois isso será impossível. Precisamos fazer isso de forma correta e
        eficiente, poderíamos ter determinado que até 20% seria um percentual ideal melhor 50%.<br><br>
        - É muito importante falar sobre viabilidade, pois certas análises podem não fazer sentido. Valor gasto por exemplo, se fosse apenas para obter um número no
        final poderíamos eliminar todos os cancelamentos da base de dados, com isso teríamos 0% de cancelamentos, mas não faria nenhum sentido.
        Por isso é importante analisar com calma e verificar se de fato é viável fazer esses ajustes.<br><br>
        - Em relação as ligações ao call center por exemplo, a empresa pode verificar onde melhorar para resolver o problema evitando que as ligações sejam mais altas, e resolver o problema dos dias de atraso ligando para o cliente ou até mesmo
        ofercer desconto nos planos anuais e trimestrais.<br><br>
        - Projeto desse tipo temos que conversar com o responsável tanto para verificar o que é possível fazer quanto para definir uma meta. 
        </span>
        """,unsafe_allow_html=True)
            




st.sidebar.subheader('', divider='gray')                
st.sidebar.subheader('Powered by: Jadson N Santos')
st.sidebar.subheader('Discord: jadson')
st.sidebar.subheader('Linkedin: https://www.linkedin.com/in/jadson-nascimento-santos/')
st.sidebar.subheader('GitHub: https://github.com/JadsonDS') 
st.sidebar.subheader('Portfolio de Projetos: https://jadsonds.github.io/portfolio_projetos/')

        
