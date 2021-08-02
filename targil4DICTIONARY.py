'''
DICTIONARY
חיבור בין שם לערך ואחסון של זוגות שם:ערך
בדומה ספר טלפונים או רשימת כתובות מגורים עם שם:מספר
מתוארים גם כMAP וMASH TABLE
'''


#הכרזה על מילון
my_dict = {"www.google.com":"8.8.8.8","www.facebook.com":"7.7.7.7","www.youtube.com":["5.5.5.5","4.4.4.4"]}
my_dict2 = {"www.net4u.com":"33.33.33.33","www.groo.com":"88.88.88.88"}
print(my_dict)
print(my_dict2)
#{'www.google.com': '8.8.8.8', 'www.facebook.com': '7.7.7.7', 'www.youtube.com': ['5.5.5.5', '4.4.4.4']}
#{'www.net4u.com': '33.33.33.33', 'www.groo.com': '88.88.88.88'}

# הוספה על מילון
my_dict.update(my_dict2)
print(my_dict)
#{'www.google.com': '8.8.8.8', 'www.facebook.com': '7.7.7.7', 'www.youtube.com': ['5.5.5.5', '4.4.4.4'], 'www.net4u.com': '33.33.33.33', 'www.groo.com': '88.88.88.88'}

#הדפסת גודל המילון LEN
print("Number of entries: " + str(len(my_dict)))
#Number of entries: 5

# הדפסת VALUE של KEY מסויים
print(my_dict["www.google.com"])
#8.8.8.8 מדפיס את הVALUE של גוגל

# הדפסת VALUE של כל מה שיש במילון
print(my_dict.values())
#dict_values(['8.8.8.8', '7.7.7.7', ['5.5.5.5', '4.4.4.4'], '33.33.33.33', '88.88.88.88'])

#שינוי הVALUE של הKEY של GOOGLE
print(my_dict["www.google.com"])
my_dict["www.google.com"]="8.8.4.4"
print(my_dict["www.google.com"])
#8.8.8.8
#8.8.4.4
print(my_dict.values())
#dict_values(['8.8.4.4', '7.7.7.7', ['5.5.5.5', '4.4.4.4'], '33.33.33.33', '88.88.88.88'])

# הדפסת העדר או קיום KEY במילון
print("www.google.com" in my_dict)
#True  (KEY)

# הדפסת העדר או קיום VALUE במילון
print("www.google.com" in my_dict.values())
#False (VALUE)
print("8.8.4.4" in my_dict.values())
#True (VALUE)

