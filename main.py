#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
sample nornir script
"""

from nornir import InitNornir

def main():
  """main"""

  args = {
    'core': {
      'num_workers': 100
    },
    'inventory': {
      'plugin': "nornir.plugins.inventory.simple.SimpleInventory",
      'options': {
        'host_file': "inventory/hosts.yml",
        'group_file': "inventory/groups.yml"
      }
    }
  }
  nr = InitNornir(**args)

  """
  nr = InitNornir(
    core={"num_workers": 100},
    inventory={
      "plugin": "nornir.plugins.inventory.simple.SimpleInventory",
      "options": {
        "host_file": "inventory/hosts.yml",
        "group_file": "inventory/groups.yml"
      }
    }
  )
  """

  print(nr.inventory.hosts)
  print(nr.inventory.groups)

  host = nr.inventory.hosts["leaf01.bma"]
  print(host.keys())

if __name__ == '__main__':
  main()
