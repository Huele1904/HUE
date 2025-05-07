import requests
from bs4 import BeautifulSoup
import pandas as pd

def crawl_24h_news():
    url = "https://www.24h.com.vn/tin-tuc-cong-nghe-c453.html"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Không thể truy cập trang web")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    articles = soup.find_all("div", class_="box26")  # Thay đổi tùy theo cấu trúc trang web
    data = []
    
    for article in articles:
        title = article.find("a").text.strip() if article.find("a") else ""
        summary = article.find("span").text.strip() if article.find("span") else ""
        link = article.find("a")["href"] if article.find("a") else ""
        
        # Lấy nội dung bài viết
        news_response = requests.get(link, headers=headers)
        news_soup = BeautifulSoup(news_response.text, "html.parser")
        content_div = news_soup.find("div", class_="news-content")  # Thay đổi tùy theo trang
        content = content_div.decode_contents() if content_div else ""
        
        # Lấy ảnh trong bài viết
        try:
            image = content_div.find("img")["src"] if content_div and content_div.find("img") else ""
        except:
            image = "https://cdn.24h.com.vn/upload/1-2025/images/2025-03-19/255x170/ax-6-1280x720-1726551438-684-width740height495-1742356286-991-width740height495.jpg"
        
        data.append([title, summary, content, image])
    
    # Lưu dữ liệu vào file Excel
    df = pd.DataFrame(data, columns=["Title", "Summary", "Content", "Image"])
    df.to_excel("24h_news_data.xlsx", index=False)
    
    print("Dữ liệu đã được lưu vào 24h_news_data.xlsx")

if __name__ == "__main__":
    crawl_24h_news()
