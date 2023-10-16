import datetime

dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]

data_atual = datetime.datetime.today()
dia_semana_atual = dias_semana[data_atual.weekday()]

print(f'Dia da semana atual: {dia_semana_atual}')

