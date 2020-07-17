# ViRuS-X-Z Team
# VXZ-Tools
# VXZ-Gathering-Website-Information-Tool

# imports
import os
from Functions import *

# Start-script-programming
loading1 ()
loading0 ()
banner2 ()
login ()
print ("Welcom in VXZ-Gathering-Website-Information-Tool")
print ("    ")

# V ========== X ========== Z

# input domain name 
dns = input ("Enter domain name ===> ")

# Start Gathering from here
os.system ("host "+ dns)
print ("V ========== X ========== Z")
os.system ("sudo nmap -sS -sV -O -T4 -v "+ dns)
print ("V ========== X ========== Z")

# V ========== X ========== Z
# V ========== X ========== Z
# E ========== N ========== D
