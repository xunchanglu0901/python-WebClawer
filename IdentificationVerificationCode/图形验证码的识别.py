import tesserocr
from PIL import Image



image = Image.open('code.jpg')
#result = tesserocr.image_to_text(image)
#print(result)
# 从结果可以看出多余线条干扰了识别

#image = image.convert('L')
#image = image.convert('1')

# 指定二值化阈值
image = image.convert('L')

threshold = 111
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table,'1')
#image.show()
result = tesserocr.image_to_text(image)
print(result)
