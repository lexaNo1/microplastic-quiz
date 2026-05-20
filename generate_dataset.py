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
tipul_de_sare = np.random.choice(["Regular salt", "Sea salt"],1000)
fumatul = np.random.choice(["No", "Occasionally", "Yes"],1000)
cosmetice = np.random.choice(["Never", "Once a week", "3 times a week", "5 times a week", "Every day"], 1000)


# Calculating mg of microplastics based on scientific literature
scor_apa = { "Tap_water": 0.05, "Filtred_water": 0.15, "Bottled_water": 0.50 }
scor_alimente = {"Never":0.0, "Once a week":0.07, "3 times a week":0.21, "5 times a week":0.35, "Every day":0.70}
scor_peste_sau_fructe_de_mare = peste_sau_fructe_de_mare*0.007
scor_recipiente = {"Never":0.0, "Once a week":0.05, "3 times a week":0.15, "5 times a week":0.25, "Every day":0.50}
scor_haine = haine_sintetice * 0.002
scor_zona = {"Rural":0.0005,"Urban":0.0021,"Industrial":0.005}
scor_munca = {"Home":0.001, "Office":0.002, "Outdoors":0.004, "Factory/Industrial":0.015}
scor_interior = ore_petrecute_in_interior * 0.0000875
scor_sare = {"Regular salt":0.002, "Sea salt":0.014}
scor_fumat = {"No": 0.0, "Occasionally": 0.003, "Yes": 0.008}
scor_cosmetice ={"Never":0.0, "Once a week":0.024, "3 times a week":0.072, "5 times a week":0.120, "Every day":0.168}

#calculation formula
mg_total = (
    np.array([scor_apa[x] for x in sursa_de_apa]) * 52 +
    np.array([scor_alimente[x] for x in alimente_procesate]) * 52 +
    scor_peste_sau_fructe_de_mare * 52 +
    np.array([scor_recipiente[x] for x in recipiente_de_plastic]) * 52 +
    scor_haine * 52 +
    np.array([scor_zona[x] for x in tipul_zonei]) * 365 +
    np.array([scor_munca[x] for x in mediul_de_lucru]) * 365 +
    scor_interior * 24 * 365 +
    np.array([scor_sare[x] for x in tipul_de_sare]) +
    np.array([scor_fumat[x] for x in fumatul]) * 365 +
    np.array([scor_cosmetice[x] for x in cosmetice]) * 52
)

df = pd.DataFrame({
    "varsta": varsta,
    "sursa_de_apa": sursa_de_apa,
    "alimente_procesate": alimente_procesate,
    "peste_sau_fructe_de_mare": peste_sau_fructe_de_mare,
    "recipiente_de_plastic": recipiente_de_plastic,
    "haine_sintetice": haine_sintetice,
    "tipul_zonei": tipul_zonei,
    "mediul_de_lucru": mediul_de_lucru,
    "ore_petrecute_in_interior": ore_petrecute_in_interior,
    "tipul_de_sare": tipul_de_sare,
    "fumatul": fumatul,
    "cosmetice": cosmetice,
    "mg_total": mg_total

})
df.to_csv("dataset.csv", index=False)
print("Dataset generat cu succes!")
