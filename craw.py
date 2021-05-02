import dload
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import random
import category
import os
 
 
def main():
    base = "https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q="
    if not os.path.exists('./imgs'):
        os.makedirs('./imgs')

    for items in get_category():
        item = items.split(", ")
        for i in item : 
            url = base + '"' + i + '"'
            get_img(url)

def get_img(url):
    driver = webdriver.Chrome('./chromedriver') # 웹드라이버 파일의 경로
    driver.get(url)
    req = driver.page_source
    
    soup = BeautifulSoup(req, 'html.parser')
    
    thumbnails = soup.select("#imgList > div > a > img")
    # 크롬에서 가져오고 싶은 이미지 오른쪽 클릭
    # 검사 -> 개발자 도구에서의 선택된 부분을 오린쪽 클릭
    # copy -> copy selector 를 하여 복사된 정보에서 중복을 삭제
    count = 0 
    for thumbnail in thumbnails:    # 해당 페이지의 이미지들의 태그들을 모두 가져옴
        src = thumbnail["src"]    # 가져온 태그 정보중에 src만 가져옴
        fname = generate_random_name()
        dload.save(src, f'./imgs/' + fname)    # 설정한 경로로 jpg파일로 다운로드
        count+=1
        if count == 3: 
            break
    
    driver.quit() # 끝나면 닫아주기
    return


def get_category():
    cat = category.imagenet_catecory.values()
    return cat

def generate_random_name(format = '.png'):
    chr_list = [chr(alpha) for alpha in range(97, 123)]
    fname = ''.join(random.sample(chr_list, 10)) + format
    return fname


if __name__ == "__main__":
    main()
