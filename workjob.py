import random
words=open("words.txt").read().split("\n")[:-1]

def mathwork():
    print("WORK")
    a = int(1/(random.random()*random.random()))
    b = int(1/(random.random()*random.random()))
    op = random.randint(0,9)
    if op <= 3:
        op = "+"
    elif op <= 6:
        op = "-"
    elif op <= 8:
        op = "*"
    else:
        op = "%"
    answer = str(eval(f"{a}{op}{b}"))
    inp = input(f"| Solve (\033[96m{a}\033[0m{op}\033[96m{b}\033[0m)=").replace(" ","").replace(",","").replace("_","").split(".")[0]
    if inp == answer:
        print("| \033[92mCorrect!\033[0m")
        return True
    else:
        print("| \033[91mWrong!\033[0m")
        return False

def wordwork():
    print("WORK")
    sent = [random.choice(words)]
    while random.random() <= 1/(2*len(sent)):
        sent.append(random.choice(words))
    sent = " ".join(sent).upper()
    print("| Repeat \"\033[96m"+sent+"\033[0m\" in lowercase!")
    inp = input("|         \033[96m")
    if inp == sent.lower():
        print("\033[0m| \033[92mCorrect!\033[0m")
        return True
    else:
        print("\033[0m| \033[91mWrong!\033[0m")
        return False

def sequencework():
    print("WORK")
    start = random.randint(1, 15)
    difference = random.randint(2, 9)
    length = random.randint(3, 5)
    sequence = [start + difference*i for i in range(length)]
    answer = sequence[-1] + difference
    print("| Complete the sequence:")
    print("| \033[96m" + ", ".join(map(str,sequence)) + ", ?\033[0m")
    inp = input("| Next number: ").strip()
    if inp == str(answer):
        print("| \033[92mCorrect!\033[0m")
        return True
    else:
        print("| \033[91mWrong!\033[0m")
        return False

def estimationwork():
    print("WORK")
    a = random.randint(20, 1000)
    b = random.randint(2, 15)
    answer = round((a/b))
    print("| Estimate the result of:")
    print("| \033[96m" + str(a) + " / " + str(b) + "\033[0m")
    print("| (Round to the nearest ten)")
    try:
        inp = round(float(input("| ").replace(" ","")))
    except ValueError:
        inp = -20
    if abs(inp-answer)<10:
        print("| \033[92mCorrect!\033[0m")
        return True
    else:
        print("| \033[91mWrong!\033[0m")
        return False

def attentionwork():
    print("WORK")
    length = random.randint(8, 20)
    target = str(random.randint(0, 9))
    sequence = "".join(str(random.randint(0, 9)) for _ in range(length))
    count = sequence.count(target)
    print("| How many times does \033[96m" + target + "\033[0m appear?")
    print("| \033[96m" + sequence + "\033[0m")
    inp = input("| ").strip()
    if inp == str(count):
        print("| \033[92mCorrect!\033[0m")
        return True
    else:
        print("| \033[91mWrong!\033[0m")
        return False

def percentwork():
    print("WORK")
    a = random.randint(20, 200)
    b = random.choice([10, 20, 25, 50])
    answer = round(a*b/100)
    print("| What is \033[96m" + str(b) + "%\033[0m of \033[96m" + str(a) + "\033[0m?")
    try:
        inp = round(float(input("| ").replace(" ", "")))
    except ValueError:
        inp = -1
    if inp == answer:
        print("| \033[92mCorrect!\033[0m")
        return True
    else:
        print("| \033[91mWrong!\033[0m"+str(answer))
        return False

def letterwork():
    print("WORK")

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    a = random.randint(0, 25)

    if random.random() < 0.5:
        print("| What is the position of \033[96m" + alphabet[a] + "\033[0m in the alphabet?")
        answer = str(a+1)
    else:
        print("| What letter is number \033[96m" + str(a+1) + "\033[0m in the alphabet?")
        answer = alphabet[a]

    inp = input("| ").strip().upper()

    if inp == answer:
        print("| \033[92mCorrect!\033[0m")
        return True
    else:
        print("| \033[91mWrong!\033[0m")
        return False

def hexwork():
    print("WORK")

    a = random.randint(10, 255)
    answer = hex(a)[2:].upper()

    print("| Convert \033[96m" + str(a) + "\033[0m to hexadecimal!")

    inp = input("| ").replace(" ", "").upper()

    if inp == answer:
        print("| \033[92mCorrect!\033[0m")
        return True
    else:
        print("| \033[91mWrong!\033[0m")
        return False

def binarywork():
    print("WORK")

    a = random.randint(1, 63)
    answer = bin(a)[2:]

    print("| Convert \033[96m" + str(a) + "\033[0m to binary!")

    inp = input("| ").replace(" ", "")

    if inp == answer:
        print("| \033[92mCorrect!\033[0m")
        return True
    else:
        print("| \033[91mWrong!\033[0m")
        return False
