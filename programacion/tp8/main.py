import csv
from datetime import datetime
from collections import defaultdict

partidos = []
equipos = defaultdict(lambda: {
    'Puntos': 0, 'PartidosJugados': 0, 'Victorias': 0, 'Empates': 0, 'Derrotas': 0, 
    'GolesAFavor': 0, 'GolesEnContra': 0, 'DiferenciaDeGoles': 0
})

def leer_fixture(nombre_archivo):
    with open(nombre_archivo, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            partidos.append({
                'Match Number': int(row['Match Number']),
                'Round Number': row['Round Number'],
                'Date': datetime.strptime(row['Date'], '%d/%m/%Y %H:%M'),
                'Location': row['Location'],
                'Home Team': row['Home Team'],
                'Away Team': row['Away Team'],
                'Group': row['Group'],
                'Result': row['Result']
            })
            equipos[row['Home Team']]
            equipos[row['Away Team']]

# Función para actualizar los resultados
def actualizar_resultados(nombre_archivo):
    with open(nombre_archivo, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            match_number = int(row['Match Number'])
            home_goals = int(row['Home Team Goals'])
            away_goals = int(row['Away Team Goals'])

            for partido in partidos:
                if partido['Match Number'] == match_number:
                    partido['Result'] = f"{home_goals}-{away_goals}"
                    actualizar_posiciones(partido['Home Team'], partido['Away Team'], home_goals, away_goals)
                    break

# Función para actualizar posiciones de los equipos
def actualizar_posiciones(home_team, away_team, home_goals, away_goals):
    equipos[home_team]['PartidosJugados'] += 1
    equipos[away_team]['PartidosJugados'] += 1
    equipos[home_team]['GolesAFavor'] += home_goals
    equipos[away_team]['GolesAFavor'] += away_goals
    equipos[home_team]['GolesEnContra'] += away_goals
    equipos[away_team]['GolesEnContra'] += home_goals
    equipos[home_team]['DiferenciaDeGoles'] += (home_goals - away_goals)
    equipos[away_team]['DiferenciaDeGoles'] += (away_goals - home_goals)

    if home_goals > away_goals:
        equipos[home_team]['Victorias'] += 1
        equipos[home_team]['Puntos'] += 3
        equipos[away_team]['Derrotas'] += 1
    elif home_goals < away_goals:
        equipos[away_team]['Victorias'] += 1
        equipos[away_team]['Puntos'] += 3
        equipos[home_team]['Derrotas'] += 1
    else:
        equipos[home_team]['Empates'] += 1
        equipos[away_team]['Empates'] += 1
        equipos[home_team]['Puntos'] += 1
        equipos[away_team]['Puntos'] += 1

# Función para calcular posiciones de los equipos en cada grupo
def calcular_posiciones():
    grupos = defaultdict(list)
    for equipo, stats in equipos.items():
        grupo = next(partido['Group'] for partido in partidos if partido['Home Team'] == equipo or partido['Away Team'] == equipo)
        grupos[grupo].append((equipo, stats))
    
    for grupo, equipos_grupo in grupos.items():
        equipos_grupo.sort(key=lambda x: (-x[1]['Puntos'], -x[1]['DiferenciaDeGoles'], -x[1]['GolesAFavor']))
        grupos[grupo] = equipos_grupo
    
    return grupos

# Función para generar el informe final
def generar_informe(nombre_archivo):
    posiciones = calcular_posiciones()
    with open(nombre_archivo, 'w', newline='') as csvfile:
        fieldnames = ['Grupo', 'Equipo', 'Puntos', 'PartidosJugados', 'Victorias', 'Empates', 'Derrotas', 'GolesAFavor', 'GolesEnContra', 'DiferenciaDeGoles']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for grupo, equipos_grupo in posiciones.items():
            for equipo, stats in equipos_grupo:
                writer.writerow({
                    'Grupo': grupo,
                    'Equipo': equipo,
                    'Puntos': stats['Puntos'],
                    'PartidosJugados': stats['PartidosJugados'],
                    'Victorias': stats['Victorias'],
                    'Empates': stats['Empates'],
                    'Derrotas': stats['Derrotas'],
                    'GolesAFavor': stats['GolesAFavor'],
                    'GolesEnContra': stats['GolesEnContra'],
                    'DiferenciaDeGoles': stats['DiferenciaDeGoles']
                })

# Cargar el fixture
leer_fixture('copa-america-2024-UTC.csv')

# Actualizar los resultados
actualizar_resultados('resultados.csv')

# Generar el informe final
generar_informe('posiciones_finales.csv')