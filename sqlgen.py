import md5crypt as md5
from sets import Set

f=open('passwords','r')
read=f.read()
data=read.replace('..','\n').splitlines()
f=open('users','r')
users=f.read().splitlines()
user=""
passwd=""
pairs={}
domains=Set()

for line in data:
	line=line.strip()
	if line.find('USER')>=0:
		user=line[line.find('USER')+5:]
	if line.find('PASS')>=0:
		passwd=line[line.find('PASS')+5:]
	"""if line.find("Mailbox open")>=0:
		if( not pairs.has_key(user)):
			pairs[user]=passwd"""
	pairs[user]=passwd
	
for user in users:
	try:
		pwhash=md5.md5crypt(pairs[user])
	except Exception:
		pwhash=md5.md5crypt("")
	domain=user.split('@')[1]
	domains.add(domain)
	maildir=domain+'/'+user.split('@')[0]
	local_part=user.split('@')[0]
	print "insert into mailbox values('%s','%s','','%s',524288000,'%s','%s',now(),now(),1);"%(user,pwhash,maildir,local_part,domain)
	print "insert into alias values('%s','%s','%s',now(),now(),1);"%(user,user,domain)
	
for domain in domains:
	print "insert into domain values('%s','',25,25,1024,1024,'virtual',0,now(),now(),1);"%(domain)

for user in users:
	try:
		print pairs[user],"\n"
        except Exception:
		print "NoPass:"+user
		
#for key,value in pairs.iteritems():
#	print key+":"+value+"\n"

