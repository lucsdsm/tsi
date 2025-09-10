import random

bois = {i: random.randint(300, 1500) for i in range(1, 90)}

boimagro = min(bois, key=bois.get)
pesoboimagro = bois[boimagro]

boigordo = max(bois, key=bois.get)
pesoboigordo = bois[boigordo]

print(f'O boi de menor peso é o boi com identificação {boimagro}, que tem {pesoboimagro} kilos.')
print(f'O boi de maior peso é o boi com identificação {boigordo}, que tem {pesoboigordo} kilos.')
