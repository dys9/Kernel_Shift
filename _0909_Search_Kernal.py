import cv2
import numpy as np

img = cv2.imread("test.jpg")
_, img = cv2.threshold(img, 255, 0, cv2.THRESH_BINARY)


kernel_size_y = int( np.shape(img)[0] * 0.1 )
kernel_size_x = int( np.shape(img)[1] * 0.1 )
kernel_size_c = int( np.shape(img)[2] )

kernel = np.zeros((kernel_size_y, kernel_size_x, kernel_size_c), dtype= np.uint8)
step = np.zeros((kernel_size_y,kernel_size_x, kernel_size_c), dtype=np.uint8)
step[np.where(step == 0)] = 2

print(np.shape(img))
print(np.shape(kernel))

for y in range(0, np.shape(img)[0], kernel_size_y):
    for x in range(0, np.shape(img)[1], kernel_size_x):
        kernel += step
        print(y,x)

        # cv2.imshow("kernel_"+str(y)+"_"+str(x), kernel)
        kernel_y = -1; kernel_x = -1
        for i in range(y, y+kernel_size_y, 1):
            kernel_y += 1
            kernel_x = -1
            for j in range(x, x + kernel_size_x, 1):
                kernel_x += 1

                img[i][j] += kernel[kernel_y][kernel_x]

                #print( "전체 [%4d, %4d] " % (i,j) , "커널 [%4d, %4d] " % (kernel_y, kernel_x) )


cv2.imshow("search_end", img)
#cv2.imshow("sdf",kernel)
cv2.waitKey(0)
cv2.destroyAllWindows()