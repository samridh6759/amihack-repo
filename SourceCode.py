#LIFELINE

import pickle
import numpy as np
from tkinter import*
import sqlite3 as sql
import tkinter.messagebox
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
from numpy import vstack
import sys


global_main_name1,global_main_name2 = "",""

sys.setrecursionlimit(10000)

def create_table():
	try:
		c.execute("CREATE TABLE patient(pname text, password text)")
		conn.commit()
	except:
		pass




def create_table2():
	try:
		c.execute("""CREATE TABLE patient2(survival text,
					age text, pericardial text, fractional text, epss text, lvdd text,
					wallmotion_score text, wallmotion_index text,name text)""")
		conn.commit()
	except:
		pass



def main_window(window,a):
	global global_main_name1,global_main_name2
	user_name_disp = ""


	font = ("Helvetica",15)
	print(a,"value of name")
	name_label_disp = Label(window,text=f"Enter Cardiovascular characterstics below : ",font=('Helvetica',20),bg='#%02x%02x%02x' % (255, 102, 102),fg="white",relief = "flat")
	name_label_disp.place(x=50,y=50)
	survival_var = StringVar()


	age_var = StringVar()
	pericardial_var = StringVar()
	fractional_var = StringVar()


	epss_var = StringVar()
	lvdd_var = StringVar()
	wallmotion_score_var=StringVar()
	wallmotion_index_var = StringVar()


	def how_to_use():
		tkinter.messagebox.showinfo("How to use","""Every year about a million patients suffering from some cardiovascular disease die after there treatment due to relapse of the disease or post-treatment complications.
These relapses or post-treatment complications can be prevented if detected earlier and can be easily treated and save patients life.
However it is very difficult for doctors to predict whether a patient will suffer from these relapses or post-treatment complications since it is something that requires decades of data and experience.

LifeLine is an application which uses Supervised Machine Learning algorithm (Logisitc Regression) in order to predict whether a patient suffering from cardiovascular disease can face relapses of disease or post-treatment complications in the following years of his/her treatment.
This application will help doctors to detect such complications or chances of relapse even before there symptoms start to show up and thus saving patients life.
""")


	def about_me():

		tkinter.messagebox.showinfo("About us","This is application is developed by Samridh Srivastava  ")

	def check():


		x_arr = np.array([[float(survival_var.get()),float(age_var.get()),
				float(pericardial_var.get()),float(fractional_var.get()),
				float(epss_var.get()),float(lvdd_var.get()),
				float(wallmotion_score_var.get()),float(wallmotion_index_var.get())]])

		l=['survival','age','pericardialeffusion','fractionalshortening','epss','lvdd','wallmotion-score','wallmotion-index']
		data=pd.read_csv('lifeline.csv')
		data=data.dropna(axis='rows')
		X=data[l]
		y=data['aliveat1']
		logistic_reg=LogisticRegression()
		X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4,random_state=101)
		logistic_reg=LogisticRegression()
		logistic_reg.fit(X_train,y_train)
		m=logistic_reg.score(X_test,y_test)
		prediction=logistic_reg.predict(x_arr)
		prediction_state=''
		if prediction==[0.]:
			print(prediction)
			prediction_state="POSITIVE"
			summary="On the basis of given data the patient has a good chances \nof having a relapse of the disease as well as suffering from\n post-treatment ailments\nFurther Medical attention and care is required\n"
		else:
			prediction_state="NEGATIVE"
			summary="On the basis of given data the patient has a lower chances \nof having a relapse of the disease as well as suffering from\n post-treatment ailments\nFurther Medical attention and care is not required\n"
		prex_lbl = Label(window,text=prediction_state,relief = "flat",bg='#FF0000',font=('Helvetica',30),fg="white")
		prex_lbl.place(x=1100,y=170)
		sum_lbl= Label(window,text=summary,relief = "flat",bg='#FF0000',font=('Franklin Gothic Demi Cond',15),fg="white")
		sum_lbl.place(x=775,y=375)
	create_table2()
	c.execute("SELECT * FROM patient2 ")
	patient2_d = c.fetchall()
	print(patient2_d)
	all_data = []
	all_data_l1 = []
	for i in patient2_d:
		if i[-1] == a:
			all_data_l1.append(i)
	if len(all_data_l1) >=1:
		all_data = all_data_l1[-1]
	survival_l = Label(window,text="Time passed since Treatment",relief = "flat",bg='#%02x%02x%02x' % (255, 102, 102),font=font,fg="white")
	survival_e = Entry(window,textvariable=survival_var,bg='#%02x%02x%02x' % (203, 203, 211),relief = "flat",font=font)
	survival_l.place(x=50,y=200)
	survival_e.place(x=400,y=200)




	age_l = Label(window,text="Age of the patient",relief = "flat",bg='#%02x%02x%02x' % (255, 102, 102),font=font,fg="white")
	age_e = Entry(window,textvariable=age_var,bg='#%02x%02x%02x' % (203, 203, 211),relief = "flat",font=font)
	age_l.place(x=50,y=250)
	age_e.place(x=400,y=250)






	pericardial_l = Label(window,text="Pericardial",relief = "flat",bg='#%02x%02x%02x' % (255, 102, 102),font=font,fg="white")
	pericardial_e = Entry(window,textvariable=pericardial_var,bg='#%02x%02x%02x' % (203, 203, 211),relief = "flat",font=font)
	pericardial_l.place(x=50,y=300)
	pericardial_e.place(x=400,y=300)






	fractional_l = Label(window,text="Fractional",relief = "flat",bg='#%02x%02x%02x' % (255, 102, 102),font=font,fg="white")
	fractional_e = Entry(window,textvariable=fractional_var,bg='#%02x%02x%02x' % (203, 203, 211),relief = "flat",font=font)
	fractional_l.place(x=50,y=350)
	fractional_e.place(x=400,y=350)






	epss_l = Label(window,text="E-Point to Septal Separation (EPSS) ",relief = "flat",bg='#%02x%02x%02x' % (255, 102, 102),font=font,fg="white")
	epss_e = Entry(window,textvariable=epss_var,bg='#%02x%02x%02x' % (203, 203, 211),relief = "flat",font=font)
	epss_l.place(x=50,y=400)
	epss_e.place(x=400,y=400)




	lvdd_l = Label(window,text="Left Ventricular Diastolic Dysfunction",relief = "flat",bg='#%02x%02x%02x' % (255, 102, 102),font=font,fg="white")
	lvdd_e = Entry(window,textvariable=lvdd_var,bg='#%02x%02x%02x' % (203, 203, 211),relief = "flat",font=font)
	lvdd_l.place(x=50,y=450)
	lvdd_e.place(x=400,y=450)





	wallmotion_score_l = Label(window,text="Wallmotion-score",relief = "flat",bg='#%02x%02x%02x' % (255, 102, 102),font=font,fg="white")
	wallmotion_score_e = Entry(window,textvariable=wallmotion_score_var,bg='#%02x%02x%02x' % (203, 203, 211),relief = "flat",font=font)
	wallmotion_score_l.place(x=50,y=500)
	wallmotion_score_e.place(x=400,y=500)






	wallmotion_index_l = Label(window,text="Wallmotion-index",relief = "flat",bg='#%02x%02x%02x' % (255, 102, 102),font=font,fg="white")
	

	wallmotion_index_e = Entry(window,textvariable=wallmotion_index_var,bg='#%02x%02x%02x' % (203, 203, 211),relief = "flat",font=font)
	wallmotion_index_l.place(x=50,y=550)
	wallmotion_index_e.place(x=400,y=550)
	check = Button(window,text="Submit",command=check,bg='#%02x%02x%02x' % (203, 203, 211),fg='#%02x%02x%02x' % (255, 30, 30),relief = "flat",font=font)
	

	check.place(x = 200, y=630,height=40,width=200)




	def save_f():
		
		c.execute(""" INSERT INTO patient2 VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(survival_var.get()
					,age_var.get(),pericardial_var.get(),fractional_var.get(),epss_var.get(),
					lvdd_var.get(),wallmotion_score_var.get(),wallmotion_index_var.get(),a))
		conn.commit()
		
		print(""" INSERT INTO patient2 VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')""".format(survival_var.get()
					,age_var.get(),pericardial_var.get(),fractional_var.get(),epss_var.get(),
					lvdd_var.get(),wallmotion_score_var.get(),wallmotion_index_var.get(),a))






	if len(all_data) >=1:
		survival_e.insert(0,all_data[0])
		age_e.insert(0,all_data[1])
		pericardial_e.insert(0,all_data[2])
		

		fractional_e.insert(0,all_data[3])
		epss_e.insert(0,all_data[4])
		
		lvdd_e.insert(0,all_data[5])
		wallmotion_score_e.insert(0,all_data[6])
		wallmotion_index_e.insert(0,all_data[7])






	save_btn = Button(window,command=save_f,text="SAVE",bg='red',fg='white',relief = "flat",font=('Helvetica',18))
	save_btn.place(x=1000,y=650)
	menuBar = Menu(window)
	window.config(menu=menuBar)


	subMenu = Menu(menuBar,tearoff=0 )
	subMenu = Menu(menuBar,tearoff=0)
	menuBar.add_cascade(label='help',menu=subMenu)
	subMenu.add_command(label='about us',command=about_me)
	subMenu.add_command(label='how to use', command=how_to_use)





def sign_up(window,c):
	global bgl,global_main_name1
	c.execute("SELECT * FROM patient")
	unique_check = c.fetchall()
	u_check = False

	def etc():
		nonlocal u_check
		if len(str(user_name_var.get())) <= 5:
			tkinter.messagebox.showerror("error","the username must have more than 5 characters")
		elif len(str(password_var.get())) <=5:
			tkinter.messagebox.showerror("error","the password entered must be more than 5 characters")
		else:
			for i in unique_check:
				if i[0] != user_name_var.get():

					u_check = True
			if u_check == True:



				tkinter.messagebox.showerror("error","the username is already taken")
				user_name.insert(0,"")
				password.insert(0,"")
			else:



				if password_var.get() == password_check_var.get() :
					c.execute("INSERT INTO patient VALUES('{}','{}')".format(str(user_name_var.get()),str(password_var.get())))
					conn.commit()
					c.execute("SELECT * FROM patient")
					print(c.fetchall())
					user_name_lbl.place_forget()


					user_name.place_forget()
					password_lbl.place_forget()


					password.place_forget()
					pass_btn.place_forget()
					password_check_lbl.place_forget()
					password_check.place_forget()


					bgl.place_forget()
					mainbg_lb = Label(window,image=mainbg)
					mainbg_lb.place(x=0,y=0)
					main_window(window,str(user_name_var.get()))



				else:


					tkinter.messagebox.showerror("sign up error","the passwords od not match")
					password.delete(0, END)


					password_var.set("")
					password_check.delete(0,END)
					password_check_var.set("")



	user_name_var = StringVar()

	password_var = StringVar()
	password_check_var = StringVar()
	bullet = "\u2022"
	font=("Helvetica", 13)



	window.title("Lifeline")
	user_name_lbl = Label(window,text="USERNAME: ",font=font,relief = "flat",bg='#%02x%02x%02x' % (255, 102, 102),fg="white")

	user_name = Entry(window,textvariable=user_name_var,font=font,bg='#%02x%02x%02x' % (203, 203, 211),relief = "flat")
	user_name_lbl.place(height=30,y=330,x=485)
	user_name.place(height=30,y=330,x=600,width=200)
	password_lbl = Label(window,text="PASSWORD: ",font=font,bg='#%02x%02x%02x' % (255, 102, 102),fg="white",relief = "flat")


	password = Entry(window,textvariable=password_var,font=font,show=bullet,relief = "flat",bg='#%02x%02x%02x' % (203, 203, 211))
	password_lbl.place(height=30,y=390,x=485)
	password.place(height=30,y=390,x=600,width=200 )


	password_check_lbl = Label(window,text="RE-ENTER:",font=font,bg='#%02x%02x%02x' % (255, 102, 102),fg="white",relief = "flat")
	password_check = Entry(window,textvariable=password_check_var,font=font,show=bullet,relief = "flat",bg='#%02x%02x%02x' % (203, 203, 211))
	password_check_lbl.place(height=30,y=450,x=485)


	password_check.place(height=30,y=450,x=600,width=200)
	

	pass_btn = Button(window,text="SIGN UP",command=etc,font=font,bg='#%02x%02x%02x' % (203, 203, 211),relief="flat")
	pass_btn.place(height=30,y=530,x=700,width=100)









def login(window,c):
	
	global bgl,mainbg,global_main_name2
	

	def add_user():
		user_name_lbl.place_forget()
		user_name.place_forget()
		

		password_lbl.place_forget()
		password.place_forget()
		

		pass_btn.place_forget()
		add_user_b.place_forget()
		

		sign_up(window,c)





	def etc():
		c.execute("SELECT * FROM patient")
		all_pass_data = c.fetchall()
		print(all_pass_data)
		ch_tup = (user_name_var.get(),password_var.get())
		print(ch_tup)



		if ch_tup in all_pass_data:
			user_name_lbl.place_forget()
			
			user_name.place_forget()
			password_lbl.place_forget()
			

			password.place_forget()
			pass_btn.place_forget()
			
			bgl.place_forget()
			mainbg_lb = Label(window,image=mainbg)
			

			mainbg_lb.place(x=0,y=0)
			main_window(window,user_name_var.get())



		else:
			tkinter.messagebox.showerror("Login error","Password or Username incorrect")
			user_name.delete(0, END)
			user_name_var.set("")
			password.delete(0, END)
			password_var.set("")




	user_name_var = StringVar()
	password_var = StringVar()
	

	password_check_var = StringVar()
	bullet = "\u2022"
	

	font=("Helvetica", 13)
	window.title("Lifeline")



	user_name_lbl = Label(window,text="USERNAME: ",font=font,relief = "flat",bg='#%02x%02x%02x' % (255, 102, 102),fg="white")
	user_name = Entry(window,textvariable=user_name_var,font=font,bg='#%02x%02x%02x' % (203,203,211),relief = "flat")
	user_name_lbl.place(height=30,y=350,x=485)
	user_name.place(height=30,y=350,x=600,width=200)



	password_lbl = Label(window,text="PASSWORD: ",font=font,bg='#%02x%02x%02x' % (255, 102, 102),fg="white",relief = "flat")
	password = Entry(window,textvariable=password_var,font=font,show=bullet,relief = "flat",bg='#%02x%02x%02x' % (203,203,211))
	password_lbl.place(height=30,y=450,x=485)
	password.place(height=30,y=450,x=600,width=200 )


	pass_btn = Button(window,text="Login",command=etc,font=font,bg='#%02x%02x%02x' % (203, 203, 211),relief="flat")
	pass_btn.place(height=30,y=520,x=700,width=100)
	add_user_b = Button(window,text="Sign Up",command=add_user,font=font,bg='#%02x%02x%02x' % (203, 203, 211),relief="flat")
	add_user_b.place(height=30,y=520,width=100,x=485)
	with open("checker.dat","wb") as ab: pickle.dump(True,ab)




def main():
	global bg,bgl,mainbg
	global conn,c
	conn = sql.connect('patient_data_db.db')
	c = conn.cursor()
	create_table()
	


	window = Tk()
	window.geometry("1360x720")
	mainbg = PhotoImage(file="mainbg.png")
	c.execute("SELECT * FROM patient")
	



	ch = c.fetchall()
	


	if len(ch)<=0:
		bg = PhotoImage(file="bg1.png")
		bgl = Label(window,image=bg)
		bgl.place(x=0,y=0)
		sign_up(window,c)
	


	else:
		bg = PhotoImage(file="bg1.png")
		bgl = Label(window,image=bg)
		bgl.place(x=0,y=0)
		login(window,c)
	


	window.mainloop()
if __name__ == "__main__":
	main()
