n=int(input("Digite um número: "))
f1=0
f2=1
sequencia="0, 1"

for i in range(2, n+1):
    fi=f1+f2
    f1=f2
    f2=fi
    sequencia=sequencia+', '+str(fi)

print(sequencia)    