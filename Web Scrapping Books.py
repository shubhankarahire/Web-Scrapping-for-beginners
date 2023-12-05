#!/usr/bin/env python
# coding: utf-8

# In[1]:


# request is use to connect with internet or we can say to fetch data from internet browser
import requests
# BeautifulSoup is import form bs4 to make imported content of web page more readalbe and understandable 
from bs4 import BeautifulSoup


# In[2]:


# Here we store data from web page using web address in variable page using request.get to connect with internet and get data
page = requests.get("https://books.toscrape.com/")
page  
# Response [200] means that data is fetched successfully. 
# There are various Response codes so Google respons code to know more about it


# In[3]:


# To see the data we have fetched.
page.content


# In[4]:


# Convert data into html format to make it more readble
Soup = BeautifulSoup(page.content,"html")
Soup


# In[5]:


# Here we fetch contant thorugh " id " with cantians all page data in it, also we identifie classes to work on.
body = Soup.find(id = "default")
print(body)


# In[6]:


# Here we fetch all the classes of "col-xs-6 col-sm-4 col-md-3 col-lg-3"
# We can also fetch sub classes but from vairable(body) where page id is stored.
forcast = body.find_all(class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
print(forcast)


# In[7]:


# Here we are checking content of first class("col-xs-6 col-sm-4 col-md-3 col-lg-3").
# prettify () is used to make contant more readable.
f1 = forcast[0]
print(f1.prettify())


# In[8]:


# Here we trying to fetch the book name of the first book on web page.
img = f1.find("img")
print(img)


# In[9]:


name  = img["alt"]
print(name)


# In[10]:


# Here we are fetching names of all books from sub classes "img", to do so we used list comprehension method.
# name of all books is store in list name_tags
name_tags = body.find_all("img")
name_tags = [i for i in name_tags]
name_tags = [i["alt"] for i in name_tags]
name_tags


# In[11]:


# Here we are fetching price of all books from sub classes "price_color", to do so we used list comprehension method.
price = body.find_all(class_="price_color")

price_tags = [i.get_text() for i in price]
print(price_tags)


# In[12]:


# Here we trying to fetch the book description of the first book on web page
dis = body.find("h3")

print(dis)


# In[13]:


d = dis.select_one("a").get_text()
print(d)


# In[14]:


# Here we are fetching description of all books from sub classes "h3", to do so we used list comprehension method.
dis_tags = [d.get_text() for d in body.select("h3")]
print(d)


# In[15]:


# Here we are making DataFrame to visualize data in form of table
import pandas as pd


# In[16]:


book = pd.DataFrame({
    "name":name_tags,
    "price":price_tags,
    "discription":dis_tags
})
book


# In[17]:


# Creating csv file to store above data (talbe) just don't for get add csv extention(.csv) at end of file name.
# We can also make excel by typing to_excel instead of csv just don't for get add excel(.xlsxS) extention at end of file name.

book.to_csv("Book.csv", index=False)

