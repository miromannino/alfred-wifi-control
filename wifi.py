# Copyright (c) 2015 Miro Mannino

import xml.etree.ElementTree as ET
import sys
import collections

commands = collections.OrderedDict()
commands['on'] = {
    'command': 'on up activate',
    'title': 'Wi-Fi On'
  }
commands['off'] = {
    'command': 'off down deactivate',
    'title': 'Wi-Fi Off'
  }
commands['toggle'] = {
    'command': 'toggle change switch',
    'title': 'Wi-Fi Toggle'
  }
commands['restart'] = {
    'command': 'restart reset',
    'title': 'Wi-Fi Restart'
  }

def suggestCommands(query):
  query = query.strip()
  rE = ET.Element('items')
  for k,e in commands.items():
    if (e['command'].find(query) == -1): continue
    iE = ET.SubElement(rE, 'item', valid = 'yes', arg = k, autocomplete = e['title'])
    tE = ET.SubElement(iE, 'title')
    tE.text = e['title']
  return rE

res = suggestCommands(sys.argv[1] if len(sys.argv) > 1 else '')
if res is not None: 
  print '<?xml version="1.0"?>'
  print ET.tostring(res)
