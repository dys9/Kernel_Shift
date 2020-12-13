import cv2
import numpy as np


def kernel_search(img, ratio_y, ratio_x):

    # -------- Get Size
    img_size_y = np.shape(img)[0]
    img_size_x = np.shape(img)[1]
    kernel_size_y = int(img_size_y * ratio_y)
    kernel_size_x = int(img_size_x * ratio_x)

    dst = np.copy(img)
    # -------- (y,x) is for Input_img, (kernel_y, kernel_x) is for Kernel
    for y in range(0, np.shape(img)[0], kernel_size_y):

        for x in range(0, np.shape(img)[1], kernel_size_x):
            kernel_y = -1; kernel_x = -1
            kernel = np.ones((kernel_size_y, kernel_size_x), dtype=np.uint8)

            # --------Kernel Sliding
            for i in range(y, y + kernel_size_y, 1):
                kernel_y += 1
                kernel_x = -1

                for j in range(x, x + kernel_size_x, 1):
                    if i >= img_size_y or j >= img_size_x: break

                    kernel_x += 1
                    kernel[kernel_y][kernel_x] = img[i][j]

            # --------Get Average
            cnt = 0; sum = 0
            for i in range(len(kernel)):
                for j in range(len(kernel)):
                    if kernel[i][j] is not 0:
                        cnt += 1
                        sum += kernel[i][j]
            avg_kernel = int(sum / cnt)
            # print((y, x), avg_kernel)  # Window Check

            for i in range(y, y + kernel_size_y, 1):
                for j in range(x, x + kernel_size_x, 1):
                    if i >= img_size_y or j >= img_size_x: break
                    if dst[i][j] <= avg_kernel:
                        # dst[i][j] += int(0.15 * avg_kernel)
                        dst[i][j] = 0

    return dst


img = cv2.imread("dst_img52.bmp", cv2.IMREAD_GRAYSCALE)
cv2.imshow("search_end", img)

dst = kernel_search(img, 0.2, 0.2)
cv2.imshow("dst0", dst)

dst = kernel_search(dst, 0.15, 0.15)
#cv2.imshow("dst1", dst)

dst = kernel_search(dst, 0.1, 0.1)
#cv2.imshow("dst2", dst)

dst = kernel_search(dst, 0.05, 0.05)
#cv2.imshow("dst3", dst)

dst = kernel_search(dst, 0.03, 0.03)
cv2.imshow("dst4", dst)




# --------------------------------------------------------
cv2.waitKey(0)
cv2.destroyAllWindows()
