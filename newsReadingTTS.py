import bs4
import urllib.request as req

import pyttsx3  
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate',180)
def male(audio):
   engine.setProperty('voice',voices[1].id)
   engine.say(audio)
   engine.runAndWait()

def female(audio):
   engine.setProperty('voice',voices[0].id)
   engine.say(audio)
   engine.runAndWait()

def intro():
   print("WELCOME")
   male("WELCOME")

intro()

htp=req.urlopen("https://www.indiatoday.in")
page=bs4.BeautifulSoup(htp,features="html.parser")
a=page.find_all("div",class_="featured-post")
print("TOP HEADLINES: \n")

male("TODAY'S TOP HEADLINES")
for i in range(len(a)):
   print(a[i].text,"\n")
   female(a[i].text)


b=page.find_all("div",class_="widget-wrapper section_wise_order")
print("\n\nCATEGORIES:\n ")
male("FOLLOWING ARE THE MAJOR CATEGORIES")
for i in range(len(b)):
    c=b[i].find("span",class_="widget-title")    
    print("   {}".format(i+1),c.text,end="\n")
    

def firstcall():
   male("ENTER THE CATEGORY OF NEWS YOU WANT TO EXPLORE")
   choice=int(input("\n\nENTER THE CATEGORY OF NEWS YOU WANT TO EXPLORE:"))

   a=page.find_all("div",class_= "widget-wrapper section_wise_order")
   if choice==9:
      s=a[8].find("div",class_="tech-trip home-shows")
      s2=s.find_all("li")
      for i in range(len(s2)):
      
         print("\n\n",s2[i].text,".")
         female(s2[i].text)
   elif choice>18:
      print("Invalid Choice")
      male("PLEASE ENTER A VALID CHOICE")
      firstcall()
      
   else:
      b=a[choice-1].find_all("p")
      c=a[choice-1].find("h3")
      print(c.text)
      female(c.text)
      for i in range(len(b)):
      
         print("\n\n",b[i].text,".")
         female(b[i].text)
firstcall()
while True:
   male("FOR SOME MORE NEWS PRESS Y. IF YOU WANT TO LEAVE PRESS N.")
   flag=input("\n\nFOR SOME MORE NEWS PRESS Y .IF YOU WANT TO LEAVE PRESS N.")
   if flag=="y" or flag=="Y":
      firstcall()
   else:
      print("THANK YOU. HAVE A NICE DAY")
      female("THANK YOU. HAVE A NICE DAY")
      break
