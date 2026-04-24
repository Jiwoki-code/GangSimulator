import random

genders = ["male", "female"]

noms_famille_japonais = [
    "Sato", "Suzuki", "Takahashi", "Tanaka", "Watanabe",
    "Ito", "Yamamoto", "Nakamura", "Kobayashi", "Kato",
    "Yoshida", "Yamada", "Sasaki", "Yamaguchi", "Saito",
    "Matsumoto", "Inoue", "Kimura", "Hayashi", "Shimizu"
]

prenoms_masculins = [
    "Haruto", "Ren", "Sota", "Kaito", "Riku",
    "Asahi", "Yuto", "Tsubasa", "Daiki", "Shun",
    "Kenji", "Hiroto", "Takumi", "Sosuke", "Ryo"
]

prenoms_feminins = [
    "Sakura", "Hina", "Yui", "Aoi", "Ichika",
    "Mio", "Nanami", "Koharu", "Akari", "Misaki",
    "Yuna", "Himari", "Rin", "Mei", "Ayaka"
]

statuses = [
    {'name': "police", 'prob': 15},
    {'name': "brigand", 'prob': 30},
    {'name': "fixer", 'prob': 10},
]

class character: 
    def __init__(self, age, name, forname, gender, loyalty, friend, status):
        self.age = age
        self.name = name
        self.forname = forname
        self.gender = gender
        self.loyalty = loyalty
        self.friend = friend
        self.status = status

def selectRandomStatuses():
    result = []
    for x in statuses:
        if random.randrange(0, 100) < x['prob']:
            result.append(x['name'])
    if result == []:
        result = ["civil"]
    return result

def generateRandomChar():

    forname = noms_famille_japonais[random.randrange(0,len(noms_famille_japonais))]
    gender = genders[random.randrange(0, len(genders))]
    name = ""
    if gender == "male":
        name = prenoms_masculins[random.randrange(0,len(prenoms_masculins))]
    else:
        name = prenoms_feminins[random.randrange(0,len(prenoms_feminins))]
    loyalty = random.randrange(25,75)
    status = selectRandomStatuses()

    char = character(100, name, forname, gender, loyalty, False, status)

    return char

cities = [
    {'name': "Tokyo", "pop": [], "max_pop": 100}
]

def generatePop():
    i = 0
    while i < 10:
        cities[0]["pop"].append(generateRandomChar())
        i += 1

generatePop()

for x in cities[0]["pop"]:
  print(x.name, x.forname, x.gender, x.loyalty, x.status) 