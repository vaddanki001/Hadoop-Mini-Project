import sys


# # [Define group level master information]
incident_type=''
make =''
year = ''
def reset(line_fields):
  # [Logic to reset master info for every new group]
  # Run for end of every group
  global incident_type
  global make
  global year
  incident_type,make,year = line_fields[1].split('_')
  
def flush(vin):
  # [Write the output]
  print('%s,%s,%s,%s' %(vin,incident_type,make,year))

# input comes from STDIN
current_vin = ''
for line in sys.stdin:
  # [parse the input we got from mapper and update the master info]
  # [detect key changes]
  line = line.strip()
  line_fields = line.split(',')
  vin = line_fields[0]  
  incident_type = line_fields[1].split('_')[0]
  
  
  if current_vin != vin:    
    # if current_vin != None:      
    # write result to STDOUT 
   
    reset(line_fields)  
    current_vin = vin
#      
  if incident_type == 'A':
    flush(current_vin)  

