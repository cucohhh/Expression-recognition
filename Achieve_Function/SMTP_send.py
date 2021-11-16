import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText





def SMTPSend():
    # 设置smtplib所需的参数
    # 下面的发件人，收件人是用于邮件传输的。
    smtpserver = 'smtp.qq.com'
    username = '2412504688@qq.com'
    password = 'ykomnbrjuwmedjii'
    sender = '2412504688@qq.com'
    # receiver='XXX@126.com'
    # 收件人为多个收件人
    receiver = ['2412504688@qq.com']

    subject = '学习状态报告'
    # 通过Header对象编码的文本，包含utf-8编码信息和Base64编码信息。以下中文名测试ok
    # subject = '中文标题'
    # subject=Header(subject, 'utf-8').encode()

    # 构造邮件对象MIMEMultipart对象
    # 下面的主题，发件人，收件人，日期是显示在邮件页面上的。
    msg = MIMEMultipart('mixed')
    msg['Subject'] = subject
    msg['From'] = '2412504688@qq.com <2412504688@qq.com>'
    # msg['To'] = 'XXX@126.com'
    # 收件人为多个收件人,通过join将列表转换为以;为间隔的字符串
    msg['To'] = ";".join(receiver)
    # msg['Date']='2012-3-16'
    txt = MIMEText("田昊学习状态评估报告已添加至附件请查收!!!")
    msg.attach(txt)

    # 构造附件

    sendfile = open(r'C:\Users\Administrator\PycharmProjects\pythonProject\aip-python-sdk-4.15.1\a.docx', 'rb').read()
    text_att = MIMEText(sendfile, 'base64', 'utf-8')
    text_att["Content-Type"] = 'application/octet-stream'
    # 以下附件可以重命名成aaa.txt
    # text_att["Content-Disposition"] = 'attachment; filename="aaa.txt"'
    # 另一种实现方式
    text_att.add_header('Content-Disposition', 'attachment', filename='学习状态评估报告.docx')

    msg.attach(text_att)

    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com')
    # 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
    # smtp.set_debuglevel(1)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
