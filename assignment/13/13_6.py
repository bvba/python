import urllib.request

wordCnt = 0     # 단어의 개수 count
file = urllib.request.urlopen("http://cs.armstrong.edu/liang/data/Lincoln.txt")
# 웹에 있는 파일을 불러온다

line = '.'  # do while 을 위한 설정
while line != '' :  # 파일의 끝까지 line을 읽음
    line = file.readline().decode()
    lst = [x for x in line.split(' ') if x != '' and x != '\r\n' and x!= '--']
    # line을 ' ' 단위로 분리하고, '', '--', 줄바꿈이 아닌 경우에만 lst에 추가
    wordCnt += len(lst)
    # 리스트의 개수만큼 단어의 수 count
file.close()

print(wordCnt)  # 단어의 개수 출력
