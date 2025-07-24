# sum = 0
# n = 3 #เเทนจำนวนเลขที่ตั้งว่าจะให้ถึง
# for i in range(n):
#     sum += i+1
#     #rangeคือมี3ค่า 
#     # 1.start ใส่ก็ได้ไม่ใส่ก็ได้
#     # 2.stop สั่งให้หยุดก่อนถึงเลขนั้นๆ
#     #for i in range(100): อันนี้มันจะเเสดงผล1-99ไม่เเสดง100 คือตัวอย่างของข้อ2
#     # 3.step 
# print(sum)

# for i in range(10):
#     # การหารใช้ตรวจเลขคู่คี่ได้
#     if (i % 2 ) == 0:
#             print("Even number:",i)



#------------------------------------------
# print ("ตารางสูตรคูณ")
# x = int(input("ใส่ตัวเลขเข้ามา!! : "))
# for i in range(12):

#     print(x,"*",i+1," = ",x * (i+1))

#-----------------------------------------

# i = 0
# while i <= 5:
#     print("hello")
#     i += 1
#     if i == 4:
#      break
#จะเเสดงhello 4รอบ

# #--------------------------------
# start = True
# while start:
#     print("เลือกข้อที่ต้องการเล่น")
#     print("ข้อที่ 1 ")
#     print("ข้อที่ 2")
#     x = int (input("กรุณาเลือกข้อ"))
#     if(x == 1):
#         print("ทำโจทย์ที่ 1")
#     elif (x == 2):
#         print("ทำโจทย์ที่ 2")
#     start = False
# #-------------------------------------




#------------------------------------GAME----------------------------------------
monster = 100
longsword = 60
dagger = 20
bow = 30
start = True
while start:
    print("---------Welcome to kiritoo! Game---------")
    print("ระหว่างที่คุณกำลังเดินทางไปเรื่อยเปื่อยคุณดันเผลอเดินไปชนกับบอสจึงทำให้บอสโกรธ")
    print(" สู้กับบอส กด 1  :")
    print(" วิ่งหนีสับตีนเเตก กด2  :")
    x = int (input("คุณจะเลือกตัวเลือกไหน  :  "))
    if(x == 1):
        attacktimes = int(input("จะตีมอนกี่ครั้ง :"))
        print("-------คุณมีอาวุธ 3 อย่างในการเลือกใช้ต่อสู้กับบอส-------")
        print("Monster มีเลือด 100 หน่วย")
        for i in range (attacktimes):
            print("----------------------------------------------------")
            print("Monster HP remaining",monster )
            print("-------คุณมีอาวุธ 3 อย่างในการเลือกใช้ต่อสู้กับบอส-------")
            print("เลือก Longsword [1] มี damage ",longsword)
            print("เลือก Dagger [2] มี Damage ",dagger)
            print("เลือก Bow [3] มี Damage ",bow)
            print("เหลือโอกาศตีอีก", attacktimes - i)
            y = int(input("คุณจะเลือกใช้อาวุธไหน :"))
            if(y == 1):
                monster -= 60
                print("Monster HP remaining",monster )
            elif(y == 2):
                monster -= 20
                print("Monster HP remaining",monster )
            elif(y == 3):
                monster -= 30
                print("Monster HP remaining",monster )
            if monster < 0:
               monster = 20 
            if monster == 0:
                print("You win")
                break
        else:
            print("You Lose")
    elif (x == 2):
        print("คุณวิ่งหนีไม่สำเร็จ ตุยเย่")
        break
    else:
        print("wrong")
        print("ไปเรื่อยละนิ")
        
    start = False
























