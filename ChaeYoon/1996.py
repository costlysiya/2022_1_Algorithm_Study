row_column=int(input())
good_array=[]
for i in range(row_column):
    line=input()
    good_array.append(line)

def what_val(i,j,list):

    if i<0 or i>=len(list) or j<0 or j>=len(list):
        return 0
    if list[i][j].isdigit()==False:
        return 0
    else:
        return int(list[i][j])

def cal_val(i,j,list):
    sumval=what_val(i-1,j-1,list)+what_val(i-1,j,list)+what_val(i-1,j+1,list)
    sumval+=what_val(i,j-1,list)+what_val(i,j+1,list)
    sumval+=what_val(i+1,j-1,list)+what_val(i+1,j,list)+what_val(i+1,j+1,list)

    if sumval<10:
        return str(sumval)
    else:
        return "M"

for i in range(row_column):
    for j in range(row_column):
        if str(good_array[i][j]).isdigit()==True:
            print("*", end="")
        else:
            print(cal_val(i,j,good_array), end="")
    print()


