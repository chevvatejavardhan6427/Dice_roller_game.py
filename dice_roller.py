
dict_dice={

1:("┌─────────┐",
   "│                      │",
   "│          ●          │",
   "│                      │",
   "└─────────┘"),
2:("┌─────────┐",
    "│  ●                   │",
    "│                       │",
    "│                    ● │",
    "└─────────┘" ),
3:("┌─────────┐",
    "│   ●                 │",
    "│          ●          │",
    "│                   ● │",
    "└─────────┘" ),
4:("┌─────────┐",
     "│●                  ● │",
     "│                        │",
     "│●                  ● │",
     "└─────────┘" ),
5:("┌─────────┐",
    "│  ●                ●│",
    "│            ●        │",
    "│  ●                ●│",
    "└─────────┘" ),
6:("┌─────────┐",
    "│ ●               ●  │",
    "│ ●               ●  │",
    "│ ●               ●  │",
    "└─────────┘" )
   
}
total=0
import random
noofdices=int(input("enter how many are you going to di  : "))
for n in range(noofdices):
	dice=int(random.randint(1,6))
	total+=dice
	for di in dict_dice.get(dice):
		print(di)
		
print(total)
