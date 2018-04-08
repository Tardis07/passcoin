# -*- coding: utf-8 -*-
# Date: 2018-04-08 20:52:00
# Author: Milktea (milktea@vmoe.info)
# Version: 0.0.1.0408

import platform, sys, os, commands

hashcat_version = '4.1.0'

def rt_split():
	if platform.system() == 'Windows':
		return '\\'
	else:
		return '/'

def rt_exe():
	for i in platform.uname():
		if 'arm' in i:
			raise Exception("ARM is in developing, please wait.")
	if platform.system() == 'Windows':
		if platform.architecture()[0] == '64bit':
			return 'hashcat64.exe'
		else:
			return 'hashcat32.exe'
	elif platform.system() == 'Linux' or platform.system() == 'Darwin':
		if platform.architecture()[0] == '64bit':
			return 'hashcat64.bin'
		else:
			return 'hashcat32.bin'
	else:
		raise Exception("System Unknown")

def hashlog(logread,logfile):
	print os.getcwd()
	f = open(logfile, 'w')
	f.write(logread)
	f.close()

def hashcat_exec(hashfile,outfile,hash_mask,hash_mode=3,hash_format=0,outfile_format=3):
	os.chdir(os.getcwd() + rt_split() + 'hashcat-' + hashcat_version)
	debugfile = '..' + rt_split() + 'log' + rt_split() + hashfile + '.log'
	hashfile = '..' + rt_split() + 'hash' + rt_split() + hashfile
	outfile = '..' + rt_split() + 'out' + rt_split() + outfile
	com_line = '.' + rt_split() + rt_exe() + ' -a ' + str(hash_mode) + ' -m ' + str(hash_format) + ' --outfile-format ' + str(outfile_format) + ' -o ' + outfile + ' --potfile-disable ' + hashfile + ' ' + hash_mask
	# com = commands.getoutput(com_line)
	com = os.popen(com_line)
	logread = com.read()
	hashlog(logread,debugfile)
	# print os.getcwd()
	# print com_line
	# print com

hashcat_exec('1.hash','1.out','?d?d?d?d?d')

# if platform.system() == 'Windows':
# 	hashcat_exec('hash\\1.hash','out\\1.out','?d?d?d?d?d')
# else:
# 	hashcat_exec('hash/1.hash','out/1.out','?d?d?d?d?d')