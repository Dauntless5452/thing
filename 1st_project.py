#i still dont know what i am going to do in here
import random
import time

rifle_ammo = 20
remaining_health = 100
current_target = 100
shields = 50
health = 10

def rifle_shot():
    print("BANG BANG, you open fire")
    damage = random.randint(5,20)
    global rifle_ammo, remaining_health, current_target
    remaining_health = current_target - damage
    rifle_ammo -= 1
    damage = str(damage)
    print("you deal " + damage + " damage")
    
def worm_attack():
    print("the worm dives at you")
    damage = random.randint(10,20)
    global health, shields
    if shields > 0:
        shields = shields - damage
        damage = str(damage)
        print("your shields take " + damage + " damage")
    else: 
        health = health - damage
        damage = str(damage)
        print("you take " + damage + " damage, find cover and regenerate your shield!!!")
        
        


# print("khhhhhhhhhhhhhhhhhhhhhhhh...this is controll do you copy")
# time.sleep(2)
# print("khhhhhhhhhhhhhhhhhhhhhhhh...this is controll do you copy!!!")
# time.sleep(2)
# print("you peel your face off the side of your ship and press a button on your suit")
# time.sleep(2)
# print("I copy, a little banged up, were exactly am I?")
# time.sleep(2)
# print("you seem to have landed on a large astroid after the blast hit your ship, we are talking the size of a moon. have a look around, if you can get a beacon set up we can send aid")
# print("roger that\n")
# time.sleep(5)
# print("as you head outside the silence of space surrounds you, and you hop onto the ground, your pulse rifle hanging off your back and carrieing a large crate.\n")
# print("got to find a good place to set this up, any suggestions?")
# time.sleep(5)
# print("give me a second, there seems to be an elevated portion of the planet that could probably brodcast the signal without any interfearance.")
# time.sleep(5)
# print("ok, heading there now\n")
# time.sleep(2)
# print("as comms go dark, you look around at the rocky landscape. there are tall spires of rock that reach up as far as the eye can see. It must have been a miracle that you didnt die in the crash that stranded you here")

