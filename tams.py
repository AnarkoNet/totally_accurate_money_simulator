import random
import time
import math
words=open("words.txt").read().split("\n")[:-1]
class workjob:
    def mathwork():
        print("WORK")
        a=int(1/(random.random()*random.random()))
        b=int(1/(random.random()*random.random()))
        op=random.randint(0,9)
        if op<=3:   # 4/10
            op="+"
        elif op<=6: # 3/10
            op="-"
        elif op<=8: # 2/10
            op="*"
        else:       # 1/10
            op="%"
        answer=str(eval(f"{a}{op}{b}"))
        inp=input(f"| Solve (\033[96m{a}\033[0m{op}\033[96m{b}\033[0m)=").replace(" ","").replace(",","").replace("_","").split(".")[0]
        if inp==answer:
            print("| \033[92mCorrect!\033[0m")
            return True
        else:
            print("| \033[91mWrong!\033[0m")
            return False
    def wordwork():
        print("WORK")
        sent=[random.choice(words)]
        while (random.random()<=1/(2*(len(sent)))):
            sent.append(random.choice(words))
        sent=" ".join(sent).upper()
        print("| Repeat \"\033[96m"+sent+"\033[0m\" in lowercase!")
        inp=input("|         \033[96m")
        if inp==sent.lower():
            print("\033[0m| \033[92mCorrect!\033[0m")
            return True
        else:
            print("\033[0m| \033[91mWrong!\033[0m")
            return False
def main():
    money=float(input("Start with $").replace(",","").replace("$",""))
    bank=0
    lastbank=time.time()
    gamblerate=0.5
    bankrate=0.001 # per second
    #paylastchecked=time.time()
    currentjob="unemployed"
    currentpay=0 # per minute
    payearned=0
    lastworked=0# time.time()
    lastcmd=""
    taxrate=0.25
    assets=[]
    # {"car":{"materialval":5000,"marketval":10000},"strength":0.8,"condition":0.9}
    def checkbank(val,rate,last):
        return (val*((1+(rate))**(time.time()-last))), time.time()
    def gamble(P,c):
        if random.random()<=c:
            print(f"\x1b[92m+${((P/c)-P):,.2f}\x1b[0m")
            return P/c
        else:
            print(f"\x1b[91m-${P:,.2f}\x1b[0m")
            return 0
    def genjobname():
        return words[random.randint(0,len(words)-1)]+"man"
    def randinrange(x,y=None):
        if y==None:
            return x/random.random()
        else:
            return (1/(random.random()/2+0.5)-1)*abs(x-y)+min(x,y)
    inp=input("\x1b[95m>>> \x1b[0m").lower().replace(",","").replace("$","")
    while inp!="q":
        inp=inp.split(" ")
        if inp[0] in ["last","l"]:
            inp=lastcmd
        if inp[0] in ["withdraw","wd","w"]:
            try:
                inp=inp[1]
                bank, lastbank = checkbank(bank,bankrate,lastbank)
                if inp=="all":
                    inp=bank
                elif inp=="half":
                    inp=bank/2
                else:
                    inp=float(inp)
                    if inp>bank or inp<0:
                        raise ValueError
                bank-=inp
                money+=inp
            except Exception:
                print("\x1b[93mAction could not be completed\x1b[0m")
        elif inp[0] in ["deposit","d","bank","save"]:
            try:
                inp=inp[1]
                
                if inp=="all":
                    inp=money
                elif inp=="half":
                    inp=money/2
                else:
                    inp=float(inp)
                    if inp>money or inp<0:
                        raise ValueError
                money-=inp
                bank, lastbank = checkbank(bank,bankrate,lastbank)
                bank+=inp
            except Exception:
                print("\x1b[93mAction could not be completed\x1b[0m")
        elif inp[0] in ["gamble","g","bet","b"]:
            try:
                if len(inp)>=4:
                    if inp[2] in ["as","at","for","by"]:
                        if "%" in inp[3]:
                            gamblerate=(float(inp[3].replace("%",""))/100)%1
                        else:
                            gamblerate=float(inp[3])%1
                inp=inp[1]
                if inp=="all":
                    inp=money
                elif inp=="half":
                    inp=money/2
                else:
                    inp=float(inp)
                    if inp>money or inp<0:
                        raise ValueError
                money-=inp
                money+=gamble(inp,gamblerate)
            except Exception:
                print("\x1b[93mAction could not be completed\x1b[0m")
        elif inp[0] in ["apply","a"]:
            joboffer={"name":genjobname(),"pay":randinrange(6646)} # 6_646 97_578 150_000_000_000
            inp=input(f"Work as \033[35m{joboffer["name"]}\033[0m for \033[92m${joboffer["pay"]:,.2f}\033[0m/min? (Y/N) ").lower().replace(" ","")[:1]
            if inp == "y":
                currentjob=joboffer["name"]
                currentpay=joboffer["pay"]
                print("Accepted!")
                lastworked=time.time()
            else:
                print("Disregarded")
        elif inp[0] in ["quitjob","qj"]:
            currentjob-"unemployed"
            currentpay=0
            print("Job quit")
        else:
            print("\x1b[93mAction could not be completed\x1b[0m")
        if currentjob!="unemployed":
            if time.time()-lastworked>=20:
                if bool(random.randint(0,1)):
                    success=workjob.mathwork()
                else:
                    success=workjob.wordwork()
                if success:
                    bank, lastbank = checkbank(bank,bankrate,lastbank)
                    bank+=currentpay/3
                    lastworked=time.time()
                else:
                    print("\033[91mFIRED!")
                    currentjob="unemployed"
                    currentpay=0
        bank, lastbank = checkbank(bank,bankrate,lastbank)
        print(f"\033[35m{currentjob} (${currentpay:,.2f}/min)") # Unemployed ($0/min) $0
        print(f"\x1b[34m${bank:,.2f} \x1b[0m${money:,.2f}")
        inp=input("\x1b[95m>>> \x1b[0m").lower().replace(",","").replace("$","")
if __name__=="__main__":
    main()
# cost of living is $21_600/min
# absolute minimum is $1_800/min (0-3600)
# taxes take 15% to 30% of pay