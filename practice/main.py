# import smtplib
#
# my_email = "zhiyuzhong666@gmail.com"
# password = "qlvuidfyhysbxgol"
#
# with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
# # connection.starttls() # 保密协议，防止邮件被别人拦截时读取邮件内容  # 文档说有上面这句就不用写这句
#     connection.login(user=my_email,password=password)
#     connection.sendmail(from_addr=my_email,
#                     to_addrs="zhiyu@myyahoo.com",
#                     msg="Subject:Hello\n\n This is the body of my email.Could you get my email ??? it is me!! have a nice day!! ")

# ___________________________________-2__________________________________
# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# # 计算机计数从0开始，即 0表示星期一，1表示星期二
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1998,month=10,day=28,hour=8)
# print(date_of_birth)

# ___________________________________-3__________________________________
import smtplib
import datetime as dt
import random

my_email = "zhiyuzhong666@gmail.com"
password = "qlvuidfyhysbxgol"

now = dt.datetime.now()
weekday = now.weekday()
# print(weekday)
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        print(all_quotes)
        quote = random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:

        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                        to_addrs="zhiyu@myyahoo.com",
                        msg=f"Subject:Monday Motivation\n\n {quote} ")