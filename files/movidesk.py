import requests
import json
from decouple import config

TOKEN_MOVIDESK = config('MOVIDESK_TOKEN')


def get_ticket(id_ticket):
    """
    Principal request para API da movidesk
    :param id_ticket: str: Id do ticket que quero procurar.
    :return: data: dict: Informações do ticket, resposta da API do movidesk
    """
    resp = requests.get(f'https://api.movidesk.com/public/v1/tickets?token={TOKEN_MOVIDESK}&id={id_ticket}')
    if not resp.status_code == 404:
        data = json.loads(resp.text.encode('utf8'))
    else:
        data = False
    return data


def get_id(ticket_resp):
    """
    :param ticket_resp: dict: Json respondido da função get_ticket()
    :return: ticket id: str
    Ex: '18445'
    """
    return ticket_resp["id"]


def get_subject_ticket(ticket_resp):
    """
    :param ticket_resp: dict: Json respondido da função get_ticket()
    :return: assunto do ticket: str
    Ex: 'Erro no Relatório'
    """
    return ticket_resp["subject"]


def get_description_ticket(ticket_resp):
    """
    :param ticket_resp: dict: Json respondido da função get_ticket()
    :return: new_description: str: Texto inicial da criação do ticket
    """
    description = ticket_resp["actions"][0]["description"]
    new_description = clean_description(description)
    return new_description


def clean_description(txt):
    """
    Limpa texto a partir de condições
    :param txt: str:
    :return: txt: str: texto limpo
    """
    return txt


def client(ticket_resp):
    """
    Nome do cliente quem abriu o ticket (se tiver)
    :param ticket_resp: dict: Json respondido da função get_ticket()
    :return: client: str: Nome do cliente do client, se ele já está cadastrado no movidesk
    """
    client = False
    if not ticket_resp['clients'][0]['organization'] is None:
        client = ticket_resp['clients'][0]['organization']['businessName']
    return client


def parser_ticket_content(id_ticket):
    """
    Cria corpo do assunto e descrição para a criação do card no trello.
    :param id_ticket: str:
    :return: subject e description: tuple: Asunto do ticket e Texto inicial (com alguns ajustes
    aprópiados para se colocar no trello)
    """
    try:
        ticket_resp = get_ticket(id_ticket)
        id = get_id(ticket_resp)
        cliente = client(ticket_resp)
        if cliente:
            subject = f'# {id} - {get_subject_ticket(ticket_resp)} - [{cliente}]'
        else:
            subject = f'# {id} - {get_subject_ticket(ticket_resp)}'
        link = f'Para ver mais detalhe accese a ' \
               f'[Link do Ticket # {id}](http://suporte.4yousee.com.br/Ticket/Edit/{id})\n\n----\n'
        description = link + get_description_ticket(ticket_resp)
        # print(f'Ticket # {id}\nAssunto: {subject}\n{description}\n----\nPara ver mais detalhe accese a {link}')
        return subject, description
    except Exception:
        return ('', '')


if __name__ == '__main__':
    ticket = input('Digite o Ticket ID: ')
    # name, description = parser_ticket_content(int(ticket))
    # print(f'Name : {name}, Description : {description}')
    # print(f'Name : {len(name)}, Description : {len(description)}')
    # if get_ticket(ticket):
    #     print(get_ticket(ticket))
