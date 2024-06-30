PartidoData: list = []

class Partido:
    def __init__(self, id_partido, home_team, away_team, fecha, grupo, id_estadio, home_id, away_id):
        self.id_partido = id_partido
        self.home_team = home_team
        self.away_team = away_team
        self.fecha = fecha
        self.grupo = grupo
        self.id_estadio = id_estadio
        self.home_id = home_id
        self.away_id = away_id
    def to_pipe(self):
        return self.id_partido +'|'+self.home_team+'|'+self.away_team+'|'+self.fecha+'|'+self.grupo+'|'+self.id_estadio+'|'+self.home_id+'|'+self.away_id+"\n"
    
def BuscaPartido(id):
    for item in PartidoData:
        if item.id_partido.strip() == str(id).strip():
            return item
    return None 

def SalvaPartido(home_team):
    PartidoData.append(home_team)
    print(PartidoData)
    TeamFile = open('PartidoData.txt','w')
    for i in PartidoData:
        TeamFile.write(i.to_pipe())
    TeamFile.close()




def LoadData():
    PartidoData.clear()

    PartidoFile = open("PartidoData.txt","r")
    Lines = PartidoFile.readlines()

    for line in Lines:
        pp=line.split("|")
        PartidoData.append(Partido(pp[0],pp[1],pp[2],pp[3],pp[4],pp[5],pp[6],pp[7]))
    PartidoFile.close()



