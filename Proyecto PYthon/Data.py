import requests 
import json 
import Cliente
import Entrada
import Venta
import VentaRest
import VentaRestProducto
import Equipo
import Partido
import Estadio
import Restaurante
import Producto

TeamData: list = []
TempData: list = []
MatchesData: list = []


def BuscaStadium(id):
    for item in TempData:
        if item["id"] == id:
            return item["name"]
    return None 

def SaveData():
    global TeamData, TempData, MatchesData

    TeamFile = open('TeamsData.txt','w')
    TeamFile.write(json.dumps(TeamData))
    TeamFile.close()

    StadiumFile = open('StadiumData.txt','w')
    StadiumFile.write(json.dumps(TempData))
    StadiumFile.close()

    MatchesFile = open('MatchesData.txt','w')
    MatchesFile.write(json.dumps(MatchesData))
    MatchesFile.close()


def LoadData():
    global TeamData, TempData, MatchesData

    StadiumFile = open("StadiumData.txt","r")
    tempData = StadiumFile.read()
    TempData = json.loads(tempData)
    StadiumFile.close()

    MatchesFile = open("MatchesData.txt","r")
    tempData = MatchesFile.read()
    MatchesData = json.loads(tempData)
    MatchesFile.close()
    Cliente.LoadData()
    Entrada.LoadData()
    Venta.LoadData()
    VentaRest.LoadData()
    VentaRestProducto.LoadData()
    Estadio.LoadData()
    Partido.LoadData()
    Equipo.LoadData()
    Restaurante.LoadData()
    Producto.LoadData()

def ReloadAPI():
    global TeamData, TempData, MatchesData

    matchesAPI = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json")
    teamData = matchesAPI.text
    TeamData = json.loads(teamData)
    Partido.PartidoData.clear()
    for equi in TeamData:
        pp = Partido.Partido(equi['id'].strip(),equi['home']['name'].strip(),equi['away']['name'].strip(),equi['date'].strip(),equi['group'].strip(),equi['stadium_id'].strip(),equi['home']['id'].strip(),equi['away']['id'].strip())
        Partido.PartidoData.append(pp)     
    TeamFile = open('PartidoData.txt','w')
    for i in Partido.PartidoData:
        TeamFile.write(i.to_pipe())
    TeamFile.close()

    stadiumAPI = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json")
    TempData = stadiumAPI.text
    TempEstadio = json.loads(TempData)
    Estadio.EstadioData.clear()
    Restaurante.RestauranteData.clear()
    Producto.ProductoData.clear()
    
    rcode = 0
    pcode = 0
    for Esta in TempEstadio:
        pp = Estadio.Estadio(Esta['id'].strip(),Esta['name'].strip(),Esta['capacity'][1],Esta['city'].strip(),Esta['capacity'][0])
        Estadio.EstadioData.append(pp)
        for rest in Esta['restaurants']:
            rr = Restaurante.Restaurante(rcode, Esta['id'].strip(), rest['name'])
            Restaurante.RestauranteData.append(rr)
            for prod in rest['products']:
                zz = Producto.Producto(rcode, prod['name'].strip(), prod['price'].strip(), prod['quantity'], 0, Esta['id'], pcode, prod['adicional'])
                Producto.ProductoData.append(zz)
                pcode += 1
            rcode += 1 
    EstadioFile = open('EstadioData.txt','w')
    for i in Estadio.EstadioData:
        EstadioFile.write(i.to_pipe())
    EstadioFile.close()
    EstadioFile = open('ProductoData.txt','w')
    for i in Producto.ProductoData:
        EstadioFile.write(i.to_pipe())
    EstadioFile.close()
    EstadioFile = open('RestauranteData.txt','w')
    for i in Restaurante.RestauranteData:
        EstadioFile.write(i.to_pipe())
    EstadioFile.close()

    
    teamAPI = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json")
    matchesData = teamAPI.text
    MatchesData = json.loads(matchesData)
    Equipo.EquipoData.clear()
    for Esta in MatchesData:
        pp = Equipo.Equipo(Esta['id'].strip(),Esta['name'].strip(),Esta['code'].strip(),Esta['group'].strip())
        Equipo.EquipoData.append(pp)
    EstadioFile = open('EquipoData.txt','w')
    for i in Equipo.EquipoData:
        EstadioFile.write(i.to_pipe())
    EstadioFile.close()
    # SaveData()
    print("Data externa descargada!")


LoadData()
