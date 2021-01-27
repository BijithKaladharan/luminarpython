queue=[]
while True:
    print("1. enqueue")
    print("2. dequeue")
    print("3. display")
    print("4. exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        size=int(input("enter size of queue:"))
        for i in range(size):
            element=input("enter the element:")
            queue.append(element)
            print(element,"is added to queue")
    elif choice==2:
        if not queue:
            print("queue is empty")
        else:
            e=queue.pop(0)
            print("removed element:",e)
    elif choice==3:
        print(queue)

    elif choice==4:
        break
    else:
        print("invalid choice")

