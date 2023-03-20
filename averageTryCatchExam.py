average=0
try:
    li = list(input("Enter a list : "))
    if len(li) == 0 :
        raise
    average = sum(li)/len(li)
except:
    average=0.0
    print("List is empty")
finally:
    print("Average : ",average)