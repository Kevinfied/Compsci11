count = int(input())


line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))

tapes1 = [0] * count
tapes2 = [0] * count




for i in range(count):
    if tapes1[i] == 1:
        if i % 2 == 0:
            if i in range(1, count-1):
                if line1[i] == line1[i-1] == 1 and line1[i] == line1[i+1] == 1:
                    if line1[i] == line2[i] == 1:
                        tapes1[i] = 0
                    else:
                        tapes1[i] = 1

                elif line1[i] == line1[i-1] == 1 or line1[i] == line1[i+1] == 1:
                    if line1[i] == line2[i] == 1:
                        tapes1[i] = 1
                    else:
                        tapes1[i] = 2

                elif line1[i] == line2[i] == 1:
                    tapes1[i] = 2

                elif line1[i] == 1:
                    tapes1[i] = 3




            if i == 0:
                if line1[0] == 1:
                    if line1[0] == line1[1] == 1:
                        if line1[0] == line2[0] == 1:
                            tapes1[0] = 1
                        else:
                            tapes1[0] = 2

                    else:
                        if line1[0] == line2[0] == 1:
                            tapes1[0] = 2
                        else:
                            tapes1[0] = 3


            if i == count-1:
                if line1[i] == 1:
                    if line1[i] == line1[i-1] == 1:
                        if line1[i] == line2[i]:
                            tapes1[i] = 1
                        else:
                            tapes1[i] = 2
                    else:
                        if line1[i] == line2[i] == 1:
                            tapes1[i] = 2
                        else:
                            tapes1[i] = 3



        else:
            if i in range(1, count-1):
                if line1[i] == line1[i-1] == 1 and line1[i] == line1[i+1] == 1:
                    tapes1[i] = 1
                elif line1[i] == line1[i-1] or line1[i] == line1[i+1]:
                    tapes1[i] = 2


for i in range(count):
    if tapes2[i] == 1:
        if i % 2 == 0:
            if i in range(1, count-1):
                if line2[i] == line2[i-1] == 1 and line2[i] == line2[i+1] == 1:
                    if line2[i] == line1[i] == 1:
                        tapes2[i] = 0
                    else:
                        tapes2[i] = 1

                elif line2[i] == line2[i-1] == 1 or line2[i] == line2[i+1] == 1:
                    if line2[i] == line1[i] == 1:
                        tapes2[i] = 1
                    else:
                        tapes2[i] = 2

                elif line2[i] == line1[i] == 1:
                    tapes2[i] = 2

                elif line2[i] == 1:
                    tapes2[i] = 3

        if i == 0:
            if line2[0] == 1:
                if line2[0] == line2[1] == 1:
                    if line2[0] == line1[0] == 1:
                        tapes2[0] = 1
                    else:
                        tapes2[0] = 2

                else:
                    if line2[0] == line1[0] == 1:
                        tapes2[0] = 2
                    else:
                        tapes2[0] = 3

        if i == count-1:
            if line2[i] == 1:
                if line2[i] == line2[i-1] == 1:
                    if line2[i] == line1[i]:
                        tapes2[i] = 1
                    else:
                        tapes2[i] = 2
                else:
                    if line2[i] == line1[i] == 1:
                        tapes2[i] = 2
                    else:
                        tapes2[i] = 3



print(tapes1)
print(tapes2)

print(sum(tapes1)+sum(tapes2))

