import datetime
import os


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    BIBlack="\[\033[1;90m\]"      # Black
    BIRed="\[\033[1;91m\]"        # Red
    BIGreen="\[\033[1;92m\]"      # Green
    BIYellow="\[\033[1;93m\]"     # Yellow
    BIBlue="\[\033[1;94m\]"       # Blue
    BIPurple="\[\033[1;95m\]"     # Purple
    BICyan="\[\033[1;96m\]"       # Cyan
    BIWhite="\[\033[1;97m\]"      # White


file_path = input(color.BOLD+"Enter your file name "+color.END)
f=open(file_path, 'r+')
line = f.read().split('\n')
line.pop(0)
invalid_list = []
for line1 in line:
    index = line.index(line1) + 2
    line_list = line1.split('|')
    #print(line_list)
    line_list.pop(0)
    line_list.pop(3)
  # print(line_list)
    line1 = ','.join(line_list)
    lower = str(line1)
    upper = str(line1).upper()
    if str(line1) == str(line1).upper():
        None
    else:
        invalid_list.append(str(index))
#f=open("hdfile.txt", 'r+')

list9=[]
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
list20=[]
list21=[]
list16=[]
list17=[]
list22=[]
a1=[]
a2=[]
a3=[]
a4=[]
a5=[]
a9=[]
a21=[]
a16=[]
a17=[]
a20=[]
k=[]
z=0
y=0
v=1





print(" ")
print(color.BOLD+"-----------------------------"+color.END)
print(color.BOLD+"Checking Of Price Range"+color.END)
print(color.BOLD+"-----------------------------"+color.END)
for x in line:
    a=[]
    a=x.split("|")
    b = line[line.index(x) - 1].split("|")
    lio = a[0]
    flag2=0
    lio2 = b[0]
    if str(lio) == str(lio2):
        #lio3 = line.index(x)
        if line.index(x) != 0:
            #print ('current_price: ' + a[6])
            #print ('previous_price: ' + b[7])
            if float(a[6]) == float(b[7])+ 0.01:
                flag2=0
            else:
                #print ('current_price: ' + a[6])
                #print ('previous_price: ' + b[7])
                print(color.BOLD+'* In Product Defination Group' +color.BOLD+color.RED+' '+a[0]+' '+color.END+ color.BOLD+'Value'+color.END+' '+color.BOLD+color.RED+a[6]+color.END +' '+color.BOLD+'is not .01 cent more than'+' '+color.BOLD+color.RED+b[7]+color.END)#.format(a[0],a[6], b[7]))
    #print (color.BOLD+color.GREEN+"Number of pipes in line "+ str(v) +color.END+":"+' '+' '+color.BOLD+str(len(a)-1)+color.END)
    b = a[0]+"|"+a[4]+"|"+a[6]+"|"+a[7]+"|"+a[8]+"|"+a[12]


    list9.append(b)
    list1.append(a[0])
    list2.append(a[2])
    list3.append(a[8])
    list20.append(a[19])
    list21.append(a[3])
    #list5.append(a[19])
    list16.append(a[16])
    list17.append(a[17])
    list22.append(a[20])
print("  ")
print (color.BOLD +"------------------ "+ color.END)
#print(list1)
#print(list21)
#print(list3)
#print(list4)
#print(list16)
#print(list17)
def unique(list1):
    unique_list = []
    for x in list1 :
        if x not in unique_list:
            unique_list.append(x)pricing 
    return unique_list

a1=unique(list1)
a9=unique(list9)
a2=unique(list2)
a3=unique(list3)
a5=unique(list5)

#print(a1)
#print(a2)
#print(a3)
#print(a5)
print (color.BOLD +"Master Price Check "+ color.END)
print (color.BOLD +"------------------ "+ color.END)

#for x in a9:
# c=list9.count(x)
# z=z+1
#print (color.BOLD +"product defination group"+ color.END +' ' +color.BLUE+ x +color.END+ ":" + ' ' +str(c))
#print (color.BOLD +"product defination group"+ color.END+":")
#print (color.BLUE+ x +color.END+ ":" + ' ' +str(c))

#print (color.BOLD +"product defination group"+ color.END+":")
# print (str(z)+":"+' '+' '+color.BOLD+color.BLUE+ x +color.END+ ":" + ' ' +color.BOLD+str(c)+color.END)


if(len(a9)==len(list9)):
    print (color.BOLD+color.GREEN +"Master Price Check Data Unique "+ color.END)
else:
    print(color.BOLD+color.RED+"Master Price Check Data NOT Unique :"+color.END)
    for x in a9:
        if(list9.count(x)>1):
            print ("*" +' '+' '+"Duplicate Master Price Check" + ' '+color.BOLD +color.DARKCYAN + "<"+ x + ">"+color.END)

for x in a9:
    c=list9.count(x)
    if(c>1):
        print ("*"+' '+' '+color.BOLD+color.BLUE+ x +color.END+ ":" + ' ' +str(c))

print (color.BOLD +""+ color.END)
print (color.BOLD +"------------------------- "+ color.END)
print (color.BOLD +"Product definition Group "+ color.END)
print (color.BOLD +"------------------------- "+ color.END)
for x in a1:
    c=list1.count(x)
    print (color.BOLD+color.BLUE+ x +color.END+ ":" + ' ' +str(c))


print(" ")




print (color.BOLD+"-----------------------"+color.END)
print (color.BOLD +"ExternalSku Data"+ color.END)
print (color.BOLD+"-----------------------"+color.END)
if(len(a2)==len(list2)):
    print(color.BOLD+"All records of ExternalSku are unique :"+color.END)
else:
    print(color.BOLD+color.RED+"External SKU NOT Unique :"+color.END)
    for x in a2:
        if(list2.count(x)>1):
            print ("*" +' '+' '+"Duplicate SKU's" + ' '+color.BOLD +color.DARKCYAN + "<"+ x + ">"+color.END)

for x in a2:
    c=list2.count(x)
    if(c>1):
        print ("*"+' '+' '+color.BOLD+color.BLUE+ x +color.END+ ":" + ' ' +str(c))




print("           ")
print (color.BOLD+"-----------------------"+color.END)
print (color.BOLD +"Pricing Condition Data"+ color.END)
print (color.BOLD+"-----------------------"+color.END)

S=1

for x in a3:
    if((x=='NEW')or(x=='USED')or(x=='REFURBISHED_90_MINUS')):

        S=1
    else:
        S=0
        break


if(S==1):
    print (color.BOLD+color.PURPLE+"Pricing Condition okay :"+color.END)
else:
    print (color.BOLD+color.RED+"Pricing Condition not okay :"+ color.END)

    #z=0



    for x in a3:
        y=y+1
        c=list3.count(x)
        print (str(y)+":" +' '+'  '+ color.BOLD+color.BLUE+ x +color.END+ ":" + ' ' +str(c))

print(" ")
print (color.BOLD+"-----------------------"+ color.END)
print (color.BOLD +"Pipe Data"+ color.END)
print (color.BOLD+"-----------------------"+ color.END)


#if(len(a5)==len(list5)):
    #print("Feature File is Correct")
    #else:
    # print("Feature File is Not Correct")

g=1

for x in line:
    v=v+1
    a=x.split("|")
    if((len(a)==32) or (len(a)==39)):
        #print(color.BOLD+color.GREEN+"pipes are okay in each SKU"+color.END)
        g=1
    else:
        g=0
        #print(color.BOLD+color.RED+"PIPES ARE NOT OKAY"+color.END)
        print(color.BOLD+color.RED+"Pipes Are Not Okay"+color.END+color.BOLD+color.RED+' '+"in line "+ str(v)+':'+color.END+' '+' '+str(len(a)-1))



if(g==1):
    print(color.BOLD+color.GREEN+"Number Of Pipes In Each SKU Are Correct"+color.END)

print(" ")
print (color.BOLD+"-----------------------"+color.END)
print (color.BOLD +"Feature SKU Data"+ color.END)
print (color.BOLD+"-----------------------"+color.END)

i=1
flag=1
#print (color.BOLD+color.GREEN+"Number of pipes in line "+ str(v) +color.END+":"+' '+' '+color.BOLD+str(len(a)-1)+color.END)
for x in list20:
    i=i+1
    if(not(x.endswith('A') )and not(x.endswith('AT') )and not(x.endswith('B'))):
        flag=0
        print(color.BOLD+color.RED+"Feature_SKU Not Okay In Line :"+' '+str(i)+' '+color.BOLD+"("+ x +")"+color.END)

if(flag==1):
    print(color.BOLD+color.GREEN+"All Feature_SKU Ends With Either 'A' or 'B' or 'AT' "+color.END)

print(" ")
print (color.BOLD+"-----------------------"+color.END)
print (color.BOLD +"Date and Time Data"+ color.END)
print (color.BOLD+"-----------------------"+color.END)

flag6=1

for x in list16:

    isValidDate= True

    try:
     newDate = datetime.datetime.strptime(x, '%m/%d/%Y %H:%M')

    except ValueError:
        isValidDate= False


    if(isValidDate== False):
        flag6=0
        print(str(x)+"is not okay")


if(flag6==1):
    print(color.BOLD+color.BLUE+"Date And Time In Start Date Okay"+color.END)

flag7=1

for x in list17:

    isValidDate= True

    try:
        newDate = datetime.datetime.strptime(x, '%m/%d/%Y %H:%M')

    except ValueError:
        isValidDate= False


    if(isValidDate== False):
        flag7=0
        print(str(x)+"is not okay")


if(flag7==1):
    print(color.BOLD+color.BLUE+"Date And Time In End Date Okay"+color.END)


print(" ")
print (color.BOLD+"-----------------------"+color.END)
print (color.BOLD +"Feature_Type Data(optional)"+ color.END)
print (color.BOLD+"-----------------------"+color.END)

w = None
r = 1
t=1
for x in list22:
    t=t+1
    if (x=='WARRANTY')or(x=='ADH')or(x=='THEFT')or(x=='LOSS')or(x=="MOBILE_SECURITY")or(x=="BUNDLED_WARRANTY_COVERAGE")or(x=="SCREEN"):
        w=1
    elif x == '':
        w=0
        r=0
        print(color.BOLD+color.RED+'No data found in line no :'+color.END+' '+color.BOLD+str(t)+color.END)
    else:
        w=0
        print (color.BOLD+color.RED+"Feature_Type Is Not Correct "+"in line"+" "+":"+color.BOLD+str(t)+ color.END)





if w==1 and r==1:
    print (color.BOLD+color.GREEN+"Feature_Type Is Correct "+color.END)

print(" ")
print(color.BOLD+"---------------------------------"+color.END)
print(color.BOLD+"Uppercase Validation Data"+color.END)
print(color.BOLD+"---------------------------------"+color.END)

#else:
    #print (color.BOLD+color.RED+"Feature_Type Is Not Correct "+"in line"+" "+str(t)+ color.END)

if len(invalid_list) > 0:
    invalid_string = ', '.join(invalid_list) if len(invalid_list) > 0 else invalid_list[0]
    print(color.BOLD+color.RED+'Data is not upper case for lines : {}'.format(invalid_string)+color.END)
else:
    print('Data is accurately upper case')





#for x in list4:
# v=int(x.find('-'))
# print(v)
#k.append(x[33,v])
#print(k)