import paramiko
import datetime
import os.path
import time
import sys
import re

# Checa arquivo de login
user_file = input("\n#  Entre com o caminho + arquivo de login (ex. D:\MyApps\myfile.txt): ")

if os.path.isfile(user_file) == True:
    print("\n* Arquivo de Login é válido :)\n")

else:
    print("\n* Arquivo {} não existe. Tente novamente.\n".format(user_file))
    sys.exit()
        
# Checando arquivo de comandos
cmd_file = input("\n# Entre com o caminho + arquivo de comandos (ex. D:\MyApps\myfile.txt): ")

if os.path.isfile(cmd_file) == True:
    print("\n* Arquivo de comandos é valido\n")

else:
    print("\n* Arquivo {} não existe. Tente novamente.\n".format(cmd_file))
    sys.exit()
    
# Abrindo a conexão SSHv2 com o dispositivo
def ssh_connection(ip):
    
    global user_file
    global cmd_file
    
    # Criando conexão SSH
    try:
        
        selected_user_file = open(user_file, 'r')
              
        selected_user_file.seek(0)
        
        username = selected_user_file.readlines()[0].split(',')[0].rstrip("\n")
        
        selected_user_file.seek(0)
        
        password = selected_user_file.readlines()[0].split(',')[1].rstrip("\n")
        
        # Logando no dispositivo
        session = paramiko.SSHClient()
        
        # Para teste, isso permite host keys desconhecidos
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        session.connect(ip.rstrip("\n"), username = username, password = password)
        
        # Starta um sessão shell
        connection = session.invoke_shell()	
        
        connection.send("enable\n")
        connection.send("terminal length 0\n")
        time.sleep(1)
        
        connection.send("\n")
        connection.send("configure terminal\n")
        time.sleep(1)
        
        selected_cmd_file = open(cmd_file, 'r')
            
        selected_cmd_file.seek(0)
        
        # Escrevendo linhas do arquivo de comando
        for each_line in selected_cmd_file.readlines():
            connection.send(each_line + '\n')
            time.sleep(2)
        
        selected_user_file.close()
        
        selected_cmd_file.close()
        
        # Checa erros de syntax
        router_output = connection.recv(65535)
        
        if re.search(b"% Invalid input", router_output):
            print("* Existe algum erro de syntax no dispositivo {}".format(ip))
            
        else:
            print("\nDispositivo atualizado {} \n".format(ip))

        # Achando o uso da CPU
        cpu = re.search(b"%Cpu\(s\):(\s)+(.+?)(\s)* us,", router_output)
        
        # Decodificando para UTF-8
        utilization = cpu.group(2).decode("utf-8")
        
        # Abrindo arquivo de CPU e inserindo novos dados
        with open("D:\\Documents\\Python\\myFirstProject\\cpu.txt", "a") as f:
            #f.write("{},{}\n".format(str(datetime.datetime.now()), utilization))
            f.write(utilization + "\n")
            
        # Teste leitura comando de output
        #print(str(router_output) + "\n")
 
        session.close()
     
    except paramiko.AuthenticationException:
        print("* Usuário ou senha inválidos\n* Por favor verifique o arquivo de login ou a configuração do dispositivo.")
        print("* Terminando o programa...")