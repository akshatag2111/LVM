import getpass
import os
print("""
""")        
while True:
                   os.system("tput setaf 3")
                   print("""
    *******************************************************************
                          WELCOME TO LVM
    *******************************************************************
               """)
                   os.system("tput setaf 10")
                   print('''
          press 1: To check information about the Harddisk 
          press 2: To create Physical Volume (PV)
          press 3: To create Volume Group (VG)
          press 4: To create  Logical Volume (LV)
          press 5: To format Logical Volume 
          press 6: To create folder and Mount Logical Volume
          press 7: To Extend Logical Volume
          press 8: To Resize/format the newly created LV
          press 9: To Exit
                          
                          ''')
                   ch=input("\nEnter yoyr choice :")
                   if int(ch)==1:
                           os.system("fdisk -l")
                           input("\npress Enter for Menu list....")
                   elif int(ch)==2:
                           Disk1 = input("\n\nEnter the name of 1st Hardisk that you want to use to create PV : ")
                           os.system("pvcreate {}" .format(Disk1))
                           os.system("pvdisplay {}" .format(Disk1))
                           Disk2 = input("\n\nEnter the name of 2nd Harddisk that you want to use to create PV : ")
                           os.system("pvcreate {}" .format(Disk2))
                           os.system("pvdisplay {}" .format(Disk2))
                           os.system("tput setaf 3")
                           print("\n\t\t\t............Physical volume created successfully......")
                           input("\npress Enter for Menu list....")
                   elif int(ch)==3:
                           Disk1 = input("\n\nEnter the name of 1st PV : ")
                           Disk2 = input("\n\nEnter thr name of 2nd PV : ")
                           name1 = input("Enter the name of your Volume Group(VG): ")
                           os.system("vgcreate {} {} {}" .format(name1,Disk1,Disk2))
                           os.system("vgdisplay {}" .format(name1))
                           os.system("tput setaf 3")
                           print("\n\t\t\t.........Volume Group Created Successfully..........")
                           input("\npress Enter for Menu list....")
                   elif int(ch)==4:
                           name1 = input("Enter the name of your Volume Group(VG): ")
                           name2 = input("Enter the name of your Logical Volume(LV): ")
                           size1 = input("Enter the size(in Gb) for your Logical Volume: ")
                           os.system("lvcreate --size {} --name {} {}" .format(size1,name2,name1))
                           os.system("lvdisplay {}/{}" .format(name1,name2))
                           os.system("tput setaf 3")
                           print("\n\t\t\t.....Logical Volume Creatred Succesfully......")
                           input("\npress Enter for Menu list....")
                   elif int(ch)==5:
                           name1 = input("Enter the name of your Volume Group(VG): ")
                           name2 = input("Enter the name of your Logical Volume(LV): ")
                           os.system("mkfs.ext4 /dev/{}/{}" .format(name1,name2))
                           os.system("tput setaf 3")
                           print("\n\t\t\t...............Logical Volume Formated Successfully......")
                           input("\npress Enter for Menu list....")
                   elif int(ch)==6:
                           mount_point = input("Enter the name of your folder: ")
                           os.system("mkdir {}" .format(mount_point))
                           name1 = input("Enter the name of your Volume Group(VG): ")
                           name2 = input("Enter the name of your Logical Group(LG): ")
                           os.system("mount /dev/{}/{} {}" .format(name1,name2,mount_point))
                           os.system("df -h")
                           print("\n\t\t\t..............Logical Volume Mounted Successfully.......")
                           input("\npress Enter for Menu list....")
                   elif int(ch)==7:
                           size1 = input("Enter the size that you want to extend : ")
                           name1 = input("Enter the name of your Volume Group(VG) : ")
                           name2 = input("Enter the name of your Logical Volume(LV): ")
                           os.system("lvextend --size +{} /dev/{}/{}" .format(size1,name1,name2))
                           os.system("tput setaf 3")
                           print("\n\t\t\t..........Logical Volume Extended successfully.......")
                           input("\npress Enter for Menu list....")
                   elif int(ch)==8:
                           name1 = input("Enter the name of your Volume Group(VG): ")
                           name2 = input("Enter the name of your Logical Volume(LV): ")
                           os.system("resize2fs /dev/{}/{}" .format(name1,name2))
                           print("\n\t\t\t......Newly extended partation Successfully formated.....")
                           input("\npress Enter for Menu list....") 
                   elif int(ch)==9:
                          break      
                   else:
                           print("Enter the correct choice : ")



