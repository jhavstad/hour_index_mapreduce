#! /usr/bin/env python

import sys # Used for stdin and stdout
import csv # Used for parsing input and output lines

def reducer():
    # The csv reader to input tab delimited lines
    reader = csv.reader(sys.stdin, delimiter='\t')
    # The csv writer to output tab delimited lines
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    
    hours_index = dict()
    
    # Iterate over each line from the input
    for line in reader:
        # Implement an error handler in case anything goes wrong
        try:
            hour = line[0] # The hour is the 1st token
            node = line[1] # The node ID is the 2nd token
            
            # If the hour isn't in the hour index then add it
            if hour not in hours_index:
                hours_index[hour]    = [0, list()]
                
            # Append the node to the index if it isn't already
            if node not in hours_index[hour]:
                hours_index[hour][1].append(node)
                
            # Increment the count for the activity of the node
            hours_index[hour][0] += 1
        
        # Catch all errors in one statement.  Just continue on to the next line.
        except:
            continue
        
    # Iterate over the list and send the indices to the output
    for hour in hours_index:
        output = [hour, hours_index[hour][0], hours_index[hour][1]]
        writer.writerow(output)

def main():
    reducer()
    
if __name__ == '__main__':
    main()