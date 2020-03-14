
def numeri_primi():
    try:
        with open('numeri_primi.txt', mode="r") as testo:
            primi_str = testo.read().split()
        primi = []
        for n in primi_str:
            primi.append(int(n))
    except FileNotFoundError:
        with open('numeri_primi.txt', mode="w") as testo:
            testo.write("2")
        primi = int(testo.read().split())
    with open("numeri_primi.txt", mode="a") as testo:
        for n in range(primi[-1],10000000000):
            primo = True
            for m in primi:
                if n%m == 0:
                    primo = False
                    break
            if primo:
                primi.append(n)
                testo.write("\n"+str(n))

if __name__ == "__main__":
    numeri_primi()