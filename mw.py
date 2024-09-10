'''
  COPYRIGHT DISCLAIMER

Script: Malwarepy or mw.py - Malware simulator for internal audits

Copyright (C) 2024 https://github.com/SysAdminSecure

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version, with the following restrictions:

1. **Credits:** Credit must be given to the original author, https://github.com/SysAdminSecure, on any redistribution or modification of the script.
In addition, any monetary gratuity is appreciated as optional acknowledgment.

2. **Copying and Permissions:** Copying the code in its entirety is not permitted without explicit permission from the author.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; even without the implied warranty of MERCHANTABILITY or 
FITNESS FOR A PARTICULAR PURPOSE. No responsibility is assumed for the use of malware generated with this script, whether for legitimate purposes or not.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

For any questions, see: https://github.com/SysAdminSecure.

'''


## MalWare.PYdd
import os  
from complemets import  Banner, color
from complemets.Script import ramsomware,clear_screen

##global
run_mwpy = True
  
def carpeta():
    ##Folder Validation and Creation
    if os.path.exists("Malwares"):
        print('la carpeta ya ha sido creada')
    else:
        os.mkdir("Malwares")
      
def exit_mwpy():
    ##exit mwpy
    global run_mwpy
    run_mwpy = False
    print("\nExiting...\n")
    
def main():
    ##display
    
    print(f'''
malware creation options{color.YELLOW}
 
 1- ramsomware            2- Clear Screan         3-Exit             
          ''')
    
    ##Malware Options 
    option = input(f'''{color.BLUE}Select option:{color.PURPLE}''')
    match option:
        case "1":
            ramsomware()
        case "2":
            clear_screen()
        case "3":
           exit_mwpy() 
        case other:
            input(f'{color.RED} Press the Enter key to retry')
            
            
carpeta()
##cycle to keep the scrip active
if run_mwpy:
   
    while run_mwpy:
        try:
            clear_screen()
            main()
        except KeyboardInterrupt:
            exit_mwpy()