def write_to_excel(b):
    with open(r'C:\Users\Administrator\Desktop\ML\test\20170309.txt','r') as y:
        import xlwt
        w = xlwt.Workbook()
        sheet = w.add_sheet('sheet2')
        listss =[]
        global c,buf
        for line in y:
            c = line.split(',')
            listss.append(c)
        for i in range(len(listss)):
                #print(type(listss[i]))
            for l in range(len(listss[i])):
                print (listss[i][l])
                sheet.write(i,l,listss[i][l])
        w.save(b)
