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
    genres = {
        'Wikipedia': 'Encyclopedia',
        'Wiktionary': 'Dictionary',
    }
    for project, genre in genres.items():
        #https://archive.org/services/docs/api/internetarchive/quickstart.html#searching
        for i in internetarchive.search_items('subject:"kiwix" AND subject:"zim" AND subject:"%s"' % (project.lower())):
            itemid = i['identifier']
            print(itemid)
            if project.lower() in itemid.lower():
                r = internetarchive.modify_metadata(itemid, metadata=dict(genre=genre))
                if r.status_code == 200:
                    print('Genre added: %s' % (genre))
                else:
                    print('Error (%s) adding genre: %s' % (r.status_code, genre))
            else:
                print('Unknown project')

if __name__ == '__main__':
    main()