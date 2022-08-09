import streamlit as st
from streamlit_player import st_player

st.set_page_config(page_title = 'Demo Projeto', layout = 'wide', page_icon = '📋')
st.markdown("<div id='inicio' style='visibility: hidden'></div>", unsafe_allow_html = True)
st.markdown('<style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} </style>', 
            unsafe_allow_html = True)

padding = 1
st.markdown(f"""<style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style>""", unsafe_allow_html = True)

st.header(body = 'Detecção de EPIs em Vídeo - Demonstração de Projeto - 📋')
st.markdown('***')

st.markdown("""O objetivo do projeto consiste em desenvolver um sistema que detecte automaticamente 
            o uso de EPIs (Equipamentos de Proteção Individual) em vídeo no contexto de ambientes médicos
            utilizando tecnologias do estado da arte da Visão Computacional. Desse modo, como parte 
            inicial do projeto foi feita uma demonstração da capacidade das Redes Neurais para resolver 
            problemas relativos à detecção de objetos em vídeo.""")

col1, col2 = st.columns(spec = [5,5])

with col1: 
    st.markdown('Os equipamentos médicos considerados na demonstração a seguir são:')  
    st.markdown('* Máscaras;')
    st.markdown('* Protetor Facial;')
    st.markdown('* Óculos de Proteção;')
    st.markdown('* Luvas;')
    st.markdown('* Macacão;')
with col2:
    st.image(image = 'imagens-app/imagem-exemplo.png', width = 300)

st.warning("""OBS: O modelo em questão é apenas uma demonstração de projeto. A equipe possui plena 
              capacidade para entregar um sistema mais aperfeiçoado e adaptável às necessidades do
              contratante.""")

st.markdown('## Portfólio de Resultados (predições feitas pelo sistema DEMO)')
st.markdown('***')

st.markdown('### > Galeria de Vídeos')

col1, col2 = st.columns(spec = [5,5])

with col1:
    st_player(url = 'https://youtu.be/p9ziIeBydTk', loop = True, height=350)
with col2:
    st_player(url = 'https://youtu.be/eMk6c5TVsWU', loop = True, height=350)

col3, col4 = st.columns(spec = [5,5])

with col3:
    st_player(url = 'https://youtu.be/9n8ER7Bd1Es', loop = True, height=350)
with col4:
    st_player(url = 'https://youtu.be/ehMlSOYgM6g', loop = True, height=350)


st.markdown('### > Galeria de Imagens')

col5, col6 = st.columns(spec = [5,5])

with col5:
    st.image(image = 'portfolio-exemplos/midia-predicao/image4-predicao.png')
with col6:
    st.image(image = 'portfolio-exemplos/midia-predicao/image2-predicao.png')

col7, col8 = st.columns(spec = [5,5])

with col7:
    st.image(image = 'portfolio-exemplos/midia-predicao/image5-predicao.png')
with col8:
    st.image(image = 'portfolio-exemplos/midia-predicao/image1-predicao.png')

st.markdown('## Métricas Avaliativas do Sistema DEMO')
st.markdown('***')

st.warning(body = 'OBS: todas as métricas foram calculadas com base nos dados de validação.')

col9, col10 = st.columns(spec = [5.5,4.5])

with col9:
    st.markdown("""
    |Classe|Imagens|Rótulos|Acurácia (%)|Precisão (%)|Sensibilidade (%)|
    |-|-|-|-|-|-|
    |Macacão|29|45|83,70|99,00|72,10|
    |Protetor Facial|29|17|89,00|86,80|76,50|
    |Luvas|29|61|79,20|83,30|70,50|
    |Óculos|29|32|73,50|76,20|65,60|
    |Máscara|29|52|88,00|92,20|84,60|
    |Todas as Classes|29|207|82,70|87,70|73,90|
    """)
with col10:
    box = st.selectbox(label = 'Selecione uma Métrica de Avaliação:', 
                       options = ['Matriz de Confusão', 'Acurácia', 'Precisão', 
                                  'Sensibilidade', 'F1-Score'], 
                       index = 0)

    if box == 'Matriz de Confusão':
        st.markdown('''Na análise preditiva, uma Matriz de Confusão é uma tabela que relata o 
                       número de ```Falsos Positivos```, ```Falsos Negativos```, 
                       ```Verdadeiros Positivos``` e ```Verdadeiros Negativos```.''')
        st.image(image = 'imagens-app/matriz-confusao.png')
    if box == 'Acurácia':
        st.markdown('''Métrica que analisa a quantidade de acertos do nosso modelo divido pelo total da 
                       amostras.''')
        st.image(image = 'imagens-app/acuracia.png')
    if box == 'Precisão':
        st.markdown('''Métrica que analisa dentre todos os dados classificados como positivos, 
                       quantos são realmente positivos.''')
        st.image(image = 'imagens-app/precisao.png')
    if box == 'Sensibilidade':
        st.markdown('''Métrica que analisa qual a porcentagem de dados classificados como positivos 
                       comparado com a quantidade real de positivos que existem nas amostras.
                       (também conhecida como *Recall*).''')
        st.image(image = 'imagens-app/sensibilidade.png')
    if box == 'F1-Score':
        st.markdown('''Métrica que une precisão e recall afim de trazer um número único que determine 
                       a qualidade geral do modelo.''')
        st.image(image = 'imagens-app/f1-score.png')
st.markdown('***')
st.markdown('### > Gráficos das Métricas de Avaliação')

col11, col12 = st.columns(spec = [5,5])

with col11:
    st.image(image = 'metricas-avaliativas/matriz-confusao.png', 
             caption = 'Matriz de Confusão do Modelo')
with col12:
    st.image(image = 'metricas-avaliativas/P-curva.png', 
             caption = 'Análise da métrica de Precisão do modelo')

col13, col14 = st.columns(spec = [5,5])

with col13:
     st.image(image = 'metricas-avaliativas/S-curva.png', 
              caption = 'Análise da Métrica de Sensibilidade do modelo')
with col14:
    st.image(image = 'metricas-avaliativas/F1-curva.png', 
              caption = 'Análise da Métrica de F1-Score do modelo')

st.markdown('## Equipe de Desenvolvimento')
st.markdown('***')

col15, col16 = st.columns(spec = [1,8])

with col15:
    st.image(image = 'https://user-images.githubusercontent.com/58775072/145095066-08ec2fd0-0e30-44b4-998d-c3e78d4409e0.jpg', 
             width = 120)
with col16:
    st.markdown(body = '**Nome**: [Luciana Ribeiro Veloso](http://lattes.cnpq.br/2498050002491677)')
    st.markdown(body = '**Formação Acadêmica**: Doutora em Engenharia Elétrica (UFCG)')
    st.markdown(body = '**Biografia**: Possui graduação em Engenharia Elétrica pela Universidade Federal da '
                       'Paraíba (1995), mestrado em Engenharia Elétrica pela Universidade Federal da Paraíba '
                       '(1998) e Doutorado em Engenharia Elétrica pela Universidade Federal de Campina Grande '
                       '(2009). Atualmente é professora da Universidade Federal de Campina Grande. Tem '
                       'experiência na área de Engenharia Elétrica, com ênfase em Processamento de Imagens, ' 
                       'atuando principalmente nos seguintes temas: Reconhecimento de Palavras Manuscritas, '
                       'Processamento de Imagens e Reconhecimento de Padrões.')

st.markdown(body = '***')

col17, col18 = st.columns(spec = [1,8])

with col17:
    st.image(image = 'https://user-images.githubusercontent.com/58775072/183263382-81336cc2-1fbe-4c33-802c-be4b4a7379c0.gif', 
             width = 120)
with col18:
    st.markdown(body = '**Nome**: [Edmar Candeia Gurjão](http://lattes.cnpq.br/9200464668550566)')
    st.markdown(body = '**Formação Acadêmica**: Doutor em Engenharia Elétrica (UFCG)')
    st.markdown(body = '**Biografia**: Graduado em Engenharia Elétrica pela Universidade Federal da Paraíba (1996), '
                        'mestre em Engenharia Elétrica pela Universidade Federal da Paraíba (1999) e doutor em Engenharia '
                        'Elétrica pela Universidade Federal de Campina Grande (2003). Realizou estágio pós-doutoral na '
                        'Universidade Notre Dame (USA) em 2012. Atualmente é professor Associado do Departamento de '
                        'Engenharia Elétrica da Universidade Federal de Campina Grande e professor colaborador do '
                        'Mestrado Profissional em Ciência e Tecnologia em Saúde da Universidade Estadual da Paraíba. '
                        'Tem experiência na área de Engenharia Elétrica, com ênfase em Amostragem Compressiva '
                        '(*Compressed Sensing*), Rádio Definido por Software, Processamento de Sinais e Aplicações de '
                        'Álgebra Linear. Senior Member do IEEE também é membro da Sociedade Brasileira de '
                        'Telecomunicações (SBrT) É Co-autor dos livros Introdução à Análise de Sinais e Sistemas, '
                        'Elsevier, 2015, e Digital Signal Processing, Momentum Press, 2018.')

st.markdown(body = '***')
        
col19, col20 = st.columns(spec = [1,8])
        
with col19:
    st.image(image = 'https://user-images.githubusercontent.com/58775072/145095291-61c00da5-211a-4b86-9728-77594fbf60e9.gif', 
             width = 120)
with col20:
    st.markdown(body = '**Nome**: [Leo de Lima Araújo](http://lattes.cnpq.br/2093156188518982)')
    st.markdown(body = '**Formação Acadêmica**: Mestrando em Engenharia Elétrica (UFCG)')
    st.markdown(body = '**Biografia**: Pós-graduando em Engenharia Elétrica pela Universidade Federal de Campina '
                       'Grande. Trabalha sobretudo com Aprendizado Profundo (*Deep Learning*) e Visão Computacional '
                       'e atua no desenvolvimento pesquisas na área de saúde, envolvendo o diagnóstico automatizado '
                       'de Distúrbios Pulmonares e *COVID-19*, além de aplicações industriais, identificando defeitos '
                       'em televisores/monitores na linha de produção.')
        
st.markdown(body = '***')
        
col21, col22 = st.columns(spec = [1,8])
        
with col21:
    st.image(image = 'https://user-images.githubusercontent.com/58775072/145095535-fb303146-1c30-40bf-85d2-6b90e4a68ab3.png', 
             width = 120)
with col22:
    st.markdown(body = '**Nome**: [Alysson Machado de Oliveira Barbosa](http://lattes.cnpq.br/0536933202710340)')
    st.markdown(body = '**Formação Acadêmica**: Graduando em Engenharia Elétrica (UFCG)')
    st.markdown(body = '**Biografia**: Possui segundo grau completo na instituição Colégio Alfredo Dantas (CAD) '
                               'e atualmente faz graduação em Engenharia Elétrica pela Universidade Federal de Campina '
                               'Grande (UFCG). Desenvolveu um projeto intitulado "Álgebra Linear com Python" , visando aplicar '
                               'computacionalmente conceitos de Álgebra Linear. Atualmente é ativo no desenvolvimento '
                               'de trabalhos em Inteligência Artificial (IA) com conhecimentos em *Machine Learning* ' 
                               'e *Deep Learning*. Tem experiência no desenvolvimento de páginas web, programação em C, '
                               'C++, Python e versionamento de projetos com Git. Desenvolveu atividades relevantes '
                               'para a comunidade acadêmica como o evento *Academic Talk* em parceria com o capítulo '
                               'PELS/IAS da UFCG associado ao Instituto de Engenheiros Elétricos e Eletrônicos (IEEE).')

st.markdown(body = '***')

col23, col24 = st.columns(spec = [1,8])
        
with col23:
    st.image(image = 'https://user-images.githubusercontent.com/58775072/183262998-b7ed918c-b41d-42a9-af00-7fa420661e6d.gif', 
             width = 120)
with col24:
    st.markdown(body = '**Nome**: [Iury Chagas da Silva Caetano](http://lattes.cnpq.br/1459944137014662)')
    st.markdown(body = '**Formação Acadêmica**: Graduando em Engenharia Elétrica (UFCG)')
    st.markdown(body = '**Biografia**: Graduando em Engenharia Elétrica pela Universidade Federal de Campina Grande. '
                       'Estudante da área de visão computacional, aprendizado de máquina e aprendizado profundo. Possui '
                       'Experiência na área de IA com projetos provenientes da disciplina TEEE Int. Processamento de Imagens '
                       'Digitais a qual foi monitor.')
