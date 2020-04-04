import random

a=10


while(True):
    p1c=50
    p2c=50
    p3c=50

    
    p1c=p1c-1
    p2c=p2c-1
    p3c=p3c-1
    

    p1=[[random.randrange(2,15,1),random.randrange(1,5,1)],[random.randrange(2,15,1),random.randrange(1,5,1)]]
    p2=[[random.randrange(2,15,1),random.randrange(1,5,1)],[random.randrange(2,15,1),random.randrange(1,5,1)]]
    p3=[[random.randrange(2,15,1),random.randrange(1,5,1)],[random.randrange(2,15,1),random.randrange(1,5,1)]]
    f3=[[random.randrange(2,15,1),random.randrange(1,5,1)],[random.randrange(2,15,1),random.randrange(1,5,1)],[random.randrange(2,15,1),random.randrange(1,5,1)]]
    preR=[random.randrange(2,15,1),random.randrange(1,5,1)]
    R=[random.randrange(2,15,1),random.randrange(1,5,1)]
    x1=p1[:2]
    x2=p2[:2]
    x3=p3[:2]

    def check(p,b,n):
     z=0
     for i in range(n):
            if( b.count(b[i])>0):
                z=1
                b[i]=[random.randrange(2,15,1),random.randrange(1,5,1)]

            elif(z==0):
                break
            
        
     
     while(True):
            
        if((p[0] in b) or (p[1] in b)):
           for i in range(n):
              if(p[0]==b[i] or p[1]==b[i]):
                 b[i]= [random.randrange(2,15,1),random.randrange(1,5,1)]
                 check(p,b,n)

        else:
            break
             

    def show(sp,n):
        #sp=[[1,3],[2,4]]
        y=[[0,0],[0,0],[0,0],[0,0],[0,0]]
        for i in range(n):
            y[i][0]=sp[i][0]
            y[i][0]=sp[i][0]
        for i in range(1,5):
            for j in range(n):
                if(sp[j][1]==i):
                        if(i==1):
                                y[j][1]='clubs'

                        if(i==2):
                                y[j][1]='diamonds'


                        if(i==3):
                                y[j][1]='hearts'

                        if(i==4):
                                y[j][1]='spade'

        for i in range(n):
            if(sp[i][0]==11):
                y[i][0]='J'

            if(sp[i][0]==12):
                y[i][0]='Q'

            if(sp[i][0]==13):
                y[i][0]='K'

            if(sp[i][0]==14):
                y[i][0]='A'

            

            

            


        print(y[:n])




                        
        
        
        
        

    


    def status(p1c,p2c,p3c):
        
     x=int(input("Enter player number for viewing status"))
     check(p1,p2,2)
     check(p1,p3,2)
     check(p2,p1,2)
     check(p2,p3,2)
     check(p3,p1,2)
     check(p3,p2,2)

     if(x==1):
        print(p1c)
        show(p1,2)

     elif(x==2):
        print(p2c)
        show(p2,2)

     elif(x==3):
        print(p3c)
        show(p3,n)

     elif(x==4):
         print(p1c)
         print(p1)
         show(p1,2)
         print(p2c)
         print(p2)
         show(p2,2)
         print(p3c)
         print(p3)
         show(p3,2) 
         

     

     

    def first3(p1,p2,p3,kcount):
        #f3=[[random.randrange(1,15,1),random.randrange(1,5,1)],[random.randrange(1,15,1),random.randrange(1,5,1)],[random.randrange(1,15,1),random.randrange(1,5,1)]]
        if(kcount==1):
            print("the flop")
            check(p1,f3,3)
            check(p2,f3,3)
            check(p3,f3,3)
            print(f3)
            show(f3,3)
        if(kcount<=3 and kcount!=1):
            preriver(f3,kcount)
        
        
        
        

    def preriver(f3,kcount):
        #preR=[random.randrange(1,15,1),random.randrange(1,5,1)]
        f3.append(preR)
        if(kcount==2):
            print("the turn")
            check(p1,f3,4)
            check(p2,f3,4)
            check(p3,f3,4)
            print(f3)
            show(f3,4)
        if(kcount==3):
            river(f3,kcount,preR)
        
        
        

    def river(f3,kcount,preR):
        #R=[random.randrange(1,15,1),random.randrange(1,5,1)]
        f3.append(R)
        check(p1,f3,3)
        check(p2,f3,3)
        check(p3,f3,3)
        if(kcount==3):
            f3.pop(4)
            print("the river")
            check(p1,f3,5)
            check(p2,f3,5)
            check(p3,f3,5)
            print(f3)
            show(f3,5)

        repetition(p1,p2,p3,f3)

    def winners(winner,flag1,flag2,flag3,status1,status2,status3,x1,x2,x3):
        #print(x1)
        #print(x2)
        #print(x3)
        highcard=[]
        #print(winner)
        winner.sort()
        w=0
        if(len(winner)>0):
            w=winner[0]
        res2=input("do you want to check result")
        if(res2=='yes'):
          if(winner.count(w)==1 and len(winner)>0):
            if(w==1):
                if(flag1==1):
                    print("p1 is winner")

                if(flag2==1):
                    print("p2 is winner")

                if(flag3==1):
                    print("p3 is winner")

            elif(w==2):
                if(flag1==w):
                    print("p1 is winner")

                if(flag2==w):
                    print("p2 is winner")

                if(flag3==w):
                    print("p3 is winner")

            elif(w==3):
                if(flag1==w):
                    print("p1 is winner")

                if(flag2==w):
                    print("p2 is winner")

                if(flag3==w):
                    print("p3 is winner")

            elif(w==4):
                if(flag1==w):
                    print("p1 is winner")

                if(flag2==w):
                    print("p2 is winner")

                if(flag3==w):
                    print("p3 is winner")

            elif(w==5):
                if(flag1==w):
                    print("p1 is winner")

                if(flag2==w):
                    print("p2 is winner")

                if(flag3==w):
                    print("p3 is winner")

            elif(w==6):
                if(flag1==w):
                    print("p1 is winner")

                if(flag2==w):
                    print("p2 is winner")

                if(flag3==w):
                    print("p3 is winner")

            elif(w==7):
                if(flag1==w):
                    print("p1 is winner")

                if(flag2==w):
                    print("p2 is winner")

                if(flag3==w):
                    print("p3 is winner")

            elif(w==8):
                if(flag1==w):
                    print("p1 is winner")

                if(flag2==w):
                    print("p2 is winner")

                if(flag3==w):
                    print("p3 is winner")

            
               

          elif(winner.count(w)>1 and len(winner)>0):
                if((w==2 or w==6) or w==8):
                    if(status1==1 and flag1==w):
                       highcard.append(x1[0][0])

                    if(status1==2 and flag1==w):
                        highcard.append(x1[1][0])

                    if(status2==1 and flag2==w):
                       highcard.append(x2[0][0])

                    if(status2==2 and flag2==w):
                        highcard.append(x2[1][0])

                    if(status3==1 and flag3==w):
                       highcard.append(x3[0][0])

                    if(status3==2 and flag3==w):
                        highcard.append(x3[1][0])
                else:
                    if(winner.count(w)==3):
                        for i in range(2):
                            highcard.append(x1[i][0])
                            highcard.append(x2[i][0])
                            highcard.append(x3[i][0])
                    elif(winner.count(w)==2 and flag3!=w):
                        for i in range(2):
                            highcard.append(x1[i][0])
                            highcard.append(x2[i][0])

                    elif(winner.count(w)==2 and flag2!=w):
                        for i in range(2):
                            highcard.append(x1[i][0])
                            highcard.append(x3[i][0])

                    elif(winner.count(w)==2 and flag1!=w):
                        for i in range(2):
                            highcard.append(x3[i][0])
                            highcard.append(x2[i][0])
                            
                            


                #print(highcard)
                high=max(highcard)
                if(x1[0][0]==high or x1[1][0]==high):
                    print("p1 is winner")

                elif(x2[0][0]==high or x2[1][0]==high):
                    print("p2 is winner")

                elif(x3[0][0]==high or x3[1][0]==high):
                     print("p3 is winner")

                elif(len(winner)==0):
                     for i in range(2):
                            highcard.append(x1[i][0])
                            highcard.append(x2[i][0])
                            highcard.append(x3[i][0])

                     high=max(highcard)
                     if(x1[0][0]==high or x1[1][0]==high):
                        print("p1 is winner")

                     elif(x2[0][0]==high or x2[1][0]==high):
                        print("p2 is winner")

                     elif(x3[0][0]==high or x3[1][0]==high):
                        print("p3 is winner")
               

                
                
            

            
                

                

                


    def sequence(p1,p2,p3,rep1,rep2,rep3,f3,winner,flag1,flag2,flag3,status1,status2,status3):
        color1=[]
        color2=[]
        color3=[]
        st=0
        fl=0
        sf=0

        for i in range(7):
            color1.append(p1[i][1])
            color2.append(p2[i][1])
            color3.append(p3[i][1])

        rep1.sort()
        rep2.sort()
        rep3.sort()
        check1=[]
        check2=[]
        check3=[]

        for i in range (6):
            if(rep1[i+1]-rep1[i]==1):
                check1.append(rep1[i])

            if(rep2[i+1]-rep2[i]==1):
                check2.append(rep2[i])

            if(rep3[i+1]-rep3[i]==1):
                check3.append(rep3[i])

        if(rep1[6]-rep1[5]==1):
            check1.append(rep1[6])

        if(rep2[6]-rep2[5]==1):
            check2.append(rep2[6])

        if(rep3[6]-rep3[5]==1
           ):
            check3.append(rep3[6])

        


        

        
        res1=input("check sequence?")
        if(res1=='yes'):
                if(len(check1)>=5):
                    print("p1 has straight")
                    
                    st=5
                    flag1=5
                    winner.append(st)

                if(len(check2)>=5):
                    print("p2 has straight")
                    st=5
                    flag2=5
                    winner.append(st)

                if(len(check3)>=5):
                    print("p3 has straight")
                    st=5
                    flag3=5
                    winner.append(st)

                if(color1.count(color1[0])>=5):
                   print("p1 has flush")
                   fl=4
                   flag1=4
                   winner.append(fl)

                if(color2.count(color2[0])>=5):
                   print("p2 has flush")
                   fl=4
                   flag2=4
                   winner.append(fl)

                if(color3.count(color3[0])>=5):
                   print("p3 has flush")
                   fl=4
                   flag3=4
                   winner.append(fl)



                if((len(check1)>=5) and (color1.count(color1[0])>=5)):
                   print("p1 has straight flush")
                   sf=1
                   flag1=1
                   winner.append(sf)
                   

                if((len(check2)>=5) and (color2.count(color2[0])>=5)):
                   print("p2 has straight flush")
                   sf=1
                   flag2=1
                   winner.append(sf)

                if((len(check3)>=5) and (color3.count(color3[0])>=5)):
                   print("p3 has straight flush")
                   sf=1
                   flag3=1
                   winner.append(sf)

                

                winners(winner,flag1,flag2,flag3,status1,status2,status3,x1,x2,x3)
    
    
    


    def repetition(p1,p2,p3,f3):
        winner=[]
        rep1=[]
        rep2=[]
        rep3=[]
        flag1=10
        flag2=10
        flag3=10
        fh=0
        tak=0
        tp=0
        thak=0
        status1=0
        status2=0
        status3=0
        
        
        for i in range(5):
            p1.append(f3[i])
            p2.append(f3[i])
            p3.append(f3[i])
        
        for i in range(7):
            rep1.append(p1[i][0])
            rep2.append(p2[i][0])
            rep3.append(p3[i][0])

        res=input("check repertition?")
        if(res=='yes'):
          #if(rep1[0]!=rep1[1] and rep2[0]!=rep2[1] and rep3[0]!=rep3[1]):
            

            if((rep1.count(rep1[0])==2 or rep1.count(rep1[1])==2)):
                if(rep1.count(rep1[0])==2):
                    status1=1
                elif(rep1.count(rep1[1])==2):
                    status1=2
                
                print("p1 has two of a kind ")
                tak=8
                flag1=8
                winner.append(tak)

            if((rep2.count(rep2[0])==2 or rep2.count(rep2[1])==2)):
                if(rep2.count(rep2[0])==2):
                    status2=1
                elif(rep2.count(rep2[1])==2):
                    status2=2
                
                
                print("p2 has two of a kind ")
                tak=8

                flag2=8
                winner.append(tak)

            if((rep3.count(rep3[0])==2 or rep3.count(rep3[1])==2)):
                if(rep3.count(rep3[0])==2):
                    status3=1
                elif(rep3.count(rep3[1])==2):
                    status3=2
                print("p3 has two of a kind ")
                tak=8
                flag3=8
                winner.append(tak)




            if((rep1.count(rep1[0])==2 and rep1.count(rep1[1])==2)):
                print("p1 has two pair")
                tp=7
                flag1=7
                winner.append(tp)

           
            if((rep2.count(rep2[0])==2 and rep2.count(rep2[1])==2)):
                print("p2 has two pair")
                tp=7
                flag2=7
                winner.append(tp)

            if((rep3.count(rep3[0])==2 and rep3.count(rep3[1])==2)):
                print("p3 has two pair")
                tp=7
                flag3=7
                winner.append(tp)


            


            if((rep1.count(rep1[0])==3 or rep1.count(rep1[1])==3)):
                if(rep1.count(rep1[0])==3):
                    status1=1
                elif(rep1.count(rep1[1])==3):
                    status1=2
                print("p1 has three of a kind ")
                thak=6
                flag1=6
                winner.append(thak)

            if((rep2.count(rep2[0])==3 or rep2.count(rep2[1])==3)):
                if(rep2.count(rep2[0])==3):
                    status2=1
                elif(rep2.count(rep2[1])==3):
                    status2=2
                print("p2 has three of a kind ")
                thak=6
                flag2=6
                winner.append(thak)

            if((rep3.count(rep3[0])==3 or rep3.count(rep3[1])==3)):
                if(rep3.count(rep2[0])==3):
                    status3=1
                elif(rep3.count(rep3[1])==3):
                    status3=2
                print("p3 has three of a kind ")
                thak=6
                flag3=6
                winner.append(thak)

            if((rep1.count(rep1[0])==2 and rep1.count(rep1[1])==3) or (rep1.count(rep1[0])==3 and rep1.count(rep1[1])==2)):
                print("p1 has full house")
                fh=3
                flag1=3
                winner.append(fh)

            if((rep1.count(rep2[0])==2 and rep2.count(rep2[1])==3) or (rep2.count(rep2[0])==3 and rep2.count(rep2[1])==2)):
                print("p2 has full house")
                fh=3
                flag2=3
                winner.append(fh)


            if((rep1.count(rep3[0])==2 and rep3.count(rep3[1])==3) or (rep3.count(rep3[0])==3 and rep3.count(rep3[1])==2)):
                print("p3 has full house")
                fh=3
                flag3=3
                winner.append(fh)

            if(rep1.count(rep1[0])==4 or rep1.count(rep1[1])==4):
                if(rep1.count(rep1[0])==4):
                    status1=1
                elif(rep1.count(rep1[1])==2):
                    status1=2
                print ("p1 has four of a kind")
                fak=2
                flag1=2
                winner.append(fak)

            if(rep2.count(rep2[0])==4 or rep2.count(rep2[1])==4):
                if(rep2.count(rep2[0])==4):
                    status2=1
                elif(rep2.count(rep2[1])==4):
                    status2=2
                print ("p2 has four of a kind")
                fak=2
                flag2=2
                winner.append(fak)

            if(rep3.count(rep3[0])==4 or rep3.count(rep3[1])==4):
                if(rep3.count(rep3[0])==4):
                    status3=1
                elif(rep3.count(rep3[1])==4):
                    status3=2
                print ("p3 has four of a kind")
                fak=2
                flag3=2
                winner.append(fak)



            sequence(p1,p2,p3,rep1,rep2,rep3,f3,winner,flag1,flag2,flag3,status1,status2,status3)

        
         
              
              
              




           


        
    
    
    def bid(p1c,p2c,p3c):
        
     kcount=0
     while(kcount!=3):  
        count=0
        while(count!=3):
            ch=input("do you want to bid")
            if(ch=='yes'):
                c=int(input("enter amount to bid"))
                if(count==0):
                    p1c=p1c-c

                if(count==1):
                    p2c=p2c-c

                if(count==2):
                    p3c=p3c-c

                count=count+1
        kcount=kcount+1
        status(p1c,p2c,p3c)
        
        
        if(kcount<=3):
            first3(p1,p2,p3,kcount)

        
        
        
        
        
        

    bid(p1c,p2c,p3c)
    


    
    


        
                





                
    
    
