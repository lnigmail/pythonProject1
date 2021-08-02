##Lists
#כמו מחרוזות
# מאחסנות בתוכן רצף של איברים (מחרוזות, מספרים, שברים וכו') במקום תווים

#הכרזה על רשימה והמרה
new_list=[]
print(new_list)
print(type(new_list))

new_list2=list()
print(type(new_list2))

#בניית רשימה
new_list=[2,6.6,"Dudu",[]]
print(new_list)

#חיבור רשימות
new_list2=new_list+[77]
print(new_list2, 'Dudu')
new_list3=new_list2+new_list
print(new_list3)

#הכפלת רשימות
new_list3=new_list2*2
print(new_list3)
#הכפלת רשימה
new_list2 = new_list*2
print(new_list2)

#כדי להדפיס תא ספציפי
new_list=[2,6.6,"leny",[44]]
print(new_list[0])
print(new_list[2])

#הכרזה על רשימה והמרה
my_list= [1,2,47,6.6,"Dudu"]
print("My name: " + my_list[4])
print("My Age is: " + str(my_list[2]))

#הכרזה על רשימה והמרה
#ניתן ליצור או לפי השורה העליונה או התחתונה
# (את השורה התחתונה בד"כ בשביל להמיר
#למשל כפי שממירים מINT לSTR ולהיפך )
my_list1 = []
my_list2 = list()

my_list= [1,2,47,6.6,"Dudu"]
print("My Age is: " + str(my_list[2]))

#בניית רשימה ממחרוזת

#להמיר מחרוזת (STRING) ל תאים ברשימה (LIST)
#['1', '2', '3', '4', '5', '6', '7']
my_list2 = list("1234567")
print(my_list2)

#בניית מחרוזת מרשימה
# להמיר בחזרה את הנ"ל מ(LIST) ל(STRING)
#1234567
my_string = ''.join(my_list2)
print(my_string)

#ניתן להוסיף בין הגירשיים תו שיכנס בין כל תו במחרוזת
#1A2A3A4A5A6A7
my_string = 'A'.join(my_list2)
print(my_string)

#המרת מחרוזת לרשימה (כלומר להכניס את המחרוזת לתא אחד בלבד ברשימה)
#['1A2A3A4A5A6A7']
my_list3 = my_string.split()
print(my_list3)

# # אלא אם כן יש רווחים בmy_string ואז יפצל בכל זאת כל רווח בתא בפני עצמו
#['Hello', 'idan,', 'How', 'are', 'you?']
my_string="Hello idan, How are you?"
my_list3=my_string.split()
print(my_list3)

#ניתן לפצל גם לפי שורות n\
#['Hello idan ', 'How are you?']
my_string="Hello idan \nHow are you?"
my_list3=my_string.splitlines()
print(my_list3)

#שימוש בLEN לתאר את אורך הרשימה
#The length is: 6
my_list= ["hello",1,6.6,"Dudu",55,7]
print("The length is: " + (str(len(my_list))))

# לא לשכוח גרשיים
#The length is: 19
my_str="1234567890123456789"
print("The length is: " + (str(len(my_str))))

#שימוש בAPPEND בכדי להוסיף ערך לסוף של הרשימה
#['hello', 1, 6.6, 'Dudu', 55, 7, 'wow', 'Dudu']
#The new length is: 8
my_list.append("wow")
my_list.append("Dudu")
print(my_list)
print("The new length is: " + (str(len(my_list))))

#נשתמש בinsert אם נרצה להוסיף עד 2 ערכים לרשימה במקום מסוים
# יש להמנע מפעולה זו מכיוון שהיא פוגעת בביצועים
#נוסף לתא מספר 7 ['hello', 1, 6.6, 'Dudu', 55, 7, 'wow', 'net4u', 'Dudu']
my_list.insert(7,'net4u')
print(my_list)

# ההיפך מפוש - נשתמש בpop בכדי להוציא ערך מסוף הרשימה
# תמיד כדאי להוציא/להוסיף ערך לסוף הרשימה כדי לא לפגוע בביצועים
my_list.pop()
print(my_list)

# ההיפך מפוש - נשתמש בpop בכדי להוציא ערך ממיקום ספציפי ברשימה
# תמיד כדאי להוציא/להוסיף ערך לסוף הרשימה כדי לא לפגוע בביצועים
#[1, 6.6, 'Dudu', 55, 7, 'wow', 'net4u'] תא0 ציין את תחילת הרשימה ולכן המילה "הלו" הראשונה הוסרה
my_list.pop(0)
print(my_list)

#נבדוק שערך קיים ברשימה
#True
my_list=["google", "facebook", "ebay", "apple"]
print("ebay" in my_list)
#False
my_list=["google", "facebook", "ebay", "apple"]
print("net4u" in my_list)
