from ninja import Ninja
from pet import Pet


belle = Pet('Belle','dog',['tug','fetch'])
roger = Pet('Roger','rabbit',['play dead'])
emile = Ninja('Emile','Thigpen',5,'Natures Own',belle,roger)

print(emile.pet1.name,emile.pet2.name)
emile.walk(2)
emile.feed(1)
emile.feed(2)
print(emile.bathe(1))
print(belle.health,roger.health)
print(belle.energy,roger.energy)
