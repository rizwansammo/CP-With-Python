def possibleSmallest(pattern):
    maxTemp=0
    valLast=0
    lenMsg=len(pattern)

    if lenMsg>8:
        return -1

    out=[]

    i=0
    while i<lenMsg:
        numofM=0
        if pattern[i]=='N':
            numofM=pattern[i+1: ].count('M')

            if i==0:
                maxTemp=numofM+2
                valLast=valLast+1
                out.append(str(valLast))
                out.append(str(maxTemp))
                valLast=maxTemp
            else:
                maxTemp=maxTemp+numofM+1
                valLast=maxTemp
                out.append(str(valLast))
            for k in range(numofM):
                valLast=valLast-1
                out.append(str(valLast))
                i=i+1
        else:
            if i==0:
                j=i+1
                numofM=0
                #find the number of next M.
                while j<lenMsg and pattern[j]=='M':
                    numofM += 1
                    j += 1
                maxTemp=numofM+2
                out.append(str(maxTemp))
                out.append(str(maxTemp-1))
                valLast=maxTemp-1
            else:
                out.append(str(valLast-1))
                valLast=valLast-1
        i=i+1
    return "".join(out)

if __name__ == "__main__":
    print(possibleSmallest("MNM"))
