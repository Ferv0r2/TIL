H, M = list(map(int, input().split()))

alreay = 45

if M >= alreay:
    print(H, M-alreay)
else:
    if H == 0:
        print(H+23, M-alreay+60)
    else:
        print(H-1, M-alreay+60)