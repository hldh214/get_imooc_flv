# -*- coding: utf-8 -*-
import urllib.request
import re
import json

course_num = '409'
video_get_url = 'http://www.imooc.com/course/ajaxmediainfo/?mid='
course_url = 'http://www.imooc.com/learn/' + course_num
video_url = []

re_video_num = re.compile(r'(?<=/video/)\d+(?=\' class)')
re_video_title = re.compile(r'(?<="J-media-item studyvideo">).+(?=\()')

opener = urllib.request.build_opener()

res = opener.open(course_url).read().decode()

video_num = re_video_num.findall(res)
video_title = re_video_title.findall(res)

for each in range(len(video_num)):
	video_get_url = 'http://www.imooc.com/course/ajaxmediainfo/?mid='
	video_get_url += video_num[each]
	res = opener.open(video_get_url).read().decode()
	data = json.loads(res)
	# 此处存在三种模式 0:超清 1:高清 2:普清
	url = data['data']['result']['mpath'][0]
	video_url.append(url)
	
print(video_url)
print(video_title)
