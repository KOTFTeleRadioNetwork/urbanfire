# Copyright (c) 2017 KOTF TeleRadio Network
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

# -*- coding: utf-8 -*-

import urllib2
import xbmc
import xbmcgui

# Stream URL here
url = urllib2.urlopen("theurbanfiregroup.com/stream_url.txt").readline().strip()
# Fake List Item for Stream Name
listitem = xbmcgui.ListItem("KOTF UrbanFire")
listitem.setInfo('video', {'Title': 'KOTF UrbanFire', 'Genre': 'Urban Programming'})
# Play the Stream
xbmc.Player().play(url, listitem)
