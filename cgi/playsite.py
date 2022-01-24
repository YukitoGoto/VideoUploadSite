#!/usr/bin/python3

import os
import sys
import datetime
import csv
import cgi
import cgitb; cgitb.enable()

CURRENT_PATH = str(os.getcwd().replace('/cgi', ''))
MOVIE_PATH =  CURRENT_PATH + '\\movie\\' if os.name == 'nt' else CURRENT_PATH + '/movie/'
THUMBNAIL_PATH = CURRENT_PATH + '\\thumbnail\\' if os.name == 'nt' else CURRENT_PATH + '/thumbnail/'

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
	print('<title>閲覧ページ</title>')
	print('</head>')
	print('')
	print('<body>')

# HTMLフッタを出力しCGIを終了
def print_footer():
	print('</body>')
	print('')
	print('</html>')

def print_movie(movieFileName):
	print('<video src="../movie/' + movieFileName + '" controls></video>')

"""
def print_title(thumbnailFileName):
	print('<video src="../movie/' + thumbnailFileName + '" controls></video>')
"""

def main():
	print_header()
	formData = cgi.FieldStorage()
	#print_movie('2022_1_21_13_41_24_example.mp4')
	print_movie(formData["value2"].value)
	#print_movie()
	print_footer()

if __name__ == '__main__':
	main()
