one=("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
two=("ten", "eleven", "twelve","thirteen", "forteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen")
tens=("twenty", "thirthy", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety")
huge=("billion", "million", "thousand", "hundred")

def get_num():
    while True:
        num=input("Enter a (positive) number to convert into a word: ")
        if not(num.isdigit()):
            print("Invalid  Input!")
        else:
            break 
    len_num=len(num)
    convert(num, len_num)
def convert(num, len):
    words=[]
    if len > 12:
        print("Number is to big.")
        exit()
    if len != 12:
        num=num.zfill(12)                      
    groups=[num[0:3], num[3:6], num[6:9], num[9:]]   
    for i, k in enumerate(groups):
        x=k
        if x[0]!="0":
            words.append(one[int(x[0])])
            words.append(huge[3])
        if x[1]!="0":
            if x[1]=="1":
                words.append(two[int(x[0])])
                if x[-1] !="0":
                    words.append(one[int(x[0])+1])
            else:
                words.append(tens[int(x[1])-2])
                words.append(one[int(x[-1])])
        if x[-1] !="0":
                if x[0]=="0" and x[1]=="0":
                    words.append(one[int(x[-1])])
                if i !=3:
                    words.append(huge[i])
        if all(n =="0" for n in num):
            words.append(one[0])            
    ans="-".join(words)
    print(ans)     
get_num()                          