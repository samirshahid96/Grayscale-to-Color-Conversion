import numpy as np
import cv2
import math
import random

class Coloring:

    def intensity_slicing(self, image, n_slices):  # done
        # Convert greyscale image to color image using color slicing technique.
        # takes as input:
        # image: the greyscale input image
        # n_slices: number of slices

        # Steps:
        # 1. Split the exising dynamic range (0, k-1) using n slices (creates n+1 intervals)
        # 2. Randomly assign a color to each interval
        # 3. Create and output color image
        # 4. Iterate through the image and assign colors to the color image based on which interval
        #    the intensity belongs to
        # 5. returns colored image
        ###############################################################################################################
        # #### setup
        greyscale_intensity = 255
        R, C = image.shape
        #final = np.zeros((R,C))
        Colored_image = [[[0, 0, 0] for m in range(C)] for n in range(R)]
        #print(image[218][1])
        #print(Colored_image[218][1])
        colors = dict()
        # #### 1 and 2 ################################################################################################
        for i in range(0,n_slices+1):
            red = random.randrange(256)
            green = random.randrange(256)
            blue = random.randrange(256)
            sectmin = int((greyscale_intensity * (0 + i))/(n_slices+1))
            sectmax = int((greyscale_intensity * (1 + i))/(n_slices+1))
            colors.setdefault(i, []).append((red, green, blue, sectmin, sectmax))
        # #### 3 and 4 ################################################################################################
        for x in range(R):
            for y in range(C):
                for i in range(0, n_slices+1):
                    key = colors.get(i)
                    #print(key)
                    if image[x][y] >= key[0][3] and image[x][y] < key[0][4]:
                        # Colored_image[x][y] = [key[0][0], key[0][1], key[0][2]]
                        # print(x,y,R,C)
                        Colored_image[x][y] = [key[0][0],key[0][1],key[0][2]]
        # #### 5 ######################################################################################################
        Colored_image = np.array(Colored_image)
        # final = Colored_image.copy()
        return Colored_image #final

    def color_transformation(self,image, n_slices, theta):  # done
        # Convert greyscale image to color image using color transformation technique.
        # takes as input:
        # image:  grayscale input image
        # colors: color array containing RGB values

        # Steps:
        # 1. Split the exising dynamic range (0, k-1) using n slices (creates n+1 intervals)
        # 2. create red values for each slice using 255*sin(slice + theta[0])
        #    similarly create green and blue using 255*sin(slice + theta[1]), 255*sin(slice + theta[2])
        # 3. Create and output color image
        # 4. Iterate through the image and assign colors to the color image based on which
        #    interval the intensity belongs to
        # 5. returns colored image
        ##############################################################################################################
        # #### setup
        pi = 22/7
        greyscale_intensity = 255
        R, C = image.shape
        Colored_image = [[[0,0,0] for m in range(C)] for n in range(R)]
        colors = dict()
        # #### 1 and 2 ################################################################################################
        for i in range(0, n_slices + 1):
            sectmin = int((greyscale_intensity * (0 + i)) / (n_slices + 1))
            sectmax = int((greyscale_intensity * (1 + i)) / (n_slices + 1))
            k = (sectmax + sectmin)/2
            red = 255 * math.sin((k + theta[0])*(pi/180))
            green = 255 * math.sin((k + theta[1])*(pi/180))
            blue = 255 * math.sin((k + theta[2])*(pi/180))
            colors.setdefault(i, []).append((red, green, blue, sectmin, sectmax))
        # #### 3 and 4 ################################################################################################
        for x in range(R):
            for y in range(C):
                for i in range(0, n_slices + 1):
                    key = colors.get(i)
                    if image[x][y] >= key[0][3] and image[x][y] < key[0][4]:
                        Colored_image[x][y] = [key[0][0], key[0][1], key[0][2]]
        # #### 5 ######################################################################################################
        Colored_image = np.array(Colored_image)
        return Colored_image