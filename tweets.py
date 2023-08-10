import snscrape.modules.twitter as sntwitter
import  pandas as pd
import sys
from openpyxl.workbook import Workbook

import time
from tkinter import *
root=Tk()
root.title("tweetPY")
root.configure(bg='black')
root.resizable(width=False, height=False)
root.geometry('800x600')

my_name = StringVar()

#===========================lable=========================
l1=Label(root,text="term")
l1.grid(row=0,column=0)

l2=Label(root,text="hashtag example:#tree")
l2.grid(row=0,column=2)

l3=Label(root,text="like Count")
l3.grid(row=1,column=0)

l4=Label(root,text="replies Count")
l4.grid(row=1,column=2)

l5=Label(root,text="retweet Count")
l5.grid(row=2,column=0)

l6=Label(root,text="since example:2020-12-31")
l6.grid(row=2,column=2)

#===========================entry=========================
termT=StringVar()
e1=Entry(root,textvariable=termT)
e1.grid(row=0,column=1)

hashtagT=StringVar()
e2=Entry(root,textvariable=hashtagT)
e2.grid(row=0,column=3)

replies=StringVar()
e3=Entry(root,textvariable=replies)
e3.grid(row=1,column=1)

likes=StringVar()
e4=Entry(root,textvariable=likes)
e4.grid(row=1,column=3)

retweets=StringVar()
e5=Entry(root,textvariable=retweets)
e5.grid(row=2,column=1)

since=StringVar()
e6=Entry(root,textvariable=since)
e6.grid(row=2,column=3)




# termT=""
# hashtagT=""
# replies=""
# likes=""
# retweets=""
# since="" #2020-12-31 format

tweetData=[]
tweetUserName=[]
tweetContent=[]
tweetHashtag=[]
retweetCount=[]
likeCount=[]
limits=1000

#
#
def print_my_name():

    query = str(termT.get())+" "+"("+str(hashtagT.get())+")"+' '+ "min_replies:"+str(replies.get())+" "+"min_faves:"+str(likes.get())+" "+"min_retweets:"+str(retweets.get())+" "+ "since:"+str(since.get())
    # str(termT.get()) +" "+ str(hashtagT.get())+" " +"min_replies:"+str(replies.get())+ " " +"min_faves:"+ str(likes.get())+" "+ "min_retweets:"+str(retweets.get()) +" "+"lang:fa"+" " + "since:"+str(since.get())

    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        # print(vars(tweet))
        if len(tweetUserName) == limits:
            break
        else:
            tweetData.append(str(tweet.date))
            tweetUserName.append(tweet.user.username)
            tweetContent.append(tweet.content)
            tweetHashtag.append(tweet.hashtags)
            retweetCount.append(tweet.retweetCount)
            likeCount.append(tweet.likeCount)

    timer = str(time.time())
    tweeter = {"tweetData": tweetData, "user": tweetUserName, "tweet": tweetContent, "hashtags": tweetHashtag,
               "like": likeCount, "retweets": retweetCount}

    my_name.set("فایل با فرمت اکسل آماده شد")
    data = pd.DataFrame.from_dict(tweeter, orient="index")
    data = data.transpose()
    writer = pd.ExcelWriter(f"twitter{termT.get()}{timer}.xlsx")
    data.to_excel(writer)
    writer.save()
    print(query)



btn = Button(root, text="کلیک کنید و سپس 2 دقیقه منتظر بمانید!", command=lambda: print_my_name())
btn.place(x=80, y=200)
label = Label(root, textvariable=my_name)
label.place(x=10,y=50)
root.mainloop()