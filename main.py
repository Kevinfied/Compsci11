"""
generator2.py

generates a truly randomized clash royale deck
"""

from random import *


commonCards = ["Goblins","Knight","Archers","Barbarians","Minions","Minion Horde","Royal Giant","Ebarbs","Bomber","Fire Spirit","Ice Spirit","Skeletons","Spear Goblins","Goblin Gang","Royal Recruits","Bats","Rascals","Skeleton Barrel","Fire Cracker","Skeleton Dragons","E spirit"]

commonBuildings = ["Cannon","Mortar","Tesla"]

commonSpells = ["Arrows","Zap","Snowball","Delivery"]

rareCards = ["Giant","Valk","Musketeer","Wizard","Mini p","Hog Rider","3M","Battle Ram","Ice Golem","Mega Minion","Dart Goblin","Zappies","Flying Machine","Royal Hogs","E Golem","Battle Healer","Heal Spirit"]

rareBuildings = ["Goblin Hut","Inferno Tower","Bomb Tower","Barb Hut","Pump","Tombstone","Furnace","Goblin Cage"]

rareSpells = ["Fire Ball","Rocket","Earthquake"]

epicCards = ["Pekka","Balloon","Witch","Golem","Skarmy","Baby Dragon","Prince","Giant Skeleton","Guards","Dark Prince","Bowler","Hunter","Exe","Cannon Cart","Wall Breakers","Goblin Giant","E Dragon","E Giant","Goblin Barrel","Mirror"]

epicBuildings = ["Xbow","Goblin Drill"]

epicSpells = ["Rage","Freeze","Lightning","Poison","Tornado","Clone","Barb Barrel"]

legendaryCards = ["Ice Wiz","Princess","Lava Hound","Miner","Sparky","Lumberjack","I-Drag","E Wiz","Bandit","Night Witch","Ghost","Ram Rider","MEGA NUT","Fisherman","Magic Archer","Mother Witch","Phoenix","Graveyard"]

legendarySpell = ['Log']

champions = ["Mighty Miner","Archer Queen","Skeleton King","Golden Knight","Monk"]

troops = commonCards + rareCards + epicCards + legendaryCards

buildings = commonBuildings + rareBuildings + epicBuildings

spells = commonSpells + rareSpells + epicSpells + legendarySpell

bundle = troops + buildings + spells

# Shuffle - To randomize 

shuffle(buildings)
shuffle(troops)
shuffle(spells)


# Troops
print("""Your Troops:
""")
for i in range(5):
  print(troops[i])
print("------------------")

# Spells
print("""Your spells are:
""")
for i in range(2):
  print(spells[i])
print("--------------------")

# Buildings
print("""Your building will be:
""")
for i in range(1):
  print(buildings[i])

print("""
HEHEHEHAW 😂""")