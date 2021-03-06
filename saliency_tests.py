from functions.generate_saliency_maps import generate_saliency_maps
from functions.adversarial import *
from functions.classification import *
import matplotlib.pyplot as plt

# image_dataset = ['panda.jpg', 'peacock.jpg', 'F16_GT.png', 'monkey.jpg', 'zebra_GT.png', 'goldfish.jpg', 'whale.jpg',
#                  'dolphin.jpg', 'spider.jpg', 'labrador.jpg', 'snake.jpg', 'flamingo_animal.JPG', 'canoe.jpg',
#                  'car_wheel.jpg', 'fountain.jpg', 'football_helmet.jpg', 'hourglass.jpg', 'refrigirator.jpg',
#                  'knife.jpg', 'rope.jpeg']

image_dataset = ['knife_FGSM_eps100.png']
# image_dataset2 = ['it_{}.png'.format(100*i) for i in range(0, 11)]
# image_dataset2.extend(['it_{}.png'.format(200*i) for i in range(6, 51)])


for i in range(len(image_dataset)):
    image = image_dataset[i]
    print('###### Working on image: ' + image.split('.')[0])

    img = cv2.imread('data/knife.jpg')[..., ::-1]
    _, ranks = classification(img, sort=True, cuda=True)
    original_class = ranks[0, 0]

    img2 = cv2.imread('results/adversarial_examples/Examples/FGSM_eps100/' + image)[..., ::-1]
    _, ranks = classification(img, sort=True, cuda=True)
    target_class = ranks[0, 0]

    name = image.split('.')[0]

    # image = name + '_original_class.png'
    img_path = 'results/adversarial_examples/Examples/FGSM_eps100/' + image

    save_path = 'results/Saliency/Dataset'
    generate_saliency_maps(save_path, img_path, name + 'oc', model_type='resnet18', cuda=True, target_label=original_class,
                        top_percentile=95, bottom_percentile=10, mask_mode=True, stdev_spread=0.01, dual=False)

    generate_saliency_maps(save_path, img_path, name, model_type='resnet18', cuda=True, target_label=target_class,
                        top_percentile=95, bottom_percentile=10, mask_mode=True, stdev_spread=0.01, dual=False)