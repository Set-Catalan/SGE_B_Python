# Importa les classes cotxe i colibrí del fitxer classes
from classes import cotxe, colibri

# Crea tres instàncies de la classe cotxe on els atributs són (matricula, rodes, color, portes, retrovisors)
cotxe1 = cotxe("bcd1234", 4, "vermell", 5, 3)
cotxe2 = cotxe("gtk7788", 4, "groc", 3, 2)
cotxe3 = cotxe("zyx0987", 8, "blanc", 2, 3)

# Crea tres instàncies de la classe colibrí on els atributs són (potes, ales, edat, mida, nom)
colibri1 = colibri(2, 2, 3, "9cm", "Pajarito")
colibri2 = colibri(1, 2, 4, "12cm", "Pajarraco")
colibri3 = colibri(2, 1, 2, "10cm", "Pajaro")

# Mostra els atributs color del primer cotxe, portes del segon cotxe, i matricula del tercer cotxe
print("El color del primer cotxe és", cotxe1.getColor())
print("El segon cotxe té", cotxe2.getPortes(), "portes")
print("La matricula del tercer cotxe és", cotxe3.getMatricula())

# Mostra els atributs mida i nom del primer colibrí, edat del segon colibrí, i ales del tercer colibrí
print("El primer colibrí medeix", colibri1.getMida())
print("El primer colibrí s'anomena", colibri1.getNom())
print("EL segon colibrí té", colibri2.getEdat(), "anys")
print("El tercer colibrí només té", colibri3.getAles(), "ala")

# Canvia els atributs retrovisors del segon cotxe i color del tercer cotxe, i després mostra el nou valor dels atributs
cotxe2.setRetrovisors(3)
print("El segon cotxe ara té", cotxe2.getRetrovisors(), "retrovisors")
cotxe3.setColor("negre")
print("El tercer cotxe ha sigut pintat de color", cotxe3.getColor())

# Canvia els atributs mida del primer colibrí i edat del tercer colibrí, i després mostra el nou valor dels atributs
colibri1.setMida("11cm")
print("El primer colibrí a crescut i ara medeix", colibri1.getMida())
colibri3.setEdat(3)
print("El tercer colibrí ha complert", colibri3.getEdat(), "anys")