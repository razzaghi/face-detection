import cv2
import matplotlib.pyplot as plt

file_name = "/home/mohammad/workspace/deeplearning/face-detection/faces/75b6f7e0-IMG_20210320_131938.jpg.jpeg"

# img_show = Image.open(file_name)
# img_show = img_show.convert('RGB')
# plt.imshow(img_show)
# plt.axis('off')
# plt.show()


width = 2592
height = 1944

x_min = int(round(9.8))
y_min = int(round(19.6))


box_width = int(round(24.5))
box_height = int(round(46.3))


etd = 1.35

x_min_percent = int(round(((x_min / 100) * width) * etd))
y_min_percent = int(round(((y_min / 100) * height) * etd))

box_width_percent = int(round(((box_width / 100) * width) * etd))
box_height_percent = int(round(((box_height / 100) * height) * etd))

x_max = int(round(x_min + box_width_percent))
y_max = int(round(y_min + box_height_percent))

img = cv2.cvtColor(cv2.imread(f'{file_name}'), cv2.COLOR_BGR2RGB)
cv2.rectangle(img, (x_min + x_min_percent, y_min + y_min_percent), (x_max, y_max), (0, 255, 0), 2)
img = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
plt.imshow(img)
plt.axis('off')
plt.show()
