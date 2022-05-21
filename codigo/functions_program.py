# ########################################################################## #
#                                  IMPORTS                                   #
# ########################################################################## #
from threading import Thread
import re
import pandas as pd
import os
from Custom_Widgets.Widgets import *

database_pandas = pd.DataFrame()


# ########################################################################## #
#                                    APIs                                    #
# ########################################################################## #
# TODO - Obter resposta de sucesso vinda da API da Mouser e Digikey.
def get_info_about_pn():
    pass


# TODO - Quando necessário comprar na Mouser ou na Digikey, deverá consultar
# a disponibilidade e selecionar o PN com o melhor custo benefício.
def get_best_value_for_money_item_in_mouser():
    pass


def get_best_value_for_money_item_in_digikey():
    pass


# TODO - Verificar possibilidade de criar um carrinho/projeto automaticamente
# na Mouser/Digikey.
def create_cart_order_in_mouser():
    pass


def create_cart_order_in_digikey():
    pass


# TODO - Deverá haver uma opção para chegar estoque na Mouser/Digikey.
# (local do botão a ser definido ainda).
def get_availability_in_mouser():
    pass


def get_availability_in_digikey():
    pass


# TODO - Para PNs possíveis de serem encontrados na Mouser/Digikey, deve ser
# possível informar preços variáveis por quantidade. (auxiliar no processo de
# criação de requisição de compra.)
def get_prices_break_in_mouser():
    pass


def get_prices_break_in_digikey():
    pass


# ########################################################################## #
#                               BANCO DE DADOS                               #
# ########################################################################## #
# TODO - Escolher um banco de dados, NoSQL, MySQL, MongoDB, SQLite, ou outro.
# --> Necessario estudar cada possibilidade.

# TODO - Criar um banco de dados.
# --> Necessario definir qual banco de dados utilizar.

# TODO - Exportar o banco de dados para realização de Backup.
def export_database_to_csv_backup():
    pass


# TODO - Importar o banco de dados para realização de Backup.
def import_database_from_csv_backup():
    pass


# TODO - Inserir uma tela de Loading antes de abrir o programa.
# --> Inserir loading ao iniciar o programa.


# TODO - Encontrar a instancia atual da janela do PyQT
def findWindowApplication() -> QMainWindow:
    app = QApplication.instance()
    for widget in app.topLevelWidgets():
        if isinstance(widget, QMainWindow):
            return widget
    return None


def create_table_widget(window, rowPosition, columnPosition, text, tableName):
    qtablewidgetitem = QTableWidgetItem()

    # USER getattr() METHOD
    getattr(window.ui, tableName).setItem(
        rowPosition, columnPosition, qtablewidgetitem)
    qtablewidgetitem = getattr(window.ui, tableName).item(
        rowPosition, columnPosition)

    qtablewidgetitem.setText(text)


def createTable_database_basic():
    window = findWindowApplication()

    for x in range(10):
        rowPosition = window.ui.database_table.rowCount()
        window.ui.database_table.insertRow(rowPosition)

        create_table_widget(
            window, rowPosition, 0, f'Teste {x}', 'database_table')
        create_table_widget(
            window, rowPosition, 1, f'Teste {x}', 'database_table')
        create_table_widget(
            window, rowPosition, 2, f'Teste {x}', 'database_table')
        create_table_widget(
            window, rowPosition, 3, f'Teste {x}', 'database_table')
        create_table_widget(
            window, rowPosition, 4, f'Teste {x}', 'database_table')
        create_table_widget(
            window, rowPosition, 5, f'Teste {x}', 'database_table')
        create_table_widget(
            window, rowPosition, 6, f'Teste {x}', 'database_table')
        create_table_widget(
            window, rowPosition, 7, f'Teste {x}', 'database_table')


def on_click(index):
    window = findWindowApplication()
    row = index.row()
    # column = index.column()
    codigo = window.ui.database_table.item(row, 1).text()
    print(codigo)

    # print(window.ui.database_table.createIndex())


def createTable_database_full():
    global database_pandas

    print(database_pandas)

    window = findWindowApplication()

    for x in range(database_pandas.shape[0]):
        rowPosition = window.ui.database_table.rowCount()
        window.ui.database_table.insertRow(rowPosition)

        data = database_pandas.iloc[x]

        create_table_widget(
            window, rowPosition, 0, data['Situação'], 'database_table')
        create_table_widget(
            window, rowPosition, 1, str(data['Código']), 'database_table')
        create_table_widget(
            window, rowPosition, 2, data['Descrição Simplificada'], 'database_table')
        create_table_widget(
            window, rowPosition, 3, data['Descrição'], 'database_table')
        create_table_widget(
            window, rowPosition, 4, (str(data['Estoque Disponível']).replace(',', '.')), 'database_table')
        create_table_widget(
            window, rowPosition, 5, str(data['Caixa']), 'database_table')
        create_table_widget(
            window, rowPosition, 6, str(data['Prateleira']), 'database_table')
        create_table_widget(
            window, rowPosition, 7, str(data['Corredor']), 'database_table')

    window.ui.database_table.resizeColumnsToContents()


def findName():
    window = findWindowApplication()

    name = window.ui.database_search.text().lower()
    for row in range(window.ui.database_table.rowCount()):
        id_item = window.ui.database_table.item(row, 1)
        basic_item = window.ui.database_table.item(row, 2)
        full_item = window.ui.database_table.item(row, 3)
        pesquisa = False

        if name not in full_item.text().lower():
            pesquisa = True

        basic_item_text = basic_item.text().lower()
        if basic_item_text:
            if name not in basic_item_text:
                pesquisa = True

        if name in id_item.text().lower():
            pesquisa = False

        # if the search is *not* in the item's text *do not hide* the row
        window.ui.database_table.setRowHidden(
            row, pesquisa)


def setTextToNotificationPopUp(message: str):
    window = findWindowApplication()
    if window:
        window.ui.notificationLabel.setText(message)
        window.ui.notificationBtn.click()


# TODO - Importar o banco de dados para realização de Backup.
def import_database_from_excel_backup():
    global database_pandas
    print('\nIniciando importação do Banco de Dados.')

    if database_pandas.empty:
        try:
            dir_to_load = 'input_output/database.xlsx'
            dir_to_save = 'input_output/database-verifica.xlsx'
            database_pandas = pd.read_excel(dir_to_load)
            database_pandas.to_excel(dir_to_save, index=False)
            print('Banco de Dados importado com sucesso.\n')
        except Exception as e:
            if e:
                message = 'Banco de Dados não encontrado.'
                setTextToNotificationPopUp(message)
                print(message)


# TODO - No banco de dados deve conter todo o histórico de informações e
# alterações realizadas em cada item.
# --> No momento vejo como requisito de criação do banco de dados.
# ---> Verificar possibilidade de utilizar um Design Pattern para este fim.


# TODO - Deve informar também quem que realizou qual alteração e data de
# alteração.
# --> No momento vejo como requisito de criação do banco de dados.


# TODO - O histórico de alterações deve guarda informações de até 10 versões,
# sendo que alterações realizadas durante o dia, conta como 1 versão.
# (1 versão por dia de alterações.)
# --> No momento vejo como requisito de criação do banco de dados.
# ---> Verificar possibilidade de utilizar um Design Pattern para este fim.


# TODO - Todas as listas de materiais devem possuir um histórico de versões
# para posterior consultas.
# --> No momento vejo como requisito de criação do banco de dados.
# ---> Verificar possibilidade de utilizar um Design Pattern para este fim.


# ########################################################################## #
#                     ESTRUTURAÇÃO DOS DADOS DE CADA ITEM                    #
# ########################################################################## #
# TODO - Criar um dicionário com as principais características de um
# determinado item.
item = {
    'code': '660629',
    'full_description': 'CAPACITOR CERÂMICO SMD 0603 150pF 50V 5% C0G (PN: GRM1885C1H151JA01J) (PN: CL10C151JB8NFNC) (PN: C0603C151J5GAC)',
    'bom_description': 'CAPACITOR CERÂMICO SMD 0603 150pF 50V 5% C0G',
    'category': 'CAPACITOR',
    'cap_type': 'CERÂMICO',
    'mounting': 'SMD',
    'encap': '0603',
    'value': '150pF',
    'voltage': '50V',
    'current': '0.1A',
    'tolerance': '5%',
    'cap_dieletric': 'C0G',
    'quantity': 2000,
    'min_quantity': 100,
    'alert_quantity': 500,
    'alert_quantity': 500,
    'pns': [
        'GRM1885C1H151JA01J',
        'CL10C151JB8NFNC',
        'C0603C151J5GAC',
    ],
    'location': {
        'aisle': '1',
        'shelf': '5',
        'box': '4'
    },
    'tax': {
        'ncm': '8541.50.20',
        'average_cost': 0.52,
        'total_cost': 5.2,
        'suppliers': [],
        'purchases_history': [
            {
                'input_data': '21/04/2022',
                'supplier': 'Mouser',
                'nf': '123456',
                'quantity': 1000,
                'unit_price': 0.25,
                'total_price': 25.00,
            },
        ]
    },
}

category = ['TRANSISTOR', 'REGULADOR DE TENSÃO', 'RESISTOR', 'CAPACITOR',
            'INDUTOR', 'DIODO', 'CRISTAL OSCILADOR', 'FERRITE BEAD', 'BUZZER', ]
mounting_type = ['SMD', 'PTH']
trans_type = ['BJT', 'MOSFET', 'JFET', 'OPTOACOPLADOR', ]
cap_dieletric = ['X5R', 'X7R', 'C0G', 'Y5V', 'X7S', 'Y5U', ]
cap_type = ['CERÂMICO', 'DE FILME', 'DE POLIESTER',
            'ELETROLÍTICO DE ALUMÍNIO', 'TÂNTALO', 'SAFETY', ]
encap_simple = ['0402', '0603', '0805', '7045', '1206', '1210', '2512', ]
power_rating = ['1/16W', '1/10W', '1/8W', '1/4W',
                '1/3W', '1/2W', '1W', '2W', '3W', '4W', '5W', ]
res_type = ['SMD', 'PTH DE FIO', 'PTH METAL-OXIDE', ]
tolerance = ['0.01%', '0.02%', '0.1%', '0.5%', '1%', '5%', '10%', '20%', ]
color = ['VERDE', 'AZUL', 'BRANCO', 'VERMELHO', ]
encap_complex = [
    '0603', '3MM', 'D2-PAK', 'D-FLAT', 'DO-201D', 'DO-214AA', 'DO-214AC',
    'DO-220AA', 'HSOP-8', 'LL-34', 'MSOP-10', 'SC70-6', 'SMD-4 OPTION9',
    'SO-8', 'SOD123', 'SOD-323F-2', 'SOD-80C', 'SOIC-14', 'SOIC-4', 'SOIC-8',
    'SOP-16', 'SOT-223-3', 'SOT23', 'SOT23-5', 'SOT23-8', 'TO-220', 'TO-220AB',
    'TO-225-3', 'TO-252', 'TSOP-6', 'TSSOP-14', 'VQFN-40', 'VSSOP-10', ]
diode_type = [
    'LED', 'PONTE RETIFICADORA', 'RETIFICADOR', 'SCHOTTKY', 'ZENER',
    'DE SINAL', 'ZENER AJUSTÁVEL', ]
trans_canal = ['N', 'P', 'NPN', 'PNP', ]
ci_type = [
    'AMPLIFICADOR', 'CONVERSOR AC/DC', 'CONVERSOR DC/DC', 'AFE', 'LED DRIVER',
    'MEMORIA', 'MICROCONTROLADOR', 'CONVERSOR DAC', 'CONVERSOR ADC',
    'ISOLADOR DIGITAL E DC/DC', ]
amplifier_type = ['DIFERENCIAL', 'OPERACIONAL', 'DE ÁUDIO', ]
voltage_regulator_type = [
    'BOOST', 'BUCK BOOST', 'CHARGE PUMP', 'FLYBACK', 'LDO', 'LINEAR',
    'STEP-DOWN', 'SWITCHING CONTROLLER', ]


# TODO - Função para adicionar PNs manualmente.
def add_pn_to_item():
    pass


def remove_pn_from_item():
    pass


# TODO - Os itens devem possuir uma descrição completa (a ser inserido no OMIE)
# e uma descrição simplificada (a ser utilizado em lista de materiais)
# --> No momento vejo como requisito de criação e padronização de descrição.


# TODO - Em cada item, deve haver a possibilidade de adicionar até 10 PN's
# compatíveis, e selecionar os principais a serem inseridos na descrição
# completa do item.
# --> No momento vejo como requisito de criação e padronização de descrição,
# junto com a interface.


# TODO - Deve possuir um campo editável em cada item na qual o item será
# classificado em 3 categorias: inserido pela Pick&Place, inserido manualmente
# mas antes do forno, inserido manualmente após o forno.
# --> Vejo neste momento como uma função, mas com interface mostrando uma lista
# para selecionar a categoria.
def set_assembly_category():
    pass


# ########################################################################## #
#                                PADRONIZACAO                                #
# ########################################################################## #
# TODO - Automatizar a criação de códigos, informando apenas 1 a 2 PNs.
def get_auto_description_from_pn():
    pass


# TODO - Verificar se a descrição de um determinado item já está padronizada
# e presente no banco de dados.
def is_description_standard():
    pass


# This is the begining of the regular expressions
# https://regex101.com/r/ILJViS/1


def is_description_in_database():
    pass


# TODO - A descrição completa de cada item deve possuir no máximo 120
# caracteres. (Regra Fiscal)
# --> Vejo como requisito de banco de dados, e validação no momento da criação
# da descrição.
def get_length_description():
    pass


# TODO - Padronização dos principais itens, itens mais comuns, como:
# resistores, capacitores, indutores, parafusos, arruelas, microcontroladores,
# PCIs, Placas montadas, etc.
# --> Necessario desenvolver uma logica de padronização para os itens mais
# comuns, e implementar durante a criação da descrição.


# TODO - As descrições simplificadas devem ser únicas, ou seja, não podem
# diferir somente pelo PN. (evitar duplicidade de códigos, e/ou ambiguidades).
# --> Requisito de banco de dados.
def is_unique_this_description():
    pass


# TODO - Alertar caso haja itens não padronizados/cadastrados no banco de
# dados.
def create_report_itens_not_in_database():
    pass


def create_report_itens_non_standard():
    pass


# TODO - Em cada item, deve possuir um campo editável para preencher a
# característica que se deseja de um determinado item. (por exemplo,
# resistente a pulso = resistor do cabo de ECG)
def create_observation_about_item():
    pass


# TODO - Quando for importado uma planilha CSV do OMIE, será necessário
# identificar se a descrição do código já está padronizada e também já
# inserido no banco de dados.
# --> Vejo como um passo a passo a ser seguido.


# ########################################################################## #
#                                  INTERFACE                                 #
# ########################################################################## #
# TODO - Desenvolver uma interface GUI.
# --> Sera elaborado no PyQT.


# TODO - Em uma aba/pagina do software, deve mostrar uma tabela listando todos
# os itens cadastrados no banco de dados.
# --> Sera elaborado no PyQT.
# ---> Banco de Dados


# TODO - Em uma aba/pagina do software, deve mostrar uma tabela listando todos
# os itens importados da planilha CSV do OMIE e que estão aguardando a
# padronização da descrição e inserção no banco de dados.
# --> Sera elaborado no PyQT.
# ---> Aguardando Padronização


# TODO - Em uma aba/pagina do software, deve mostrar opções de determinar a
# previsão de quantidade de placas a serem montadas nos próximos meses.
# --> Sera elaborado no PyQT.
# ---> Previsão de consumo


# TODO - Em uma aba/pagina, deve mostrar uma tabela mostrando todas as listas
# de materiais já montadas.
# --> Sera elaborado no PyQT.
# ---> Listas de Materiais


# TODO - Quando clicar em uma lista de materiais, deve abrir uma janela PopUp
# mostrando todos os itens da lista.
# --> Sera elaborado no PyQT.


# TODO - Quando clicar em um determinado item, deve abrir uma janela PopUp
# mostrando todas as informações referente a esse item. PNs, ultimas NFs,
# todas as listas de materiais na quais o item está inserido. Observações
# extras e informações que possa auxiliar tanto o estoque como também o
# setor de compras.
# --> Sera elaborado no PyQT.


# TODO - Em uma aba/pagina do software, deve conter uma tabela/imagem
# mostrando informações sobre todos os alimentadores da Pick&Place.
# --> Sera elaborado no PyQT.
# ---> Pick&Place.


# TODO - Na aba/pagina referente a Pick&Place, deve possuir informações como:
# localização do item nos alimentadores, nome de como está definido dentro do
# programa da Pick&Place, estimativa de uso trimestral.
# --> Sera elaborado no PyQT.


# TODO - Na aba/pagina referente a KITs, deve possuir uma tabela informando
# quais KITs já foram montados.
# --> Sera elaborado no PyQT.


# TODO - Na aba/pagina de conversões de medidas, deve possuir opções de
# calculadoras para a conversão fácil e rápida de unidades e quantidades.
# --> Sera elaborado no PyQT.


# TODO - Quando criar/editar uma lista de materiais, deve ser possível
# selecionar o item através do código numérico do OMIE ou selecionar pela
# descrição. Será mostrado as opções à medida que for escrevendo no campo
# de busca.
# --> Sera elaborado no PyQT.


# TODO - As categorias de cada item devem ser mostradas visualmente em todas
# as listas de materiais de Placas Montadas, através de uso de cores.
# --> Sera elaborado no PyQT.


# TODO - Deve haver um espaço que informe em quais listas de materiais o item
# se encontra e a quantidade utilizada em cada uma das listas.
# --> Sera elaborado no PyQT.


# ########################################################################## #
#                               FUNCIONALIDADES                              #
# ########################################################################## #
# TODO - Criar usuários para utilizar o programa.
def create_user():
    pass


# TODO - Quando criar o código de cada componente eletrônico, o usuário deverá
# inserir um PN desejado e deverá retornar com uma descrição padronizada
# simplificada, completa, e até 10 PNs alternativos, que possuam estoque
# frequentes na Mouser/Digikey.
# --> Vejo como requisito para criação de descrição.


# TODO - Em um primeiro momento, o software é focado em componentes
# eletrônicos, porém não limitados a isto.
# --> Vejo como requisito extra para foco da criação de descrição.


# TODO - O PopUp de notificação deverá mostrar diariamente cerca de 5 itens
# a serem realizado contagem física para conferencia de estoque.
def get_five_items_to_check():
    pass


# TODO - Cada item deve possuir um campo informando a localização física
# dentro do estoque.
def get_physical_location_item():
    pass


# TODO - A cada entrada de quantidade no estoquem deverá associar uma NF ou
# outra rastreabilidade, permitindo o responsável controlar quais itens devem
# ser utilizados para criar os KITs.
def add_nf_to_item():
    pass


def get_the_oldest_nf_from_item():
    pass


# TODO - Possibilidade de importar um programa de montagem feito pelo Altium
# Designer, converter e exportar o programa de montagem já com os nomes
# definidos previamente na Pick&Place.
def import_pick_and_place_altium_program():
    pass


def convert_pick_and_place_altium_program():
    pass


def export_pick_and_place_altium_program():
    pass


# TODO - Quando o usuário criar uma requisição de compra, deverá inserir a
# informação de requisição e pedido de compra para cada item, para que seja
# possível conferir posteriormente se o item já foi solicitado a compra e o
# prazo para entrega. Datas da requisição.
def add_qtd_to_storage_with_nf():
    pass


# TODO - Cada item deve possuir um campo de fácil edição para atualização de
# quantidade em estoque dos itens em questão devido a conferencia física
# do estoque.
def get_quantity_item_in_storage():
    pass


def set_quantity_item_in_storage():
    pass


# ########################################################################## #
#                               CSV/PDF/EXCEL                                #
# ########################################################################## #


# TODO - Ler a planilha CSV oriunda do OMIE.
def thread_read_omie_sheet():
    t = Thread(target=read_omie_sheet, args=())
    t.start()


def read_omie_sheet():
    global database_pandas
    print('\nIniciando import.')
    # import matplotlib.pyplot as plt

    excel_file_dir = \
        'local_settings\compras,_estoque_e_producao_318635218276261.xlsx'
    df_data = pd.read_excel(excel_file_dir)
    clean = df_data
    col_subset_delete = [
        'CEST', 'Código EAN (GTIN)', 'Preço Unitário de Venda',
        'Marca', 'Dias de Garantia', 'Dias de Crossdocking',
        'Cupom Fiscal (PDV)', 'Marketplace', 'Tipo do Item (Bloco K)',
        'Origem da Mercadoria', 'Preço Tabelado (Pauta)',
        'Produzido em Escala Relevante', 'CNPJ Fabricante', 'Características']
    clean = clean.drop(axis=1, labels=col_subset_delete)
    clean_df_data = clean
    regex = re.compile(r'[5679]{1}[0-9]{5}')

    database_pandas = clean_df_data[clean_df_data['Código'].str.len() == 6]
    database_pandas = database_pandas[database_pandas['Código'].str.match(
        regex)]
    database_pandas['Descrição Simplificada'] = ''
    reorder_columns = [
        'Situação', 'Descrição', 'Descrição Simplificada', 'Código',
        'Família de Produto', 'Código NCM', 'Estoque Disponível', 'Unidade',
        'Custo Médio Contábil', 'Estoque Mínimo', 'Peso Líquido', 'Peso Bruto',
        'Altura', 'Largura', 'Profundidade', 'Inclusão', 'Última Alteração',
        'Incluído por', 'Alterado por', ]
    database_pandas = database_pandas[reorder_columns]
    database_pandas['Corredor'] = 0
    database_pandas['Prateleira'] = 0
    database_pandas['Caixa'] = 0

    print('Import realizado com sucesso.')

    # pass


# TODO - Exportar o arquivo CSV recem lido e tratado para o HD
def thread_export_excel_sheet_omie():
    t = Thread(target=export_excel_sheet_omie, args=())
    t.start()


def export_excel_sheet_omie():
    global database_pandas
    if not database_pandas.empty:
        print('\nIniciando exportação do arquivo em Excel.')
        dir_to_save = 'input_output/database.xlsx'
        database_pandas.to_excel(dir_to_save, index=False)
        print('Arquivo exportado com sucesso.\n')
    else:
        message = 'Banco de Dados vazio!\nNecessário importar ou '\
            'adicionar novos itens primeiro.'
        setTextToNotificationPopUp(message)
        print('\n' + message)



# read_omie_sheet()
"""
This file was created so I could config the virtual enviromment and install
what I would need for the course.
# """
# if __name__ == "__main__":
#     os.system('jupyter notebook')


# TODO - Utilizar Pandas para realizar a filtragem necessaria para o arquivo
# excel, e separar em algumas tabelas, como: já padronizados, faltando
# informacoes, faltando padronizar, codigo incoerente e ativo.


# TODO - Exportar uma planilha CSV possível de ser importada pelo OMIE.
def export_sheet_to_omie():
    pass


# TODO - Exportar uma planilha CSV com itens a serem comprados.
def export_sheet_to_buy():
    pass


# TODO - Exportar a planilha acima em PDF, possivelmente utilizando um layout
# pré estabelecido.
def export_sheet_to_pdf_to_buy():
    pass


# TODO - Gerar um relatório, planilha CSV/PDF, informando ao responsável do
# estoque quais itens estarão em falta, e que precisam gerar uma requisição
# de compra.
def export_report_itens_to_buy():
    pass


# TODO - Exportar uma planilha estilizada / PDF, da lista de materiais e
# apresentando informações de rastreabilidade.
def export_bom_in_excel_with_tracking():
    pass


def export_bom_in_pdf_with_tracking():
    pass


# TODO - Exportar uma planilha estilizada / PDF, da lista de materiais e
# informando a localização física no estoque para a montagem de KITs.
def export_bom_to_print_with_physical_location():
    pass


# TODO - Planilhas EXCEL devem ser fornecidas layouts pre estabelecidos, na
# qual o programa apenas irá preencher.
def import_layout_from_excel():
    pass


# TODO - Todas as listas de materiais devem possuir campos de observações.
# --> No momento vejo como processo de criação da interface/preenchimento da
# lista de materiais, e nao como uma função propriamente dita.

# TODO - Quando mostradas e/ou exportadas as listas de materiais, as cores
# devem estar visíveis e com legenda ao final da página.
# --> No momento vejo como processo de criação da interface/preenchimento da
# lista de materiais, e nao como uma função propriamente dita.
