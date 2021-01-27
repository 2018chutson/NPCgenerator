# Carly Hutson
# Version 1.1, 1/21/21
# Started 1/14/21
# Random NPC generator for Cyberpunk campaign
# Product for Corban Reade

import random
import string

# Returns file data
def getfilecontents(filename):
    return open(filename).read().splitlines()

# get file contents

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


# start
print("\nGreetings, DM. So you'd like to create some NPCs.")
num = int(input("\nHow many?\t"))
role = int(input("\nCool, what class? (Enter number)\n1. Rockerboy\t2. Solo\t\t3. Netrunner"
             "\n4. Techie\t5. Med Tech\t6. Media\n7. Cop\t\t8. Corporate"
             "\t9. Fixer\n10. Nomad\t11. (Random)\t12. (Generic)\n\t"))
gender = int(input('\nAnd finally, which gender? (Enter number)\n1. Female\t2. Male\t\t3. Don\'t care\n\t'))
count = 0

# print function

def print_everything(first, last, classrole, int, ref, tech, cool, attr, luck,
                     ma, body, emp, run, leap, lift, save, btm, special_ability,
                     clothes, hairstyle, affectations, education, personality,
                     mvp, important, mvpossession, feelings, cyber, aw):
    print('\n\nNAME: ', first, ' ', last, '\tCLASS: ', classrole)
    print('STATS:')
    print('INT [', int, ']\tREF [', ref, ']\tTECH [', tech, ']\tCOOL [',
          cool, ']')
    print('ATTR [', attr, ']\tLUCK [', luck, ']\tMA [', ma, ']\tBODY [', body, ']')
    print('EMP [', emp, ']\tRun [', run, ']\tLeap [', leap, ']\tLift [',
          lift, ']')
    print('Armor:\t', aw[0])
    print('Weapon:\t', aw[1])
    print('SAVE: ', save, '\tBTM: ', btm)
    print('Special Ability: ', special_ability)
    print('Education Level: ', education)
    print('\tCYBERNETICS:')
    for item in cyber:
        print(item)
    print('\tSTYLE:')
    print('Clothes:\t', clothes)
    print('Hairstyle:\t', hairstyle)
    print('Affectations:\t', affectations)
    print('\tMOTIVATIONS:')
    print('Personality:\t\t\t', personality)
    print('Most Valuable Person:\t\t', mvp)
    print('Most Important Value:\t\t', important)
    print('Feelings towards most people:\t', feelings)
    print('Most valuable possession:\t', mvpossession)
    return


# print skills function

def print_skills(a, b, c, d, e, f, g, h, i, table):
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
    return


# basic info (non-class specific)

def set_first_name():
    if gender == 1:
        first = random.choice(femnames)
    if gender == 2:
        first = random.choice(mascnames)
    else:
        randomgender = random.randint(1, 2)
        if randomgender == 1:
            first = random.choice(femnames)
        if randomgender == 2:
            first = random.choice(mascnames)
    return first

def set_last_name():
    last = random.choice(lastnames)
    return last

def set_clothes():
    clothes = random.choice(style_clothes)
    return clothes

def set_hair():
    hair = random.choice(style_hairstyle)
    return hair

def set_aff():
    aff = random.choice(style_affectations)
    return aff


# skills (ft. budgeting magic)

def generate_skills():
    skillsgen = list()
    while len(skillsgen) != 8:
        x = random.randint(0, 40)
        if x != 0 and x != 1 and x != 39 and x != 40:
            if (x-1) not in skillsgen:
                if (x+1) not in skillsgen:
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
        skills_10_adjust(skillslist, z)
    return skillslist

def skills_10_adjust(skillslist, z):
    while z > 0:
        buff = random.randint(0, 8)
        if skillslist[buff] < 10:
            skillslist[buff] += 1
            z = z - 1
        else:
            skills_10_adjust(skillslist, z)
        return


# cybernetics generator

def cybernetics(solo): # parameter T/F check for solo
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


# Armor and Weapons selection

def armor_weapons(role):
    armor = 'TBD'
    weapon = 'TBD'
    x = random.randint(1, 10)
    if role == 'Generic':
        x -= 5
    if role == 'Nomad' or role == 'Cop':
        x += 2
    if role == 'Solo':
        x += 3
    if x <= 1:
        armor = 'Heavy Leather'
        weapon = 'Knife'
    if x == 2:
        armor = 'Armor Vest'
        weapon = 'Light Pistol'
    if x == 3:
        armor = 'Light Armor Jacket'
        weapon = 'Medium Pistol'
    if x == 4:
        armor = 'Light Armor Jacket'
        weapon = 'Heavy Pistol'
    if x == 5:
        armor = 'Medium Armor Jacket'
        weapon = 'Heavy Pistol'
    if x == 6:
        armor = 'Medium Armor Jacket'
        weapon = 'Heavy Pistol'
    if x == 7:
        armor = 'Medium Armor Jacket'
        weapon = 'Light Assault Rifle'
    if x == 8:
        armor = 'Heavy Armor Jacket'
        weapon = 'Medium Assault Rifle'
    if x == 9:
        armor = 'Heavy Armor Jacket'
        weapon = 'Heavy Assault Rifle'
    if x >= 10:
        armor = 'MetalGear(TM)'
        weapon = 'Heavy Assault Rifle'
    y = [armor, weapon]
    return y


# class functions

def rockerboy():
    first = set_first_name()
    last = set_last_name()
    classrole = 'Rockerboy'
    int = random.randint(2, 5)
    ref = random.randint(5, 10)
    tech = random.randint(2, 5)
    cool = random.randint(5, 10)
    attr = random.randint(5, 10)
    luck = random.randint(2, 10)
    ma = random.randint(2, 10)
    body = random.randint(2, 10)
    emp = random.randint(2, 10)
    run = ma * 3
    leap = run / 4
    lift = body * 10
    save = body
    if body == 2:
        btm = 0
    if body == 3 or body == 4:
        btm = -1
    if body == 5 or body == 6 or body == 7:
        btm = -2
    if body == 8 or body == 9:
        btm = -3
    if body == 10:
        btm = -4
    special_ability = 'Charismatic Leadership'
    skillstable = generate_skills()
    clothes = random.choice(style_clothes)
    hairstyle = random.choice(style_hairstyle)
    affectations = random.choice(style_affectations)
    education = random.choice(education_level)
    personality = random.choice(motivations_personality)
    mvp = random.choice(motivations_mvp)
    important = random.choice(motivations_important)
    mvpossession = random.choice(most_valuable_possession)
    feelings = random.choice(feelings_towards_people)
    cyber = cybernetics(False)
    aw = armor_weapons('Rockerboy')
    print_everything(first, last, classrole, int, ref, tech, cool, attr, luck,
                     ma, body, emp, run, leap, lift, save, btm, special_ability,
                     clothes, hairstyle, affectations, education, personality,
                     mvp, important, mvpossession, feelings, cyber, aw)
    print_skills('Awareness/Notice:\t', 'Perform:\t\t', 'Wardrobe & Style:\t', 'Composition:\t\t',
                 'Brawling:\t\t', 'Play Instrument:\t', 'Streetwise:\t\t', 'Persuasion:\t\t',
                 'Seduction:\t\t', skillstable)

def solo():
    first = set_first_name()
    last = set_last_name()
    classrole = 'Solo'
    int = random.randint(2, 10)
    ref = random.randint(5, 10)
    tech = random.randint(2, 10)
    cool = random.randint(5, 10)
    attr = random.randint(2, 10)
    luck = random.randint(2, 10)
    ma = random.randint(2, 10)
    body = random.randint(2, 10)
    emp = random.randint(2, 5)
    run = ma * 3
    leap = run / 4
    lift = body * 10
    save = body
    if body == 2:
        btm = 0
    if body == 3 or body == 4:
        btm = -1
    if body == 5 or body == 6 or body == 7:
        btm = -2
    if body == 8 or body == 9:
        btm = -3
    if body == 10:
        btm = -4
    special_ability = 'Combat Sense'
    skillstable = generate_skills()
    clothes = random.choice(style_clothes)
    hairstyle = random.choice(style_hairstyle)
    affectations = random.choice(style_affectations)
    education = random.choice(education_level)
    personality = random.choice(motivations_personality)
    mvp = random.choice(motivations_mvp)
    important = random.choice(motivations_important)
    mvpossession = random.choice(most_valuable_possession)
    feelings = random.choice(feelings_towards_people)
    cyber = cybernetics(True)
    aw = armor_weapons('Solo')
    print_everything(first, last, classrole, int, ref, tech, cool, attr, luck,
                     ma, body, emp, run, leap, lift, save, btm, special_ability,
                     clothes, hairstyle, affectations, education, personality,
                     mvp, important, mvpossession, feelings, cyber, aw)
    print_skills('Awareness/Notice:\t', 'Handgun:\t\t', 'Martial Arts:\t\t', 'Melee:\t\t\t',
                 'Weapons Tech:\t\t', 'Rifle:\t\t\t', 'Athletics:\t\t', 'Submachinegun:\t\t', 'Stealth:\t\t',
                 skillstable)

def netrunner():
    first = set_first_name()
    last = set_last_name()
    classrole = 'Netrunner'
    int = random.randint(5, 10)
    ref = random.randint(2, 10)
    tech = random.randint(2, 10)
    cool = random.randint(2, 10)
    attr = random.randint(2, 10)
    luck = random.randint(2, 10)
    ma = random.randint(2, 10)
    body = random.randint(2, 10)
    emp = random.randint(2, 10)
    run = ma * 3
    leap = run / 4
    lift = body * 10
    save = body
    if body == 2:
        btm = 0
    if body == 3 or body == 4:
        btm = -1
    if body == 5 or body == 6 or body == 7:
        btm = -2
    if body == 8 or body == 9:
        btm = -3
    if body == 10:
        btm = -4
    special_ability = 'Interface'
    skillstable = generate_skills()
    clothes = random.choice(style_clothes)
    hairstyle = random.choice(style_hairstyle)
    affectations = random.choice(style_affectations)
    education = random.choice(education_level)
    personality = random.choice(motivations_personality)
    mvp = random.choice(motivations_mvp)
    important = random.choice(motivations_important)
    mvpossession = random.choice(most_valuable_possession)
    feelings = random.choice(feelings_towards_people)
    cyber = cybernetics(False)
    aw = armor_weapons('Netrunner')
    print_everything(first, last, classrole, int, ref, tech, cool, attr, luck,
                     ma, body, emp, run, leap, lift, save, btm, special_ability,
                     clothes, hairstyle, affectations, education, personality,
                     mvp, important, mvpossession, feelings, cyber, aw)
    print_skills('Awareness/Notice:\t', 'Basic Tech:\t\t', 'Education:\t\t', 'System Knowledge:\t',
                 'CyberTech:\t\t', 'Cyberdeck Design:\t', 'Composition:\t\t', 'Electronics:\t\t',
                 'Programming:\t\t', skillstable)

def techie():
    first = set_first_name()
    last = set_last_name()
    classrole = 'Techie'
    int = random.randint(2, 10)
    ref = random.randint(2, 10)
    tech = random.randint(5, 10)
    cool = random.randint(2, 10)
    attr = random.randint(2, 10)
    luck = random.randint(2, 10)
    ma = random.randint(2, 10)
    body = random.randint(2, 10)
    emp = random.randint(2, 10)
    run = ma * 3
    leap = run / 4
    lift = body * 10
    save = body
    if body == 2:
        btm = 0
    if body == 3 or body == 4:
        btm = -1
    if body == 5 or body == 6 or body == 7:
        btm = -2
    if body == 8 or body == 9:
        btm = -3
    if body == 10:
        btm = -4
    special_ability = 'Jury Rig'
    skillstable = generate_skills()
    clothes = random.choice(style_clothes)
    hairstyle = random.choice(style_hairstyle)
    affectations = random.choice(style_affectations)
    education = random.choice(education_level)
    personality = random.choice(motivations_personality)
    mvp = random.choice(motivations_mvp)
    important = random.choice(motivations_important)
    mvpossession = random.choice(most_valuable_possession)
    feelings = random.choice(feelings_towards_people)
    cyber = cybernetics(False)
    aw = armor_weapons('Techie')
    print_everything(first, last, classrole, int, ref, tech, cool, attr, luck,
                     ma, body, emp, run, leap, lift, save, btm, special_ability,
                     clothes, hairstyle, affectations, education, personality,
                     mvp, important, mvpossession, feelings, cyber, aw)
    techieskills = ['Gyro:\t\t\t', 'Aero:\t\t\t', 'Weapons:\t\t', 'Electronic Security:\t']
    techieskills.remove(random.choice(techieskills))
    print_skills('Awareness/Notice:\t', 'Basic Tech:\t\t', 'Education:\t\t', 'Teaching:\t\t',
                 'CyberTech:\t\t', 'Electronics:\t\t', techieskills[0], techieskills[1],
                 techieskills[2], skillstable)

def medtech():
    first = set_first_name()
    last = set_last_name()
    classrole = 'Med Tech'
    int = random.randint(2, 10)
    ref = random.randint(2, 10)
    tech = random.randint(5, 10)
    cool = random.randint(2, 10)
    attr = random.randint(2, 10)
    luck = random.randint(2, 10)
    ma = random.randint(2, 10)
    body = random.randint(2, 10)
    emp = random.randint(2, 10)
    run = ma * 3
    leap = run / 4
    lift = body * 10
    save = body
    if body == 2:
        btm = 0
    if body == 3 or body == 4:
        btm = -1
    if body == 5 or body == 6 or body == 7:
        btm = -2
    if body == 8 or body == 9:
        btm = -3
    if body == 10:
        btm = -4
    special_ability = 'Medical Tech'
    skillstable = generate_skills()
    clothes = random.choice(style_clothes)
    hairstyle = random.choice(style_hairstyle)
    affectations = random.choice(style_affectations)
    education = random.choice(education_level)
    personality = random.choice(motivations_personality)
    mvp = random.choice(motivations_mvp)
    important = random.choice(motivations_important)
    mvpossession = random.choice(most_valuable_possession)
    feelings = random.choice(feelings_towards_people)
    cyber = cybernetics(False)
    aw = armor_weapons('Med Tech')
    print_everything(first, last, classrole, int, ref, tech, cool, attr, luck,
                     ma, body, emp, run, leap, lift, save, btm, special_ability,
                     clothes, hairstyle, affectations, education, personality,
                     mvp, important, mvpossession, feelings, cyber, aw)
    print_skills('Awareness/Notice:\t', 'Basic Tech:\t\t', 'Education:\t\t', 'Diagnose:\t\t',
                 'Cryotank Operation:\t', 'Library Search:\t\t', 'Pharmaceuticals:\t', 'Zoology:\t\t',
                 'Human Perception:\t', skillstable)


def media():
    first = set_first_name()
    last = set_last_name()
    classrole = 'Media'
    int = random.randint(2, 10)
    ref = random.randint(2, 10)
    tech = random.randint(2, 10)
    cool = random.randint(2, 10)
    attr = random.randint(5, 10)
    luck = random.randint(2, 10)
    ma = random.randint(2, 10)
    body = random.randint(2, 10)
    emp = random.randint(2, 10)
    run = ma * 3
    leap = run / 4
    lift = body * 10
    save = body
    if body == 2:
        btm = 0
    if body == 3 or body == 4:
        btm = -1
    if body == 5 or body == 6 or body == 7:
        btm = -2
    if body == 8 or body == 9:
        btm = -3
    if body == 10:
        btm = -4
    special_ability = 'Credibility'
    skillstable = generate_skills()
    clothes = random.choice(style_clothes)
    hairstyle = random.choice(style_hairstyle)
    affectations = random.choice(style_affectations)
    education = random.choice(education_level)
    personality = random.choice(motivations_personality)
    mvp = random.choice(motivations_mvp)
    important = random.choice(motivations_important)
    mvpossession = random.choice(most_valuable_possession)
    feelings = random.choice(feelings_towards_people)
    cyber = cybernetics(False)
    aw = armor_weapons('Media')
    print_everything(first, last, classrole, int, ref, tech, cool, attr, luck,
                     ma, body, emp, run, leap, lift, save, btm, special_ability,
                     clothes, hairstyle, affectations, education, personality,
                     mvp, important, mvpossession, feelings, cyber, aw)
    print_skills('Awareness/Notice:\t', 'Composition:\t\t', 'Education:\t\t', 'Persuasion:\t\t',
                 'Human Perception:\t', 'Social:\t\t\t', 'Streetwise:\t\t', 'Photo & Film:\t\t',
                 'Interview:\t\t', skillstable)

def cop():
    first = set_first_name()
    last = set_last_name()
    classrole = 'Cop'
    int = random.randint(2, 10)
    ref = random.randint(5, 10)
    tech = random.randint(2, 10)
    cool = random.randint(2, 10)
    attr = random.randint(2, 10)
    luck = random.randint(2, 10)
    ma = random.randint(2, 10)
    body = random.randint(2, 10)
    emp = random.randint(2, 10)
    run = ma * 3
    leap = run / 4
    lift = body * 10
    save = body
    if body == 2:
        btm = 0
    if body == 3 or body == 4:
        btm = -1
    if body == 5 or body == 6 or body == 7:
        btm = -2
    if body == 8 or body == 9:
        btm = -3
    if body == 10:
        btm = -4
    special_ability = 'Authority'
    skillstable = generate_skills()
    clothes = random.choice(style_clothes)
    hairstyle = random.choice(style_hairstyle)
    affectations = random.choice(style_affectations)
    education = random.choice(education_level)
    personality = random.choice(motivations_personality)
    mvp = random.choice(motivations_mvp)
    important = random.choice(motivations_important)
    mvpossession = random.choice(most_valuable_possession)
    feelings = random.choice(feelings_towards_people)
    cyber = cybernetics(False)
    aw = armor_weapons('Cop')
    print_everything(first, last, classrole, int, ref, tech, cool, attr, luck,
                     ma, body, emp, run, leap, lift, save, btm, special_ability,
                     clothes, hairstyle, affectations, education, personality,
                     mvp, important, mvpossession, feelings, cyber, aw)
    print_skills('Awareness/Notice:\t', 'Handgun:\t\t', 'Education:\t\t', 'Athletics:\t\t',
                 'Human Perception:\t', 'Melee:\t\t\t', 'Streetwise:\t\t', 'Brawling:\t\t',
                 'Interrogation:\t\t', skillstable)

def corporate():
    first = set_first_name()
    last = set_last_name()
    classrole = 'Corporate'
    int = random.randint(5, 10)
    ref = random.randint(2, 10)
    tech = random.randint(2, 10)
    cool = random.randint(2, 10)
    attr = random.randint(2, 10)
    luck = random.randint(2, 10)
    ma = random.randint(2, 10)
    body = random.randint(2, 10)
    emp = random.randint(2, 10)
    run = ma * 3
    leap = run / 4
    lift = body * 10
    save = body
    if body == 2:
        btm = 0
    if body == 3 or body == 4:
        btm = -1
    if body == 5 or body == 6 or body == 7:
        btm = -2
    if body == 8 or body == 9:
        btm = -3
    if body == 10:
        btm = -4
    special_ability = 'Resources'
    skillstable = generate_skills()
    clothes = random.choice(style_clothes)
    hairstyle = random.choice(style_hairstyle)
    affectations = random.choice(style_affectations)
    education = random.choice(education_level)
    personality = random.choice(motivations_personality)
    mvp = random.choice(motivations_mvp)
    important = random.choice(motivations_important)
    mvpossession = random.choice(most_valuable_possession)
    feelings = random.choice(feelings_towards_people)
    cyber = cybernetics(False)
    aw = armor_weapons('Corporate')
    print_everything(first, last, classrole, int, ref, tech, cool, attr, luck,
                     ma, body, emp, run, leap, lift, save, btm, special_ability,
                     clothes, hairstyle, affectations, education, personality,
                     mvp, important, mvpossession, feelings, cyber, aw)
    print_skills('Awareness/Notice:\t', 'Library Search:\t\t', 'Education:\t\t', 'Persuasion:\t\t',
                 'Human Perception:\t', 'Social:\t\t\t', 'Stock Market:\t\t', 'Wardrobe & Style:\t',
                 'Personal Grooming:\t', skillstable)

def fixer():
    first = set_first_name()
    last = set_last_name()
    classrole = 'Fixer'
    int = random.randint(2, 10)
    ref = random.randint(2, 10)
    tech = random.randint(2, 10)
    cool = random.randint(5, 10)
    attr = random.randint(2, 10)
    luck = random.randint(2, 10)
    ma = random.randint(2, 10)
    body = random.randint(2, 10)
    emp = random.randint(2, 10)
    run = ma * 3
    leap = run / 4
    lift = body * 10
    save = body
    if body == 2:
        btm = 0
    if body == 3 or body == 4:
        btm = -1
    if body == 5 or body == 6 or body == 7:
        btm = -2
    if body == 8 or body == 9:
        btm = -3
    if body == 10:
        btm = -4
    special_ability = 'Streetdeal'
    skillstable = generate_skills()
    clothes = random.choice(style_clothes)
    hairstyle = random.choice(style_hairstyle)
    affectations = random.choice(style_affectations)
    education = random.choice(education_level)
    personality = random.choice(motivations_personality)
    mvp = random.choice(motivations_mvp)
    important = random.choice(motivations_important)
    mvpossession = random.choice(most_valuable_possession)
    feelings = random.choice(feelings_towards_people)
    cyber = cybernetics(False)
    aw = armor_weapons('Fixer')
    print_everything(first, last, classrole, int, ref, tech, cool, attr, luck,
                     ma, body, emp, run, leap, lift, save, btm, special_ability,
                     clothes, hairstyle, affectations, education, personality,
                     mvp, important, mvpossession, feelings, cyber, aw)
    print_skills('Awareness/Notice:\t', 'Forgery:\t\t', 'Handgun:\t\t', 'Persuasion:\t\t',
                 'Pick Lock:\t\t', 'Pick Pocket:\t\t', 'Brawling:\t\t', 'Melee:\t\t\t',
                 'Intimidate:\t\t', skillstable)

def nomad():
    first = set_first_name()
    last = set_last_name()
    classrole = 'Nomad'
    int = random.randint(2, 5)
    ref = random.randint(5, 10)
    tech = random.randint(2, 10)
    cool = random.randint(5, 10)
    attr = random.randint(2, 10)
    luck = random.randint(2, 10)
    ma = random.randint(2, 10)
    body = random.randint(2, 10)
    emp = random.randint(2, 10)
    run = ma * 3
    leap = run / 4
    lift = body * 10
    save = body
    if body == 2:
        btm = 0
    if body == 3 or body == 4:
        btm = -1
    if body == 5 or body == 6 or body == 7:
        btm = -2
    if body == 8 or body == 9:
        btm = -3
    if body == 10:
        btm = -4
    special_ability = 'Family'
    skillstable = generate_skills()
    clothes = random.choice(style_clothes)
    hairstyle = random.choice(style_hairstyle)
    affectations = random.choice(style_affectations)
    education = random.choice(education_level)
    personality = random.choice(motivations_personality)
    mvp = random.choice(motivations_mvp)
    important = random.choice(motivations_important)
    mvpossession = random.choice(most_valuable_possession)
    feelings = random.choice(feelings_towards_people)
    cyber = cybernetics(False)
    aw = armor_weapons('Nomad')
    print_everything(first, last, classrole, int, ref, tech, cool, attr, luck,
                     ma, body, emp, run, leap, lift, save, btm, special_ability,
                     clothes, hairstyle, affectations, education, personality,
                     mvp, important, mvpossession, feelings, cyber, aw)
    print_skills('Awareness/Notice:\t', 'Endurance:\t\t', 'Melee:\t\t\t', 'Rifle:\t\t\t',
                 'Wilderness Survival:\t', 'Drive:\t\t\t', 'Basic Tech:\t\t', 'Brawling:\t\t',
                 'Athletics:\t\t', skillstable)

def generic():
    first = set_first_name()
    last = set_last_name()
    classrole = 'Generic'
    clothes = random.choice(style_clothes)
    hairstyle = random.choice(style_hairstyle)
    affectations = random.choice(style_affectations)
    personality = random.choice(motivations_personality)
    mvp = random.choice(motivations_mvp)
    important = random.choice(motivations_important)
    mvpossession = random.choice(most_valuable_possession)
    feelings = random.choice(feelings_towards_people)
    aw = armor_weapons('Generic')
    print('\n\nNAME:', first, last, '\tCLASS: Generic')
    print('Armor:\t', aw[0])
    print('Weapon:\t', aw[1])
    print('\tSTYLE:')
    print('Clothes:\t', clothes)
    print('Hairstyle:\t', hairstyle)
    print('Affectations:\t', affectations)
    print('\tMOTIVATIONS:')
    print('Personality:\t\t\t', personality)
    print('Most Valuable Person:\t\t', mvp)
    print('Most Important Value:\t\t', important)
    print('Feelings towards most people:\t', feelings)
    print('Most valuable possession:\t', mvpossession)

# driving function
def create_humans(classrole, count):
    while count < num:
        if classrole == 1:
            rockerboy()
            count = count + 1
        if classrole == 2:
            solo()
            count = count + 1
        if classrole == 3:
            netrunner()
            count = count + 1
        if classrole == 4:
            techie()
            count = count + 1
        if classrole == 5:
            medtech()
            count = count + 1
        if classrole == 6:
            media()
            count = count + 1
        if classrole == 7:
            cop()
            count = count + 1
        if classrole == 8:
            corporate()
            count = count + 1
        if classrole == 9:
            fixer()
            count = count + 1
        if classrole == 10:
            nomad()
            count = count + 1
        if classrole == 11:
            count = count + 1
            create_humans(random.randint(1, 10), count)
        if classrole == 12:
            generic()
            count = count + 1
        if classrole > 12 or classrole < 1:
            count += 1
            print('\n\nOut of bounds. Seriously, you can\'t even count to 12? Whatever, creating generics.')
            create_humans(12, count)

create_humans(role, count)

# Can run in command prompt. Navigate to working directory and use 'python NPCgenerator.py'.
# Formatting is designed around use in command prompt.
# Version 1.0, finished 1/20/21.

# This code is a mess and a half, and very long, but the UI is clean and simple.

# Edit 1.1: Added option to choose between genders or select random.