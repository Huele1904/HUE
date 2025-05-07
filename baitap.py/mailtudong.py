import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender, receiver, subject, body, password):
    # Tạo message
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject

    # Thêm nội dung email
    message.attach(MIMEText(body, 'plain'))

    # Kết nối đến server Gmail
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        # Bảo mật kết nối
        server.starttls()
        server.login(sender, password)

        # Gửi email
        text = message.as_string()
        server.sendmail(sender, receiver, text)
        print(f"Email đã được gửi đến {receiver}")

        # Đóng kết nối
        server.quit()
    except Exception as e:
        print(f"Lỗi khi gửi email: {e}")

if __name__ == "__main__":
    sender_email = "nguyen.van.ro.it@gmail.com"
    # Bật xác thực 2 bước
    # Tạo App Password
    app_password = "hfjg xdrg mqkv mlnn"
    receiver_email = "test@gmail.com"
    subject = "Thông báo tự động"
    body = "Đây là email tự động được gửi từ Python. Không cần trả lời email này."

    send_email(sender_email, receiver_email, subject, body, app_password)
