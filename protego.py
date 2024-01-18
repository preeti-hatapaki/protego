import mysql.connector 
import plotly.express as px
import datetime
import plotly
import pandas as pd
import requests  
from bs4 import BeautifulSoup
import plyer
from tkinter import *
from tkinter import messagebox,filedialog
con=mysql.connector.connect(host="localhost",user="root",password='root',database='myrun')
cur=con.cursor()
n=5
def Map():
    covids='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series
/time_series_covid19_confirmed_global.csv'   
    covs='C:/Users/Admin/Documents/Documents/summarymohfw1updated.csv'
    print("###################")
    print(" COVID-19 MAPPING")
    print("###################")
    print("Which type of map would you like to view?")
    print("1. Worldwide")
    print("2. Statewise")
    print("3. Both")
    ch=int(input("Enter your choice:"))
    df=pd.read_csv(covids)
    db=pd.read_csv(covs)
    da=datetime.datetime.now()
    def WorWid():
        fig=px.density_mapbox(df,lat='Lat',lon='Long',z=h,radius=30,center=dict(lat=9,lon=9),
                zoom=3,opacity=0.8,hover_name=h,
                color_continuous_scale=px.colors.diverging.BrBG,
                mapbox_style='stamen-terrain',
                title='Covid-19 Mapping(22/1/20-The Day Before Present)(Worldwide)')
        fig.show() 
        plotly.offline.plot(fig,filename='E:\map_exp.html',auto_open=True)
    def StatWid():
        fin=px.density_mapbox(db,lat='Lat',lon='Long',z=p,radius=30,center=dict(lat=9,lon=9),
                      zoom=3,opacity=0.8,hover_name=p,hover_data=['States/Uts'],
                      color_continuous_scale=px.colors.diverging.BrBG,
                      mapbox_style='stamen-terrain',
                      title='Covid-19 Mapping(Statewise)(New cases)')
        fin.show()    
        plotly.offline.plot(fin,filename='E:\map_exxp.html',auto_open=True)
    if ch==1:
        print("To display Covid-19 map(Worldwide):-")
        print("Enter according to the range:22/1/20-the day before present(",
        da.strftime("%d-%m-%y"),")")
        print("Enter the day:",end="")
        d=int(input())
        print("Enter the month(1-12):",end="")
        m=int(input())
        print("Enter the year(20-",da.strftime("%y"),"):",end="")
        y=int(input())
        h=str(m)+'/'+str(d)+'/'+str(y)
        WorWid()
    elif ch==2:
        print("To display Covid-19 map(Statewise):-")
        print("Enter according to the range:03-01-22 - 16-01-22")
        print("Enter the day:",end="")
        dd=int(input())
        p='1-'+str(dd)+'-22'
        StatWid()
    elif ch==3:
        print("To display Covid-19 map(Worldwide & Statewise):-")
        print("Enter according to the range:03-01-22 - 16-01-22")
        print("Enter the day:",end="")
        dd=int(input())
        h='1/'+str(dd)+'/22'
        p='1-'+str(dd)+'-22'
        WorWid()
        StatWid()
    else:
        print("Oops! This is an uncompatible request")
def Graph():
    print("##############")
    print("COVID-19 GRAPH")
    print("##############")
    df = pd.read_excel('C:\protegograph\protegograph.xlsx')
    Place = df['Place']
    Cases = df['Cases']
    Date = df['Date'].dt.strftime('%Y-%m-%d')
    fig = px.bar(df,x=Place,y=Cases,color=Place,animation_frame=Date,animation_group=Place,range_y=[0,8000000])
    plotly.offline.plot(fig,filename='protegograph.html')
def Track():
    print("###############")
    print("COVID-19 TRACKER")
    print("###############")
    def datacollected():
        def notification(title, message):
            plyer.notification.notify(title= title,message= message,timeout = 15)
        url = "https://www.worldometers.info/coronavirus/"
        res = requests.get(url)
        soup = BeautifulSoup(res.content,'html.parser') 
        tbody = soup.find('tbody')
        abc = tbody.find_all('tr')
        countrynotification = cntdata.get()
        if(countrynotification == ""):
            countrynotification = "world"
        serial_number,countries , total_cases , new_cases , total_death , new_deaths, total_recovered,active_cases = [],[],[],[],[],[],[],[]
        serious_critical , total_cases_permn, total_deaths_permn, total_tests, total_test_permillion, total_pop = [],[],[],[],[],[]
        header = ['serial_number','countries' , 'total_cases' , 'new_cases' , 'total_death' , 'new_deaths', 'total_recovered','active_cases',
            'serious_critical' , 'total_cases_permn', 'total_deaths_permn', 'total_tests', 'total_test_permillion', 'total_pop' ]
        for i in abc:
             id = i.find_all('td')
             if(id[1].text.strip().lower() == countrynotification):
                 totalcases1 = int(id[2].text.strip().replace(',',""))
                 totaldeath = id[4].text.strip()
                 newcases = id[3].text.strip()
                 newdeaths = id[5].text.strip()
                 notification("CORONA RECENT UPDATES OF  {}".format(countrynotification),"Total Cases : {}\nTotal Deaths : {}\nNew Cases : {}\nNew Deaths : {}".format(totalcases1,totaldeath,newcases,newdeaths))
             serial_number.append(id[0].text.strip())
             countries.append(id[1].text.strip())
             total_cases.append(id[2].text.strip().replace(',',""))
             new_cases.append(id[3].text.strip())
             new_deaths.append(id[5].text.strip())
             total_death.append(id[4].text.strip())
             total_recovered.append(id[6].text.strip())
             active_cases.append(id[7].text.strip())
             serious_critical.append(id[8].text.strip())
             total_cases_permn.append(id[9].text.strip())
             total_deaths_permn.append(id[10].text.strip())
             total_tests.append(id[11].text.strip())
             total_test_permillion.append(id[12].text.strip())
             total_pop.append(id[13].text.strip())
        dataframe = pd.DataFrame(list(zip(serial_number,countries , total_cases , new_cases , total_death , 
                    new_deaths, total_recovered,active_cases,
                    serious_critical , total_cases_permn, total_deaths_permn, total_tests, total_test_permillion, 
                    total_pop)),columns=header)
        sorts = dataframe.sort_values('total_cases',ascending = False)
        for a in flist:
            if (a == 'html'):
                path2 = '{}/coronadata.html'.format(path)
                sorts.to_html(r'{}'.format(path2))
            if (a == 'json'):
                path2 = '{}/coronadata.json'.format(path)
                sorts.to_json(r'{}'.format(path2))
            if (a == 'csv'):
                path2 = '{}/coronadata.csv'.format(path)
                sorts.to_csv(r'{}'.format(path2))
            if(len(flist) != 0):
                messagebox.showinfo("Notification","Corona Record is saved {}".format(path2),parent =coro)
    def downloaddata():
        global path
        if(len(flist) != 0):
            path = filedialog.askdirectory()
        else:
            pass
        datacollected()
        flist.clear()
        Inhtml.configure(state = 'normal')
        Injson.configure(state = 'normal')
        Inexcel.configure(state = 'normal')
    def inhtmldownload():
        flist.append('html')
        Inhtml.configure(state = 'disabled')
    def injsondownload():
        flist.append('json')
        Injson.configure(state = 'disabled')
    def inexceldownload():
        flist.append('csv')
        Inexcel.configure(state = 'disabled')
    coro = Tk()
    coro.title("Covid-19 Tracker and Notifications")
    coro.geometry('800x500+200+80')
    coro.configure(bg='#556B2F')
    flist = []
    path = ''
    mainlabel = Label(coro,text="Corona Virus Live Tracker",font=("new roman",30,"italic bold"), bg = "#FF8C00",width=33
                        ,fg = "black",bd=5)
    mainlabel.place(x=0,y=0)
    label2 = Label(coro,text="Download File in ",font=("arial",20,"italic bold"), bg = "#556B2F")
    label2.place(x=15,y=200)
    cntdata = StringVar()
    entry1 = Entry(coro,textvariable = cntdata ,font = ("arial",20,"italic bold"), relief = RIDGE,bd = 2 , width = 32)
    entry1.place(x = 280, y = 100)
    Inhtml = Button(coro,text = "Html", bg = "#2DAE9A", font = ("arial",15,"italic bold"),relief = RIDGE,activebackground = "#05945B",
                activeforeground = "white",bd = 5,width = 5,command = inhtmldownload)
    Inhtml.place(x = 300, y = 200)
    Injson = Button(coro,text = "json", bg = "#2DAE9A", font = ("arial",15,"italic bold"),relief = RIDGE,activebackground = "#05945B",
                activeforeground = "white",bd = 5,width = 5,command = injsondownload)
    Injson.place(x = 300, y = 260)
    Inexcel = Button(coro,text = "Excel", bg = "#2DAE9A", font = ("arial",15,"italic bold"),relief = RIDGE,activebackground = "#05945B",
                activeforeground = "white",bd = 5,width = 5,command = inexceldownload )
    Inexcel.place(x = 300, y = 320)
    Submit = Button(coro,text = "Submit", bg = "#CB054A", font = ("arial",15,"italic bold"),relief = RIDGE,activebackground = "#7B0519",
                activeforeground = "white",bd = 5,width = 25,command = downloaddata)
    Submit.place(x = 450, y = 260)
    coro.mainloop()
def  Quiz():
    print("################")
    print("COVID-19 MCQ QUIZ")
    print("################")
    score = 0
    answer1 = input ("Where was Covid-19 first detected? \na. INDIA \nb. CHINA \nc.TURKEY  \nAnswer: ")
    if  answer1== "b" or answer1 =="CHINA":
        score  += 1
        print ("Correct!")
        print ("Score: ", score)
        print("\n")
    else:
        print ("Incorrect! The answer is CHINA.")
        print ("Score: ", score)
        print ("\n")
    answer2= input ("What can prevent us from Covid-19? \na.  SOCIAL DISTANCING \nb. WEARING MASK \nc. ALL OF THESE \nAnswer: ")
    if answer2 == "c" or  answer2 == "ALL OF THESE":
        score += 1
        print("Correct!")
        print ("Score: ", score)
        print("\n")
    else:
        print ("Incorrect! The answer is ALL OF THESE")
        print ("Score: ", score)
        print ("\n")
    answer1 = input ("What is the minimum distance to be kept from each other to avoid COVID-19? \na. 1-2m  \nb. 5-8m \nc. 1km  \nAnswer: ")
    if  answer1== "a" or answer1 =="1-2m":
        score  += 1
        print ("Correct!")
        print ("Score: ", score)
        print("\n")
    else:
        print ("Incorrect! The answer is 1-2m.")
        print ("Score: ", score)
        print ("\n")
    answer1 = input ("For how long should one be quarantine if exposed to COVID-19? \na. no need to be quarantined \nb. 14 days  \nc.14 weeks \nAnswer: ")
    if  answer1== "b" or answer1 =="14 days":
        score  += 1
        print ("Correct!")
        print ("Score: ", score)
        print("\n")
    else:
        print ("Incorrect! The answer is 14 days.")
        print ("Score: ", score)
        print ("\n")
    answer1 = input ("When was COVID-19 first reported in India? \na. 2021 \nb. 2019 \nc.2020  \nAnswer: ")
    if  answer1== "c" or answer1 =="2020":
        score  += 1
        print ("Correct!")
        print ("Score: ", score)
        print("\n")
    else:
        print ("Incorrect! The answer is 2020.")
        print ("Score: ", score)
        print ("\n")
    answer1 = input ("Where was COVID-19 first reported in India? \na. Delhi \nb. Kerala \nc. Maharashtra \nAnswer: ")
    if  answer1== "b" or answer1 =="Kerala":
        score  += 1
        print ("Correct!")
        print ("Score: ", score)
        print("\n")
    else:
        print ("Incorrect! The answer is Kerala.")
        print ("Score: ", score)
        print ("\n")
    answer1 = input ("What are the most common symptoms of Covid ? \na. Fever \nb.Cough  \nc. both a and b  \nAnswer: ")
    if  answer1== "c" or answer1 =="both a and b":
        score  += 1
        print ("Correct!")
        print ("Score: ", score)
        print("\n")
    else:
        print ("Incorrect! The answer is both a and b.")
        print ("Score: ", score)
        print ("\n")
    answer1 = input ("Which state mostly had highest number of cases of Covid in India? \na. Maharashtra \nb. Tamil Nadu \nc. Uttar Pradesh  \nAnswer: ")
    if  answer1== "a" or answer1 =="Maharashtra":
        score  += 1
        print ("Correct!")
        print ("Score: ", score)
        print("\n")
    else:
        print ("Incorrect! The answer is Maharashtra.")
        print ("Score: ", score)
        print ("\n")
    answer1 = input ("When did the 2nd wave of Coronavirus hit in India ? \na. 2019 \nb. 2020 \nc.2021  \nAnswer: ")
    if  answer1== "b" or answer1 =="2020":
        score  += 1
        print ("Correct!")
        print ("Score: ", score)
        print("\n")
    else:
        print ("Incorrect! The answer is 2020.")
        print ("Score: ", score)
        print ("\n")
    answer1 = input ("Where was Omicron (Variant of Covid-19) first detected? \na. South Africa \nb. India \nc.China  \nAnswer: ")
    if  answer1== "a" or answer1 =="South Africa":
        score  += 1
        print ("Correct!")
        print ("Score: ", score)
        print("\n")
    else:
        print ("Incorrect! The answer is South Africa.")
        print ("Score: ", score)
        print ("\n")
    answer1 = input ("Are you fully vaccinated ? \na. Yes \nb. No not yet \nAnswer: ")
    if  answer1== "a" or answer1 =="Yes":
        print ("That's GREAT! You are expected to follow all other Government guidelines too like Social distancing, etc. Keep it up.")
        print("\n")
    else:
        print ("We encourage you to get vaccinated as soon as possible. Your small action can curb the spread. You are also expected to follow all other Government guidelines too like Social distancing, etc.")
        print ("\n")
    if score <=5:
        print ("your total score is :",score," -nice try, better luck next time")
    elif score >=6:
        print ("your total score is :",score,"- you are doing great!")
print("#####################")
print("PROTEGO COVID-19 HELPDESK")
print("#####################")
print("1. Register/Forgot your credentials")
print("2. Login")
choice=int(input("Enter your choice:"))
while True:
    if choice==1:
        No=n
        Name=input("Enter your name:")
        Loginid=input("Enter your new 10-digit Login id:")
        password=input("Enter your new 6-digit password:")
        query="Insert into Log values({},'{}','{}','{}')".format(No,Name,Loginid,password)
        n+=1
        cur.execute(query)
        con.commit()
        print("Successfully inserted....!")
        print("Now you may login!")
        Log=input("Enter the Login Id:")
        pas=input("Enter your password:")
        if  Loginid==Log and  password==pas:
            print("You have successfully logged in....!")
            print("#####################")
            print("1. Maps")
            print("2. Graphs")
            print("3. Tracker")
            print("4. Quiz")
            gh=int(input("Enter your choice:"))
            if gh==1:
                Map()
            elif gh==2:
                Graph()
            elif gh==3:
                Track()
            elif gh==4:
                Quiz()
            else:
                print("Choose from the options")
            poi="Y"
            while poi=="Y" or poi=="y":
                poi=input("Do you want to view other choices?(Y/N):")
                if poi!="Y" and poi!="y":
                    print("Exiting...")
                    print("#####################")
                    break
                print("1. Maps")
                print("2. Graphs")
                print("3. Tracker")
                print("4. Quiz")
                pop=int(input("Enter  your choice:"))
                if pop==1:
                    Map()
                elif pop==2:
                    Graph()
                elif pop==3:
                    Track()
                elif pop==4:
                    Quiz()
                else:
                    print("Choose from the options")
        else:
            print("Something went wrong...Credentials not matching")
    elif  choice==2:
        print("Now you may login!")
        Log=input("Enter the Login Id:")
        pas=input("Enter your password:")
        cur.execute("Select Loginid,password from Log where Loginid='{}' and password='{}'".format(Log,pas))
        row=cur.fetchone()
        if row!=None:
            print("You have successfully logged in....!")
            print("#####################")
            print("1. Maps")
            print("2. Graphs")
            print("3. Tracker")
            print("4. Quiz")
            gh=int(input("Enter your choice:"))
            if gh==1:
                Map()
            elif gh==2:
                Graph()
            elif gh==3:
                Track()
            elif gh==4:
                Quiz()
            else:
                print("Choose from the options")
            poi="Y"
            while poi=="Y" or poi=="y":
                    poi=input("Do you want to view other choices?(Y/N):")
                    if poi!="Y" and poi!="y":
                        print("Exiting...")
                        print("#####################")
                        break
                    print("1. Maps")
                    print("2. Graphs")
                    print("3. Tracker")
                    print("4. Quiz")
                    pop=int(input("Enter  your choice:"))
                    if pop==1:
                        Map()
                    elif pop==2:
                        Graph()
                    elif pop==3:
                        Track()
                    elif pop==4:
                        Quiz()
                    else:
                        print("Choose from the options")
        else:
            print("Something went wrong...Credentials not found")
    else:
        print("Choose from the options")
