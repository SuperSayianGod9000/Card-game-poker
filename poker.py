import random

a=10


while(True):
    p1c=50
    p2c=50
    p3c=50
    p1c=p1c-1
    p2c=p2c-1
    p3c=p3c-1
    

    p1=[[random.randrange(1,15,1),random.randrange(1,5,1)],[random.randrange(1,15,1),random.randrange(1,5,1)]]
    p2=[[random.randrange(1,15,1),random.randrange(1,5,1)],[random.randrange(1,15,1),random.randrange(1,5,1)]]
    p3=[[random.randrange(1,15,1),random.randrange(1,5,1)],[random.randrange(1,15,1),random.randrange(1,5,1)]]
    f3=[[random.randrange(1,15,1),random.randrange(1,5,1)],[random.randrange(1,15,1),random.randrange(1,5,1)],[random.randrange(1,15,1),random.randrange(1,5,1)]]
    preR=[random.randrange(1,15,1),random.randrange(1,5,1)]
    R=[random.randrange(1,15,1),random.randrange(1,5,1)]


    def status(p1c,p2c,p3c):
        
     x=int(input("Enter player number for viewing status"))

     if(x==1):
        print(p1c)
        print(p1)

     elif(x==2):
        print(p2c)
        print(p2)

     elif(x==3):
        print(p3c)
        print(p3)

     elif(x==4):
         print(p1c)
         print(p1)
         print(p2c)
         print(p2)
         print(p3c)
         print(p3) 
         

     

     

    def first3(p1,p2,p3,kcount):
        #f3=[[random.randrange(1,15,1),random.randrange(1,5,1)],[random.randrange(1,15,1),random.randrange(1,5,1)],[random.randrange(1,15,1),random.randrange(1,5,1)]]
        if(kcount==1):
            print(f3)
        if(kcount<=3 and kcount!=1):
            preriver(f3,kcount)
        
        
        
        

    def preriver(f3,kcount):
        #preR=[random.randrange(1,15,1),random.randrange(1,5,1)]
        f3.append(preR)
        if(kcount==2):
            print(f3)
        if(kcount==3):
            river(f3,kcount,preR)
        
        
        

    def river(f3,kcount,preR):
        #R=[random.randrange(1,15,1),random.randrange(1,5,1)]
        f3.append(R)
        if(kcount==3):
            f3.pop(4)
            print(f3)

        repetition(p1,p2,p3,f3)


    def sequence(p1,p2,p3,rep1,rep2,rep3,f3):
        color1=[]
        color2=[]
        color3=[]

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

                if(len(check2)>=5):
                    print("p2 has straight")

                if(len(check3)>=5):
                    print("p3 has straight")

                if(color1.count(color1[0])>=5):
                   print("p1 has flush")

                if(color2.count(color2[0])>=5):
                   print("p2 has flush")

                if(color3.count(color3[0])>=5):
                   print("p3 has flush")



                if((len(check1)>=5) and (color1.count(color1[0])>=5)):
                   print("p1 has straight flush")

                if((len(check2)>=5) and (color2.count(color2[0])>=5)):
                   print("p2 has straight flush")

                if((len(check3)>=5) and (color3.count(color3[0])>=5)):
                   print("p3 has straight flush")
    
    
    


    def repetition(p1,p2,p3,f3):
        
        rep1=[]
        rep2=[]
        rep3=[]
        
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
            if((rep1.count(rep1[0])==2 and rep1.count(rep1[1])==3) or (rep1.count(rep1[0])==3 and rep1.count(rep1[1])==2)):
                print("p1 has full house")

            if((rep1.count(rep2[0])==2 and rep2.count(rep2[1])==3) or (rep2.count(rep2[0])==3 and rep2.count(rep2[1])==2)):
                print("p2 has full house")

            if((rep1.count(rep3[0])==2 and rep3.count(rep3[1])==3) or (rep3.count(rep3[0])==3 and rep3.count(rep3[1])==2)):
                print("p3 has full house")


            if((rep1.count(rep1[0])==2 and rep1.count(rep1[1])==2)):
                print("p1 has two pair")

            if((rep2.count(rep2[0])==2 and rep2.count(rep2[1])==2)):
                print("p1 has two pair")

            if((rep2.count(rep2[0])==2 and rep2.count(rep2[1])==2)):
                print("p2 has two pair")

            if((rep3.count(rep3[0])==2 and rep3.count(rep3[1])==2)):
                print("p3 has two pair")


            if((rep1.count(rep1[0])==2 or rep1.count(rep1[1])==2)):
                print("p1 has two of a kind ")

            if((rep2.count(rep2[0])==2 or rep2.count(rep2[1])==2)):
                print("p2 has two of a kind ")

            if((rep3.count(rep3[0])==2 or rep3.count(rep3[1])==2)):
                print("p3 has two of a kind ")


            if((rep1.count(rep1[0])==3 or rep1.count(rep1[1])==3)):
                print("p1 has three of a kind ")

            if((rep2.count(rep2[0])==3 or rep2.count(rep2[1])==3)):
                print("p2 has three of a kind ")

            if((rep3.count(rep3[0])==3 or rep3.count(rep3[1])==3)):
                print("p3 has three of a kind ")

            sequence(p1,p2,p3,rep1,rep2,rep3,f3)

        
         
              
              
              




           


        
    
    
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
    


    
    


        
                





                
    
    
