# Gọi thư viện schedule
import schedule
import time

# Định nghĩa hàm
def job():
    print("Huế ...")

# Lập lịch chạy tự động cứ 2 phút chạy 1 lần
schedule.every(0.001).minutes.do(job)

# # Lập lịch theo giờ, ngày, tuần nếu cần:
# schedule.every().hour.do(job)              # Mỗi giờ
# schedule.every().day.at("07:00").do(job)   # Mỗi ngày lúc 7h sáng
# schedule.every().monday.do(job)            # Mỗi thứ 2
# schedule.every().friday.at("18:00").do(job) # Thứ 6 lúc 18h

# Vòng lặp kiểm tra và chạy công việc đã được lập lịch
while True:
    schedule.run_pending()
    time.sleep(1)
