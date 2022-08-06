# Demo Detecção de EPIs

> Projeto de Demonstração de Detecção de EPIs Médicas em Imagens e em Vídeo

### Objetivo do Projeto

O objetivo do projeto consiste em desenvolver um sistema que detecte automaticamente o uso de EPIs (Equipamentos de Proteção Individual) em vídeo utilizando tecnologias do estado da arte da Visão Computacional. Desse modo, como parte inicial do projeto foi feita uma demonstração da capacidade das Redes Neurais Convolucionais para resolver problemas relativos à detecção de objetos em vídeo através da arquitetura de rede YOLO.

### Demonstração da Capacidade da Rede

|![imagem1](portfolio-exemplos/midia-predicao/image2-predicao.png)|![imagem2](portfolio-exemplos/midia-predicao/image4-predicao.png)|![imagem3](portfolio-exemplos/midia-predicao/image5-predicao.png)|
|-|-|-|

### Métricas Avaliativas

|Classe|Imagens|Rótulos|Precisão|Sensibilidade|
|-|-|-|-|-|
|Macacão|29|45|1|0.721|
|Protetor Facial|29|17|0.868|0.765|
|Luvas|29|61|0.833|0.705|
|Óculos|29|32|0.762|0.656|
|Máscara|29|52|0.922|0.846|
|Todas as Classes|29|207|0.877|0.739|

|![matriz-confusao](metricas-avaliativas/matriz-confusao.png)|![PS-curva](metricas-avaliativas/PS-curva.png)|
|-|-|

|![P-curva](metricas-avaliativas/P-curva.png)|![S-curva](metricas-avaliativas/S-curva.png)|
|-|-|