# Name: Ho Yeung Chan (Sunny)    Date: 12 Aug 2022
class FileItem:
    name = ""
    size = 0 # size in Bytes
    owner = ""
    permission = ""
    directory = ""
    def __init__(self,name,size,owner,permission,directory):
        self.name = name
        self.size = size
        self.owner = owner
        self.permission = permission
        self.directory = directory
        
class CsvFile(FileItem):
    row = 0 # number of rows
    col = 0 # number of columns
    def __init__(self,name,size,owner,permission,directory,row,col):
        FileItem.__init__(self,name,size,owner,permission,directory)
        self.row = row
        self.col = col
        
class JpgFile(FileItem):
    width = 0
    height = 0
    def __init__(self,name,size,owner,permission,directory,width,height):
        FileItem.__init__(self,name,size,owner,permission,directory)
        self.width = width
        self.height = height
        
class Mp3File(FileItem):
    time = 0.0
    def __init__(self,name,size,owner,permission,directory,time):
        FileItem.__init__(self,name,size,owner,permission,directory)
        self.time = time
        
class Directory(FileItem):
    pass

# Include a directory structure with a depth of at least three (directory in a directory in a directory)
'''Directory structure:
mycollection 
-- myphoto
---- friend_photo
---- family_photo
-- mymusic
---- japan_song
---- hk_song'''
mycollection = Directory("My Collection", 1000000, "Sunny", "wr", "home")
myphoto = Directory("My Photos", 300000, "Sunny", "wr", "My Collection")
friend_photo = Directory("Friend Photos", 200000, "Sunny", "wr", "My Photos")
family_photo = Directory("Family Photos", 100000, "Sunny", "wr", "My Photos")
mymusic = Directory("My Music", 700000, "Sunny", "wr", "My Collection")
japan_song = Directory("Japan Songs", 400000, "Sunny", "wr", "My Music")
hk_song = Directory("Hong Kong Songs", 300000, "Sunny", "wr", "My Music")
# files in the above directories
disney = JpgFile("In Disneyland", 2000, "Sunny", "r", "Friend Photos", 1200, 1600)
games = JpgFile("Games with friends", 2000, "Sunny", "r", "Friend Photos", 1200, 1600)
park = JpgFile("In Ocean Park", 2000, "Sunny", "r", "Friend Photos", 1200, 1600)
camp = JpgFile("Camping with family", 2000, "Sunny", "r", "Family Photos", 1200, 1600)
grad = JpgFile("Graduation", 2000, "Sunny", "r", "Family Photos", 1200, 1600)
yoru = Mp3File("Yoru ni Kakeru", 20000, "Sunny", "r", "Japan Songs", 240.0)
young = Mp3File("young forever", 20000, "Sunny", "r", "Hong Kong Songs", 180.0)
# Include at least one directory that contains at least two other directories and at least two files.
hw = Directory("Homework", 1000000, "Sunny", "wr", "home")
math = Directory("Math course", 300000, "Sunny", "wr", "hw")
comp = Directory("Comp course", 400000, "Sunny", "wr", "hw")
fina = Directory("Fina course", 300000, "Sunny", "wr", "hw")
math1 = JpgFile("Math4004 HW1", 5000, "Sunny", "wr", "Math course", 1200, 1600)
math2 = JpgFile("Math4004 HW2", 5000, "Sunny", "wr", "Math course", 1200, 1600)
fina1 = JpgFile("Fina2001 HW1", 5000, "Sunny", "wr", "Fina course", 1200, 1600)
fina2 = CsvFile("Fina2001 Lab", 10000, "Sunny", "wr", "Fina course", 30, 20)
comp1 = CsvFile("COMP2031 Lab", 10000, "Sunny", "wr", "Comp course", 40, 30)
comp2 = JpgFile("COMP2031 HW1", 5000, "Sunny", "wr", "Comp course", 1200, 1600)
train1 = CsvFile("Training ex1", 10000, "Sunny", "wr", "hw", 30, 16)
train2 = CsvFile("Training ex2", 10000, "Sunny", "wr", "hw", 50, 20)
train3 = CsvFile("Training final ex", 20000, "Sunny", "wr", "hw", 100, 46)

