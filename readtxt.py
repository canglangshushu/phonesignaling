def readtxt(a ,b,c):
    global s
    s =0
    listss = []
    with open(a,'r') as f:
        with open(b,'r') as g:
            with open(c,'w') as h:
                for line2 in g.readlines():#将b文件里的每一行的第一个元素写入到listss列表里
                    l = line2.split(',')
                    listss.append(l[0])
                for line1 in f.readlines():#用逗号分割a文件里的每一行用
                    q = line1.split(',')
                    for j in listss:
                        if int(q[1]) ==int(j):
                            h.write(line1)
                            print(line1+'writed')
                            s += 1
                            print(s)