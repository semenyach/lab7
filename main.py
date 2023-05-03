from PIL import Image, ImageFilter
im="1.jpg"
with Image.open(im) as img:
    img.load()
img.show()
w, h = img.size
print('Ширина:',w )
print('Высота:', h)
print('Формат:', img.format)
print('Модель:',img.mode )
def zad2():
    im = "1.jpg"
    with Image.open(im) as im:
        im.load()
    img=im.resize((im.width // 3, im.height // 3))
    img1= img.transpose(Image.FLIP_TOP_BOTTOM)
    img2 = img.transpose(Image.FLIP_LEFT_RIGHT)
    img1.save("topbottom.jpg")
    img2.save("leftright.jpg")
def zad3():
    names= ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
    for files in names:
        with Image.open(files) as im:
            im.load()
            nim=im.filter(ImageFilter.CONTOUR)
            nim.save("new_" + files)
def zad4():
    mark= 'mark.png'
    with Image.open(mark) as imw:
        imw.load()
    imw=Image.open(mark)
    imw=imw.resize((imw.width//3, imw.height//3))
    sob= "sobaken.jpg"
    with Image.open(sob) as imag:
        imag.load()
    imag.paste(imw, (42, 40), imw)
    imag.save("watermark.jpg")
zad2()
zad3()
zad4()