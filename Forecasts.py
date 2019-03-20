import pandas as pd
from CuotasUso import Cuotas_forecast
from PDN import PDN_forecast
from VentaNueva import VentaNueva_forecast
from Upgrades import Upgrades_forecast

r2_cts = Cuotas_forecast
r2_pdn = PDN_forecast
r2_upg = Upgrades_forecast
r2_vts = VentaNueva_forecast

ls = []
for i in [mod for mod in globals() if mod.startswith('r2_')]:
    ls.append((i,globals()[i].r_squareds()))

df = pd.DataFrame(ls, columns = ['Model','r2'])
df.to_csv('r2.csv', index = False)
print(df)