from data.listeCibi import lista_carbo, lista_proteine, lista_verdure
from verdure import Verdure
from proteine import Proteine
from carboidrati import Carboidrati
import random

tabella_tot={
             "lunedi":{
             "pranzo":{"proteine": Proteine("", "", 0).to_string(), "verdure": Verdure("", "", 0, "").to_string(), "carboidrati": Carboidrati("", "", 0).to_string()}, 
             "cena":{"proteine": Proteine("", "", 0).to_string(), "verdure": Verdure("", "", 0, "").to_string(), "carboidrati": Carboidrati("", "", 0).to_string()},
              }, 
             "martedi":{
             "pranzo":{"proteine": Proteine("", "", 0).to_string(), "verdure": Verdure("", "", 0, "").to_string(), "carboidrati": Carboidrati("", "", 0).to_string()}, 
             "cena":{"proteine": Proteine("", "", 0).to_string(), "verdure": Verdure("", "", 0, "").to_string(), "carboidrati": Carboidrati("", "", 0).to_string()},
              }, 
             "mercoledi":{
             "pranzo":{"proteine": Proteine("", "", 0).to_string(), "verdure": Verdure("", "", 0, "").to_string(), "carboidrati": Carboidrati("", "", 0).to_string()}, 
             "cena":{"proteine": Proteine("", "", 0).to_string(), "verdure": Verdure("", "", 0, "").to_string(), "carboidrati": Carboidrati("", "", 0).to_string()},
              }, 
             "giovedi":{
             "pranzo":{"proteine": Proteine("", "", 0).to_string(), "verdure": Verdure("", "", 0, "").to_string(), "carboidrati": Carboidrati("", "", 0).to_string()}, 
             "cena":{"proteine": Proteine("", "", 0).to_string(), "verdure": Verdure("", "", 0, "").to_string(), "carboidrati": Carboidrati("", "", 0).to_string()},
              }, 
             "venerdi":{
             "pranzo":{"proteine": Proteine("", "", 0).to_string(), "verdure": Verdure("", "", 0, "").to_string(), "carboidrati": Carboidrati("", "", 0).to_string()}, 
             "cena":{"proteine": Proteine("", "", 0).to_string(), "verdure": Verdure("", "", 0, "").to_string(), "carboidrati": Carboidrati("", "", 0).to_string()},
              }, 
             "sabato":{
             "pranzo":{"proteine": Proteine("", "", 0).to_string(), "verdure": Verdure("", "", 0, "").to_string(), "carboidrati": Carboidrati("", "", 0).to_string()}, 
             "cena":{"proteine": Proteine("", "", 0).to_string(), "verdure": Verdure("", "", 0, "").to_string(), "carboidrati": Carboidrati("", "", 0).to_string()},
              }, 


            }

def crea_piano_alimentare():
    for key, value in tabella_tot.items():
        print(f"{key}\n")
        for k, v in tabella_tot[key].items():
            print(f" {k}:\n")
            for ke, va in tabella_tot[key][k].items():
                if ke == "proteine":
                    va=lista_proteine[random.randint(0,len(lista_proteine)-1)].to_string()
                elif ke == "verdure":
                    va=lista_verdure[random.randint(0,len(lista_verdure)-1)].to_string()
                else: 
                    va=lista_carbo[random.randint(0,len(lista_carbo)-1)].to_string()
                print(f"  {ke}: {va}\n")
            
        print("_________________________________________________________________________________________\n\n")

        




