import random
random.seed(66)

# Mean function
def mean(lstM):
    avg = 0
    for item in lstM:
        avg += item/len(lstM)
    return avg

# Summation function
def summation(lstS):
    sum1 = 0
    for item in lstS:
        sum1 += item
    return sum1

class Pokemon:
    # Pokemon(name, health, attack, sp_attack, defence, speed, experience, rank, lvltracker, type, moves, strength, weaknesses)
    def __init__(self, n, h, a, sa, d, s, e, r, lvlt, types, moves, strengths, weaknesses):
        self.name = n
        self.health = h
        self.health2 = h
        self.attack = a
        self.special_att = sa
        self.defense = d
        self.speed = s
        self.expe = e
        self.rank = r
        self.lvl_tracker = lvlt
        self.t1 = types
        self.skills = moves
        self.str = strengths
        self.w = weaknesses
        self.paired_dict_skills = [[k,v] for k, v in self.skills.items()]
        self.item = []

    # Chooses a random number that depends on the amount of the skill inputed into the pokemon character
    def random_Num(self):
        z = random.randint(0, (len(self.paired_dict_skills) - 1))
        return z

    def lvl(self):
        if self.expe > ((summation([self.health, self.attack, self.defense, self.speed*10]) * (self.lvl_tracker+1))):
            self.lvl_tracker += 1
            self.attack += (random.uniform(0.2, 0.3)) * self.attack
            self.defense += (random.uniform(0.2, 0.3)) * self.defense
            self.health += (random.uniform(0.2, 0.3)) * self.health

    def reductionHealth(self, rH):
        self.health -= rH

    def exp(self, ex):
        self.expe += ex

class Battle:
    def __init__(self, poke1, poke2):
          self.p1 = poke1
          self.p2 = poke2

    def fight(self):
          count = 0

          # Stores all necessary information for easy reference
          p1_attack = self.p1.attack
          p2_attack = self.p2.attack

          p1_special = self.p1.special_att
          p2_special = self.p2.special_att

          p1_def = self.p1.defense
          p2_def = self.p2.defense

          p1_attack2_1 = 0.045*(p1_attack)
          p1_attack2_2 = 0.02*(p1_attack)
          p1_attack2_3 = 0.001*(p1_attack)

          p2_attack2_1 = 0.045*(p2_attack)
          p2_attack2_2 = 0.02*(p2_attack)
          p2_attack2_3 = 0.001*(p2_attack)

          # If the pokemon speed is faster than the opponent
          if self.p1.speed > self.p2.speed:

              r1 = self.p1.random_Num()
              P1_attackName = self.p1.paired_dict_skills[r1][0]
              P1_moveType = self.p1.paired_dict_skills[r1][1][0]
              P1_moveSpecial = self.p1.paired_dict_skills[r1][1][1]
              P2_strengthlist = self.p2.str
              P2_weaknesseslist = self.p2.w

              ## Player 1 moves first ######
              if (P1_moveType in P2_weaknesseslist) and (P1_moveSpecial == False):
                  p1_attack3 = 2*p1_attack

                  if ((p1_attack3) - p2_def) > 0:
                    self.p2.reductionHealth(p1_attack2_1)
                  elif ((p1_attack3) - p2_def) == 0:
                    self.p2.reductionHealth(p1_attack2_2)
                  elif ((p1_attack3) - p2_def) < 0:
                    self.p2.reductionHealth(p1_attack2_3)

              elif (P1_moveType in P2_strengthlist) and (P1_moveSpecial == False):
                  p1_attack3 = (1/2)*p1_attack

                  if ((p1_attack3) - p2_def) > 0:
                    self.p2.reductionHealth(p1_attack2_1)
                  elif ((p1_attack3) - p2_def) == 0:
                    self.p2.reductionHealth(p1_attack2_2)
                  elif ((p1_attack3) - p2_def) < 0:
                    self.p2.reductionHealth(p1_attack2_3)

              elif (P1_moveType not in (P2_weaknesseslist and P2_strengthlist)) and (P1_moveSpecial == False):
                  p1_attack3 = p1_attack

                  if ((p1_attack3) - p2_def) > 0:
                    self.p2.reductionHealth(p1_attack2_1)
                  elif ((p1_attack3) - p2_def) == 0:
                    self.p2.reductionHealth(p1_attack2_2)
                  elif ((p1_attack3) - p2_def) < 0:
                    self.p2.reductionHealth(p1_attack2_3)

              elif (P1_moveType in P2_weaknesseslist) and (P1_moveSpecial == True):
                 p1_attack3 = 2*p1_special

                 if ((p1_attack3) - p2_def) > 0:
                   self.p2.reductionHealth(p1_attack2_1)
                 elif ((p1_attack3) - p2_def) == 0:
                   self.p2.reductionHealth(p1_attack2_2)
                 elif ((p1_attack3) - p2_def) < 0:
                   self.p2.reductionHealth(p1_attack2_3)

              elif (P1_moveType in P2_strengthlist) and (P1_moveSpecial == True):
                  p1_attack3 = (1/2)*p1_special

                  if ((p1_attack3) - p2_def) > 0:

                    self.p2.reductionHealth(p1_attack2_1)
                  elif ((p1_attack3) - p2_def) == 0:

                    self.p2.reductionHealth(p1_attack2_2)
                  elif ((p1_attack3) - p2_def) < 0:

                    self.p2.reductionHealth(p1_attack2_3)

              elif (P1_moveType not in (P2_weaknesseslist and P2_strengthlist)) and (P1_moveSpecial == True):
                  p1_attack3 = p1_special

                  if ((p1_attack3) - p2_def) > 0:

                    self.p2.reductionHealth(p1_attack2_1)
                  elif ((p1_attack3) - p2_def) == 0:

                    self.p2.reductionHealth(p1_attack2_2)
                  elif ((p1_attack3) - p2_def) < 0:

                    self.p2.reductionHealth(p1_attack2_3)

              self.p1.exp((mean([self.p2.attack, self.p1.defense])))

          # The actual beginning of the battle. Will keep looping until one or both have zero health.
          while (self.p1.health > 0) and (self.p2.health > 0):
              r2 = self.p2.random_Num()
              P2_attackName = self.p2.paired_dict_skills[r2][0]
              P2_moveType = self.p2.paired_dict_skills[r2][1][0]
              P2_moveSpecial = self.p2.paired_dict_skills[r2][1][1]
              P2_strengthlist = self.p2.str
              P2_weaknesseslist = self.p2.w

              r1 = self.p1.random_Num()
              P1_attackName = self.p1.paired_dict_skills[r1][0]
              P1_moveType = self.p1.paired_dict_skills[r1][1][0]
              P1_moveSpecial = self.p1.paired_dict_skills[r1][1][1]
              P1_strengthlist = self.p1.str
              P1_weaknesseslist = self.p1.w

              ## Player 2 moves ##

              if (P2_moveType in P1_weaknesseslist) and (P2_moveSpecial == False):
                  P2_attack3 = 2*p2_attack

                  if ((P2_attack3) - p1_def) > 0:
                    self.p1.reductionHealth(p2_attack2_1)
                  elif ((P2_attack3) - p1_def) == 0:
                    self.p1.reductionHealth(p2_attack2_2)
                  elif ((P2_attack3) - p1_def) < 0:
                    self.p1.reductionHealth(p2_attack2_3)

              elif (P2_moveType in P1_strengthlist) and (P2_moveSpecial == False):
                  P2_attack3 = (1/2)*p2_attack

                  if ((P2_attack3) - p1_def) > 0:
                    self.p1.reductionHealth(p2_attack2_1)
                  elif ((P2_attack3) - p1_def) == 0:
                    self.p1.reductionHealth(p2_attack2_2)
                  elif ((P2_attack3) - p1_def) < 0:
                    self.p1.reductionHealth(p2_attack2_3)

              elif (P2_moveType not in (P1_weaknesseslist and P1_strengthlist)) and (P1_moveSpecial == False):
                  P2_attack3 = p2_attack

                  if ((P2_attack3) - p1_def) > 0:
                    self.p1.reductionHealth(p2_attack2_1)
                  elif ((P2_attack3) - p1_def) == 0:
                    self.p1.reductionHealth(p2_attack2_2)
                  elif ((P2_attack3) - p1_def) < 0:
                    self.p1.reductionHealth(p2_attack2_3)

              elif (P2_moveType in P1_weaknesseslist) and (P1_moveSpecial == True):
                 P2_attack3 = 2*p2_special

                 if ((P2_attack3) - p1_def) > 0:
                   self.p1.reductionHealth(p2_attack2_1)
                 elif ((P2_attack3) - p1_def) == 0:
                   self.p1.reductionHealth(p2_attack2_2)
                 elif ((p1_attack3) - p1_def) < 0:
                   self.p1.reductionHealth(p2_attack2_3)

              elif (P2_moveType in P1_strengthlist) and (P1_moveSpecial == True):
                  P2_attack3 = (1/2)*p2_special

                  if ((P2_attack3) - p1_def) > 0:
                    self.p1.reductionHealth(p2_attack2_1)
                  elif ((P2_attack3) - p1_def) == 0:
                    self.p1.reductionHealth(p2_attack2_2)
                  elif ((P2_attack3) - p1_def) < 0:
                    self.p1.reductionHealth(p2_attack2_3)

              elif (P2_moveType not in (P1_weaknesseslist and P1_strengthlist)) and (P1_moveSpecial == True):
                  P2_attack3 = p2_special

                  if ((P2_attack3) - p1_def) > 0:
                    self.p1.reductionHealth(p2_attack2_1)
                  elif ((P2_attack3) - p1_def) == 0:
                    self.p1.reductionHealth(p2_attack2_2)
                  elif ((P2_attack3) - p1_def) < 0:
                    self.p1.reductionHealth(p2_attack2_3)

              ## Player 1 moves ##

              if (P1_moveType in P2_weaknesseslist) and (P1_moveSpecial == False):
                  p1_attack3 = 2*p1_attack

                  if ((p1_attack3) - p2_def) > 0:

                    self.p2.reductionHealth(p1_attack2_1)
                  elif ((p1_attack3) - p2_def) == 0:

                    self.p2.reductionHealth(p1_attack2_2)
                  elif ((p1_attack3) - p2_def) < 0:

                    self.p2.reductionHealth(p1_attack2_3)

              elif (P1_moveType in P2_strengthlist) and (P1_moveSpecial == False):
                  p1_attack3 = (1/2)*p1_attack

                  if ((p1_attack3) - p2_def) > 0:

                    self.p2.reductionHealth(p1_attack2_1)
                  elif ((p1_attack3) - p2_def) == 0:

                    self.p2.reductionHealth(p1_attack2_2)
                  elif ((p1_attack3) - p2_def) < 0:

                    self.p2.reductionHealth(p1_attack2_3)

              elif (P1_moveType not in (P2_weaknesseslist and P2_strengthlist)) and (P1_moveSpecial == False):
                  p1_attack3 = p1_attack

                  if ((p1_attack3) - p2_def) > 0:

                    self.p2.reductionHealth(p1_attack2_1)
                  elif ((p1_attack3) - p2_def) == 0:

                    self.p2.reductionHealth(p1_attack2_2)
                  elif ((p1_attack3) - p2_def) < 0:

                    self.p2.reductionHealth(p1_attack2_3)

              elif (P1_moveType in P2_weaknesseslist) and (P1_moveSpecial == True):
                 p1_attack3 = 2*p1_special

                 if ((p1_attack3) - p2_def) > 0:

                   self.p2.reductionHealth(p1_attack2_1)
                 elif ((p1_attack3) - p2_def) == 0:

                   self.p2.reductionHealth(p1_attack2_2)
                 elif ((p1_attack3) - p2_def) < 0:

                   self.p2.reductionHealth(p1_attack2_3)

              elif (P1_moveType in P2_strengthlist) and (P1_moveSpecial == True):
                  p1_attack3 = (1/2)*p1_special

                  if ((p1_attack3) - p2_def) > 0:
                    self.p2.reductionHealth(p1_attack2_1)
                  elif ((p1_attack3) - p2_def) == 0:
                    self.p2.reductionHealth(p1_attack2_2)
                  elif ((p1_attack3) - p2_def) < 0:
                    self.p2.reductionHealth(p1_attack2_3)

              elif (P1_moveType not in (P2_weaknesseslist and P2_strengthlist)) and (P1_moveSpecial == True):
                  p1_attack3 = p1_special
                  if ((p1_attack3) - p2_def) > 0:
                    self.p2.reductionHealth(p1_attack2_1)
                  elif ((p1_attack3) - p2_def) == 0:
                    self.p2.reductionHealth(p1_attack2_2)
                  elif ((p1_attack3) - p2_def) < 0:
                    self.p2.reductionHealth(p1_attack2_3)

              # Calculates the experience gained by each pokemon
              self.p1.exp((count+1)*(mean([self.p2.attack, self.p1.defense])))
              self.p2.exp((count+1)*(mean([self.p1.attack, self.p2.defense])))
              count += 1


t = 0
rounds = 1000
itemCounter = 0
Winner_Tracker = []

while t < rounds:
    # Pokemon(name, health, attack, sp_attack, defence, speed, experience, rank, lvltracker, type, moves, strength, weaknesses)
    R1 = Pokemon("MewtwoX",  106, 190, 154, 100, 130, 0, 1, 0, "PSYCHIC", {"Swift":["NORMAL", True], "Life Dew":["WATER", False], "Laser Focus":["NORMAL", False], "Disable":["NORMAL", False], "Confusion":["PSYCHIC", True]}, ["FIGHTING", "PSYCHIC"], ["BUG", "GHOST", "DARK"])
    R2 = Pokemon("Rayquaza", 105, 180, 180, 100, 115, 0, 2, 0, "DRAGON", {"Twister":["DRAGON", True], "Scary Face":["NORMAL", False], "Ancient Power":["ROCK", True], "Crunch":["DARK", False]}, ["FIRE", "WATER", "ELECTRIC", "GRASS", "FIGHTING", "BUG"], ["ICE","DRAGON", "GHOST", "FAIRY"])
    R3 = Pokemon("Groudon", 100, 180, 150, 90, 90, 0, 3, 0, "GROUND", {"Ancient Power":["ROCK", True], "Scary Face":["NORMAL", False], "Mud Shot":["GROUND", True], "Earth Power":["GROUND", True], "Lava Plume":["FIRE", True]}, ["FIRE", "WATER", "ELECTRIC", "POISON", "BUG", "STEEL", "FAIRY"], ["GROUND"])
    R4 = Pokemon("Tyranitar", 100, 164, 95, 120, 71, 0, 4, 0, "ROCK", {"Fire Fang":["FIRE", False], "Ice Fang":["ICE", False], "Iron Defense":["STEEL", False], "Leer":["NORMAL", False], "Payback":["Dark", False]}, ["FIRE", "WATER", "ELECTRIC", "POISON", "BUG", "STEEL", "FAIRY"], ["GROUND"])
    R5 = Pokemon("Kyogre", 100, 150, 180, 160, 90, 0, 5, 0, "WATER", {"Ancient Power":["ROCK", True], "Water Pulse":["WATER", True], "Scary Face":["NORMAL", False], "Aqua Tail":["WATER", False], "Body Slam":["NORMAL", False]}, ["FIRE", "WATER", "ICE", "STEEL"], ["ELECTRIC", "GRASS"])
    R6 = Pokemon("MewtwoY", 106, 150, 194, 120, 140, 0, 6, 0, "PSYCHIC", {"Swift":["NORMAL", True], "Life Dew":["WATER", False], "Laser Focus":["NORMAL", False], "Disable":["NORMAL", False], "Confusion":["PSYCHIC", True]}, ["FIGHTING", "PSYCHIC"], ["BUG", "GHOST", "DARK"])
    R7 = Pokemon("Salamence", 95, 145, 120, 90, 120, 0, 7, 0, "ROCK", {"Bite":["DARK", False], "Dragon Tail":["DRAGON", False], "Ember":["FIRE", True], "Fire Fang":["FIRE", False], "Fly":["FLYING", False]}, ["FIRE", "WATER", "GRASS", "FIGHTING", "BUG"], ["ICE", "ROCK", "DRAGON", "FAIRY"])
    R8 = Pokemon("Arceus", 120, 120, 120, 120, 120, 4, 8, 0, "ROCK", {"Cosmic Power":["PSYCHIC", False], "Natural Gift":["NORMAL", False], "Punishment":["DARK", False], "Seismic Toss":["FIGHTING", False], "GRAVITY":["PSYCHIC", False]}, ["GHOST"], ["FIGHTING"])
    lst_Pokemons = [R1, R2, R3, R4, R5, R6, R7, R8]

    j = 0
    lst_Pokemons2 = lst_Pokemons
    i = len(lst_Pokemons2)
    k = len(lst_Pokemons2) - 1

    # Calculates
    while i > 1:
        # Choose 2 random pokemons to battle
        A = lst_Pokemons2[random.randint(j,k)]
        B = lst_Pokemons2[random.randint(j,k)]

        # To handle the event where the pokemons chosen are the same
        while A == B:
            A = lst_Pokemons2[random.randint(j,k)]
            B = lst_Pokemons2[random.randint(j,k)]

        C = Battle(A , B)
        C.fight()

        # If functions to check who wins and who lost. Level up the winner.
        if (A.health > 0) and (B.health <= 0):
            A.health += ((random.uniform(0.35,0.4))*A.health2)
            A.lvl() #Levels up A
            lst_Pokemons2.remove(B)

        # Get rid of pokemon A instead of pokemon B
        elif (B.health > 0) and (A.health <= 0):
            B.health += ((random.uniform(0.35,0.4))*B.health2)
            B.lvl() #Levels up B
            lst_Pokemons2.remove(A)

        # Remove both if both dies during the last turn
        elif (B.health <= 0) and (A.health <= 0):
            lst_Pokemons2.remove(A)
            lst_Pokemons2.remove(B)
            k -= 1
            i -= 1
        k-=1
        i -= 1

    # Append the winners name or append "No winner" to a winner tracker list
    if len(lst_Pokemons2) == 1:
        Winner_Tracker.append(lst_Pokemons2[0].name)

    elif len(lst_Pokemons2) == 0:
        Winner_Tracker.append("No winner")

    # Prints out how many rounds are left
    print("Rounds left  = ", (rounds - t - 1))
    t+=1

z = 1
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0

# Counts how many each name won
for item in Winner_Tracker:
     if item == "MewtwoX":
         count1 += 1
     if item == "Rayquaza":
         count2 += 1
     if item == "Groudon":
         count3 += 1
     if item == "Tyranitar":
         count4 += 1
     if item == "Kyogre":
         count5 += 1
     if item == "MewtwoY":
         count6 += 1
     if item == "Salamence":
         count7 += 1
     if item == "Arceus":
         count8 += 1
     if item == "No winner":
         count9 += 1
     z+=1

# Prints out the number of wins and winrate of the pokemon
print("MewtwoX = {} with winrate of {}%".format(count1, (count1/summation([count1, count2, count3, count4, count5, count6, count7, count8]))*100))
print("Rayquaza = {} with winrate of {}%".format(count2, (count2/(summation([count1, count2, count3, count4, count5, count6, count7, count8])))*100))
print("Groudon = {} with winrate of {}%".format(count3, (count3/(summation([count1, count2, count3, count4, count5, count6, count7, count8]))) * 100))
print("Tyranitar = {} with winrate of {}%".format(count4, (count4/(summation([count1, count2, count3, count4, count5, count6, count7, count8])))*100))
print("Kyogre = {} with winrate of {}%".format(count5, (count5/(summation([count1, count2, count3, count4, count5, count6, count7, count8]))) * 100))
print("MewtwoY = {} with winrate of {}%".format(count6, (count6/(summation([count1, count2, count3, count4, count5, count6, count7, count8]))) * 100))
print("Salamence = {} with winrate of {}%".format(count7, (count7/(summation([count1, count2, count3, count4, count5, count6, count7, count8]))) * 100))
print("Arceus = {} with winrate of {}%".format(count8, (count8/(summation([count1, count2, count3, count4, count5, count6, count7, count8]))) * 100))

print("count no winners = {}".format(count9))
