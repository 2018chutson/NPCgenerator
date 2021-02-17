# Carly Hutson
# Version 2.0, 2/16/21
# Started 1/14/21
# Random NPC generator for Cyberpunk campaign
# Product for Corban Reade

import random

# preliminary data processing

def getfilecontents(filename):
    return open(filename).read().splitlines()

femnames = getfilecontents('femalenames.txt')
mascnames = getfilecontents('mascnames.txt')
lastnames = getfilecontents('lastnames.txt')
style_clothes = getfilecontents('style_clothes.txt')
style_hairstyle = getfilecontents('style_hairstyle.txt')
style_affectations = getfilecontents('style_affectations.txt')
education_level = getfilecontents('education.txt')
feelings_towards_people = getfilecontents('feelings_towards_people.txt')
most_valuable_possession = getfilecontents('most_valuable_possession.txt')
motivations_important = getfilecontents('motivations_important.txt')
motivations_mvp = getfilecontents('motivations_mvp.txt')
motivations_personality = getfilecontents('motivations_personality.txt')
cybernetics_master = getfilecontents('cybernetics_master.txt')
cyberoptics = getfilecontents('cybernetics_1.txt')
cyberarm_w_gun = getfilecontents('cybernetics_2.txt')
cyberaudio = getfilecontents('cybernetics_3.txt')

# introduction

def greeting():
    print("\nGreetings, DM. So you'd like to create some NPCs.")
    num = int(input("\nHow many?\t"))
    return num
def determine_class():
    role = int(input("\nCool, what class? (Enter number)\n1. Rockerboy\t2. Solo\t\t3. Netrunner"
                     "\n4. Techie\t5. Med Tech\t6. Media\n7. Cop\t\t8. Corporate"
                     "\t9. Fixer\n10. Nomad\t11. (Generic)\t12. (Random)\n\t"))
    return role
def determine_gender():
    gender = int(input('\nAnd finally, which gender? (Enter number)\n1. Female\t2. Male\t\t3. Don\'t care\n\t'))
    return gender


# superclass. beefy, but effective.

class Character:
    def __init__(self):
        self.first = 'unidentified_first_name'
        self.last = random.choice(lastnames)
        self.classrole = 'unidentified_classrole'
        self.int = random.randint(2, 10)
        self.ref = random.randint(2, 10)
        self.tech = random.randint(2, 10)
        self.cool = random.randint(2, 10)
        self.attr = random.randint(2, 10)
        self.luck = random.randint(2, 10)
        self.ma = random.randint(2, 10)
        self.body = random.randint(2, 10)
        self.emp = random.randint(2, 10)
        self.run = self.ma * 3
        self.leap = self.run / 4
        self.lift = self.body * 10
        self.save = self.body
        if self.body <= 2:
            self.btm = 0
        elif self.body == 3 or self.body == 4:
            self.btm = -1
        elif self.body == 5 or self.body == 6 or self.body == 7:
            self.btm = -2
        elif self.body == 8 or self.body == 9:
            self.btm = -3
        else:
            self.btm = -4
        self.special_ability = 'unidentified_special_ability'
        self.clothes = random.choice(style_clothes)
        self.hairstyle = random.choice(style_hairstyle)
        self.affectations = random.choice(style_affectations)
        self.education = random.choice(education_level)
        self.personality = random.choice(motivations_personality)
        self.mvp = random.choice(motivations_mvp)
        self.important = random.choice(motivations_important)
        self.possession = random.choice(most_valuable_possession)
        self.feelings = random.choice(feelings_towards_people)
        self.cyber = self.roll_cybernetics(False)
        self.aw = self.armor_weapons(0)
        self.skillstable = self.generate_skills()


    def roll_cybernetics(self, solo):  # parameter T/F check for solo
        one = random.choice(cybernetics_master)
        two = random.choice(cybernetics_master)
        three = random.choice(cybernetics_master)
        cyberneticslist = [one]
        while two in cyberneticslist:
            two = random.choice(cybernetics_master)
        cyberneticslist.append(two)
        while three in cyberneticslist:
            three = random.choice(cybernetics_master)
        cyberneticslist.append(three)
        if solo is True:
            four = random.choice(cybernetics_master)
            while four in cyberneticslist:
                four = random.choice(cybernetics_master)
            cyberneticslist.append(four)
            five = random.choice(cybernetics_master)
            while five in cyberneticslist:
                five = random.choice(cybernetics_master)
            cyberneticslist.append(five)
            six = random.choice(cybernetics_master)
            while six in cyberneticslist:
                six = random.choice(cybernetics_master)
            cyberneticslist.append(six)
        if 'Cyberoptics' in cyberneticslist:
            cyberneticslist.remove('Cyberoptics')
            cyberneticslist.append(random.choice(cyberoptics))
        if 'Cyberarm with gun' in cyberneticslist:
            cyberneticslist.remove('Cyberarm with gun')
            cyberneticslist.append(random.choice(cyberarm_w_gun))
        if 'Cyberaudio' in cyberneticslist:
            cyberneticslist.remove('Cyberaudio')
            cyberneticslist.append(random.choice(cyberaudio))
        return cyberneticslist

    def generate_skills(self):
        skillsgen = list()
        while len(skillsgen) != 8:
            x = random.randint(0, 40)
            if x != 0 and x != 1 and x != 39 and x != 40:
                if (x - 1) not in skillsgen:
                    if (x + 1) not in skillsgen:
                        if x not in skillsgen:
                            skillsgen.append(x)
        skillsgen.sort()
        a = skillsgen[0]
        b = skillsgen[1] - skillsgen[0]
        c = skillsgen[2] - skillsgen[1]
        d = skillsgen[3] - skillsgen[2]
        e = skillsgen[4] - skillsgen[3]
        f = skillsgen[5] - skillsgen[4]
        g = skillsgen[6] - skillsgen[5]
        h = skillsgen[7] - skillsgen[6]
        i = 40 - skillsgen[7]
        skillslist = [a, b, c, d, e, f, g, h, i]
        y = 0
        z = 0
        while y <= 8:
            if skillslist[y] > 10:
                z += skillslist[y] - 10
                skillslist[y] = 10
            y = y + 1
        if z > 0:
            self.skills_10_adjust(skillslist, z)
        return skillslist

    def skills_10_adjust(self, skillslist, z):
        while z > 0:
            buff = random.randint(0, 8)
            if skillslist[buff] < 10:
                skillslist[buff] += 1
                z -= 1
            else:
                self.skills_10_adjust(skillslist, z)

    def armor_weapons(self, modifier):
        armor = 'TBD'
        weapon = 'TBD'
        x = (random.randint(1, 10)) + modifier
        if x <= 1:
            armor = 'Heavy Leather'
            weapon = 'Knife'
        elif x == 2:
            armor = 'Armor Vest'
            weapon = 'Light Pistol'
        elif x == 3:
            armor = 'Light Armor Jacket'
            weapon = 'Medium Pistol'
        elif x == 4:
            armor = 'Light Armor Jacket'
            weapon = 'Heavy Pistol'
        elif x == 5:
            armor = 'Medium Armor Jacket'
            weapon = 'Heavy Pistol'
        elif x == 6:
            armor = 'Medium Armor Jacket'
            weapon = 'Heavy Pistol'
        elif x == 7:
            armor = 'Medium Armor Jacket'
            weapon = 'Light Assault Rifle'
        elif x == 8:
            armor = 'Heavy Armor Jacket'
            weapon = 'Medium Assault Rifle'
        elif x == 9:
            armor = 'Heavy Armor Jacket'
            weapon = 'Heavy Assault Rifle'
        else:
            armor = 'MetalGear(TM)'
            weapon = 'Heavy Assault Rifle'
        y = [armor, weapon]
        return y

    def print_everything(self):
        print('\n\nNAME: ', self.first, ' ', self.last, '\tCLASS: ', self.classrole)
        print('STATS:')
        print('INT [', self.int, ']\tREF [', self.ref, ']\tTECH [', self.tech, ']\tCOOL [',
              self.cool, ']')
        print('ATTR [', self.attr, ']\tLUCK [', self.luck, ']\tMA [', self.ma, ']\tBODY [', self.body, ']')
        print('EMP [', self.emp, ']\tRun [', self.run, ']\tLeap [', self.leap, ']\tLift [',
              self.lift, ']')
        print('Armor:\t', self.aw[0])
        print('Weapon:\t', self.aw[1])
        print('SAVE: ', self.save, '\tBTM: ', self.btm)
        print('Special Ability: ', self.special_ability)
        print('Education Level: ', self.education)
        print('\tCYBERNETICS:')
        for item in self.cyber:
            print(item)
        print('\tSTYLE:')
        print('Clothes:\t', self.clothes)
        print('Hairstyle:\t', self.hairstyle)
        print('Affectations:\t', self.affectations)
        print('\tMOTIVATIONS:')
        print('Personality:\t\t\t', self.personality)
        print('Most Valuable Person:\t\t', self.mvp)
        print('Most Important Value:\t\t', self.important)
        print('Feelings towards most people:\t', self.feelings)
        print('Most valuable possession:\t', self.possession)

    def print_skills(self, a, b, c, d, e, f, g, h, i, table):
        print('\tSKILLS:')
        print(a, table[0])
        print(b, table[1])
        print(c, table[2])
        print(d, table[3])
        print(e, table[4])
        print(f, table[5])
        print(g, table[6])
        print(h, table[7])
        print(i, table[8])

# subclasses

class Rockerboy(Character):
    def __init__(self):
        super().__init__()
    def modify(self):
        self.classrole = 'Rockerboy'
        self.int = random.randint(2, 5)
        self.ref = random.randint(5, 10)
        self.tech = random.randint(2, 5)
        self.cool = random.randint(5, 10)
        self.attr = random.randint(5, 10)
        self.special_ability = 'Charismatic Leadership'

class Solo(Character):
    def __init__(self):
        super().__init__()
    def modify(self):
        self.classrole = 'Solo'
        self.ref = random.randint(5, 10)
        self.cool = random.randint(5, 10)
        self.emp = random.randint(2, 5)
        self.special_ability = 'Combat Sense'
        self.cyber = self.roll_cybernetics(True)
        self.aw = self.armor_weapons(3)

class Netrunner(Character):
    def __init__(self):
        super().__init__()
    def modify(self):
        self.classrole = 'Netrunner'
        self.int = random.randint(5, 10)
        self.special_ability = 'Interface'

class Techie(Character):
    def __init__(self):
        super().__init__()
    def modify(self):
        self.classrole = 'Techie'
        self.tech = random.randint(5, 10)
        self.special_ability = 'Jury Rig'

class Medtech(Character):
    def __init__(self):
        super().__init__()
    def modify(self):
        self.classrole = 'MedTech'
        self.tech = random.randint(5, 10)
        self.special_ability = 'Medical Tech'

class Media(Character):
    def __init__(self):
        super().__init__()
    def modify(self):
        self.classrole = 'Media'
        self.attr = random.randint(5, 10)
        self.special_ability = 'Credibility'

class Cop(Character):
    def __init__(self):
        super().__init__()
    def modify(self):
        self.classrole = 'Cop'
        self.ref = random.randint(5, 10)
        self.special_ability = 'Authority'
        self.aw = self.armor_weapons(2)

class Corporate(Character):
    def __init__(self):
        super().__init__()
    def modify(self):
        self.classrole = 'Corporate'
        self.int = random.randint(5, 10)
        self.special_ability = 'Resources'

class Fixer(Character):
    def __init__(self):
        super().__init__()
    def modify(self):
        self.classrole = 'Fixer'
        self.cool = random.randint(5, 10)
        self.special_ability = 'Streetdeal'

class Nomad(Character):
    def __init__(self):
        super().__init__()
    def modify(self):
        self.classrole = 'Nomad'
        self.ref = random.randint(5, 10)
        self.cool = random.randint(5, 10)
        self.int = random.randint(2, 5)
        self.special_ability = 'Family'
        self.aw = self.armor_weapons(2)

class Generic(Character):
    def __init__(self):
        super().__init__()
    def print_everything(self):
        self.aw = self.armor_weapons(-5)
        print('\n\nNAME:', self.first, self.last, '\tCLASS: Generic')
        print('Armor:\t', self.aw[0])
        print('Weapon:\t', self.aw[1])
        print('\tSTYLE:')
        print('Clothes:\t', self.clothes)
        print('Hairstyle:\t', self.hairstyle)
        print('Affectations:\t', self.affectations)
        print('\tMOTIVATIONS:')
        print('Personality:\t\t\t', self.personality)
        print('Most Valuable Person:\t\t', self.mvp)
        print('Most Important Value:\t\t', self.important)
        print('Feelings towards most people:\t', self.feelings)
        print('Most valuable possession:\t', self.possession)

# first name function that's awkwardly floating out in the open

def set_first_name(gender): # something is wrong with this. entering 1 doesn't always give female names.
    name = 'unidentified_first_name'
    if gender == 1:
        name = random.choice(femnames)
    elif gender == 2:
        name = random.choice(mascnames)
    else:
        randomgender = random.randint(1, 2)
        if randomgender == 1:
            name = random.choice(femnames)
        elif randomgender == 2:
            name = random.choice(mascnames)
    return name

# driver function

def driver(count, role, gender):
    if role == 1:
        while count > 0:
            person = Rockerboy()
            person.first = set_first_name(gender)
            person.modify()
            person.print_everything()
            person.print_skills('Awareness/Notice:\t', 'Perform:\t\t', 'Wardrobe & Style:\t', 'Composition:\t\t',
                 'Brawling:\t\t', 'Play Instrument:\t', 'Streetwise:\t\t', 'Persuasion:\t\t',
                 'Seduction:\t\t', person.skillstable)
            count -= 1
    elif role == 2:
        while count > 0:
            person = Solo()
            person.first = set_first_name(gender)
            person.modify()
            person.print_everything()
            person.print_skills('Awareness/Notice:\t', 'Handgun:\t\t', 'Martial Arts:\t\t', 'Melee:\t\t\t',
                 'Weapons Tech:\t\t', 'Rifle:\t\t\t', 'Athletics:\t\t', 'Submachinegun:\t\t', 'Stealth:\t\t',
                                person.skillstable)
            count -= 1
    elif role == 3:
        while count > 0:
            person = Netrunner()
            person.first = set_first_name(gender)
            person.modify()
            person.print_everything()
            person.print_skills('Awareness/Notice:\t', 'Basic Tech:\t\t', 'Education:\t\t', 'System Knowledge:\t',
                 'CyberTech:\t\t', 'Cyberdeck Design:\t', 'Composition:\t\t', 'Electronics:\t\t',
                 'Programming:\t\t', person.skillstable)
            count -= 1
    elif role == 4:
        while count > 0:
            person = Techie()
            person.first = set_first_name(gender)
            person.modify()
            person.print_everything()
            techieskills = ['Gyro:\t\t\t', 'Aero:\t\t\t', 'Weapons:\t\t', 'Electronic Security:\t']
            techieskills.remove(random.choice(techieskills))
            person.print_skills('Awareness/Notice:\t', 'Basic Tech:\t\t', 'Education:\t\t', 'Teaching:\t\t',
                 'CyberTech:\t\t', 'Electronics:\t\t', techieskills[0], techieskills[1],
                 techieskills[2], person.skillstable)
            count -= 1
    elif role == 5:
        while count > 0:
            person = Medtech()
            person.first = set_first_name(gender)
            person.modify()
            person.print_everything()
            person.print_skills('Awareness/Notice:\t', 'Basic Tech:\t\t', 'Education:\t\t', 'Diagnose:\t\t',
                 'Cryotank Operation:\t', 'Library Search:\t\t', 'Pharmaceuticals:\t', 'Zoology:\t\t',
                 'Human Perception:\t', person.skillstable)
            count -= 1
    elif role == 6:
        while count > 0:
            person = Media()
            person.first = set_first_name(gender)
            person.modify()
            person.print_everything()
            person.print_skills('Awareness/Notice:\t', 'Composition:\t\t', 'Education:\t\t', 'Persuasion:\t\t',
                 'Human Perception:\t', 'Social:\t\t\t', 'Streetwise:\t\t', 'Photo & Film:\t\t',
                 'Interview:\t\t', person.skillstable)
            count -= 1
    elif role == 7:
        while count > 0:
            person = Cop()
            person.first = set_first_name(gender)
            person.modify()
            person.print_everything()
            person.print_skills('Awareness/Notice:\t', 'Handgun:\t\t', 'Education:\t\t', 'Athletics:\t\t',
                 'Human Perception:\t', 'Melee:\t\t\t', 'Streetwise:\t\t', 'Brawling:\t\t',
                 'Interrogation:\t\t', person.skillstable)
            count -= 1
    elif role == 8:
        while count > 0:
            person = Corporate()
            person.first = set_first_name(gender)
            person.modify()
            person.print_everything()
            person.print_skills('Awareness/Notice:\t', 'Library Search:\t\t', 'Education:\t\t', 'Persuasion:\t\t',
                 'Human Perception:\t', 'Social:\t\t\t', 'Stock Market:\t\t', 'Wardrobe & Style:\t',
                 'Personal Grooming:\t', person.skillstable)
            count -= 1
    elif role == 9:
        while count > 0:
            person = Fixer()
            person.first = set_first_name(gender)
            person.modify()
            person.print_everything()
            person.print_skills('Awareness/Notice:\t', 'Forgery:\t\t', 'Handgun:\t\t', 'Persuasion:\t\t',
                 'Pick Lock:\t\t', 'Pick Pocket:\t\t', 'Brawling:\t\t', 'Melee:\t\t\t',
                 'Intimidate:\t\t', person.skillstable)
            count -= 1
    elif role == 10:
        while count > 0:
            person = Nomad()
            person.first = set_first_name(gender)
            person.modify()
            person.print_everything()
            person.print_skills('Awareness/Notice:\t', 'Endurance:\t\t', 'Melee:\t\t\t', 'Rifle:\t\t\t',
                 'Wilderness Survival:\t', 'Drive:\t\t\t', 'Basic Tech:\t\t', 'Brawling:\t\t',
                 'Athletics:\t\t', person.skillstable)
            count -= 1
    elif role == 11:
        while count > 0:
            person = Generic()
            person.first = set_first_name(gender)
            person.print_everything()
            count -= 1
    elif role == 12:
        x = random.randint(1, 10)
        driver(count, x, gender)
    else:
        print('\n\nOut of bounds. Seriously, you can\'t even count to 12? Whatever, choosing random class.')
        driver(count, 12, gender)

# this would be "main"

count = greeting()
role = determine_class()
gender = determine_gender()
driver(count, role, gender)

# Version 2.0, 2/16/2021
# Redesigned for the sake of elegance, clarity, efficiency, and my own ego.
# Fixed bug where requesting female names doesn't always return female names. Hopefully.
# (Random) now chooses one random class, and all the NPCs generated are of that same class. Not ideal,
# but can be worked around by running the program multiple times.
