#!/usr/bin/python3

import os
import sys
import datetime
import csv
import cgi
import cgitb; cgitb.enable()

print("Content-Type: text/html;charset=UTF-8")
print()

CURRENT_PATH = str(os.getcwd().replace('/cgi', ''))
MOVIE_PATH =  CURRENT_PATH + '\\movie\\' if os.name == 'nt' else CURRENT_PATH + '/movie/'
#MOVIE_PATH = '.\\movie\\' if os.name == 'nt' else './title'
THUMBNAIL_PATH = CURRENT_PATH + '\\thumbnail\\' if os.name == 'nt' else CURRENT_PATH + '/thumbnail/'
#THUMBNAIL_PATH = '.\\thumbnail\\' if os.name == 'nt' else './thumbnail'
TITLE_PATH = CURRENT_PATH + '\\title\\' if os.name == 'nt' else CURRENT_PATH + '/title/'
#TITLE_PATH = '.\\title\\' if os.name == 'nt' else './title'

ATTRIBUTE_NAME_MOVIE = 'movie'
ATTRIBUTE_NAME_THUMBNAIL = 'thumbnail'
ATTRIBUTE_NAME_TITLE = 'title'

# HTMLヘッダを出力
def print_header():
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
	print('<title>Upload has done.</title>')
	print('</head>')
	print('')
	print('<body>')

# HTMLフッタを出力しCGIを終了
def print_footer():
	print('</body>')
	print('')
	print('</html>')
	sys.exit(0)

# name属性ごとにファイルを保存
def save_uploaded_file():
	formData = cgi.FieldStorage()
	nowTime = get_now_time_as_str()
	save_title_as_csv(nowTime, formData, ATTRIBUTE_NAME_TITLE)
	save_movie_or_thumbnail(nowTime, formData, ATTRIBUTE_NAME_THUMBNAIL)
	save_movie_or_thumbnail(nowTime, formData, ATTRIBUTE_NAME_MOVIE)

# 現在時刻を文字列で取得 YYYY_MM_DD_HH_MM_SS
def get_now_time_as_str():
	nowTime = datetime.datetime.now()
	return str(nowTime.year) + '_' + str(nowTime.month) + '_' + str(nowTime.day) + '_' + str(nowTime.hour) + '_' + str(nowTime.minute) + '_' + str(nowTime.second) + '_'

# 動画と画像を保存する
def save_movie_or_thumbnail(uploadDate, formData, attributeName):
  	fileName = uploadDate + formData[attributeName].filename
  	filePath = MOVIE_PATH + fileName if attributeName == ATTRIBUTE_NAME_MOVIE else THUMBNAIL_PATH + fileName if attributeName == ATTRIBUTE_NAME_THUMBNAIL else None
  	if filePath == None:
		print('<p>unexpected attributeName specified.</p>')
		print_footer()
  	item = formData[attributeName]
  	try:
		uploadedFile = open(filePath, 'wb')
  	except:
		print('<p> Failed open file. Check filePath.</p>')
		print('<p>' + filePath + ' is filePath.</p>')
		print_footer()
  	while True:
		chunk = item.file.read(512)
		byteValue = uploadedFile.write(chunk)
		#print('<p>' + str(chunk) + ' = chunk.</p>')
		#print('<p>' + str(byteValue) + ' = byteValue.</p>')
		if len(str(chunk)) < 512:
	  	break
  	uploadedFile.close()
  	print('<p>' + fileName + ' has just been uploaded.</p>')

# タイトルをcvsファイルに保存する
def save_title_as_csv(uploadDate, formData, attributeName):
  	filePath = TITLE_PATH + 'title.csv' if attributeName == ATTRIBUTE_NAME_TITLE else None
  	if filePath == None:
		print('<p>unexpected attributeName specified.</p>')
		print_footer()
  	title = formData[attributeName].value
  	try:
		csvFile = open(filePath, 'a', encoding = 'utf-8')
  	except:
		print('<p> Failed open file. Check filePath.</p>')
		print('<p>' + filePath + ' is filePath.</p>')
		print_footer()
	csv.writer(csvFile).writerow([uploadDate, title])
	csvFile.close()
	print('<p>' + title + ' has just been written to csv.</p>')

def main():
	print_header()
	save_uploaded_file()
	print_footer()

if __name__ == '__main__':
	main()
