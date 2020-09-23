import requests
import json
from decouple import config

# https://developer.atlassian.com/cloud/trello/rest/api-group-cards/#api-cards-post
# How to get the Trello Token https://trello.com/app-key
BOARD = config('TRELLO_BOARD')
KEY = config('TRELLO_KEY')
TOKEN = config('TRELLO_TOKEN')

query = {
    'key': KEY,
    'token': TOKEN
}

url = "https://api.trello.com/1/"


def request(values):
    """
    Principal request para trello.
    :param values: str: valores a serem acrescentados para o Request.
    :return: data: dict: response do request do trello.
    """
    response = requests.get(url + values, params=query)
    data = json.loads(response.text.encode('utf8'))
    return data


def load_boards():
    """
    Request para obter os BOARDs que o usuário tem, baseado no TOKEN_TRELLO e TOKEN_KEY.
        Essa função é necessária para estabelecer o BOARD a tratar.
        O board a tratar é definido no arquivo .env que fica na raiz, com o nome TOKEN_BOARD
    :return: data: list of dicts: Informações dos Boards (name, id, url).
    """
    values = 'members/me/boards?fields=name,url'
    response = request(values)
    for i in response:
        if i['name'] == BOARD:
            global ID_BOARD
            ID_BOARD = i['id']
    return response


def board_info():
    """
    Obtem a informação de um board
        Precisa da execução previa de load_boards()
        O board a tratar é definido no arquivo .env que fica na raiz, com o nome TOKEN_BOARD
    :return: response: dict: Informações do board (id, name, url, labels, backgroundImage, etc)
    """
    info_board = f'boards/{ID_BOARD}'
    response = request(info_board)
    return response


def labels():
    """
    Obtem a informação dos labels de um determinado board
        Precisa da execução previa de load_boards()
        O board a tratar é definido no arquivo .env que fica na raiz, com o nome TOKEN_BOARD
    :return: response: List of dicts: Informações dos labels (id, idBoard, name e color)
    """
    info_labels = f'boards/{ID_BOARD}/labels'
    response = request(info_labels)
    return response


def id_of_labels(list_of_labels):
    """
    Procura os id dos labels a partir do nome deles. se não acha nada, retorna uma lista vazía.
    :param list_of_labels: list: nome dos labels.
    :return: response: List: Id dos labels do board definido no arquivo .env
    """
    ids = []
    for j in list_of_labels:
        for i in labels():
            if i['name'] == j:
                ids.append(i['id'])
    return ids


def lists_of_lists():
    """"
    Obtem as listas no Board.
    Precisa da execução previa de load_boards()
        O board a tratar é definido no arquivo .env que fica na raiz, com o nome TOKEN_BOARD
    :return: response: List of dicts: Informações de cada lista (id, name, idBoard, closed, pos, softLimit e subscribed)
    """
    info_lists = f'boards/{ID_BOARD}/lists'
    response = request(info_lists)
    return response


def id_of_list(name_of_list):
    """
    Procura o id da lista a partir do nome dela.
    Precisa da execução previa de load_boards()
        O board a tratar é definido no arquivo .env que fica na raiz, com o nome TOKEN_BOARD
    :param name_of_list: str: nome da lista
    :return: str: id interno no trello da lista
    """
    for dicts in lists_of_lists():
        if dicts['name'] == name_of_list:
            id = dicts['id']
    return id


def members():
    """
    Obtem informações dos membros associado ao board.
    Precisa da execução previa de load_boards()
        O board a tratar é definido no arquivo .env que fica na raiz, com o nome TOKEN_BOARD
    :return:List of dicts: Informações dos membros (id, username, fullName)
    """
    membersofboard = f'boards/{ID_BOARD}/members'
    response = request(membersofboard)
    return response


def id_of_members(list_of_members):
    """
    Procura os id dos membros a partir do nome deles. se não acha nada, retorna uma lista vazía.
    :param list_of_membros: list: nome dos membros.
    :return: response: List: Id dos membros que acha na trello, se não não acrescentará o id na lista.
    """
    ids = []
    for j in list_of_members:
        for i in members():
            if i['fullName'].split()[0] == j.split()[0]:
                ids.append(i['id'])
    return ids


def create_card(idList, name, description, members, labels):
    """
    :param idList(str): id of the list where the card will be
    :param name(str): name of the card, comes from movidesk
    :param description(str): description of the card, comes from movidesk
    :param members[list of member IDs]: members of the card. comes from get_trello.members()
    :param labels[list of label IDs]: labels of the card. comes from get_trello.members()
    :return:
    """
    url = "https://api.trello.com/1/cards"
    query["idList"] = idList
    query["name"] = name
    query["desc"] = description
    if len(members):
        query["idMembers"] = members
    if len(labels):
        query["idLabels"] = labels
    query["pos"] = 'top'
    response = requests.post(url, params=query)
    if response.status_code == 200:
        data = json.loads(response.text.encode('utf8'))
    else:
        data = response.text
    return data


if __name__ == '__main__':
    data0 = load_boards()
    # data1 = board_info()
    # data2 = lists_of_lists()
    # data3 = members()
    # data4 = labels()
    # data5 = id_of_list('Lista de tareas')
    # data6 = id_of_labels(['Verde', 'Azul', 'Morado'])
    # data6 = id_of_members(['Alfonso Areiza', 'Fabio Sanches', 'Thiago'])
    # data7 = create_card()
    # print(data4)
    print(json.dumps(data0, indent=2))
