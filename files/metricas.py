import json
import requests
from files.movidesk import TOKEN_MOVIDESK

query = {
    'token': TOKEN_MOVIDESK,
}

url = "https://api.movidesk.com/public/v1/tickets"
tipo_de_ticket = ['Tarefa', 'Pergunta', 'Problema', 'Sugestão', 'Crítica', 'Incidente']


def tickets(*dates):
    """
    Recebe uma tupla com data inicial e data final
    :param dates(str): exemplo: '08-21' e '08-27'
    :return: json com todos os tickets no estado atual deles dentro do intervalo das datas recebidas
    """
    query['$select'] = 'id,category,status,createdDate,ResolvedIn,lifeTimeWorkingTime,subject'
    query['$filter'] = f'createdDate ge 2020-{dates[0]} and createdDate le 2020-{dates[1]}'
    query['$orderby'] = 'id desc'
    response = requests.get(url, params=query)
    if response.status_code == 200:
        data = json.loads(response.text.encode('utf8'))
    else:
        data = response.text
    return data

def no_filter(info_tickets):
    pass

def filter_by_one_category(info_tickets, category='Problema'):
    """
    Essa função recebe o json com os tickets e filtra por category
    :param info_tickets: Todos os tickets em formato json. Costuma receber o json gerado da função tickets()"
    :return: json segundo filtro com os tickets do tipo escolhido e a media de tempo resolução deles
    """
    all_prome, hourpromedio, minutepromedio = 0, 0, 0
    all_tickets = []
    for ticket in info_tickets:
        if ticket['category'] in tipo_de_ticket and (ticket['status'] == 'Resolvido' or ticket['status'] == 'Fechado'):
            if ticket['category'] == category:
                ticket['lifeTimeWorkingTimeInHours'] = minutes_to_hourformat(ticket['lifeTimeWorkingTime'])
                all_prome += ticket['lifeTimeWorkingTime']
                all_tickets.append(ticket)
    if all_prome > 0:
        all_prome = all_prome / len(all_tickets)
        all_prome = minutes_to_hourformat(all_prome)
    return all_tickets, all_prome


def minutes_to_hourformat(minutos):
    """
    Essa função transforma minutos a horas
    :param minutos(str): Ex: 4581
    :return: 76:21:00
    """
    horas = int(minutos // 60)
    minutos = int(minutos % 60)
    return f'{horas}:{minutos}:00'


def execution():
    """
    Essa função lê a data inicial e data final e consulta a media de tempo de resolução dos tickets tipo problema
    :return: nothing
    """
    cicle = True
    print(4*'==',' Esse programa calcula a media de resolução dos tickets tipo PROBLEMA num intervalo de datas ',9*'==')
    while cicle == True:
        try:
            initialDate = input('Qual é a Data Inicial [mm-dd] : ')
            endDate = input('Qual é a Data Final [mm-dd] : ')
            result_of_tickets = tickets(initialDate, endDate)
            tipo = 'Problema'
            all_tickets, promedio = filter_by_one_category(result_of_tickets, category=tipo)
            print(f'Total de tickets tipo {tipo} \t: {len(all_tickets)}')
            if len(result_of_tickets):
                print(f'Promedio de Resolução \t\t\t: {promedio}')
            print(json.dumps(all_tickets, indent=2))
            decision = True
        except Exception:
            print('Lembre de escrever a data no formato mm-dd, Exemplo: 08-21 ou 08-01 ')
            decision = False

        while decision == True:
            try:
                decision = input('Quer consultar outro intervalo? (S/N) : ').upper()
                if decision == 'N':
                    cicle = False
                elif decision == 'S':
                    cicle = True
                else:
                    decision = True
            except Exception:
                print('Pode digitar só S caso queira consultar outro invervalo ou N caso não queira')


if __name__ == '__main__':
    execution()
