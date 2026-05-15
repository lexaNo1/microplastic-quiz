import numpy as np
import pandas as pd
varsta = np.random.randint(18, 80, 1000)
sursa_de_apa = np.random.choice(["Tap_water", "Filtred_water", "Bottled_water"], 1000)
alimente_procesate = np.random.choice(["Never", "Once a week", "3 times a week", "5 times a week", "Every day"], 1000)
peste_sau_fructe_de_mare = np.random.randint(0, 15, 1000)
recipiente_de_plastic = np.random.choice(["Never", "Once a week", "3 times a week", "5 times a week", "Every day"], 1000)
haine_sintetice = np.random.randint(0, 100, 1000)
tipul_zonei = np.random.choice(["Rural","Urban","Industrial"],1000)
mediul_de_lucru = np.random.choice(["Office", "Factory/Industrial", "Outdoors", "Home"], 1000)
ore_petrecute_in_interior = np.random.randint(0, 24, 1000)
tipul_de_sare = np.random.choice(["Regular salt", "Sea Salt"],1000)
fumatul = np.random.choice(["No", "Occasionally", "Yes"],1000)
cosmetice = np.random.choice(["Never", "Once a week", "3 times a week", "5 times a week", "Every day"], 1000)