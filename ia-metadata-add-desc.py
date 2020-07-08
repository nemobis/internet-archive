#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2020 emijrp <emijrp@gmail.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import time
import internetarchive

def main():
    desc = 'You can open ZIM files with <a href="https://www.kiwix.org/">Kiwix</a> software.'
    for i in internetarchive.search_items('subject:"kiwix" AND subject:"zim"').iter_as_items():
        itemid = i.item_metadata['metadata']['identifier']
        print(itemid)
        if not 'description' in i.item_metadata['metadata']:
            r = internetarchive.modify_metadata(itemid, metadata=dict(description=desc))
            if r.status_code == 200:
                print('Description added: %s' % (desc))
            else:
                print('Error (%s) adding description: %s' % (r.status_code, desc))
        else:
            print('Already has description: %s' % (i.item_metadata['metadata']['description']))

if __name__ == '__main__':
    main()
