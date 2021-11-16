import pickle
import tkinter as tk
import tkinter.messagebox
from PIL import Image, ImageTk
from Expression_posture import GetView
from Expression_posture import stopLearning
from DocumentGeneration import generateDocument
usr_name=''
usr_pwd=''
usr_info=''

import cv2
from Expression_posture import cap

flag = False
def usr_login_win():
    try:
        with open('usr_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except:
        with open('usr_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)
    def loginCheck( ):
        usr_name = var_usr_name.get()
        usr_pwd = var_usr_pwd.get()

        if usr_name in usrs_info:
            if usr_pwd == usrs_info[usr_name]:
                tk.messagebox.showinfo(title='Welcome', message='欢迎' + usr_name+'登录！')
                btn2 = tk.Button(win, width=265, image=startLearning_photo, compound=tk.CENTER, bg='#FFFFFF',
                                 relief='flat', command=GetView)

                btn2.place(x=210, y=330)
                stopLabel = tk.Label(win, text='注:开始学习后输入q字母退出学习', font=('Bold', 13), fg='#5B0261',
                                        bg='#FFFFFF')
                stopLabel.place(x=210,y=380)
                # stop_learning = tk.Button(win, width=265, image=startLearning_photo, compound=tk.CENTER, bg='#FFFFFF',
                #                  relief='flat', command=stopLearning)
                # stop_learning.place(x=210,y=300)
                btn3.place_forget()
                btn4.place_forget()
                window_login.destroy()
            else:
                tk.messagebox.showerror(message='ERROR!')
        # 用户名密码不能为空
        elif usr_name == '' or usr_pwd == '':
            tk.messagebox.showerror(message='用户名不能为空！')
    window_login = tk.Toplevel(win)
    window_login.title('login')
    window_login.geometry('400x300')
    background = tk.Label(window_login, image=login_bg_photo, compound=tk.CENTER, relief='flat')
    background.pack()
    tk.Label(window_login, text='账户：',font=("Bold",11),fg='#707070',bg='#FFFFFF').place(x=100, y=100)
    tk.Label(window_login, text='密码：',font=("Bold",11),fg='#707070',bg='#FFFFFF').place(x=100, y=140)
    var_usr_name = tk.StringVar()
    var_usr_pwd = tk.StringVar()

    enter_usr_name = tk.Entry(window_login, textvariable=var_usr_name,font=('Arail',15),width=20,relief='groove',bd=2)
    enter_usr_name.place(x=160, y=100)


    enter_usr_pwd = tk.Entry(window_login, textvariable=var_usr_pwd, show='*',font=('Arail',15),width=20,relief='groove',bd=2)
    enter_usr_pwd.place(x=160, y=140)
    btn_login = tk.Button(window_login, image=login_photo, compound=tk.CENTER, bg='#FFFFFF', relief='flat',
                     command=lambda: [loginCheck()])

    #btn_login = tk.Button(window_login, text="login", width=10, height=2, command=loginCheck)
    btn_login.place(x=100, y=200)

    #btn2 = tk.Button(win,text = '开始学习',width=20,height=2,font=("Bold", 10))
    #btn2.place(x=50,y=300)



    #判断
    #loginCheck(usr_name,usr_pwd,usrs_info)


    # if usr_name == 'aa' and usr_pwd =='111':
    #     tk.messagebox.showinfo(title='Welcome', message='###' + usr_name)
    #
    # else:
    #     tk.messagebox.showerror(message='ERROR!')




def usr_sign_window():
    def signtowcg():
        NewName = new_name.get()
        NewPwd = new_pwd.get()
        ConfirPwd = pwd_comfirm.get()
        receiveEmail = receive_email.get()
        try:
            with open('usr_info.pickle', 'rb') as usr_file:
                exist_usr_info = pickle.load(usr_file)
        except FileNotFoundError:
            exist_usr_info = {}
        if NewName in exist_usr_info:
            tk.messagebox.showerror(message='用户名存在！')
        elif NewName == '' and NewPwd == '':
            tk.messagebox.showerror(message='用户名和密码不能为空！')
        elif NewPwd != ConfirPwd:
            tk.messagebox.showerror(message='密码前后不一致！')
        else:
            exist_usr_info[NewName] = NewPwd

            with open('usr_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
                tk.messagebox.showinfo(message='注册成功！')
                window_sign_up.destroy()
    #注册界面自定义函数
    def close_regWin():
        window_sign_up.destroy()

    # 新建注册窗口
    window_sign_up = tk.Toplevel(win)
    sw = window_sign_up.winfo_screenwidth()  # 得到屏幕宽度
    sh = window_sign_up.winfo_screenheight()  # 得到屏幕高度

    ww = 500
    wh = 400

    # 窗口宽高为100
    x = (sw - ww) / 2
    y = (sh - wh) / 2
    window_sign_up.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

    #注册页面背景设置
    window_sign_up.overrideredirect(False)
    register_background = tk.Label(window_sign_up, image=register_bg_photo, compound=tk.CENTER, relief='flat')
    register_background.pack()

    #关闭窗口按钮
    # reg_close = tk.Button(window_sign_up,image=close_photo, relief='flat',command=close_regWin,compound=tk.CENTER,bd=0)
    # reg_close.place(x=475,y=1)

    # 注册编辑框
    new_name = tk.StringVar()
    new_pwd = tk.StringVar()
    pwd_comfirm = tk.StringVar()
    receive_email = tk.StringVar()

    tk.Label(window_sign_up, text='账户名：',font=('Bold',11),fg='#707070',bg='#FFFFFF').place(x=110, y=50)
    enter_new_name=tk.Entry(window_sign_up, textvariable=new_name,font=('Arail',15),width=20,relief='groove',bd =2)
    enter_new_name.place(x=190,y=50)

    tk.Label(window_sign_up, text='密码：',font=('Bold',11),fg='#707070',bg='#FFFFFF').place(x=110, y=100)
    enter_new_pwd=tk.Entry(window_sign_up, textvariable=new_pwd, show='*',font=('Arail',15),width=20,relief='groove',bd =2)
    enter_new_pwd.place(x=190,y=100)

    tk.Label(window_sign_up, text='确认密码：',font=('Bold',11),fg='#707070',bg='#FFFFFF').place(x=110, y=150)
    enter_pwd_comfirm=tk.Entry(window_sign_up, textvariable=pwd_comfirm, show='*',font=('Arail',15),width=20,relief='groove',bd =2)
    enter_pwd_comfirm.place(x=190,y=150)

    tk.Label(window_sign_up,text ='注册邮箱：',font=('Bold',11),fg='#707070',bg='#FFFFFF').place(x=110,y=200)
    enter_new_email = tk.Entry(window_sign_up,font=('Arail',15),width=20,relief='groove',bd =2)
    enter_new_email.place(x=190,y=200)

    tk.Label(window_sign_up,text='收件邮箱：',font=('Bold',11),fg='#707070',bg='#FFFFFF').place(x=110, y=250)
    enter_new_email2 = tk.Entry(window_sign_up, textvariable=receive_email, font=('Arail', 15), width=20, relief='groove', bd=2)
    enter_new_email2.place(x=190, y=250)

    alert_lable1 = tk.Label(window_sign_up,text='注:完成学习后将向此邮箱发送学习状态评估报告',font=('Bold',8),fg='#5B0261',bg='#FFFFFF')
    alert_lable1.place(x=190,y=280)
    # 确认注册
    bt_confirm = tk.Button(window_sign_up,image=reg_reg_photo,compound=tk.CENTER,relief='flat',bg='#FFFFFF',bd=0, command=signtowcg)
    bt_confirm.place(x=270,y=310)




#自己创建的函数

def StopLearning():
    print("stoplearning")
    cap.release()

# def My_loginCheck( ):
#     try:
#         with open('usr_info.pickle', 'rb') as usr_file:
#             usrs_info = pickle.load(usr_file)
#     except:
#         with open('usr_info.pickle', 'wb') as usr_file:
#             usrs_info = {'admin': 'admin'}
#             pickle.dump(usrs_info, usr_file)
#     usr_name = var_usr_name.get()
#     usr_pwd = var_usr_pwd.get()
#     print(usr_name+usr_pwd)
#     print("dianji")
#     if usr_name in usrs_info:
#         if usr_pwd == usrs_info[usr_name]:
#             tk.messagebox.showinfo(title='Welcome', message='###' + usr_name)
#             btn2 = tk.Button(win, width=265, image=startLearning_photo, compound=tk.CENTER, bg='#FFFFFF',
#                              relief='flat', command=GetView)
#
#             btn2.place(x=210, y=260)
#
#             stop_learning = tk.Button(win, width=265, image=startLearning_photo, compound=tk.CENTER, bg='#FFFFFF',
#                                       relief='flat', command=stopLearning)
#             stop_learning.place(x=210, y=300)
#             btn3.place_forget()
#             btn4.place_forget()
#             # enter_usr_name.place_forget()
#             # enter_usr_pwd.place_forget()
#             # usr_name_label.place_forget()
#             # usr_pwd_label.place_forget()
#             #window_login.destroy()
#         else:
#             tk.messagebox.showerror(message='ERROR!')
#         # 用户名密码不能为空
#     elif usr_name == '' or usr_pwd == '':
#         tk.messagebox.showerror(message='用户名不能为空！')
#
#
#


#主界面内容设置
win = tk.Tk()
win.configure(bg='#FFFFFF')
sw = win.winfo_screenwidth() #得到屏幕宽度
sh = win.winfo_screenheight() #得到屏幕高度

ww = 700
wh = 465

#窗口宽高为100
x = (sw-ww) / 2
y = (sh-wh) / 2
win.geometry("%dx%d+%d+%d" %(ww,wh,x,y))
win.title("Study Supervise")


def changeBtn2State():
    print("change")
    #btn2['state'] = tk.NORMAL

def CloseWin():
    win.destroy()


#登录窗口涉及图片

login_bg_img = Image.open('UI_image/login_bg.png')
login_bg_photo = ImageTk.PhotoImage(login_bg_img)

#注册窗口涉及图片变量
register_bg_img = Image.open('UI_image/Register_bg.png')
register_bg_photo = ImageTk.PhotoImage(register_bg_img)

reg_close_img= Image.open('UI_image/close.png')
reg_close_photo= ImageTk.PhotoImage(reg_close_img)

reg_reg_img = Image.open('UI_image/register.png')
reg_reg_photo = ImageTk.PhotoImage(reg_reg_img)


# 主界面样式设置
bg_img = Image.open('UI_image/bg_img3.png')
background_img = ImageTk.PhotoImage(bg_img)

win.overrideredirect(False)


background = tk.Label(win,image=background_img,compound=tk.CENTER,relief='flat')
background.pack()

# img = Image.open('UI_image/logo1.png')
# photo = ImageTk.PhotoImage(img)
# tk.Label(win, image=photo,width=100,height=100,bd=0).place(x=300,y=60)

# close_img = Image.open("UI_image/close.png")
# close_photo = ImageTk.PhotoImage(close_img)
# btn1 = tk.Button(win,image=close_photo, font=("Bold", 10),relief='flat',command=CloseWin,compound=tk.CENTER,bd=0)
# btn1.place(x=673,y=1)



# tittle = tk.Label(win,text='Study Superivse',font=('Arial',13),bg='#FFFFFF',fg='#ADADAD')
# tittle.place(x=10,y=1)

startLearning_img = Image.open('UI_image/StartLearning.png')
startLearning_photo = ImageTk.PhotoImage(startLearning_img)

# btn2 = tk.Button(win, width=265,image=startLearning_photo,compound=tk.CENTER,bg='#FFFFFF',relief='flat' ,command=GetView)
#
# btn2.place(x=210,y=300)

login_img = Image.open('UI_image/login.png')
login_photo = ImageTk.PhotoImage(login_img)
btn3 = tk.Button(win,image=login_photo,compound=tk.CENTER,bg='#FFFFFF',relief='flat',command=lambda:[usr_login_win(),changeBtn2State()],)
btn3.place(x=165,y=330)

register_img = Image.open('UI_image/register.png')
register_photo = ImageTk.PhotoImage(register_img)
btn4 = tk.Button(win,image=register_photo,compound=tk.CENTER,bg='#FFFFFF',relief='flat',command=usr_sign_window)
btn4.place(x=400,y = 330)


# usr_name_label=tk.Label(win, text='账户：',font=("Bold",11),fg='#707070',bg='#FFFFFF').place(x=210, y=180)
# usr_pwd_label=tk.Label(win, text='密码：',font=("Bold",11),fg='#707070',bg='#FFFFFF').place(x=210, y=220)
# var_usr_name = tk.StringVar()
# var_usr_pwd = tk.StringVar()
#
# enter_usr_name = tk.Entry(win, textvariable=var_usr_name,font=('Arail',15),width=20,relief='groove',bd=2)
# enter_usr_name.place(x=270, y=180)
#
#
# enter_usr_pwd = tk.Entry(win, textvariable=var_usr_pwd,font=('Bold',15), show='*',width=20,relief='groove',bd=2)
# enter_usr_pwd.place(x=270, y=220)




win.mainloop()