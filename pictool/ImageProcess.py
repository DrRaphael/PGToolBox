import time
import os
from PIL import Image
# def concat_image(filePath):
#     target = Image.new('RGB',(1920,1080))
#     target.paste(Image.open(path + file), (0, 0))
#     target.save(path+'1.jpg')

path  = "C:\\Users\\gengx\\Desktop\\t2\\"
def getfileList(dirPath):
    if(os.path.isdir(dirPath)):
        fileList = os.listdir(dirPath)
        filePathList = []
        for file in fileList:
            filePathList.append(dirPath + file)
        return filePathList
    else:
        return None

def getImgSize(filePath):
    return Image.open(filePath).size

def computePerSize(fileList ,direct = 'LR'):
    width = (getImgSize(fileList[0])[0])
    height = (getImgSize(fileList[0])[1])
    totalImage = len(fileList)
    if direct == 'LR':
        batchBasic = width // totalImage
        batchBasicPlus = width % totalImage
        batchHead = batchBasicPlus // 2
        batchTail = batchBasicPlus - batchHead
        return batchBasic,batchHead,batchTail
    else:
        return None

def concatImageHorizontal(dirpath, direct = "LR", perCb=None, showCB =None):
    batchsie, head, tail = computePerSize(getfileList(dirpath))
    targetImage = Image.new('RGB', getImgSize(getfileList(dirpath)[0]))
    fileList = getfileList(dirpath)
    if direct == 'LR' or direct == 'RL':
        if direct == 'RL':
            fileList.reverse()
        for i in range(0, head):
            temp = Image.open(fileList[i])
            box = (
                i * (batchsie + 1),
                0,
                i * (batchsie + 1) + (batchsie + 1),
                getImgSize(getfileList(dirpath)[0])[1]
            )
            temp = temp.crop(box)
            targetImage.paste(temp, box)
            if perCb != None:
                perCb(i / len(fileList),targetImage)
        for i in range(head, len(fileList) - tail):
            temp = Image.open(fileList[i])

            box = (
                i * (batchsie) + head,
                0,
                i * (batchsie) + (batchsie) + head,
                getImgSize(getfileList(dirpath)[0])[1]
            )
            temp = temp.crop(box)
            targetImage.paste(temp, box)
            if perCb != None:
                perCb(i / len(fileList),targetImage)
        for i in range(0, tail):
            temp = Image.open(fileList[i + len(fileList) - tail])

            box = (
                i * (batchsie + 1) + ((len(fileList) - tail) * batchsie) + head,
                0,
                i * (batchsie + 1) + ((len(fileList) - tail) * batchsie) + head + (batchsie + 1),
                getImgSize(getfileList(dirpath)[0])[1]
            )
            temp = temp.crop(box)
            targetImage.paste(temp, box)
            if perCb != None:
                perCb((i + (len(fileList) - tail)) / len(fileList),targetImage)
        targetImagePath = "temp.jpg"
        targetImage.save(targetImagePath)
        showCB(targetImagePath)