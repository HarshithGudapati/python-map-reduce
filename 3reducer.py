s = open("02.txt","r")
r = open("03.txt", "w")

thisKey = ""
thisValue = 0.0

for line in s:
  data = line.strip().split('\t')

  if paymentType != thisKey:
    if thisKey:
     thisKey = paymentType 
     thisValue = 0.0
  
  # apply the aggregation function
  thisValue += 1
=======
    thisKey = store 
    thisValue = 0.0
  
  # apply the aggregation function
  thisValue += float(amount)


# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()
