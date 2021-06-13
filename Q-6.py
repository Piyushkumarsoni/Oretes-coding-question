import re
if __name__=="__main__":
    input = input()

    integers = re.findall("[0-9]",input)
    lowercase = re.findall("[a-z]",input)
    uppercase = re.findall("[A-Z]",input)
    special = re.findall("[@_!.#$%^&*()<>?/|}{~:]",input)
    spaces = re.findall(" ", input)

    lower = ""
    upper = ""
    spec = ""
    space = ""
    for i in lowercase:
        lower+=i

    for i in uppercase:
        upper+=i

    for i in special:
        spec+=i

    for i in spaces:
        space+=i
   
    odd = ""
    even = ""
    for i in integers:
        if int(i)%2 == 0:
            even+=str(i)
        else:
            odd+=str(i)

    integer = odd+" "+even

    ans=""

    ans+=spec+" "+lower+" "+upper+" "+integer+" "+str(len(space))

    print(ans)