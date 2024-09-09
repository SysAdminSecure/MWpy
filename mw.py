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