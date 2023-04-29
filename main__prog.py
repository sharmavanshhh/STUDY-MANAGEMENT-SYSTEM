import csv
import datetime
import os

ValidUser = ''

def gettime() :
    return datetime.datetime.now()

def upload() :
    print("In which subject do you want to add new record ?")
    print(" 1. PHYSICS")
    print(" 2. CHEMISTRY")
    print(" 3. MATHEMATICS")
    print(" 4. ENGLISH")
    print(" 5. COMPUTER SCIENCE")
    sub = input()
    subj = ["physics", "chemistry", "maths", "english", "CS"]
    if sub ==  "1" :
        hw = ValidUser + "_" + subj[0] + ".txt"
        f = open(hw, "a")
        data = input("Add New Record : ")
        f.write((str(gettime()) + "  " + data + "\n").lower())
        print("Added Successfully !! ")
        f.close()

    elif sub == "2":
        hw = ValidUser + "_" + subj[1] + ".txt"
        f = open(hw, "a")
        data = input("Add New Record : ")
        f.write((str(gettime()) + "  " + data + "\n").lower())
        print("Added Successfully !! ")
        f.close()

    elif sub == "3" :
        hw = ValidUser + "_" + subj[2] + ".txt"
        f = open(hw, "a")
        data = input("Add New Record : ")
        f.write((str(gettime()) + "  " + data + "\n").lower())
        print("Added Successfully !! ")
        f.close()

    elif sub ==  "4" :
        hw = ValidUser + "_" + subj[3] + ".txt"
        f = open(hw, "a")
        data = input("Add New Record : ")
        f.write((str(gettime()) + "  " + data + "\n").lower())
        print("Added Successfully !! ")
        f.close()

    elif sub ==  "5" :
        hw = ValidUser + "_" + subj[4] + ".txt"
        f = open(hw, "a")
        data = input("Add New Record : ")
        f.write((str(gettime()) + "  " + data + "\n").lower())
        print("Added Successfully !! ")
        f.close()

    else :
        print("Enter Valid Choice : ")
        upload()

    add_rec()

def retrieve() :
    print("For which subject do you want to view old record?")
    print(" 1. PHYSICS")
    print(" 2. CHEMISTRY")
    print(" 3. MATHEMATICS")
    print(" 4. ENGLISH")
    print(" 5. COMPUTER SCIENCE")
    sub = input()
    subj = ["physics", "chemistry", "maths", "english", "CS"]
    if sub == "1":
        hw = ValidUser + "_" + subj[0] + ".txt"
        if os.path.exists(hw) == False :
            print("Currently their are no records for this subject...")
        elif os.path.exists(hw) == True :
            if os.stat(hw).st_size == 0 :
                print("Currently their are no records for this subject...")
                chk_rec()
                return True
            f = open(hw, "r")
            dd = f.readlines()
            for i in dd:
                print("⦿ " + i)
            f.close()

    elif sub == "2":
        hw = ValidUser + "_" + subj[1] + ".txt"
        if os.path.exists(hw) == False:
            print("Currently their are no records for this subject...")
        elif os.path.exists(hw) == True:
            if (os.stat(hw).st_size == 0) == True:
                print("Currently their are no records for this subject...")
                chk_rec()
                return True
            f = open(hw, "r")
            dd = f.readlines()
            for i in dd:
                print("⦿ " + i)
            f.close()

    elif sub == "3":
        hw = ValidUser + "_" + subj[2] + ".txt"
        if os.path.exists(hw) == False:
            print("Currently their are no records for this subject...")
        elif os.path.exists(hw) == True :
            if (os.stat(hw).st_size == 0) == True:
                print("Currently their are no records for this subject...")
                chk_rec()
                return True
            f = open(hw, "r")
            dd = f.readlines()
            for i in dd:
                print("⦿ " + i)
            f.close()

    elif sub == "4":
        hw = ValidUser + "_" + subj[3] + ".txt"
        if os.path.exists(hw) == False :
            print("Currently their are no records for this subject...")
        elif os.path.exists(hw) == True :
            if (os.stat(hw).st_size == 0) == True:
                print("Currently their are no records for this subject...")
                chk_rec()
                return True
            f = open(hw, "r")
            dd = f.readlines()
            for i in dd:
                print("⦿ " + i)
            f.close()

    elif sub == "5":
        hw = ValidUser + "_" + subj[4] + ".txt"
        if os.path.exists(hw) == False :
            print("Currently their are no records for this subject...")
        elif os.path.exists(hw) == True :
            if (os.stat(hw).st_size == 0) == True:
                print("Currently their are no records for this subject...")
                chk_rec()
                return True
            f = open(hw, "r")
            dd = f.readlines()
            for i in dd:
                print("⦿ " + i)
            f.close()

    else :
        print("Enter Valid Choice : ")
        retrieve()

    chk_rec()

def remove() :
    print("For which subject do you want to delete an old new record ?")
    print(" 1. PHYSICS")
    print(" 2. CHEMISTRY")
    print(" 3. MATHEMATICS")
    print(" 4. ENGLISH")
    print(" 5. COMPUTER SCIENCE")
    sub = input()
    subj = ["physics", "chemistry", "maths", "english", "CS"]
    if sub == "1":
        hw = ValidUser + "_" + subj[0] + ".txt"
        if os.path.exists(hw) == False:
            print("Currently their are no records for this subject...")
            del_rec()
            return False
        f = open(hw, "r")
        dd = f.readlines()
        if (os.stat(hw).st_size == 0) == True :
            print("Currently their are no records for this subject...")
            del_rec()
            return True
        for i in dd:
            print("⦿ " + i)
        fr = open(hw, "w")
        print("Which record do you want to delete?")
        _del = input()
        _del = _del.lower()
        for line in dd :
            if _del not in line :
                fr.write(line)
        fr.close()
        f.close()

    elif sub == "2":
        hw = ValidUser + "_" + subj[1] + ".txt"
        if os.path.exists(hw) == False:
            print("Currently their are no records for this subject...")
            del_rec()
            return False
        f = open(hw, "r")
        dd = f.readlines()
        if (os.stat(hw).st_size == 0) == True :
            print("Currently their are no records for this subject...")
            del_rec()
            return True
        for i in dd:
            print("⦿ " + i)
        fr = open(hw, "w")
        print("Which record do you want to delete?")
        _del = input()
        _del = _del.lower()
        for line in dd :
            if _del not in line :
                fr.write(line)
        fr.close()
        f.close()

    elif sub == "3":
        hw = ValidUser + "_" + subj[2] + ".txt"
        if os.path.exists(hw) == False:
            print("Currently their are no records for this subject...")
            del_rec()
            return False
        f = open(hw, "r")
        dd = f.readlines()
        if (os.stat(hw).st_size == 0) == True :
            print("Currently their are no records for this subject...")
            del_rec()
            return True
        for i in dd:
            print("⦿ " + i)
        fr = open(hw, "w")
        print("Which record do you want to delete?")
        _del = input()
        _del = _del.lower()
        for line in dd :
            if _del not in line :
                fr.write(line)
        fr.close()
        f.close()

    elif sub == "4":
        hw = ValidUser + "_" + subj[3] + ".txt"
        if os.path.exists(hw) == False:
            print("Currently their are no records for this subject...")
            del_rec()
            return False
        f = open(hw, "r")
        dd = f.readlines()
        if (os.stat(hw).st_size == 0) == True :
            print("Currently their are no records for this subject...")
            del_rec()
            return True
        for i in dd:
            print("⦿ " + i)
        fr = open(hw, "w")
        print("Which record do you want to delete?")
        _del = input()
        _del = _del.lower()
        for line in dd :
            if _del not in line :
                fr.write(line)
        fr.close()
        f.close()

    elif sub == "5":
        hw = ValidUser + "_" + subj[4] + ".txt"
        if os.path.exists(hw) == False:
            print("Currently their are no records for this subject...")
            del_rec()
            return False
        f = open(hw, "r")
        dd = f.readlines()
        if (os.stat(hw).st_size == 0) == True :
            print("Currently their are no records for this subject...")
            del_rec()
            return True
        for i in dd:
            print("⦿ " + i)
        fr = open(hw, "w")
        print("Which record do you want to delete?")
        _del = input()
        _del = _del.lower()
        for line in dd :
            if _del not in line :
                fr.write(line)
        fr.close()
        f.close()

    else:
        print("Enter Valid Choice : ")
        remove()

    print("Deleted Successfully !! ")
    del_rec()

def add_rec():
    print(" Do you want to add more entries ? (Yes/No)")
    more = input()
    temp = 'Yes'
    if more.lower() == temp.lower():
        upload()
    else:
        print("Thank You :)")
        go_menu()

def chk_rec():
    print("Do you want to check for any other subject ? (Yes/No)")
    check = input()
    chk = "Yes"
    if check.lower() == chk.lower():
        retrieve()
    else:
        print("Thank You :)")
        go_menu()

def del_rec():
    print("Do you want to delete for any other subject ? (Yes/No)")
    check = input()
    chk = "Yes"
    if check.lower() == chk.lower():
        remove()
    else:
        print("Thank You :)")
        go_menu()

def go_menu():
    print("Do you want to go back to main menu ? (Yes/No)")
    _menu = input()
    _temp = "Yes"
    if _menu.lower() == _temp.lower():
        main_menu()
    else:
        print("Thank You :)")
        print("Sucessfully Logged Out !!")

def register() :
     with open("database.csv", mode = "a", newline = "")  as fh :
        writer = csv.writer(fh, delimiter = "|")
        username = input("Create An Username : ")
        username = username.lower()
        with open("database.csv", "r") as tt:
            reader = csv.reader(tt, delimiter="|")
            for row in reader:
                if username in row:
                    print("Existing user\n", "Try Again !!")
                    return register()
        password = input("Create Password : ")
        pass_check = input("Confirm Your Password : ")
        if password == pass_check :
            if len(password) < 6 :
                print("Password is too short it should contain minimum 6 characters...")
                print("Re - enter !! \n")
                register()
            else :
                writer.writerow([username,password])
                print("Congratulations !! You have successfully registered...")
        else :
            print("Signup Error !! \n","Please Try Again !! ")
            register()

     print("Do you want to Login now ? (Yes/No)")
     log = input()
     temp = "Yes"
     if log.lower() == temp.lower() :
         access()
     else :
         print("Thank You :)")

def access() :
    with open("database.csv", "r") as fh :
        username = input("Enter Username : ")
        username = username.lower()
        password = input("Enter Password : ")
        reader = csv.reader(fh, delimiter = "|")
        for row in reader :
            if row == [username, password] :
                print("Successfully Logged In...")
                print("Welcome !! ",username)
                global ValidUser
                ValidUser = username
                main_menu()
                return True
    print("Invalid Credentials !! \n","Please Try Again...")
    return access()


def task():
    print("What Do You Want To Do ?")
    print("1. Add Tasks/Notes")
    print("2. View Your Tasks/Notes ")
    tk = int(input())
    if tk == 1 :
        add_task()
    elif tk == 2 :
        view_task()
    else :
        print("Enter Valid Choice")
        task()

def add_task() :
    tsk = ValidUser + "_task"
    f = open(tsk, "a")
    t = input("Please Add Your Task/Note :-\n")
    f.write(str(t + "\n"))
    print("Added Successfully !! ")
    f.close()
    op = input("Do You Want Add More Task/Note ? (yes/no)\n")
    chk = "Yes"
    if op.lower() == chk.lower():
        add_task()
    else:
        print("Thank You :)")
        go_menu()

def view_task() :
    print("Following Are The All Tasks/Notes Added By You : - ")
    tsk = ValidUser + "_task"
    f = open(tsk, "r")
    dd = f.readlines()
    for i in dd:
        print("⦿ " + i)
    f.close()
    go_menu()

def main_menu() :
    print("What do you want to do ? ")
    print(" 1. Add New Study Record")
    print(" 2. View Old Study Record")
    print(" 3. Delete Old Study Record")
    print(" 4. Tasks/Notes")
    print(" 5. Exit")
    entry = input()
    if entry == "1" :
        upload()
    elif entry == "2" :
        retrieve()
    elif entry == "3" :
        remove()
    elif entry == "4" :
        task()
    elif entry == "5":
        print("Thank You :)")
    else :
        print("Enter Valid Choice : ")
        main_menu()

def home() :
    print("Enter your choice : ")
    option = input("Signup | Login \n")
    a = "Login"
    b = "Signup"
    if option.lower() == a.lower() :
        access()
    elif option.lower() == b.lower() :
        register()
    else :
        print("Enter Valid Choice !! \n ")
        home()

print("\n|| STUDY MANAGEMENT SYSTEM ||")
print("***********************************")
home()
