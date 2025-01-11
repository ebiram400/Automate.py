import os
import openpyxl

# # بارگذاری فایل اکسل
# file_path = "E:product0.xlsx"
# wb = openpyxl.load_workbook(file_path)
# ws = wb.active

# columns = {
#     "شناسه": 1,
#     "شناسه_محصول": 2,
#     "name": 3,
# }

for j in os.listdir("E:pictures"):
    # nameOldPic=int(j.split('.')[0])
    # newNamePic=ws.cell(row=nameOldPic, column=columns["name"]).value
    # newNamePic = newNamePic.replace('*','').replace('/','')
    # basePath='E:New folder'+"/"
    # os.rename(basePath+j , basePath+newNamePic+".jpg")
    
    nameOldPic=j.split('.')[0]
    basePath="E:pictures"+"/"
    nameNewPic=nameOldPic.replace(" ","_")
    os.rename(basePath+j , basePath+nameNewPic+".jpg")
    print("rename "+j+" success...")

print("***********the end***********")
