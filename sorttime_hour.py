def sorttime():
    import os
    basepath = r'C:\Users\Administrator\Desktop\ML\结果3'
    sPath = r'C:\Users\Administrator\Desktop\ML\test'
    global s
    s =0
    lisy = []
    list0 = [0]*24
    listsssss =[]
    listssss = []
    listss = []
    listsss = ['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath,sChild)
        sChildPath2 =os.path.join(basepath,sChild)
        filename1 =sChildPath
        filename = sChildPath2
        with open(filename1,'r') as f:
            for line1 in f.readlines():
                q =line1.split(',')
                listss.append(q)
                listssss.append(q[1])
            listns = list(set(listssss))
            with open(filename,'w') as g:
                for l in range(len(listns)):
                    while len(list0)<25:
                        list0.insert(0,int(listns[l]))
                        for j in listsss:
                            for i in range(len(listss)):
                                if int(listns[l]) ==int(listss[i][1]):
                                    if int(j) == int(listss[i][0][8:10]):
                                        list0[int(j)+1] =int(listss[i][2])
                                        if int(j) == 23:
                                            print(list0)
                                            g.write(str(list0)+'\n')
                                    
                    list0 =[0]*24
                            
                            
            #w.save(r'C:\Users\Administrator\Desktop\ML\结果3\20170309.xls')