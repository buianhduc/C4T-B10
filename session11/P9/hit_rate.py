import random
skills = [
    {
        'Name':'Tackle',
        'Minimum level':1,
        'Damage':5,
        'Hit rate' : 0.3,
    },
    {
        'Name':'Quick Attack',
        'Minimum level':2,
        'Damage':3,
        'Hit rate' : 0.5,
    },
    {
        'Name':'Strong Kick',
        'Minimum level':4,
        'Damage':9,
        'Hit rate' : 0.2,
    }
]

lev = int(input("Enter your character's level: "))
print("Choose skill")

count = 0 

for skill in skills :
    count+=1
    print(count,". ",end = "")
    for key in skill:
        print(key, ': ',skill[key])
    print("\n")

choice = int(input("Choose skill: "))

if(skills[choice-1]['Minimum level'] > lev): print("Skill can't be used :<")
else :    
    hit = random.uniform(0,1)
    
    if(hit > skills[choice-1]['Hit rate']): print(skills[choice-1]['Damage'])
    else: print("U missed :<")

