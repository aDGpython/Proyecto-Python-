import Data
import Estadio
import Partido
import Equipo
def equipos():
    print()
    print("---------------------------------------------------------------------------------------------")
    print('EQUIPOS:')
    print("Nombre                       Code Grupo")
    for team in Equipo.EquipoData:
        print(f'{team.nombre.ljust(30," ")}{team.codigo.ljust(4, " ")}{team.grupo.ljust(2, " ")}')
    print()
    print("---------------------------------------------------------------------------------------------")
    print()

def partido_equipo():
    p = 0
    print()
    print("---------------------------------------------------------------------------------------------")
    print('Seleccione un equipo: ')
    print("Num Nombre                       Code Grupo")
    for team in Equipo.EquipoData:
        print(f'{p} | {team.nombre.ljust(30," ")}{team.codigo.ljust(4, " ")}{team.grupo.ljust(2, " ")}')
        p += 1
    print()
    print("---------------------------------------------------------------------------------------------")
    print()
    while True:
        try:
            equipo = int(input("seleccione un equipo:  "))
            if 0 <= equipo < len(Equipo.EquipoData):
                selected_team = Equipo.EquipoData[equipo]
                selected_team_code = selected_team.id_equipo

                print(f"\nPartidos del equipo {selected_team.nombre}:")
                for match in Partido.PartidoData:
                    if match.home_id == selected_team_code or match.away_id == selected_team_code:
                        match_date = match.fecha
                        home_team = match.home_team
                        away_team = match.away_team
                        print(f"Fecha: {match_date} - {home_team} vs {away_team}")

                break
            else:
                print("Número de equipo inválido. Ingrese un número entre 1 y", len(Data.TeamData))
        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")
    print()
    print("---------------------------------------------------------------------------------------------")
    print()
def partido_estadio():
    print()
    print("---------------------------------------------------------------------------------------------")
    print('Seleccione un estadio: ') 
    z = 0
    print(f' | ciudad             |  estadio')
    for stadium in Estadio.EstadioData: 
        ciudad = stadium.ciudad.strip().ljust(20," ")
        estadio = stadium.nombre_estadio.ljust(30," ")
        print(f'{z}|{ciudad}|{estadio}')  
        z += 1
    print()
    print("---------------------------------------------------------------------------------------------")
    print()
    while True:
        try:
            estadio = int(input("Ingrese el número del estadio:  "))
            if estadio < z:
                estadio_seleccionado = Estadio.EstadioData[estadio]
                print(f"\nPartidos en el estadio {estadio_seleccionado.nombre_estadio}:")
                for match in Partido.PartidoData:
                    if match.id_estadio == estadio_seleccionado.id_estadio:
                        match_date = match.fecha.ljust(10," ")
                        home_team = match.home_team.ljust(30," ")
                        away_team = match.away_team.ljust(30," ")
                        print(f"{match_date}: {home_team} vs {away_team}")
                break
            else:
                print("Número de estadio inválido. Ingrese un número entre 1 y", z)
        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")
    print()
    print("---------------------------------------------------------------------------------------------")
    print()
def partido_fecha():
    print()
    print("---------------------------------------------------------------------------------------------")
    print('Seleccione una fecha: ')
    unique_dates = set()
    z = -1 
    for i, match in enumerate(Partido.PartidoData):
        date = match.fecha
        z+= 1
        if date not in unique_dates:
            unique_dates.add(date)
            print(f'{z}| Fecha: {date}')
    print()
    print("---------------------------------------------------------------------------------------------")
    print()

    while True:
        try:
            fecha = int(input("Ingrese el número de la fecha:  "))
            if 0 <= fecha < len(Partido.PartidoData):
                selected_match = Partido.PartidoData[fecha]
                selected_date = selected_match.fecha

                print(f"\nPartidos para la fecha {selected_date}:")
                for match in Partido.PartidoData:
                    if match.fecha == selected_date:
                        home_team = match.home_team
                        away_team = match.away_team
                        print(f"{home_team} vs {away_team}")

                break
            else:
                print("Número de fecha inválido. Ingrese un número entre 1 y", len(Partido.PartidoData))
        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")
    print()
    print("---------------------------------------------------------------------------------------------")
    print()

def menu():
    while True: 
        print("\nGestion de partidos y estadios:\n")
        print("1. Carga de datos externos") 
        print("2. Lista de equipos")
        print("3. Partidos por estadio")
        print("4. Partidos por fecha")
        print("5. Partidos por equipo")
        print("0. SALIR")
        x=input("Ingrese el numero de la opcion:  ")
        match x:
            case "1":
                Data.ReloadAPI()
            case "2":
                equipos()
            case "3":
                partido_estadio()
            case "4":
                partido_fecha()
            case "5":
                partido_equipo()   
            case "0":
                break     
            case _:  
                print("Opcion invalida")