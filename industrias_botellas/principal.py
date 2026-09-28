from botella_termica import BotellaTermica
from termica_plastica import TermicaPlastica
from termica_vidrio import TermicaVidrio

botella_deportiva = TermicaPlastica("750 ml", "cilindrica", "antideslizante", "tapa deportiva", "medidas laterales")
botella_cafe = TermicaVidrio("500 ml", "recta", "elegante", "tapa hermetica", "hojas decorativas")

print(botella_deportiva.llenar("agua con hielo"))
print(botella_deportiva.servir())
print(botella_deportiva.precintar())
print(botella_deportiva.llevar())
print(botella_deportiva.sostener())
print(botella_deportiva.uso_en_bebidas("frias"))
print(botella_deportiva.reciclar())
print(botella_deportiva.se_ve_el_liquido())

print(botella_cafe.llenar("cafe caliente"))
print(botella_cafe.servir())
print(botella_cafe.precintar())
print(botella_cafe.llevar())
print(botella_cafe.sostener())
print(botella_cafe.uso_en_bebidas("calientes"))
print(botella_cafe.reciclar())
print(botella_cafe.se_ve_el_liquido())
