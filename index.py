#!/usr/bin/python3

import os
import sys
import datetime
import csv
import cgi
import cgitb; cgitb.enable()

# HTMLヘッダを出力
def print_header():
	print("Content-Type: text/html;charset=UTF-8")
	print()
	print('<!DOCTYPE html>')
	print('')
	print('<html lang = "ja">')
	print('')
	print('<head>')
	print('<!-- BootstrapのCSS読み込み -->')
	print('<link href = "css/bootstrap.min.css" rel = "stylesheet">')
	print('<!-- jQuery読み込み -->')
	print('<script src = "https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>')
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
	#sys.exit(0)

def print_uploadpage():
	print('<a href = "upload.html">投稿ページ</a>')

def print_moviecard(title, thumbnailFileName, movieFileName = None):
	print('<form class = "form-inline">')
	print('<div class = "w-25">')
	#print('<div class = "card" value = ' + movieFileName + 'onclick = "location.href = \'cgi/playsite.py\'">')
	print('<div class = "card"')
	print('<img class = "card-img-top" src = "thumbnail/' + thumbnailFileName + '" alt = "960x540" style = "width:auto">')
	print('<div class = "card-body">' + title + '</div>')
	print('</div>')
	print('</div>')
	print('</form>')

def main():
	print_header()
	print_moviecard('test2', '2022_1_21_13_41_24_example2.jpg')
	print_footer()

if __name__ == '__main__':
	main()
