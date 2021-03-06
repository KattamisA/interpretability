from functions.classification import *
from functions.utils.imagenet_classes import classes
import cv2

image_dataset = ['panda.jpg', 'peacock.jpg', 'F16_GT.png', 'monkey.jpg', 'zebra_GT.png', 'goldfish.jpg', 'whale.jpg',
                 'dolphin.jpg', 'spider.jpg', 'labrador.jpg', 'snake.jpg', 'flamingo_animal.JPG', 'canoe.jpg',
                 'car_wheel.jpg', 'fountain.jpg', 'football_helmet.jpg', 'hourglass.jpg', 'refrigirator.jpg',
                 'knife.jpg', 'rope.jpeg']

f = open("data/True_Class_resnet152.txt", "w+")
for i in image_dataset:
    img = cv2.imread("data/" + i)[..., ::-1]
    confidence, ranks = classification(img, sort=True, show=False, model_name='resnet152', cuda=True)
    Class = classes[int(ranks[0, 0])].split(',')[0]
    f.write("{:<30}{:>10.6f}\n".format(Class, confidence[0, 0]))

f = open("data/True_Class_vgg19.txt", "w+")
for i in image_dataset:
    img = cv2.imread("data/" + i)[..., ::-1]
    confidence, ranks = classification(img, sort=True, show=False, model_name='vgg19', cuda=True)
    Class = classes[int(ranks[0, 0])].split(',')[0]
    f.write("{:<30}{:>10.6f}\n".format(Class, confidence[0, 0]))