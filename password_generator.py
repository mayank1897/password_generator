import string
import random


def pass_gen(pass_size):
    s1=list(string.ascii_lowercase)
    s2=list(string.ascii_uppercase)
    s3=list(string.digits)
    s4=list(string.punctuation)

    c=[]
    c.extend(s1)
    c.extend(s2)
    c.extend(s3)
    c.extend(s4)
    random.shuffle(c)
    #result=random.sample(c,4)
    #return result
    return ("".join(c[:pass_size]))
   

if __name__ == "__main__":
    while(True):
        n=input("Enter the size of your password= ")
        if (n.isdigit()==True):
            n=int(n)
            break
        else:
            print("input is not as integer")
    print(f"Generated Password= {pass_gen(n)}")


