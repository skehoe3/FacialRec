# Motivation
This project was initiated as the result of an archival project I took on at my parents house.  My parents were getting ready to move from the home I grew up in to a smaller home, and as a result a lot of items had to be done away with.  We had a LOT of photos that no one ever looked at except very rare occasions; usually by accidentally coming across them, leafing through, then moving them someplace else to be happily stumbled upon in another few years.

To preserve the memories and sentimental value, but eliminate the physical storage issue, I bought an EPSON ES-500W feed scanner and scanned everything.  Then I found a few more boxes, this time with photos from my grandparents era.  Then I found my biological grandfather's photo album of his 1950s military service... and so on, and so on.  Eventually I had well over 60GB purely of photos, most of which were uncategorized or unlabled -- usually both.  In order to introduce some labeling and order into this mass of data, I decided to kick off a facial detection project.

# Plan
1) detect faces in images
2) record information about face locations in a DB
    2a) what kind of db?
        - use logging.  Log to the db with a timestamp, path, image name, image path. 
        - ALSO - include areas to store the results of the face detector, and whether or not the detector has been applied
            - detectionCompleted: boolean
            - faceLocations: raw numpy outout (IE - the raw output from the detector)
    2b) what info is in db?
    2c) how to retain date/location information when images moved from existing file struc to new db?

most applications just use the file system.  

could create a mini db in the form of a json file for each folder.  the json would notate which images had faces detected, and where those faces are in the pixel structure.

do it on a folder by folder basis to make it easier to break up batch operations.
