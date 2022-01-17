#!/opt/anaconda3/bin/python

import sys
import cgi

MOVIE_PATH = 'C:\\Users\\ykt36\\OneDrive\\ドキュメント\\VideoUploadSite\\develop\\movie\\'
THUMBNAIL_PATH = 'C:\\Users\\ykt36\\OneDrive\\ドキュメント\\VideoUploadSite\\develop\\thumbnail\\'
TITLE_PATH = 'C:\\Users\\ykt36\\OneDrive\\ドキュメント\\VideoUploadSite\\develop\\title\\'

DATA_SIZE = 10000000

# HTMLヘッダを出力
def print_header():
  print('Content-Type: text/html')
  print('')
  print('<!DOCTYPE html>')
  print('')
  print('<html lang="ja">')
  print('')
  print('<head>')
  print('  <meta charset="UTF-8">')
  print('  <meta name="description" content="file upload">')
  print('  <meta name="keywords" content="upload">')
  print('  <title>File upload</title>')
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
def save_uploaded_file(attributeName):
  formData = cgi.FieldStorage()
  fileName = formData[attributeName].filename
  if(attributeName == 'movie'):
    filePath = MOVIE_PATH + fileName
  elif(attributeName == 'thumbnail'):
    filePath = THUMBNAIL_PATH + fileName
  elif(attributeName == 'title'):
    filePath = TITLE_PATH + fileName
  else:
    print('unexpected attributeName specified.<br>')
    print_footer()
  uploadedFile = open(filePath, 'wb')
  item = formData[attributeName]
  while True:
    chunk = item.file.read(DATA_SIZE)
    if not chunk:
      break
  uploadedFile.write(chunk)
  uploadedFile.close()
  print(fileName + ' has just been uploaded.<br>')

print_header()
save_uploaded_file('movie')
save_uploaded_file('thumbnail')
save_uploaded_file('title')
print_footer()
