from os import system
def numeri_primi():
    primi=[]
    totale=0
    n_finale=""
    while type(n_finale) is not int:
        try:
            n_finale=int(input("\nFino a che numero? "))
        except:
            None
    for n in range(2,n_finale+1):
        primo=True
        for m in primi:
            if n%m==0:
                primo=False
                break
        if primo==True:
            print(n)
            primi.append(n)
    totale=len(primi)
    print(f"\nI numeri primi fino a {n_finale} sono: {totale}")
    replay=input("\nVuoi usare ancora l'applicazione?\nrispondere con s/n (default=s) ").lower()
    return replay=="s" or replay==""

if __name__ == "__main__":
    while numeri_primi():
        None