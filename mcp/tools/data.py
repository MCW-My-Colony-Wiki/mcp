import re
import json
from os import chdir

from .path import run_here

__all__ = [
	'format_source_data',
	'source_data',
	'class_name',
	'format_name'
]

def format_source_data(data):
	data = re.sub(r', *//.*', ',', data) #Remove comment
	data = re.sub(r': *\.', ': 0.', data) #Remove float-like(.1, .2, ...)
	data = data.strip() #Remove space at start and end
	list_data = data.split('\n') #Prepare for get first line and last line
	while '"' not in list_data[1]:
		data = data[len(list_data[0]):-len(list_data[-1])].strip() #Remove first line and last line
		list_data = data.split('\n') #Overwrite list_data with new data
	
	data = data.replace(list_data[0], '{') #Let first line turn into "{"
	data = data.replace(list_data[-1], '}') #Let last line turn into "}"
	
	return data

@run_here
def source_data(file):
	chdir('..')
	with open(f'source/{file}.js', 'r', encoding = 'UTF-8') as game_file:
		data = format_source_data(game_file.read())
		data = json.loads(data, encoding = 'UTF-8')
		return data

def class_name(object):
	if object == type:
		return type.__class__.__name__
	else:
		return object().__class__.__name__

def format_name(name):
	name = re.sub(r"[\s']", '-', name)
	return name