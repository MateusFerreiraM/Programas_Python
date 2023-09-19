x0, y0, x1, y1 = map(int,input().split())
x2, y2, x3, y3 = map(int,input().split())

if (x2 > x0 and x2 < x1) or (x3 > x0 and x3 < x1):
    print("1")

else:
    if (y2 > y0 and y2 < y1) and (y3 > y0 and y3 < y1):
        print("1")
        
    else:
        print("0")
