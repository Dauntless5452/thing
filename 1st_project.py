import random
import time

rifle_ammo = 10
remaining_health = 100
current_target = 100
shields = 50
health = 10
target_AC = 10
hit_modifier = 2
player_AC = 13
worm_modifier = 2
worm = 1
items = ["grenade", "Med kit", "Portable radio tower"]

def rifle_shot():
    global rifle_ammo, remaining_health, current_target, target_AC, hit_modifier
    if rifle_ammo <= 0:
        print("you are out of rifle ammo, find a spot to reload")
    else:
        print("BANG BANG, you open fire")
        hit = random.randint(0,21)
        rifle_ammo -= 1
        if hit + hit_modifier >= target_AC:
            damage = random.randint(10,20)
            remaining_health = remaining_health - damage
            damage = str(damage)
            print("you hit and deal " + damage + " damage")
        else:
            print("your rifle bolt misses")
    
def worm_attack():
    print("the worm dives at you")
    global health, shields, player_AC, worm_modifier
    worm_hit = random.randint(1,21)
    if worm_modifier + worm_hit >= player_AC:
    
        damage = random.randint(10,20)
        if shields > 0:
            shields = shields - damage
            damage = str(damage)
            print("your shields take " + damage + " damage")
        else: 
            health = health - damage
            damage = str(damage)
            print("you take " + damage + " damage, find cover and regenerate your shield!!!")
    else:
        print("you jump out of the way in the nick of time")

def Cover():
    print("you dive behid the nearest boulder")
    global shields
    shields = shields + 20
    print("you regenerate 20 shields as you recharge your suit")

def find_positioning(chosen_location):
    global rifle_ammo, player_AC, hit_modifier
    if chosen_location == "A":
        print("you get a better place to shoot from")
        hit_modifier = 5
    elif chosen_location == "B":
        print("you hide become harder to hit")
        player_AC = 16
    elif chosen_location == "C":
        print("you find a ditch to hide in, you reload your rifle")
        rifle_ammo = 10
    else:
        print("chose A, B, or C")
        

def use_item():
    global remaining_health, health
    print(items)
    chosen = input("\n what would you like to use\n")
    if chosen == 'grenade':
        items.remove("grenade")
        g_damage = random.randint(5, 10)
        remaining_health = remaining_health - g_damage
        print("you throw a grenade\n")
        g_damage = str(g_damage)
        print("\nyou deal " + g_damage + " to the worm")
        g_damage = int(g_damage)
    elif chosen == 'Med kit':
        items.remove('Med kit')
        health = 10
        print('your health regenerates to 10')
    elif chosen == 'Portable radio tower':
        if worm == 1:
            print("you can't raido in the middle of a fight!")
        else:
            print("you manage to request help")
    else:
        print("chose an item")
        use_item()


print("khhhhhhhhhhhhhhhhhhhhhhhh...this is control do you copy")
time.sleep(5)
print("khhhhhhhhhhhhhhhhhhhhhhhh...this is control do you copy!!!")
time.sleep(5)
print("you peel your face off the side of your ship and press a button on your suit")
time.sleep(5)
print("I copy, a little banged up, were exactly am I?")
time.sleep(5)
print("you seem to have landed on a large astroid after the blast hit your ship, we are talking the size of a moon. have a look around, if you can get a beacon set up we can send aid")
time.sleep(5)
print("roger that\n")
time.sleep(5)
print("as you head outside the silence of space surrounds you, and you hop onto the ground, your pulse rifle hanging off your back and carrieing a large crate.\n")
time.sleep(5)
print("got to find a good place to set this up, any suggestions?")
time.sleep(5)
print("give me a second, there seems to be an elevated portion of the planet that could probably brodcast the signal without any interfearance.")
time.sleep(5)
print("ok, heading there now\n")
time.sleep(5)
print("as comms go dark, you look around at the rocky landscape. there are tall spires of rock that reach up as far as the eye can see. It must have been a miracle that you didnt die in the crash that stranded you here")
time.sleep(5)
print("Sudenly, you hear something behind you, and you turn around to see a massive space worm standing round 20ft from you. It bears its teeth and hisses as you draw your weapon.\n")
time.sleep(5)

while remaining_health >= 0:
    time.sleep(3)
    if health <= 0:
        print("you lose, game over")
    else:
        print("what would you like to do?")
        print("A. fire your rifle")
        print("B. recharge shield")
        print("C. Check health, stants, and invantory")
        print("D. Find better positioning")
        print("E. Use Item")
        choice = input("what would you like to do? \n ")
        if choice == "A":
            rifle_shot()
            print("\n")
            time.sleep(3)
            worm_attack()
            print("\n")
        elif choice == "B":
            Cover()
            print("\n")
            time.sleep(3)
            worm_attack()
            print("\n")
        elif choice == "C":
            rifle_ammo = str(rifle_ammo)
            print("loaded rifle shots = " + rifle_ammo)
            rifle_ammo = int(rifle_ammo)
            shields = str(shields)
            print("shields = " + shields)
            shields = int(shields)
            health = str(health)
            print("health = " + health)
            health = int(health)
            print(items)
            hit_modifier = str(hit_modifier)
            print("Curent hit modifier = " + hit_modifier)
            hit_modifier = int(hit_modifier)
            player_AC = str(player_AC)
            print("armor class = " + player_AC)
            player_AC = int(player_AC)
            print ("\n")
        elif choice == "D":
            print("\n")
            print("you see a boulder to climb on, a piller to hide behind, or a ditch to retreat to")
            chosen_location = input(" A. climb on a boulder \n B. hide behind the pillar \n C. retreat to the ditch \n")
            find_positioning(chosen_location)
            print("\n")
            time.sleep(3)
            worm_attack()
            print("\n")
        elif choice == "E":
            print("\n")
            use_item()
            print("\n")
            time.sleep(3)
            worm_attack()
            print("\n")
        else:
            print("chose A, B, C, D, or E")


if remaining_health <= 0:
    worm = 2
    print("The worm slumps dead in front of you, and you move on toward your destination.")

