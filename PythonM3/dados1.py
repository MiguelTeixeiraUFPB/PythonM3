def fat(n):
    if (n==0) or (n==1):
        print("Retornando 1")
        return 1
    else:
        print("Vai chamar fat(",n-1,")")
        return n*fat(n-1)
print(fat(6))