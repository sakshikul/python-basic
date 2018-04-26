#There are 21 sticks, first the user picks number of sticks between 1-4,
# then the computer picks sticks(1-4). Who ever will pick the last stick will loose. 
#Can you find out the case when the user will win ?


print ("you chose 1-4 sticks at a time")
print("if you pick last one stick ,then you lose the game")
sticks = 21
while True:
    print("sticks left", sticks)
    sticks_taken = int(input("No. of sticks taken:"))
    if sticks == 1:
        print("you lose the game")
        break
    if sticks_taken >=5 or sticks_taken <=0:
        print("wrong choice")   
        continue
    print("computer took sticks", (5-sticks_taken))
    sticks= sticks-5     