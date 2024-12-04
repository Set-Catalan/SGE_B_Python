class cotxe:
    def __init__(self, matricula, rodes, color, portes, retrovisors):
        self.matricula = matricula
        self.rodes = rodes
        self.color = color
        self.portes = portes
        self.retrovisors = retrovisors
    
    def getMatricula(self):
        return self.matricula
    def setMatricula(self, new_matricula):
        self.matricula = new_matricula

    def getRodes(self):
        return self.rodes
    def setRodes(self, new_rodes):
        self.rodes = new_rodes
    
    def getColor(self):
        return self.color
    def setColor(self, new_color):
        self.color = new_color
    
    def getPortes(self):
        return self.portes
    def setPortes(self, new_portes):
        self.portes = new_portes
    
    def getRetrovisors(self):
        return self.retrovisors
    def setRetrovisors(self, new_retrovisors):
        self.retrovisors = new_retrovisors


class colibri:
    def __init__(self, potes, ales, edat, mida, nom):
        self.potes = potes
        self.ales = ales
        self.edat = edat
        self.mida = mida
        self.nom = nom
    
    def getPotes(self):
        return self.potes
    def setPotes(self, new_potes):
        self.potes = new_potes
    
    def getAles(self):
        return self.ales
    def setAles(self, new_ales):
        self.ales = new_ales
    
    def getEdat(self):
        return self.edat
    def setEdat(self, new_edat):
        self.edat = new_edat
    
    def getMida(self):
        return self.mida
    def setMida(self, new_mida):
        self.mida = new_mida
    
    def getNom(self):
        return self.nom
    def setNom(self, new_nom):
        self.nom = new_nom