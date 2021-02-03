import sys
import subprocess

#Testa o ping nos IP's
def ip_reach(list):

    for ip in list:
        ip = ip.rstrip("\n")
        
        ping_reply = subprocess.call('ping %s -n 2' % (ip,), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        if ping_reply == 0:
            print("\n* {} é alcançavel\n".format(ip))
            continue
        
        else:
            print('\n* {} não é alcançavel. Chece sua conexão e tente novamente!'.format(ip))
            sys.exit()