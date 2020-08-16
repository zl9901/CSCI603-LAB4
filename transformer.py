import math
arr=[]
brr=[]


def rotate(message1,exp):
    str1=message1
    # https://developers.google.com/edu/python/strings
    exp=int(exp)
    if exp>0:
        for i in range(exp):
            str1=str1[len(str1)-1]+str1[0:len(str1)-1]
    else:
        exp1=abs(exp)
        for j in range(exp1):
            str1=str1[1:]+str1[0]
    return str1
        #print(str)

def shift(message,index,exponent):
    exponent=int(exponent)
    #ASC value of Z is 90
    deposit=index[-1]
    if exponent>=0:
        exponent=exponent%26
        indexof=int(deposit)
        str2=message[indexof]
        value=ord(str2)
        if (value+exponent)<=90 :
            value=value+exponent
        else:
            value=value+exponent-90+64
    else:
        exponent1=abs(exponent)
        exponent1 = exponent1 % 26
        indexof = int(deposit)
        str2 = message[indexof]
        value = ord(str2)
        if (value-exponent1)>=65 :
            value=value-exponent1
        else:
            value=value+26-exponent1
    newstr=chr(value)
    message1=message[0:indexof]+newstr+message[indexof+1:len(message)]
    return message1

    #print(message)

def exchange(message2,index1,index2):
    str3=index1[1]
    str3=int(str3)
    index2=int(index2)
    message3=message2[:str3]+message2[index2]+message2[str3+1:index2]+message2[str3]+message2[index2+1:]
    #print(message3)
    return message3

def reverse(message4,index):
    index=int(index)
    str4 = message4
    str5 = str4[::-1]
    return str5

def store(str):
    arr.append(str)
    print(arr)
def processFile(fileName):
    """
    Process the entire CSV file and display each individuals information.
    :param fileName (str): The file name
    :exception: FileNotFoundError if fileName does not exist:
    <TAB>IP (hex): <hex ip addr>
    :return: None
    """

    # using 'with' means the file handle, f, will be automatically closed
    # when the region finishes
    with open(fileName) as f:
        # discard first line (column labels)
        f.readline()

        # process the remainder of the lines
        for line in f:
            # strip the newline at the end of the line
            line = line.strip()
            data = line.split(',')
            store(data[0])
            store(data[1])

def handleFile(fileName1):
    """
    Process the entire CSV file and display each individuals information.
    :param fileName (str): The file name
    :exception: FileNotFoundError if fileName does not exist:
    <TAB>IP (hex): <hex ip addr>
    :return: None
    """

    # using 'with' means the file handle, f, will be automatically closed
    # when the region finishes
    with open(fileName1) as f1:
        # discard first line (column labels)
        f1.readline()
        f2 = open("output.txt", "a")
        f2.write("\n")
        # process the remainder of the lines
        for line in f1:
            # strip the newline at the end of the line
            line = line.strip()
            info0=shift(line,arr[0],arr[1])
            info1=rotate(info0,arr[3])
            info2=exchange(info1,arr[4], arr[5])
            info3=reverse(info2, arr[7])
            f2.write(info3)
            f2.write("\n")

def handleFile1(filename):
    """
    Process the entire CSV file and display each individuals information.
    :param fileName (str): The file name
    :exception: FileNotFoundError if fileName does not exist:
    <TAB>IP (hex): <hex ip addr>
    :return: None
    """

    # using 'with' means the file handle, f, will be automatically closed
    # when the region finishes
    with open(filename) as f1:
        # discard first line (column labels)
        f1.readline()
        # process the remainder of the lines
        for line in f1:
            # strip the newline at the end of the line
            line = line.strip()
            info5=reverse(line,arr[7])
            info6=exchange(info5,arr[4],arr[5])
            str66 = arr[3]
            str66 = "-" + str66
            info7 = rotate(info6, str66)
            str99=arr[1]
            str99="-"+str99
            info8=shift(info7,arr[0],str99)
            brr.append(info8)

        f3=open("output.txt","a")
        f3.write("\n")
        for k in range(len(brr)):
            f3.write(brr[k])
            f3.write("\n")

def main():
    import sys
    print(sys.argv)
    if sys.argv[4]=="e":
        #try:
        fileName = sys.argv[2]+ '.txt'
        processFile(fileName)
        fileName1 = sys.argv[1] + '.txt'

        handleFile(fileName1)
    else:
        #try:
        fileName = sys.argv[2]+'.txt'
        processFile(fileName)
        fileName2 = sys.argv[3]+'.txt'
        handleFile1(fileName2)

    #except FileNotFoundError as fnfe:
        #print(fnfe, file=sys.stderr)


if __name__ == "__main__":
    #rotate("name",1)
    #shift("YEAH","S0",2)
    main()
    #exchange("JAMES",1,3)