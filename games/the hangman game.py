import random
print('''\n 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    \n\n''')
words=[
'abruptly','absurd','abyss','affix','askew','avenue','awkward','axiom','azure',
'bagpipes','bandwagon','banjo','bayou','beekeeper','bikini','blitz','blizzard','boggle','bookworm','boxcar','boxful','buckaroo','buffalo','buffoon','buxom','buzzard','buzzing','buzzwords',
'caliph','cobweb','cockiness','croquet','crypt','curacao','cycle',
'daiquiri','dirndl','disavow','dizzying','duplex','dwarves', 
'embezzle','equip','espionage','euouae','exodus', 
'faking','fishhook','fixable','fjord','flapjack','flopping','fluffiness','flyby','foxglove','frazzled','frizzled','fuchsia','funny', 
'gabby','galaxy','galvanize','gazebo','giaour','gizmo', 'glowworm', 'glyph', 'gnarly', 'gnostic', 'gossip', 'grogginess', 
'haiku', 'haphazard', 'hyphen', 
'iatrogenic', 'icebox', 'injury', 'ivory', 'ivy',
'jackpot', 'jaundice', 'jawbreaker', 'jaywalk', 'jazziest', 'jazzy', 'jelly', 'jigsaw', 'jinx', 'jiujitsu', 'jockey', 'jogging', 'joking', 'jovial', 'joyful', 'juicy', 'jukebox', 'jumbo',
'kayak', 'kazoo', 'keyhole', 'khaki', 'kilobyte', 'kiosk', 'kitsch', 'kiwifruit', 'klutz', 'knapsack', 
'larynx', 'lengths', 'lucky', 'luxury', 'lymph',
'marquis', 'matrix', 'megahertz', 'microwave', 'mnemonic', 'mystify',
'naphtha', 'nightclub', 'nowadays', 'numbskull', 'nymph',
'onyx', 'ovary', 'oxidize', 'oxygen', 
'pajama', 'peekaboo', 'phlegm', 'pixel', 'pizazz', 'pneumonia', 'polka', 'pshaw', 'psyche', 'puppy', 'puzzling',
'quartz', 'queue', 'quips', 'quixotic', 'quiz', 'quizzes', 'quorum', 
'razzmatazz', 'rhubarb', 'rhythm', 'rickshaw',
'schnapps', 'scratch', 'shiv', 'snazzy', 'sphinx', 'spritz', 'squawk', 'staff', 'strength', 'strengths', 'stretch', 'stronghold', 'stymied', 'subway','swivel','syndrome',
'thriftless','thumbscrew','topaz','transcript','transgress','transplant','triphthong', 
'twelfth','twelfths', 
'unknown','unworthy','unzip','uptown', 
'vaporize','vixen','vodka','voodoo','vortex','voyeurism', 
'walkway','waltz','wave','wavy','waxy','wellspring','wheezy','whiskey','whizzing','whomever','wimpy','witchcraft','wizard','woozy','wristwatch','wyvern', 
'xylophone', 
'yachtsman','yippee','yoked','youthful','yummy',
'zephyr','zigzag','zigzagging','zilch','zipper','zodiac','zombie']


n=random.choice(words)
r=""
k=7
s=[]
z=""


for i in range(0,len(n)):
    s.append(" _ ")

while r!="loss":
    z=""
    x=0
    g=input("guess a letter : ").lower()
    for i in range(0,len(n)):
        if n[i]==g:
            s[i]=" "+g+" "
            x+=1
    for i in range(0,len(s)):
        z=z+s[i]
        
    if x==0:
        k-=1
        if k==6:
            print(f"""you took {g} which is not in the letter\n{z}\n      _______
     |/      |
     |  
     |  
     |       
     |      
     |
     |___\n""")
        elif k==5:
            print(f"""you took {g} which is not in the letter\n\n{z}\n      _______
     |/      |
     |      (_)
     |  
     |       
     |      
     |
     |___\n""")
        elif k==4:
            print(f"""you took {g} which is not in the letter\n\n{z}\n      _______
     |/      |
     |      (_)
     |      \|
     |      
     |      
     |
     |___\n""")
        elif k==3:
            print(f"""you took {g} which is not in the letter\n\n{z}\n      _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
     |___\n""")
        elif k==2:
            print(f"""you took {g} which is not in the letter\n\n{z}\n      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
     |___\n""")
        elif k==1:
            print(f"""you took {g} which is not in the letter\n\n{z}\n      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
     |___\n""")
        elif k==0:
            r="loss"
            print(f"""you took {g} which is not in the letter\n\n{z}\n      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \ 
     |
     |___\n\nyou lost""")
    else:
        print(f"""you took {g} which is in the letter\n{z}\n""")

    if z==n:
        print("you won")
        break
