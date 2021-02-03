import os.path
import sys

#Checa se é valido o Arquivo de endereços de IP
def ip_file_valid():

    ip_file = input("\n# Entre com o caminho + arquivo de IP's (ex. D:\MyApps\myfile.txt): ")


    if os.path.isfile(ip_file) == True:
        print("\n* Arquivo de IP é válido\n")
    
    else:
        print("\n* Arquivo {} não existe. Tente novamente!.\n".format(ip_file))
        sys.exit()

    selected_ip_file = open(ip_file, 'r')
 
    selected_ip_file.seek(0)
    
    ip_list = selected_ip_file.readlines()
    
    selected_ip_file.close()
        
    return ip_list