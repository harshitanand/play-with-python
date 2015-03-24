import cv2
import glob
import os
def Image_finder(sample,images):
    flag = 0
    img = cv2.imread(sample,0)
    img2 = img.copy()
    W, H = img.shape[::-1]
    for template in images:
        image = cv2.imread(template,0)
        if(image != 'None'):
            w, h = image.shape[::-1]
            if(W<=w and H<=h):
                meth = 'cv2.TM_SQDIFF'
                img = img2.copy()
                method = eval(meth)
                # Apply template Matching
                res = cv2.matchTemplate(img,image,method)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
                if(min_val == 0 and max_val == 0):
                    print template
                    flag = 1
    if (flag == 0):
        print "Null"

print "Enter path of image to search"
image_to_search = raw_input();
if(os.path.isfile(image_to_search)):
    images = glob.glob('images/*.jpg')
    Image_finder(image_to_search, images)
else:
    print "No such Image exists"
