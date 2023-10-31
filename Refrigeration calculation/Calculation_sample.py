from CoolProp.CoolProp import PropsSI

import CoolProp

a= PropsSI('H', 'T', 273-22, 'P', 70000, 'Q', 1, 'R600a')
print(a)
