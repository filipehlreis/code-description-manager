# TODO - Ler a planilha CSV oriunda do OMIE.
# TODO - Escolher um banco de dados, NoSQL, MySQL, MongoDB, SQLite, ou outro.
# TODO - Criar um banco de dados.
# TODO - Criar um dicionário com as principais características de um
# determinado item.
# TODO - Obter resposta de sucesso vinda da API da Mouser e Digikey.
# TODO - Função para adicionar PNs manualmente.
# TODO - Desenvolver uma interface GUI.
# TODO - Exportar uma planilha CSV possível de ser importada pelo OMIE.
# TODO - Exportar uma planilha CSV com itens a serem comprados.
# TODO - Exportar a planilha acima em PDF, possivelmente utilizando um layout
# pré estabelecido.
# TODO - Exportar o banco de dados para realização de Backup.
# TODO - Criar usuários para utilizar o programa.
# TODO - Automatizar a criação de códigos, informando apenas 1 a 2 PNs.
# TODO - Verificar se a descrição de um determinado item já está padronizada
# e presente no banco de dados.
# TODO - Os itens devem possuir uma descrição completa (a ser inserido no OMIE)
# e uma descrição simplificada (a ser utilizado em lista de materiais)
# TODO - As descrições simplificadas devem ser únicas, ou seja, não podem
# diferir somente pelo PN. (evitar duplicidade de códigos, e/ou ambiguidades).
# TODO - Em uma aba/pagina do software, deve mostrar uma tabela listando todos
# os itens cadastrados no banco de dados.
# TODO - Em uma aba/pagina do software, deve mostrar uma tabela listando todos
# os itens importados da planilha CSV do OMIE e que estão aguardando a
# padronização da descrição e inserção no banco de dados.
# TODO - Em uma aba/pagina do software, deve mostrar opções de determinar a
# previsão de quantidade de placas a serem montadas nos próximos meses.
# TODO - Gerar um relatório, planilha CSV/PDF, informando ao responsável do
# estoque quais itens estarão em falta, e que precisam gerar uma requisição
# de compra.
# TODO - Cada item deve possuir um campo de fácil edição para atualização de
# quantidade em estoque dos itens em questão.
# TODO - Em uma aba/pagina, deve mostrar uma tabela mostrando todas as listas
# de materiais já montadas.
# TODO - Quando clicar em uma lista de materiais, deve abrir uma janela PopUp
# mostrando todos os itens da lista.
# TODO - Quando clicar em um determinado item, deve abrir uma janela PopUp
# mostrando todas as informações referente a esse item. PNs, ultimas NFs,
# todas as listas de materiais na quais o item está inserido. Observações
# extras e informações que possa auxiliar tanto o estoque como também o
# setor de compras.
# TODO - No banco de dados deve conter todo o histórico de informações e
# alterações realizadas em cada item.
# TODO - Deve informar também quem que realizou qual alteração e data de
# alteração.
# TODO - A descrição completa de cada item deve possuir no máximo 120
# caracteres. (Regra Fiscal)
# TODO - Padronização dos principais itens, itens mais comuns, como:
# resistores, capacitores, indutores, parafusos, arruelas, microcontroladores,
# PCIs, Placas montadas, etc.
# TODO - Em cada item, deve haver a possibilidade de adicionar até 10 PN's
# compatíveis, e selecionar os principais a serem inseridos na descrição
# completa do item.
# TODO - Quando criar/editar uma lista de materiais, deve se possível
# selecionar o item através do código numérico do OMIE ou selecionar pela
# descrição. Será mostrado as opções à medida que for escrevendo no campo
# de busca.
# TODO - Em uma aba/pagina do software, deve conter uma tabela/imagem
# mostrando informações sobre todos os alimentadores da Pick&Place.
# TODO - Deve possuir um campo editável em cada item na qual o item será
# classificado em 3 categorias: inserido pela Pick&Place, inserido manualmente
# mas antes do forno, inserido manualmente após o forno.
# TODO - As categorias de cada item devem ser mostradas visualmente em todas
# as listas de materiais de Placas Montadas, através de uso de cores.
# TODO - Quando mostradas e/ou exportadas as listas de materiais, as cores
# devem estar visíveis e com legenda ao final da página.
# TODO - Quando for importado uma planilha CSV do OMIE, será necessário
# identificar se a descrição do código já está padronizada e também já
# inserido no banco de dados.
# TODO - Alertar caso haja itens não padronizados/cadastrados no banco de
# dados.
# TODO - Na aba/pagina referente a Pick&Place, deve possuir informações como:
# localização do item nos alimentadores, nome de como está definido dentro do
# programa da Pick&Place, estimativa de uso trimestral.
# TODO - Possibilidade de importar um programa de montagem feito pelo Altium
# Designer, converter e exportar o programa de montagem já com os nomes
# definidos previamente na Pick&Place.
# TODO - Quando criar o código de cada componente eletrônico, o usuário deverá
# inserir um PN desejado e deverá retornar com uma descrição padronizada
# simplificada, completa, e até 10 PNs alternativos, que possuam estoque
# frequentes na Mouser/Digikey.
# TODO - Deverá haver uma opção para chegar estoque na Mouser/Digikey.
# (local do botão a ser definido ainda).
# TODO - O PopUp de notificação deverá mostrar diariamente cerca de 5 itens
# a serem realizado contagem física para conferencia de estoque.
# TODO - Para PNs possíveis de serem encontrados na Mouser/Digikey, deve ser
# possível informar preços variáveis por quantidade. (auxiliar no processo de
# criação de requisição de compra.)
# TODO - O histórico de alterações deve guarda informações de até 10 versões,
# sendo que alterações realizadas durante o dia, conta como 1 versão.
# (1 versão por dia de alterações.)
# TODO - Em cada item, deve possuir um campo editável para preencher a
# característica que se deseja de um determinado item. (por exemplo,
# resistente a pulso = resistor do cabo de ECG)
# TODO - A cada entrada de quantidade no estoquem deverá associar uma NF ou
# outra rastreabilidade, permitindo o responsável controlar quais itens devem
# ser utilizados para criar os KITs.
# TODO - Na aba/pagina referente a KITs, deve possuir uma tabela informando
# quais KITs já foram montados.
# TODO - Cada item deve possuir um campo informando a localização física
# dentro do estoque.
# TODO - Deve haver um espaço que informe em quais listas de materiais o item
# se encontra e a quantidade utilizada em cada uma das listas.
# TODO - Exportar uma planilha estilizada / PDF, da lista de materiais e
# apresentando informações de rastreabilidade.
# TODO - Exportar uma planilha estilizada / PDF, da lista de materiais e
# informando a localização física no estoque para a montagem de KITs.
# TODO - Planilhas EXCEL devem ser fornecidas layouts pre estabelecidos, na
# qual o programa apenas irá preencher.
# TODO - Quando o usuário criar uma requisição de compra, deverá inserir a
# informação de requisição e pedido de compra para cada item, para que seja
# possível conferir posteriormente se o item já foi solicitado a compra e o
# prazo para entrega. Datas da requisição.
# TODO - Quando necessário comprar na Mouser ou na Digikey, deverá consultar
# a disponibilidade e selecionar o PN com o melhor custo benefício.
# TODO - Verificar possibilidade de criar um carrinho/projeto automaticamente
# na Mouser/Digikey.
# TODO - Todas as listas de materiais devem possuir um histórico de versões
# para posterior consultas.
# TODO - Todas as listas de materiais devem possuir campos de observações.
# TODO - Na aba/pagina de conversões de medidas, deve possuir opções de
# calculadoras para a conversão fácil e rápida de unidades e quantidades.
# TODO - Em um primeiro momento, o software é focado em componentes
# eletrônicos, porém não limitados a isto.
# TODO - Ajustes de quantidade devido a conferencia física do estoque.
# TODO -
