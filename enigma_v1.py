def list_move(l,n):
    cnt = 0
    for _ in range(len(l)):
        if cnt == n:
            break
        l.append(l[0])
        l.remove(l[0])
        cnt +=1
    return l

def list_reverse(l,n):
    cnt = 0
    for i in range(len(l)):
        if cnt == n:
            break
        l.insert(0,l.pop())
        cnt +=1
    return l



list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
list2 = ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

list3 = ['X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
list4 = ['K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W']

list5 = ['P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','A','B']
list6 = ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M','N','O']

reflect_list = ['T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E','F']
reflect_list_1 = ['G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S']



ec1 = list1.copy()
ec2 = list2.copy()
ec3 = list3.copy()
ec4 = list4.copy()
ec5 = list5.copy()
ec6 = list6.copy()
ec_rl = reflect_list.copy()
ec_rl1 = reflect_list_1.copy()

dc1 = list1.copy()
dc2 = list2.copy()
dc3 = list3.copy()
dc4 = list4.copy()
dc5 = list5.copy()
dc6 = list6.copy()
dc_rl = reflect_list.copy()
dc_rl1 = reflect_list_1.copy()


Enc1 = {}
Enc2 = {}
Enc3 = {}
Reflector = {}

Dnc1 = {}
Dnc2 = {}
Dnc3 = {}
Dnc_rl = {}

def generate_Dnc():
    #print(dc1,dc2)
    for i in range(0,13):
        Dnc1[dc1[i]] = dc2[i]
        Dnc1[dc2[i]] = dc1[i]

        Dnc2[dc3[i]] = dc4[i]
        Dnc2[dc4[i]] = dc3[i]

        Dnc3[dc5[i]] = dc6[i]
        Dnc3[dc6[i]] = dc5[i]

        Dnc_rl[dc_rl[i]] = dc_rl1[i]
        Dnc_rl[dc_rl1[i]] = dc_rl[i]

def generate_Enc():
    #print(ec1,ec2)
    for i in range(0,13):
        Enc1[ec1[i]] = ec2[i]
        Enc1[ec2[i]] = ec1[i]

        Enc2[ec3[i]] = ec4[i]
        Enc2[ec4[i]] = ec3[i]

        Enc3[ec5[i]] = ec6[i]
        Enc3[ec6[i]] = ec5[i]

        Reflector[ec_rl[i]] = ec_rl1[i]
        Reflector[ec_rl1[i]] = ec_rl[i]


def encryption():
    ans = []
    print('Enter "EXIT" to exit || 输入"EXIT"退出')
    print('Enter "DONE" to print the answer || 输入"DONE"打印答案')
    while True:
        generate_Enc()
        #print(ec1,'\n',ec2)
        #print(Enc1)
        w = input("Enter the word: || 输入单词: ")
        if w == 'exit' or w == 'Exit' or w == 'EXIT':
            break
        elif w == 'done' or w == 'Done' or w == 'DONE' :
            print("".join(ans))
            ans.clear()
        else:
            #print(w,'->')
            w = Enc1[w]  #一号转子加密
            #print(w,'->')
            w = Enc2[w]  #二号转子加密
            #print(w,'->')
            w = Enc3[w] #三号转子加密
            #print(w,'->')  
            w = Reflector[w] #反射器加密
            #print(w,'->')  
            w = Enc3[w] #三号转子加密
            #print(w,'->')  
            w = Enc2[w]  #二号转子加密
            #print(w,'->') 
            w = Enc1[w]  #一号转子加密
            print(w)
            ans.append(w)
            
            list_move(ec1,1) #一号转子移动
            #list_move(ec2,1) 
            
            if ec1[0] == 'A': #一号转子到达A时，二号转子移动
                list_move(ec3,1)
                #list_move(ec4,1)

                if ec3[0] == 'X': #二号转子到达X时，三号转子移动
                    list_move(ec5,1)
                    #list_move(ec6,1)

                    if ec5[0] == 'P':
                        list_move(ec_rl,1)
                        #list_move(ec_rl1,1)
            
            

def decryption():
    ans = []
    print('Enter "EXIT" to exit || 输入"EXIT"退出')
    print('Enter "DONE" to print the answer || 输入"DONE"打印答案')
    while True:
        generate_Dnc()
        #print(dc1,'\n',dc2)
        #print(Dnc1)
        
        w = input("Enter the word: || 输入单词: ")
        if w == 'exit' or w == 'Exit' or w == 'EXIT':
            break
        elif w == 'done' or w == 'Done' or w == 'DONE':
            print("".join(ans))
            ans.clear()
        else:
            #print(w,'->')
            w = Dnc1[w]  #一号转子加密
            #print(w,'->')
            w = Dnc2[w]  #二号转子加密
            #print(w,'->')
            w = Dnc3[w] #三号转子加密
            #print(w,'->')  
            w = Dnc_rl[w] #反射器加密
            #print(w,'->')  
            w = Dnc3[w] #三号转子加密
            #print(w,'->')  
            w = Dnc2[w]  #二号转子加密
            #print(w,'->') 
            w = Dnc1[w]  #一号转子加密
            print(w)  
            ans.append(w)
            
            list_move(dc1,1) #一号转子移动
            #list_move(dc2,1) 
            if dc1[0] == 'A': #一号转子到达A时，二号转子移动
                list_move(dc3,1)
                #list_move(dc4,1)

                if dc3[0] == 'X': #二号转子到达X时，三号转子移动
                    list_move(dc5,1)
                    #list_move(dc6,1)

                    if dc5[0] == 'P':
                        list_move(dc_rl,1)
                        #list_move(dc_rl1,1)
            



if __name__ == '__main__':
    print('Enter "EXIT" to exit || 输入"EXIT"退出')
    print("Enter '1' to enter the encryption mode || 输入 '1' 进入加密模式")
    print("Enter '2' to enter the decryption mode || 输入 '2' 进入解密模式") 
    print("Invalid mode will not be accepted || 无效模式将不被接受")
    while True:
        mode = input("Enter the mode: / 输入模式: ")
        if mode == '1':
            encryption()
        elif mode == '2':
            decryption()
        elif mode == 'exit' or mode == 'Exit' or mode == 'EXIT':
            break
        else:
            print("Invalid mode || 无效模式")
            continue