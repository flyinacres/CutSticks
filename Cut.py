__author__ = 'rfischer'


num_sticks = input()

m = []

sticks = raw_input()

m = sticks.split()


while num_sticks > 0:
    print num_sticks
    shortest = 1001;
    deleted = 0
    for x in range(num_sticks):
        if int(m[x]) < shortest:
            shortest = int(m[x])

    #print ("shortest stick is " + str(shortest))

    x = 0
    still_deleting = 1
    while x < len(m):
        if int(m[x]) - shortest <= 0:
            #print "deleting " + str(m[x])
            del m[x]
            #print m
            deleted += 1
        else:
            m[x] = int(m[x]) - shortest
            x += 1

    #print "Deleted a total of " + str(deleted)
    num_sticks -= deleted
    #print "Number of sticks: " + str(num_sticks)



