#!/usr/bin/python3

import os
import sys
import datetime
import csv
import cgi
import cgitb; cgitb.enable()

# HTMLヘッダを出力
def print_header():
	# need for cgi
	print("Content-Type: text/html;charset = utf-8")
	print()
	# head
	print('<!DOCTYPE html>')
	print('')
	print('<html lang = "ja">')
	print('')
	print('<head>')
	print('<!-- BootstrapのCSS読み込み -->')
	print('<link href = "css/bootstrap.min.css" rel = "stylesheet">')
	print('<!-- BootstrapのJS読み込み -->')
	print('<script src = "js/bootstrap.min.js"></script>')
	print('<meta charset = "utf-8">')
	print('<meta name = "viewport" content = "width = device - width, initial - scale = 1.0">')
	print('<title>動画投稿サイト</title>')
	print('</head>')
	print('')
	print('<body>')

# HTMLフッタを出力しCGIを終了
def print_footer():
	print('</body>')
	print('')
	print('</html>')

def print_uploadpage():
	print('<a href = "upload.html">投稿ページ</a>')

def print_moviecard(titleName, thumbnailFileName, movieFileName):
	print('<form class = "form-inline">')
	print('<div class = "w-25">')
	print('<div class = "card" onclick = "location.href = \'cgi/playsite.py?value1=' + thumbnailFileName + '&value2=' + movieFileName + '\'">')
	#print('<div class = "card">')
	print('<img class = "card-img-top" src = "thumbnail/' + thumbnailFileName + '" alt = "960x540" style = "width:auto">')
	print('<div class = "card-body">' + titleName + '</div>')
	print('</div>')
	print('</div>')
	print('</form>')

def main():
	print_header()
	print_uploadpage()
	print_moviecard('test2', '2022_1_21_13_41_24_example2.jpg', '2022_1_21_13_41_24_example.mp4')
	print_moviecard('test1', '2022_1_21_13_41_24_example2.jpg', '2022_1_21_14_0_0_splatoon2_sample.mp4')
	print_moviecard('test3', '2022_1_21_13_41_24_example2.jpg', '2022_1_21_13_41_24_example.mp4')
	print_footer()

if __name__ == '__main__':
	main()
