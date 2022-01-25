#!/usr/bin/python3

import os
import sys
import csv
import cgi
import cgitb; cgitb.enable()

CURRENT_PATH = str(os.getcwd())
TITLE_PATH = CURRENT_PATH + '\\title\\' if os.name == 'nt' else CURRENT_PATH + '/title/'
THUMBNAIL_PATH = CURRENT_PATH + '\\thumbnail\\' if os.name == 'nt' else CURRENT_PATH + '/thumbnail/'
MOVIE_PATH =  CURRENT_PATH + '\\movie\\' if os.name == 'nt' else CURRENT_PATH + '/movie/'

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
	sys.exit(0)

def print_upload_page():
	print('<a href = "upload.html">投稿ページ</a>')

def print_movie(titleName, thumbnailFileName, movieFileName):
	print('<form class = "form-inline">')
	print('<div class = "w-25">')
	print('<div class = "card" onclick = "location.href = \'cgi/playsite.py?value1=' + thumbnailFileName + '&value2=' + movieFileName + '\'">')
	print('<img class = "card-img-top" src = "thumbnail/' + thumbnailFileName + '" alt = "960x540" style = "width:auto">')
	print('<div class = "card-body">' + titleName + '</div>')
	print('</div>')
	print('</div>')
	print('</form>')

# ファイル名のリストを取得
def get_file_name_list(filePath):
	try:
		fileList = os.listdir(filePath)
	except:
		print('<p>Failed open file. Check filePath.</p>')
		print('<p>' + filePath + ' is filePath.</p>')
		print_footer()
	return fileList

# アップロード日とタイトルのリストを取得
def get_uploaded_date_title_list():
	filePath = TITLE_PATH + 'title.csv'
	try:
		csvFile = open(filePath, 'r', encoding = 'utf-8')
	except:
		print('<p>Failed open file. Check filePath.</p>')
		print('<p>' + filePath + ' is filePath.</p>')
		print_footer()
	reader = csv.reader(csvFile)
	uploadedList = [row for row in reader]
	return uploadedList

# アップロード日に合致するファイル名を取得
def get_match_file_by_date(fileList, uploadedDate):
	for fileName in fileList:
		if uploadedDate in fileName:
			return fileName
	return None


def main():
	print_header()
	print_upload_page()
	uploadedList = get_uploaded_date_title_list()
	thumbnailList = get_file_name_list(THUMBNAIL_PATH)
	movieList = get_file_name_list(MOVIE_PATH)
	for i in range(1, len(uploadedList)):
		date = uploadedList[i][0]
		title = uploadedList[i][1]
		thumbnail = get_match_file_by_date(thumbnailList, date)
		movie = get_match_file_by_date(movieList, date)
		print_movie(title, thumbnail, movie)
	print_footer()

if __name__ == '__main__':
	main()
