
# library


from tkinter import messagebox;
from plyer import notification ;
import smtplib as s;
import requests ;
from bs4 import BeautifulSoup;
import  tkinter as tk ; 
from tkinter import *;
import plyer ;
import pyttsx3;

# library



  

    # web scrapping scrapping
def get_html_data(url):
     data = requests.get(url);
     return data.text;

def get_corona_details_of_india():
    url="https://www.mohfw.gov.in/";
    html_data = get_html_data(url);
    bs  = BeautifulSoup(html_data,'html.parser')
    info = bs.find("div",class_="site-stats-count").find_all('strong',class_="mob-hide");
    ptr =[];
    string ="";
    for data in info:
        string = f"{data.text}";
        ptr.append(string);
    data_item=[];
    for x in ptr:   
        data_item.append(x.split());

    Data = data_item;

    str = f"""{Data[0][0]} cases are {Data[1][0]}
{Data[2][0]} cases are {Data[3][0]}
{Data[4][0]} cases are {Data[5][0]}
""" 



    return str;    

    # web scrapping scrapping

# alert for downloaded
def alerForDownloaded():
    messagebox.showinfo('Download', "Download Completed.") 


# To Download The file
path = r'C:\Users\preet\Desktop\Project\DataTrackerAppwithNotification\folder'
i =1;
def forDownloadButton():
    global i;
    global path;
    f = open(f'{path}\data{i}.txt','w');
    getData = get_corona_details_of_india();
    f.write(getData);
    print(i);
    i+=1;
    alerForDownloaded();
 


# for speaking
def speak():
    engine = pyttsx3.init();
    engine.say(get_corona_details_of_india());
    engine.runAndWait();

    # notification in windows
def notifyMe():
    plyer.notification.notify(
        title = "COVID CASES OF INDIA",
        message =  get_corona_details_of_india(),
        timeout =20,
        app_icon = 'coro.ico'
        )
    
        # notification in windows

### refreshing
def refresh():
    getNewData = get_corona_details_of_india();
    print("refreshing...");
    print(mainLabel['text']);


# alet message Box for Email button:

def alert(userEmail):
    if userEmail=="":
        messagebox.showwarning("warning","empty box");
        return True;
    for char in userEmail:
        if char == '@' :
            messagebox.showinfo("Sent","sent it succesfully");
            return False;
           
    messagebox.showerror("warning","Incorrect Email-Id !");
    return True;       

    


    
    


# giving COVID  -19 information in e-mail.

def sent(userEmail):
    doAlert=False;
    doAlert=alert(userEmail);
    if not doAlert:
        ob = s.SMTP("smtp.gmail.com",587);
        ob.starttls();
        # // put your own password and gmail so that you can check
        ob.login(put your own gmail id, gmail password); 
        # // put your own password and gmail so that you can check
        subject = "Covid-19";
        body = get_corona_details_of_india();
        message = f"""Subject: {subject}                          
        {body}
        """;
        listOfAddress = userEmail;
        print(listOfAddress);
        ob.sendmail("sahilnegi.pang",listOfAddress,message);
        ob.quit();
        print("send successfully");      
        



#### creating GUI #######
root = tk.Tk();
root.geometry("400x700");
root.iconbitmap('coro.ico');
f =("poppins",15);
root.title("CORONA DATA TRACKER - INDIA "); 
banner = tk.PhotoImage(file = "pic.png");
bannerLabel = tk.Label(root,image = banner);
bannerLabel.pack();
mainLabel = tk.Label(root,foreground ='green',text=get_corona_details_of_india(),font =f)
mainLabel.config(font=('poppins',15),pady=18);
mainLabel.pack();
lbl = Label(root,text = "Email : " ,foreground = 'white', bd =0 ,highlightbackground = "white",highlightthickness = 2, width=7  ,bg='grey',activebackground ='orange',activeforeground='white'  ,font=f, relief="solid")
lbl.place(x= 50 , y=470);

# email inputbox
userEmail = StringVar();
emailInput = Entry(root,width=20 , font =('poppins',12), textvariable = userEmail );
emailInput.place(x=160,y=470);

# function for email button
def functionforButton():
    sent(userEmail.get());

  


# refresh button
reBtn = tk.Button(root,foreground = 'white', text = "Refresh",bd=0, font = f ,bg='grey',activebackground ='orange',width=10,activeforeground='white',relief = "solid",command = refresh)
reBtn.place(x=50,y=405);

# notification button 
notification_btn = tk.Button(root,text='Notify',foreground = 'white',bd=0, highlightbackground = "white",highlightthickness = 0, width=10,bg='grey',activebackground ='orange',activeforeground='white'  ,font=f, relief="solid", command=notifyMe);
notification_btn.place(x=200,y=405);

# send button
sendEmailBtn = tk.Button(root,text='Send', bg='grey',bd=0,foreground = 'white',activebackground  ='orange',activeforeground='white',width=10,  font=f, relief="solid", command=functionforButton);
sendEmailBtn.place(x=200,y=520);

# speak button
speakBtn = tk.Button(root,text='Speak',font=f ,bd=0,relief="solid",foreground = 'white',width=10, command= speak ,bg='grey',activebackground ='orange',activeforeground='white');
speakBtn.place(x=45,y=520)

# download button
downloadBtn = tk.Button(root,text='DOWNLOAD',font=f ,bd=0,relief="solid",foreground = 'white',width=23, command= forDownloadButton ,bg='red',activebackground ='orange',activeforeground='white'); 
downloadBtn.place(x=50,y=590)
root.mainloop();    

### creating GUI #######
        
