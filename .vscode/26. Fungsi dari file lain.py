import os
os.system("cls")

import Rumus_Fisika as Rumus
from importlib import reload
reload(Rumus)

print(f'''
1. Hukum Newton 2 : 
--> {Rumus.Hukum_Newton_2(11,3)}
''')

print(f'''
2. Hukum Ohm :
--> {Rumus.Hukum_Ohm(2,3)}
''')

print(f'''
3. Energi Kinetik :
--> {Rumus.Energi_Kinetik(2,3)}
''')