# import pandas as pd

# # Đọc file Excel (Cập nhật đường dẫn nếu cần)
# df = pd.read_excel(r"c:\Users\DUCCOMPUTER\Downloads\exercise_data.xlsx")

# # Hiển thị dữ liệu trước khi xử lý
# print("Dữ liệu ban đầu:")
# print(df)

# # 1. Xử lý ô trống trong cột "Ngày" bằng cách điền giá trị trước đó (forward fill)
# df['Ngày'] = df['Ngày'].fillna(method='ffill')

# # 2. Điền giá trị cụ thể cho mộtpyth ô nhất định (ví dụ: hàng 20, cột "Ngày")
# df.loc[20, 'Ngày'] = '2020/12/20'

# # 3. Xử lý ô trống trong cột "Lượng calo" bằng cách điền giá trị trung bình của cột
# df['Lượng calo'] = df['Lượng calo'].fillna(df['Lượng calo'].mean())

# # Hiển thị dữ liệu sau khi xử lý
# print("Dữ liệu sau khi xử lý:")
# print(df)

# # Lưu lại dữ liệu sau khi xử lý vào file mới
# df.to_excel("exercise_data_cleaned.xlsx", index=False)



#bài genk.vn
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. Gửi HTTP request đến trang web
response = requests.get("https://genk.vn/tin-ict.chn")

# 2. Kiểm tra nếu request thành công
if response.status_code == 200:
    # 3. Sử dụng BeautifulSoup để phân tích HTML
    soup = BeautifulSoup(response.content, "html.parser")

    # 4. Tìm kiếm các bài báo có thẻ h4 và class="knswli-title"
    news = soup.findAll('h4', class_='knswli-title')
    print(news)

    # Lấy link của tất cả các bài viết đó
    links = []
    for link in news:
        url = link.find('a').attrs["href"]
        links.append(url)

    # Tạo danh sách để lưu dữ liệu
    data = []

    # 5. Đối với mỗi bài báo, lấy tiêu đề, tóm tắt, nội dung, link ảnh bài viết
    for link in links:
        news = requests.get("https://genk.vn" + link)
        soup = BeautifulSoup(news.content, "html.parser")

        title = soup.find("h1", class_="kbwc-title clearfix").text
        summary = soup.find("h2", class_="knc-sapo").text
        body = soup.find("div", id="ContentDetail")

        try:
            content = body.decode_contents()
        except:
            content = ""

        try:
            image = body.find("img")["src"]
        except:
            image = ""

        item = [title, summary, content, image]
        data.append(item)

    # Lưu dữ liệu vào file Excel
    df = pd.DataFrame(data, columns=["Title", "Summary", "Content", "Image"])
    df.to_excel("news_data.xlsx", index=False)

    print("Dữ liệu đã được lưu vào news_data.xlsx")




