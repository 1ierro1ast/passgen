########################_OUT_######################

def extPrint(text,delay):
	import time,sys
	text = text+"\n"
	for i in text:
		time.sleep(delay)
		sys.stdout.write(i)
		sys.stdout.flush()
	return text

def logger(text):
	from sys import platform,stdout
	splitter = '\n###=============================###\n'
	stdout.write(splitter+'#~'+platform+'_logMsg: '+text+splitter)

###########################_JSON_####################

def jsonOpen(filename):
	import json
	with open(filename,"r",encoding = 'UTF-8') as file:
		f = json.load(file)
	return f

def jsonSave(data,filename,indent):
	import json
	try:
		with open(filename,"w",encoding ='UTF-8')  as file:
			json.dump(data,file,ensure_ascii=False,indent = indent)
		return True
	except Exception:
		return False

##########################_FILES_###################

def saveToFile(data,filename,mode):
	with open(filename, mode,encoding = "UTF-8") as file:
		file.write(data+'\n')
		file.close
	return data

def openFile(filename,*args):
	try:
		if args[0] == 'r':
			with open(filename,"r",encoding = "UTF-8") as file:
				data = file.read()
				dataList = data.split("\n")
				return dataList
		elif args[0] == 'l':
			with open(filename,"r",encoding = "UTF-8") as file:
				data = file.read()
				dataList = data.split(args[1])
				return dataList
		elif args[0] == 's':
			with open(filename,"r",encoding = "UTF-8") as file:
				data = file.read()
				return data
	except Exception:
		with open(filename,"r",encoding = "UTF-8") as file:
			data = file.read()
			dataList = data.split("\n")
			return dataList

#########################_CROSSPLATFORM_FUNC_################

def cClear():
	import subprocess
	from sys import platform
	if platform == 'linux' or platform == 'linux2':
		subprocess.call(['clear'],shell = True)
		return True
	elif platform == 'win32':
		subprocess.call(['cls'],shell = True)
		return True
	elif platform == "darwin":
		subprocess.call(['clear && printf \'\\e[3J\''],shell = True)
		return True
	else:
		logger('Unknow system :(')
		return False

def makeDir(path):
	import subprocess, os
	from sys import platform
	if platform == 'linux' or platform == 'linux2':
		subprocess.call(['mkdir '+path],shell = True)
		return True
	elif platform == 'win32':
		os.mkdir(path)
		return True
#	elif platform == "darwin":
#		subprocess.call(['clear && printf \'\\e[3J\''],shell = True)
	else:
		logger('Unknow system :(')
		return False

def remove(path):
	import subprocess, os
	from sys import platform
	if platform == 'linux' or platform == 'linux2':
		subprocess.call(['rm -rf '+path],shell = True)
		return True
	elif platform == 'win32':
		try:
			os.rmdir(path)
			return True
		except:
			os.remove(path)
			return True
#	elif platform == "darwin":
#		subprocess.call(['clear && printf \'\\e[3J\''],shell = True)
	else:
		logger('Unknow system :(')
		return False

def copy(path,toPath):
	import subprocess, os
	from sys import platform
	if platform == 'linux' or platform == 'linux2':
		subprocess.call(['cp -r'+path+' '+toPath+'/'+path],shell = True)
		return True
	elif platform == 'win32':
		subprocess.call(['copy /Y'+path+' '+toPath+'/'+path],shell = True)
		return True
#	elif platform == "darwin":
#		subprocess.call(['clear && printf \'\\e[3J\''],shell = True)
	else:
		logger('Unknow system :(')
		return False

def clipCopy(data):
	try:
		import pyperclip
	except:
		install("pyperclip")
		import pyperclip
	try:
		pyperclip.copy(data)
		return True
	except:
		logger('Clipboard error :(')
		return False

def clipPaste():
	try:
		import pyperclip
	except:
		install("pyperclip")
		import pyperclip
	try:
		return pyperclip.paste()
	except:
		logger('Clipboard error :(')
		return None

def install(*modulesNames):
	import subprocess
	listM = ''
	for module in modulesNames:
		try:
			subprocess.call(['pip','install',module])
		except:
			subprocess.call(['pip3','install',module])
		listM += (module+', ')
	cClear()
	return listM+'- successfully installed'
