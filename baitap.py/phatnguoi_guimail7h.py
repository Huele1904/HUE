import schedule
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
from bs4 import BeautifulSoup

# Hàm kiểm tra phạt nguội (giả sử bạn có một URL hoặc API)
def kiem_tra_phat_nguoi():
    url = 'https://example.com/check-fine'  # Thay bằng URL chính thức
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Giả sử phạt nguội là trong một thẻ có class 'fine-info'
        fine_info = soup.find(class_='fine-info')
        if fine_info:
            return fine_info.text.strip()
        else:
            return 'Không có phạt nguội.'
    else:
        return 'Lỗi kết nối với trang web.'

# Hàm gửi email
def gui_email(noi_dung):
    sender_email = "your_email@example.com"  # Thay bằng email của bạn
    receiver_email = "receiver_email@example.com"  # Thay bằng email người nhận
    password = "your_password"  # Thay bằng mật khẩu của bạn (hoặc sử dụng OAuth2 nếu bảo mật cao hơn)

    # Tạo nội dung email
    subject = "Thông báo phạt nguội"
    body = f"Chào bạn,\n\nThông tin phạt nguội:\n{noi_dung}\n\nChúc bạn một ngày tốt lành!"
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("Email đã được gửi thành công!")
    except Exception as e:
        print(f"Đã xảy ra lỗi khi gửi email: {e}")

# Hàm thực hiện kiểm tra và gửi email vào mỗi 7h sáng
def chay_he_thong():
    phat_nguoi = kiem_tra_phat_nguoi()
    gui_email(phat_nguoi)

# Lên lịch công việc để chạy hàng ngày vào lúc 7h sáng
schedule.every().day.at("07:00").do(chay_he_thong)

# Vòng lặp chính để theo dõi và thực hiện công việc
while True:
    schedule.run_pending()
    time.sleep(60)  # Kiểm tra mỗi phút một lần
