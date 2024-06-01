def management():
    import csv
    import pickle
    print(" Menu Code  ")
    print(" 1. To Handle Text File ")
    print(" 2. To Handle CSV File ")
    print(" 3. To Handle Binary File ")
    print(" 4. To End the Program ")
    i1=int(input("Enter Code Here →  "))
    if i1==1:
        print(" Sub Menu Code ")
        print(" 1.1 To Write a Text File ")
        print(" 1.2 To Append Text File ")
        print(" 1.3 To Read Text File ")
        i2=float(input("Enter Sub Menu Code Here → "))
        if i2==1.1:
            a=open("C:\\'Enter_your_path_address'\\SchoolManagement.txt","w")
            freq=int(input("set Frequency : "))
            #Frequency to define how many times the execution would take place
            for i in range(freq):
                nm=input("Enter Name : ")
                cl=int(input("Enter Class : "))
                cls=str(cl)
                sec=input("Enter Section : ")
                rl=int(input("Enter Roll Number : "))
                rlnm=str(rl)
                subject=input("Enter Subject : ")
                a.write("Name : ")
                a.write(nm)
                a.write("\n")
                a.write("Class : ")
                a.write(cls)
                a.write("\n")
                a.write("Section : ")
                a.write(sec)
                a.write("\n")
                a.write("Roll Number : ")
                a.write(rlnm)
                a.write("\n")
                a.write("Subject : ")
                a.write(subject)
                a.write("\n")
                a.write("\n")
            a.close()
        elif i2==1.2:
            a=open("C:\\'Enter_your_path_address'\\SchoolManagement.txt","a")
            freq=int(input("set Frequency : "))
            #Frequency to define how many times the execution would take place
            for i in range(freq):
                nm=input("Enter Name : ")
                cl=int(input("Enter Class : "))
                cls=str(cl)
                sec=input("Enter Section : ")
                rl=int(input("Enter Roll Number : "))
                rlnm=str(rl)
                subject=input("Enter Subject : ")
                a.write("Name : ")
                a.write(nm)
                a.write("\n")
                a.write("Class : ")
                a.write(cls)
                a.write("\n")
                a.write("Section : ")
                a.write(sec)
                a.write("\n")
                a.write("Roll Number : ")
                a.write(rlnm)
                a.write("\n")
                a.write("Subject : ")
                a.write(subject)
                a.write("\n")
                a.write("\n")
            a.close()
            
        elif i2==1.3:
            a=open("C:\\'Enter_your_path_address'\\SchoolManagement.txt","w")
            print("1. To read File in String Format ")
            print("2. To read first Line of The file in the form of List ")
            print("3. To read entire file in the form of List ")
            Q=input("Enter Code Here → 	")
            if Q==1:
                h=a.read()
                print(h)
            elif Q==2:
                h1=a.readline()
                print(h1)
            elif Q==3:
                h2=a.readlines()
                print(h2)
            else:
                print("***** Code Invalid Please Try Again ***** ")
                print("\n")
                return management()
        else:
            print("\n")
            print("***** Code Invalid Please Try Again ***** ")
            print("\n")
            return management()
            

    elif i1==2:
        print(" Sub Menu Code ")
        print(" 2.1 To Write a CSV File ")
        print(" 2.2 To Append CSV File ")
        print(" 2.3 To Read CSV File ")
        print("\n")
        i3=float(input("Enter Sub Menu Code Here → "))
        if i3==2.1:
            a=open("C:\\'Enter_your_path_address'\\SchoolManagement.csv","w")
            b=csv.writer(a)
            c=['Name','Class','Section','Roll Number','Subject']
            b.writerow(c)
            freq=int(input("Set Frequency : "))
            for i in range(freq):
                nm=input("Enter Name : ")
                cls=int(input("Enter Class : "))
                sec=input("Enter Section : ")
                rlnm=int(input("Enter Roll Number : "))
                sub=input("Enter Subject : ")
                lst=[nm,cls,sec,rlnm,sub]
                b.writerow(lst)
            a.close()

                          
        elif i3==2.2:
            a=open("C:\\'Enter_your_path_address'\\SchoolManagement.csv","a")
            b=csv.writer(a)
            c=['Name','Class','Section','Roll Number','Subject']
            b.writerow(c)
            freq=int(input("Set Frequency : "))
            for i in range(freq):
                nm=input("Enter Name : ")
                cls=int(input("Enter Class : "))
                sec=input("Enter Section : ")
                rlnm=int(input("Enter Roll Number : "))
                sub=input("Enter Subject : ")
                lst=[nm,cls,sec,rlnm,sub]
                b.writerow(lst)
            a.close()
                
        elif i3==2.3:
            a=open("C:\\'Enter_your_path_address'\\SchoolManagement.csv","r")
            b=csv.reader(a)
            for i in b:
                print(i)
            a.close()
        else:
            print("\n")
            print("***** Code Invalid Please Try Again ***** ")
            print("\n")
            return management()
        
            
            
    elif i1==3:
        print(" Sub Menu Code ")
        print(" 3.1 To Write a Text File ")
        print(" 3.2 To Append Text File ")
        print(" 3.3 To Read Text File ")
        i5=float(input("Enter Sub Menu Code Here → "))
        if i5==3.1:
            a=open("C:\\'Enter_your_path_address'\\SchoolManagement.dat","wb")
            freq=int(input("Set Frequency : "))
            for i in range(freq):
                nm=input("Enter Name : ")
                cls=int(input("Enter Class : "))
                sec=input("Enter Section : ")
                rlnm=int(input("Enter Roll Number : "))
                sub=input("Enter Subject : ")
                lst=[nm,cls,sec,rlnm,sub]
                pickle.dump(lst,a)
            a.close()
            
        elif i5==3.2:
            a=open("'Enter_your_path_address'\\SchoolManagement.dat","ab")
            freq=int(input("Set Frequency : "))
            for i in range(freq):
                nm=input("Enter Name : ")
                cls=int(input("Enter Class : "))
                sec=input("Enter Section : ")
                rlnm=int(input("Enter Roll Number : "))
                sub=input("Enter Subject : ")
                lst=[nm,cls,sec,rlnm,sub]
                pickle.dump(lst,a)
            a.close()
            
        elif i5==3.3:
            a=open("C:\\'Enter_your_path_address'\\SchoolManagement.dat","rb")
            b=pickle.load(a)
            print(b)
            a.close()
        else:
            print("\n")
            print("***** Code Invalid Please Try Again ***** ")
            print("\n")
            return management()
            
    elif i1==4:
        print(" ")
        print("***** Program Ended *****")
    else:
        print("\n")
        print("*****Sorry That's an Invalid Code. Please Try Again.*******")
        print("\n")
        return management()
management()
            

            
                
                       
            

