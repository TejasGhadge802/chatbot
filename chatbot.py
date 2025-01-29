print("By TEJAS\n")
print("Hello Frnds")

name = "TG Chatbot"
print(f"chatBot: Hey, I am {name}")

while(True):
    useName = input("chatBot: What is your name\t").capitalize()

    #Bot age function
    age = 2
    def botAge(age):
        print("chatBot: I am",age,"year old")
    botAge(age) # call

    userAge = int(input(f"chatBot: {useName}, What about you:\t"))

    # Age different function
    def ageDiff(a,b):
        diff = a-b;
        if(diff > b):
            print(f'chatbot: {userName} you are {diff} year older then me')
        elif(diff == 0):
            print(f'chatbot: ooh!, {userName} we both are 2 year old')
        else:
            print(f'chatbot: ooh!, {userName} you are {abs(diff)} year younger then me')
    ageDiff(userAge,age) #call

    
    # Userid
    print (f"chatBot; Hey, (useName) can I suggest a user ID for you")
    responce = input("chatBot; yes/no: \t").lower()
    
    if(responce == "yes"):
        resYes = input("Enter your full name without space: \t")
        userld = len(res Yes)
        print("Your userld is:",useName.lower()+"_"+str(userld))

    # restart
    print (f"chatBot; Hey, (useName) Do you want to try again!")
    res = input("chatBot; yes/no: \t").lower()
    if(res == 'no'):
        break

print("exiting...")
print("Thanks, for interaction")
    

