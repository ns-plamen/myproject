#!/usr/bin/env python

import os, sys, os.path, stat, time
from stat import *
from django.http import HttpResponse
from django.template import Template, Context

#funk. za print na stat-a
def fileprint (name_0):
	file_stats = os.stat(name_0)
	file_info = {
		'fsize': file_stats [stat.ST_SIZE],
		'f_lm': time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(file_stats[stat.ST_MTIME])),
		'f_la': time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(file_stats[stat.ST_ATIME])),
		'f_ct': time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(file_stats[stat.ST_CTIME]))
		}
	filesize = ("%(fsize)s bytes" % file_info)
	crtdat = ("%(f_ct)s" % file_info)
	lstmod = ("%(f_lm)s" % file_info)
	lstacc = ("%(f_la)s" % file_info)
	allstat = [name_0, filesize, crtdat, lstmod,lstacc]
	
	return allstat

def listdir (name):
	answer = {'isdir': True}
	result = []
	#proverka validen put
	if not os.path.exists(name):
		error = 'error'
		return error
	
	#proverka na targeta - dir ili file	
	if not os.path.isfile (name):
		#TRQQ DA sloja proverka dali (name) ima '/' nakraq!!!!i ako ne da +
		mytail = name[-1:]
		#print mytail

		#print name
		if not mytail == '/':
			name += '/'
		
		
		#target is DIR                
		answer ['path'] = (name)
		contain = os.listdir(name)
		for a in (contain):
			in_name = name + a
			#file_stats = os.stat(in_name)
			#proverka sudurjanieto na DIR
			if not os.path.isfile (in_name):
				dirtarget = [(in_name), 'True']
				result.append(dirtarget)
			else:
				#current_target = fileprint(in_name)
				result.append(fileprint(in_name))
	#ne e dir => print		
	else:
		answer ['path'] = (name)
		answer ['isdir'] = False
		#print file_stats
		target_file = fileprint(name)
		result.append(target_file)
	answer ['listdir'] = (result)
	return answer






