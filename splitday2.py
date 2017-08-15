def splitday2(a,b):
    import os
    basepath = r'C:\Users\Administrator\Desktop\ML\结果'
    global s
    s =0
    listss = []
    with open(a,'r') as f:
        with open(b,'r') as g:
            for line1 in f.readlines():#将b文件里的每一行的第一个元素写入到listss列表里
                q = line1.split(',')
                listss.append(q)
            for line2 in g.readlines():#用逗号分割a文件里的每一行用
                l = line2.split(',')
                for i in range(len(listss)):
                    if int(l[0]) == int(listss[i][0][:8]):
                        basename = l[0]+'.txt'
                        filename = os.path.join(basepath,basename)
                        with open(filename,'a+') as h:
                            h.write(str(listss[i])+ '\n')
                        s += 1
                        print(s)