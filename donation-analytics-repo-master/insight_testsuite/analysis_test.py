# read line by line
import os
import sys
import numpy as np # for percentile calculation

file_it = sys.argv[1] # itcont
file_per = sys.argv[2] # percentile
file_rd = sys.argv[3] # repeated_donor

fileHandle = open(file_per, 'r') # open percentile.txt
percent = fileHandle.read() # read percentile.txt
fileHandle.close()
per = int(percent[:2]) # store percentile number to 'per'
# read itcont.txt
fileHandle = open(file_it, 'r') # open itcont.txt
file_write = open(file_rd, 'w') # open repeated_donor.txt for write

# prepare fields
good = set('QWERTYUIOPASDFGHJKLZXCVBNM, ') # for name check
good_cmte=set('C1234567890') # for cmte_id check
a=[] # prepare for total
seen = set()
uniq = [] 

i=0;j=0;tot=0
# read fields
for line in fileHandle:
    fields = line.split('|') # split line into different parts.
    cmte = fields[0] # CMTE_ID
    name = fields[7] # name
    zip_code = fields[10] #zip code
    tran_dt = fields[13][-4:] # TRANSACTION_DT
    tran_amt = fields[14]# TRANSACTION_AMT
    other_id = fields[15]# other_id

    i=i+1 # counter
    
    if (len(cmte)<0 and set(cmte)<=good): 1  # check CMTE_ID 
    elif (len(name)<0 and set(name)<=good): 1 # check name 
    elif (len(zip_code)<5 and zip_code.isdigit()==False): 1 # check zip code
    elif (len(tran_dt)<0 and tran_dt.isdigit()==False): 1 # check TRANSACTION_DT 
    elif (len(tran_amt)<0 and tran_amt.isdigit()==False): 1 # check TRANSACTION_AMT 
    elif (len(other_id)>0): 1 # check other id

    else:
        # populate name
        if name not in seen:
            uniq.append(name)
            seen.add(name)
        else:
            j=j+1 # counter for repeated name
 
            tot=int(tran_amt)+tot # create total
            a.append(tot)# store total
            perc = np.percentile(a, per, interpolation='lower') # calculate percentile
            # write file
            file_write.write(cmte+'|'+zip_code[:5]+'|'+tran_dt+'|'+str(perc)+'|'+str(tot)+'|'+str(j)+'\n') 


fileHandle.close()
file_write.close() 