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
from complemets import color
VERIOSN = "V1.0.1"



BANER1 = f'''
{color.RED}
                __       __   ______   __        __       __   ______   _______   ________  {color.PURPLE}_______  __      __ 
                {color.RED}|  \     /  \ /      \ |  \      |  \  _  |  \ /      \ |       \ |        \{color.PURPLE}|       \|  \    /  \\
                {color.RED}| $$\   /  $$|  $$$$$$\| $$      | $$ / \ | $$|  $$$$$$\| $$$$$$$\| $$$$$$$${color.PURPLE}| $$$$$$$\\$$\  /  $$
                {color.RED}| $$$\ /  $$$| $$__| $$| $$      | $$/  $\| $$| $$__| $$| $$__| $$| $$__    {color.PURPLE}| $$__/ $$ \$$\/  $$ 
                {color.RED}| $$$$\  $$$$| $$    $$| $$      | $$  $$$\ $$| $$    $$| $$    $$| $$  \   {color.PURPLE}| $$    $$  \$$  $$  
                {color.RED}| $$\$$ $$ $$| $$$$$$$$| $$      | $$ $$\$$\$$| $$$$$$$$| $$$$$$$\| $$$$$   {color.PURPLE}| $$$$$$$    \$$$$   
                {color.RED}| $$ \$$$| $$| $$  | $$| $$_____ | $$$$  \$$$$| $$  | $$| $$  | $$| $$_____ {color.PURPLE}| $$         | $$    
                {color.RED}| $$  \$ | $$| $$  | $$| $$     \| $$$    \$$$| $$  | $$| $$  | $$| $$     \{color.PURPLE}| $$         | $$    
                {color.RED} \$$      \$$ \$$   \$$ \$$$$$$$$ \$$      \$$ \$$   \$$ \$$   \$$ \$$$$$$$$ {color.PURPLE}\$$          \$$    
                                                                                                                                                                                            
                                        {color.WHITE}BY:{color.BLUE}SysAdminSecure             {color.WHITE}{VERIOSN}           
'''
             
BANER2 = f''' 
{color.PURPLE}
                ___ ___   ____  _      __    __   ____  ____     ___  ____   __ __ 
                |   |   | /    || |    |  |__|  | /    ||    \   /  _]|    \ |  |  |
                | _   _ ||  o  || |    |  |  |  ||  o  ||  D  ) /  [_ |  o  )|  |  |
                |  \_/  ||     || |___ |  |  |  ||     ||    / |    _]|   _/ |  ~  |
                |   |   ||  _  ||     ||  `  '  ||  _  ||    \ |   [_ |  |   |___, |
                |   |   ||  |  ||     | \      / |  |  ||  .  \|     ||  |   |     |
                |___|___||__|__||_____|  \_/\_/  |__|__||__|\_||_____||__|   |____/ 
                                                                                
                {color.WHITE}BY:{color.BLUE}SysAdminSecure                                             {color.WHITE}{VERIOSN}   
''' 


BANER3 =f'''
{color.RED}
                *                (                          (            (          )  
                (  `       (       )\ )   (  (        (       )\ )         )\ )    ( /(  
                )\))(      )\     (()/(   )\))(   '   )\     (()/(   (    (()/(    )\()) 
                ((_)()\  ((((_)(    /(_)) ((_)()\ ) ((((_)(    /(_))  )\    /(_))  ((_)\  
                (_()((_)  )\ _ )\  (_))   _(())\_)() )\ _ )\  (_))   ((_)  (_))   __ ((_){color.BLUE} 
                |  \/  |  {color.RED}(_){color.BLUE}_\{color.RED}(_) {color.BLUE}| |    \ \{color.RED}((_){color.BLUE}/ / {color.RED}(_){color.BLUE}_\{color.RED}(_) {color.BLUE}| _ \  | __| | _ \  \ \ / / 
                | |\/| |   / _ \   | |__   \ \/\/ /   / _ \   |   /  | _|  |  _/   \ V /  
                |_|  |_|  /_/ \_\  |____|   \_/\_/   /_/ \_\  |_|_\  |___| |_|      |_|   
                                                                                        
                {color.WHITE}BY:{color.BLUE}SysAdminSecure                                             {color.WHITE}{VERIOSN}  
'''
BANER4 =f'''
{color.DARK_GRAY}

                ░  ░░░░  ░░░      ░░░  ░░░░░░░░  ░░░░  ░░░      ░░░       ░░░        ░░       ░░░  ░░░░  ░
                ▒   ▒▒   ▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒  ▒  ▒  ▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒  ▒▒▒  ▒▒  ▒▒
                ▓        ▓▓  ▓▓▓▓  ▓▓  ▓▓▓▓▓▓▓▓        ▓▓  ▓▓▓▓  ▓▓       ▓▓▓      ▓▓▓▓       ▓▓▓▓▓    ▓▓▓
                █  █  █  ██        ██  ████████   ██   ██        ██  ███  ███  ████████  ███████████  ████
                █  ████  ██  ████  ██        ██  ████  ██  ████  ██  ████  ██        ██  ███████████  ████
                                                                                                        
                                          {color.WHITE}BY:{color.BLUE}SysAdminSecure              {color.WHITE}{VERIOSN}
'''


BANER5 =f'''
{color.PURPLE}
                                                                                                              
                    @@@@@@@@@@    @@@@@@   @@@       @@@  @@@  @@@   @@@@@@   @@@@@@@   @@@@@@@@  @@@@@@@   @@@ @@@  
                    @@@@@@@@@@@  @@@@@@@@  @@@       @@@  @@@  @@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@ @@@  
                    @@! @@! @@!  @@!  @@@  @@!       @@!  @@!  @@!  @@!  @@@  @@!  @@@  @@!       @@!  @@@  @@! !@@  
                    !@! !@! !@!  !@!  @!@  !@!       !@!  !@!  !@!  !@!  @!@  !@!  @!@  !@!       !@!  @!@  !@! @!!  
                    @!! !!@ @!@  @!@!@!@!  @!!       @!!  !!@  @!@  @!@!@!@!  @!@!!@!   @!!!:!    @!@@!@!    !@!@!   
                    !@!   ! !@!  !!!@!!!!  !!!       !@!  !!!  !@!  !!!@!!!!  !!@!@!    !!!!!:    !!@!!!      @!!!   
                    !!:     !!:  !!:  !!!  !!:       !!:  !!:  !!:  !!:  !!!  !!: :!!   !!:       !!:         !!:    
                    :!:     :!:  :!:  !:!   :!:      :!:  :!:  :!:  :!:  !:!  :!:  !:!  :!:       :!:         :!:    
                    :::     ::   ::   :::   :: ::::   :::: :: :::   ::   :::  ::   :::   :: ::::   ::          ::    
                    :      :     :   : :  : :: : :    :: :  : :     :   : :   :   : :  : :: ::    :           :     
                                         
                                             {color.WHITE}BY:{color.BLUE}SysAdminSecure              {color.WHITE}{VERIOSN}                                                                                                                                                                            
'''                                                                                     

list_baner = BANER1,BANER2,BANER3,BANER4,BANER5