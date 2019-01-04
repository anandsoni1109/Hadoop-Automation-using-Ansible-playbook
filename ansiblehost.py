def slave(ips):
	f=open('/etc/ansible/hosts' , 'a')
	a='[slave]\n'
	f.write(a)
	for i in ips:
		c='{}	ansible_user=root	ansible_ssh_pass={}\n'.format(i[0],i[1])
		f.write(c)

def tt(ips):
	f=open('/etc/ansible/hosts' , 'a')
	a='[tt]\n'
	f.write(a)
	for i in ips:

		c='{}	ansible_user=root	ansible_ssh_pass={}\n'.format(i[0],i[1])
		f.write(c)


def master(ips):
	f=open('/etc/ansible/hosts' , 'a')
	a='[master]\n'
	f.write(a)
	c='{}	ansible_user=root	ansible_ssh_pass={}\n'.format(ips[0][0],ips[0][1])
	f.write(c)


def jt(ips):
	f=open('/etc/ansible/hosts' , 'a')
	a='[jt]\n'
	f.write(a)
	c='{}	ansible_user=root	ansible_ssh_pass=toor\n'.format(ips[0][0],ips[0][1])
	f.write(c)
