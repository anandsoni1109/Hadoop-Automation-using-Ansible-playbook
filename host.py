

def slave(ips):
	j=0
	import subprocess 
	f=open('/etc/hosts'  , 'a')
	for i in ips:
		j=j+1
		c='{}       slave{}.avn\n'.format(i[0],j)
		
		f.write(c)
	f.close()

	


def master(ips):
	import subprocess 
	f=open('/etc/hosts'  , 'a')
	c='{}       master.avn\n'.format(ips[0][0])
	f.write(c)
	f.close()	
def tt(ips):
	import subprocess 
	f=open('/etc/hosts'  , 'a')
	b=[]
	j=0
	for i in ips:
		j=j+1
		c='{}       tt{}.avn\n'.format(i[0],j)
		f.write(c)
	f.close()

def jt(ips):
	import subprocess 
	f=open('/etc/hosts'  , 'a')
	c='{}       jt.avn\n'.format(ips[0][0])
	f.write(c)	
	f.close()





