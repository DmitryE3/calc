def gen(cubs,arg)
    while True:
        for i in range(len(cubs)):
            print(cubs)
            cubs[i]+=1
            yield cubs