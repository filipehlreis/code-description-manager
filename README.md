# Code Description Manager - v0.01
O programa *Code Description Manager* auxiliará na padronização de descrição de códigos no sistema online da empresa, focando mais em componentes eletrônicos e tudo relacionado e usado para a montagem em placas de circuito impresso, as PCI's.

## Siglas e terminologias utilizadas ao longo do arquivo readme.md
- PCI - **P**laca de **C**ircuito **I**mpresso;
- PCB - ***P**rinted **C**ircuit **B**oard* (ingles para placa de circuito impresso);
- PN - ***P**art **N**umber*, ou código único de componente eletrônico definido pelo fabricante.
- CI - **C**ircuito **I**ntegrado, seria um componente eletrônico com finalidade mais especifica.
- PROCV - Função do Microsoft Excel usada para fazer buscas em linhas de uma tabela ou intervalo.
- *Pick&Place* - Equipamento eletromecânico responsável por retirar o componente eletrônico de sua embalagem e inserir em posição XY exata em uma PCI.
- CSV - Formato de arquivo que significa “***C**omma-**S**eparated-**V**alues*” (valores separados por vírgulas).
- PDF - ***P**ortable **D**ocument **F**ormat*, é um formato de arquivo usado para exibir e compartilhar documentos com segurança, independentemente de software, hardware ou sistema operacional.
- *Mouser* / *Digikey* - Distribuidores mundiais de componentes eletrônicos.

## Como era feito antigamente?
Antigamente, era simplesmente criado um código no sistema online da empresa sem o uso de nenhuma padronização, então, se hoje era criado utilizando um formato, amanhã não necessariamente seria criado da mesma forma, e dependendo, nem pela mesma pessoa.

As listas de materiais das Placas de Circuito Impresso montadas eram criados logo após finalizar a confecção da PCI, sendo cada lista de materiais um arquivo Excel diferente, e eram copiados os códigos e suas descrições diretamente do sistema online da empresa para o Excel.

Se houvesse qualquer alteração na descrição do código no sistema online da empresa, provavelmente nas listas de materiais ficariam com a descrição antiga, podendo gerar ambiguidade ou, no pior dos casos, fazer referencia a outro componente eletrônico totalmente diferente ou inativado.

## O que tem-se hoje?
Atualmente, tem-se utilizado o Excel para auxiliar na tarefa de padronização das descrições de códigos, definido previamente os requisitos mínimos de acordo com cada tipo de componente eletrônico, como capacitores, resistores, diodos, microcontroladores e CI's de modo geral.

O Excel é utilizado também para armazenar todos os códigos já criados e padronizados e todos que ainda estão em processo de padronização, oferecendo um formato de banco de dados.

Todas as listas de materiais das PCI's montadas estão sendo transferidos para o mesmo Excel que contem o banco de dados acima, cada qual com sua planilha separada, e sendo buscados através de **PROCV**.

## Quais as necessidades atuais?
A ser preenchido.

## Objetivo com a criação do software:
A ser preenchido.

## Para quem será visado? Quem testará?
A ser preenchido.


## Requisitos
A ser preenchido.

### Requisitos de interface:
A ser preenchido.

### Requisitos operacionais:
A ser preenchido.

## Informações técnicas:
A ser preenchido.

## User stories:
A ser preenchido.


### A ser organizado:
Na planilha onde se encontra a base de dados, há colunas referente a cada lista de materiais já criado, mostrando a quantidade utilizada em cada uma. Com um campo editável para determinar uma previsão de quantidade de placas a serem montadas, multiplica-se cada item, e na ultima coluna da planilha, há um somatório para que o responsável do estoque confira e analise se há quantidade suficiente ou se será necessário criar uma requisição de compra. Para tal, há campos informando a quantidade em estoque dos itens em questão.

Ainda nessa planilha da base de dados, há colunas informando a descrição anterior dos códigos, e as novas descrições, sendo uma mais ampla, simplificada, para ser inclusa e preenchida nas listas de materiais, e outra sendo a real descrição a ser atualizada no sistema da empresa, na qual conterá além dos requisitos mínimos do item, como também até 5 PN's (Part Numbers, são códigos únicos e definidos pelo fabricante do componente eletrônico). 

Na base de dados deverá possuir a possibilidade de adicionar até 10 PN's.

Nas listas de materiais, deve contem campos para a inserção do código numérico do nosso sistema, e deverá retornar as descrições simplificadas presente no banco de dados.

Ainda nas listas de materiais, os itens são classificados em 3 cores, sendo uma cor para componentes eletrônicos inseridos pela Pick&Place, outra cor para componentes que não são inseridos pela Pick&Place, seja por não ser possível ou por simplesmente não haver espaço disponível,  e então são inseridos manualmente mas ANTES de a placa ir ao forno, e a segunda cor seria para todos os componentes eletrônicos que precisam ser inseridos manualmente e DEPOIS do forno.

Deverá ser implementado um campo na base de dados na qual deverá ser informado em qual das 3 cores cada item é classificado, para automatizar a pintura nas listas de materiais.

Necessário haver uma forma de inserir o arquivo CSV fornecido pelo nosso sistema para atualizar as descrições atuais do sistema, e realizar a verificação se o código está padronizado ou não.

Deverá possuir uma aba contendo todas as informações de componentes eletrônicos utilizados na Pick&Place, possuindo informações como: localização do item nos alimentadores, nome de como está definido dentro do programa da Pick&Place, estimativa de uso trimestral, possibilidade de importar um programa exportado e convertido do programa Altium Designer  e exportar com os nomes definidos na planilha.

Para criar o código de cada componente eletrônico, deverá ser possível entrar com um PN desejado, e o programa deverá se comunicar com a Mouser e a Digikey (Arrow e outros ainda a serem analisados), e deverá gerar uma descrição padronizada, e deve prover automaticamente até 10 PN's alternativos presentes ou na Mouser ou na Digikey.

Para cada componente eletrônico, deve conter informações de características especificas do item, e até 10 PN's, na qual deve possuir também informação dos preços variáveis por quantidade, na qual auxiliará no processo de criação da requisição de compra. Deverá haver a possibilidade de mostrar até as ultimas 10 versões no histórico, mostrando as alterações realizadas.

Deverá mostrar também um campo/relatório detalhando em quais listas de materiais está presente e a quantidade utilizada em cada uma.

A cada entrada de estoque para o item, deverá associar uma nota fiscal, ou algum código para rastreabilidade, permitindo o responsável controlar quais lotes utilizar quando criar os kits.

Deverá ser possível exportar a lista de materiais em formato Excel e/ou em PDF, já estilizado, e apresentando informações de código de rastreabilidade. Uma versão dessa lista deverá conter a localização de cada item no estoque para facilitar a montagem dos kits.

Ao criar uma requisição de compra, o responsável deverá inserir a informação da requisição e do pedido de compra a cada código, para que seja possível conferir posteriormente se o item já foi solicitado a compra.

Quando for necessário realizar alguma compra nos sites Mouser ou Digikey, deverá verificar a disponibilidade de cada um dos PN's e selecionar o PN com a disponibilidade e com o melhor custo beneficio.

O software deverá salvar versões finais das listas de materiais para posterior verificação, caso necessário.

O software deverá possuir tela especificamente para a conversão de medidas.

O software deverá possibilitar consultar também a base de dados geral do sistema da empresa, não somente os itens relacionado a componente eletrônicos.

O software deverá possibilitar ajustes de quantidade, devido a conferencia física do estoque.

O software deverá possibilitar exportar uma planilha em formato padronizado para ser importado no sistema da empresa.
As descrições simplificadas dos códigos deverão ser únicos, ou seja, não poderá possuir códigos na qual diferente somente pelo PN, podendo gerar ambiguidade.
