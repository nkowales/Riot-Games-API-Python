# makedict.py, creates dictionaires of champion ids to champion names, and champion names to champion ids
#    Copyright (C) 2017  Nathan Kowaleski, Alanna McEachen

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import RiotGamesAPIPython
from info import API_KEY
import time

#create dictionaries of champion names to champion ids and champion ids to champion names

rito = riotgamesapipy.riotgamesapipy(API_KEY)
f = open('id2name.py', 'w')
st = 'NAME2ID = {'

champs = rito.getChampionData()

for key in champs['data']:
	st = st +'"' + str(champs['data'][key]['name']) + '" : "' + str(champs['data'][key]['id']) + '", '

st = st + "}\n"
st = st.replace(", }\n", "}\n")
f.write(st)
st2 = 'ID2NAME = {'

for key in champs['data']:
	st2 = st2 + '"' + str(champs['data'][key]['id']) + '" : "' + str(champs['data'][key]['name']) + '", '

st2 = st2 + '}\n'
st2 = st2.replace(', }\n', '}\n')
f.write(st2)
f.write('\n')
f.close()
