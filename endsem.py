patient_list=[]
k = True
while k:
    print("Select a service\n")
    print("Enter 1 to add a patient\nEnter 2 to display patients\nEnter 3 to exit")
    u = int(input("Enter : "))
    if u == 1:
        z = True
        while z:
            details={}
            details["Name"] = input("Enter patient name : ")
            details["Age"]  = input("Enter Age : ")
            details["Bloof Group"]=input("Blood Group : ")
            details["Contact number"]=int(input("Contact Number : "))
            patient_list.append(details)
            print("Updated")
            ok= input("Anymore patient (yes or no) : ").lower()
            if ok == 'no':
                z = False
    if u == 2:
        for i, details in enumerate(patient_list,start=1):
            print(f"\nPatient{i}")
            for k, value in details.items():
                print(f"{k.capitalize()}:{value}")
    if u == 3:
        print("Have a nice day")
        k = False