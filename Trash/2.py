def validate(n):
    m = str(n)
    for index in range(len(m)):
        n_list = []
        for i in range(-2,3):
            n_list.append(index + i)
        n_list.pop(2)
        for j in range(3):
            if n_list[0]<0:
                n_list.remove(n_list[0])
            if n_list[-1]>4:
                n_list.remove(n_list[-1])
        c = 0
        for k in n_list:
            if m[c] == m[k]:
                print(False)
            else:
                print(True)
            c = c+1
                
            
validate(12225)