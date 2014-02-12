#! /usr/bin/env python

import sys # Used for stdin and stdout
import csv # Used for parsing input and output lines

# Used for parsing date values from input strings
from datetime import datetime

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    
    # This is the list of hours to search for (in this case all 24 hours)
    #search_hours = [i for i in range(24)]
    # This is the list of hours to search for (midnight, 5 AM, noon, 6 PM, 9 PM)
    search_hours = [0, 5, 12, 6, 9]
    
    for line in reader:
        try:
            forum_id   = line[0] # The forum ID is the 1st token
            date_added = line[8] # The hour is in the date added field which is the 9th token
            
            # The key is the hour, which is parsed below
            key   = None
            # The value is forum ID
            value = forum_id
            
             # Try to parse the added date field as a proper date,
            # implementing an error handler in the event something
            # goes wrong.
            try:
                # The input time has superfluous information after the
                # period, which should be discarded in order to
                # correctly parse the date
                dot_index  = date_added.index('.')
                date_added = date_added[:dot_index]
                # Now, attempt to parse the date string and retrieve the hour field
                # which is a value between 0 to 23
                hour       = datetime.strptime(date_added, '%Y-%m-%d %H:%M:%S').hour
                # Set the key to the hour
                key = hour
                
            # If an error was caught, then move on to the next line, nothing to see here
            except:
                continue
            
            # If the hour is not the hour in the search then continue
            if int(hour) not in search_hours:
                continue
            
            # If the key is blank then continue
            if value == None:
                continue
            
            # Create the output with the key/value pair and send it to the reducer
            output = [key, value]
            writer.writerow(output)
            
        except:
            continue

def main():
    mapper()
    
if __name__ == '__main__':
    main()