# username = input ("Username:")
# password = input ("Password:")

# if username == "admin":
#     if password == "admin123":
#         print("U R admin")
#     else:
#         print("wrong")
# elif username ==   "user":
#     if password== "user123":
#         print("U R user")
#     else:
#         print("wrong")
# else:
#     print("Not found")



#----------------------------------------
#รับข้อความเข้ามาโดยที่เลือกมีมจาก ig reel มีสามเงื่อนไข

# x = 10
# x += 1
# print(x)

Meme = input("Meme(ต๊ะเเหน่ว or brainrot):")
story_inside = ""
B = "เดอะมอลล์บางกะปิ"
T = "ขี้เกียจทำทุกยอย่าง"
word = ""#ให้มีค่าเท่ากับ string เปล่าๆ
if Meme == "ต๊ะเเหน่ว":
    word += "เรื่องที่ 1"
    story_inside = input("ตรงกับมีมอะไร(B เดอะมอลล์บางกะปิ , T ขี้เกียจทำทุกยอย่าง: ")
    if(story_inside == B):
        print("เดอะมอลล์บางกะปิ")
    elif(story_inside == T):
        print("ขี้เกียจทำทุกยอย่าง")
else:
    print("wrong")
        


