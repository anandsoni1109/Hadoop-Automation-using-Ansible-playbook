import subprocess
import socket
import hadoop
import host
import ansiblehost
import pickle
s=socket.socket()
s.bind(("192.168.43.112" , 1235))
s.listen(5)
#session,addr =s.accept()
#data=session.recv(100)


#session.send(b'helloworld')



while True:

	session,addr =s.accept()
	data=session.recv(100)
	cmd=data.decode()
	print(cmd)
	if cmd == 'one' or cmd == '1':
			hadoop.hadooprunmaster()
			hadoop.hadooprunslave()


	if cmd == 'second' or cmd == '2':
			hadoop.hadooprunjt()
			hadoop.hadoopruntt()

	if cmd == 'three' or cmd == '3':
		session,addr =s.accept()
		ips=session.recv(10000)
		ips=pickle.loads(ips)
		print(ips)
		host.master(ips)
		ansiblehost.master(ips)
		hadoop.hadoopsetmaster()
	
	if cmd == 'four' or cmd == '4':
                session,addr =s.accept()
                ips=session.recv(10000)
                ips=pickle.loads(ips)
                print(ips)
                a=host.slave(ips)
                ansiblehost.slave(ips)
                hadoop.hadoopsetslave()

	if cmd == 'five' or cmd == '5':
                session,addr =s.accept()
                ips=session.recv(10000)
                ips=pickle.loads(ips)
                print(ips)
                a=host.jt(ips)
                ansiblehost.jt(ips)
                hadoop.hadoopsetjt()

	if cmd == 'six' or cmd == '6':
                session,addr =s.accept()
                ips=session.recv(10000)
                ips=pickle.loads(ips)
                print(ips)
                a=host.tt(ips)
                ansiblehost.tt(ips)
                hadoop.hadoopsettt()

	if cmd == 'seven' or cmd == '7':
                hadoop.hadoopreset()



	if cmd == 'eight' or cmd == '8':
		break



		






#session.send(foutpiut)
#session.send(b"your requestis not processed or it is invalid")
