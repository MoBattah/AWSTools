import boto3


import base64
import paramiko
import sys



key = paramiko.RSAKey(data=base64.b64decode(b'AAAAB3NzaC1yc2EAAAADAQABAAAAgQC37NsG62lBjOkOIB63EpK3R0ZPM4ZOPmvRlt57OBgzysA6zkbS8u/Q4r87bzdwwFiXzMlBwzvJJ0oAmFqVzfMVamuPCVN7tc1Ur/sDFsP7qbrRvQTF5MuXnHP3QSC4DwN6UAMExvdfw5OgwbpGe1KS3iMKk53W2YTLQIEUW2+AsQ=='))
client = paramiko.SSHClient()
client.get_host_keys().add('intsa245au.vsp.sas.com', 'ssh-rsa', key)
client.connect('intsa245au.vsp.sas.com', username='mobatt', password='Menal10r$')
stdin, stdout, stderr = client.exec_command('ls')
for line in stdout:
    print('... ' + line.strip('\n'))
client.close()