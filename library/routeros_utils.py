#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2017 Sam Edwards
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

# NOTE: This is not a module. This becomes ansible.module_utils.routeros if
# merged into the Ansible codebase.


try:
    import librouteros
    HAS_LIB = True
except ImportError:
    HAS_LIB = False

from ansible.module_utils.basic import env_fallback

routeros_provider_spec = {
    'host': dict(),
    'port': dict(type='int'),

    'username': dict(fallback=(env_fallback, ['ANSIBLE_NET_USERNAME'])),
    'password': dict(fallback=(env_fallback, ['ANSIBLE_NET_PASSWORD']), no_log=True),
    'ssh_keyfile': dict(fallback=(env_fallback, ['ANSIBLE_NET_SSH_KEYFILE']), type='path'),

    'timeout': dict(type='int'),

    'transport': dict(default='cli', choices=['cli', 'api'])
}
routeros_argument_spec = {
    'provider': dict(type='dict', options=routeros_provider_spec),
}

del librouteros
