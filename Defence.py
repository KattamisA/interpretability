from functions.adversarial import *
from functions.dip import *
from functions.generate_results import *
# from functions.adversarial import *
from functions.classification import *
import matplotlib.pyplot as plt
import cv2


image_dataset = ['panda.jpg', 'peacock.jpg', 'F16_GT.png', 'monkey.jpg', 'zebra_GT.png', 'goldfish.jpg', 'whale.jpg',
                 'dolphin.jpg', 'spider.jpg', 'labrador.jpg', 'snake.jpg', 'flamingo_animal.JPG', 'canoe.jpg',
                 'car_wheel.jpg', 'fountain.jpg', 'football_helmet.jpg', 'hourglass.jpg', 'refrigirator.jpg',
                 'rope.jpeg', 'knife.jpg']

z = []
q=0.0
p=0.0
for i in range(len(image_dataset)):
    image_path = image_dataset[i]
    image_name = '{}'.format(image_path.split('.')[0])
    print(image_name)
    orig = cv2.imread("data/" + image_path)[..., ::-1]
    _, ranks = classification(orig, sort=True, show=False, model_name='resnet18', cuda=True)
    orig_rank = ranks[0,0]
    adv = cv2.imread("results/adversarial_examples/Examples/FGSM_eps1/" + image_name + "_FGSM_eps1.png")[..., ::-1]
    _, ranks = classification(adv , sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        p = p + 1
    output = dip(adv, 'complex', 0.01, 301, save=False, plot=False, name=image_name)
    _, ranks = classification(output * 255, sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        q = q + 1
    print(q)
print("\n\n#Results: Adversary - " + p/20.0 + "   Recovered - "  + q/20.0)
z.append([q / 20.0, p / 20.0])
print(z)

q=0.0
p=0.0
for i in range(len(image_dataset)):
    image_path = image_dataset[i]
    image_name = '{}'.format(image_path.split('.')[0])
    print(image_name)
    orig = cv2.imread("data/" + image_path)[..., ::-1]
    _, ranks = classification(orig, sort=True, show=False, model_name='resnet18', cuda=True)
    orig_rank = ranks[0,0]
    adv = cv2.imread("results/adversarial_examples/Examples/FGSM_eps5/" + image_name + "_FGSM_eps5.png")[..., ::-1]
    _, ranks = classification(adv , sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        p = p + 1
    output = dip(adv, 'complex', 0.01, 301, save=False, plot=False, name=image_name)
    _, ranks = classification(output * 255, sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        q = q + 1
    print(q)
print("\n\n#Results: Adversary - " + p/20.0 + "   Recovered - "  + q/20.0)
z.append([q / 20.0, p / 20.0])
print(z)

q=0.0
p=0.0
for i in range(len(image_dataset)):
    image_path = image_dataset[i]
    image_name = '{}'.format(image_path.split('.')[0])
    print(image_name)
    orig = cv2.imread("data/" + image_path)[..., ::-1]
    _, ranks = classification(orig, sort=True, show=False, model_name='resnet18', cuda=True)
    orig_rank = ranks[0,0]
    adv = cv2.imread("results/adversarial_examples/Examples/FGSM_eps25/" + image_name + "_FGSM_eps25.png")[..., ::-1]
    _, ranks = classification(adv , sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        p = p + 1
    output = dip(adv, 'complex', 0.01, 301, save=False, plot=False, name=image_name)
    _, ranks = classification(output * 255, sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        q = q + 1
    print(q)
print("\n\n#Results: Adversary - " + p/20.0 + "   Recovered - "  + q/20.0)
z.append([q / 20.0, p / 20.0])
print(z)

q=0.0
p=0.0
for i in range(len(image_dataset)):
    image_path = image_dataset[i]
    image_name = '{}'.format(image_path.split('.')[0])
    print(image_name)
    orig = cv2.imread("data/" + image_path)[..., ::-1]
    _, ranks = classification(orig, sort=True, show=False, model_name='resnet18', cuda=True)
    orig_rank = ranks[0,0]
    adv = cv2.imread("results/adversarial_examples/Examples/FGSM_eps100/" + image_name + "_FGSM_eps100.png")[..., ::-1]
    _, ranks = classification(adv , sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        p = p + 1
    output = dip(adv, 'complex', 0.01, 301, save=False, plot=False, name=image_name)
    _, ranks = classification(output * 255, sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        q = q + 1
    print(q)
print("\n\n#Results: Adversary - " + p/20.0 + "   Recovered - "  + q/20.0)
z.append([q / 20.0, p / 20.0])
print(z)

q=0.0
p=0.0
for i in range(len(image_dataset)):
    image_path = image_dataset[i]
    image_name = '{}'.format(image_path.split('.')[0])
    print(image_name)
    orig = cv2.imread("data/" + image_path)[..., ::-1]
    _, ranks = classification(orig, sort=True, show=False, model_name='resnet18', cuda=True)
    orig_rank = ranks[0,0]
    adv = cv2.imread("results/adversarial_examples/Examples/BI_eps1/" + image_name + "_BI_eps1.png")[..., ::-1]
    _, ranks = classification(adv , sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        p = p + 1
    output = dip(adv, 'complex', 0.01, 301, save=False, plot=False, name=image_name)
    _, ranks = classification(output * 255, sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        q = q + 1
    print(q)
print("\n\n#Results: Adversary - " + p/20.0 + "   Recovered - "  + q/20.0)
z.append([q / 20.0, p / 20.0])
print(z)

q=0.0
p=0.0
for i in range(len(image_dataset)):
    image_path = image_dataset[i]
    image_name = '{}'.format(image_path.split('.')[0])
    print(image_name)
    orig = cv2.imread("data/" + image_path)[..., ::-1]
    _, ranks = classification(orig, sort=True, show=False, model_name='resnet18', cuda=True)
    orig_rank = ranks[0,0]
    adv = cv2.imread("results/adversarial_examples/Examples/BI_eps5/" + image_name + "_BI_eps5.png")[..., ::-1]
    _, ranks = classification(adv , sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        p = p + 1
    output = dip(adv, 'complex', 0.01, 301, save=False, plot=False, name=image_name)
    _, ranks = classification(output * 255, sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        q = q + 1
    print(q)
print("\n\n#Results: Adversary - " + p/20.0 + "   Recovered - "  + q/20.0)
z.append([q / 20.0, p / 20.0])
print(z)

q=0.0
p=0.0
for i in range(len(image_dataset)):
    image_path = image_dataset[i]
    image_name = '{}'.format(image_path.split('.')[0])
    print(image_name)
    orig = cv2.imread("data/" + image_path)[..., ::-1]
    _, ranks = classification(orig, sort=True, show=False, model_name='resnet18', cuda=True)
    orig_rank = ranks[0,0]
    adv = cv2.imread("results/adversarial_examples/Examples/BI_eps25/" + image_name + "_BI_eps25.png")[..., ::-1]
    _, ranks = classification(adv , sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        p = p + 1
    output = dip(adv, 'complex', 0.01, 301, save=False, plot=False, name=image_name)
    _, ranks = classification(output * 255, sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        q = q + 1
    print(q)
print("\n\n#Results: Adversary - " + p/20.0 + "   Recovered - "  + q/20.0)
z.append([q / 20.0, p / 20.0])
print(z)

q=0.0
p=0.0
for i in range(len(image_dataset)):
    image_path = image_dataset[i]
    image_name = '{}'.format(image_path.split('.')[0])
    print(image_name)
    orig = cv2.imread("data/" + image_path)[..., ::-1]
    _, ranks = classification(orig, sort=True, show=False, model_name='resnet18', cuda=True)
    orig_rank = ranks[0,0]
    adv = cv2.imread("results/adversarial_examples/Examples/BI_eps100/" + image_name + "_BI_eps100.png")[..., ::-1]
    _, ranks = classification(adv , sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        p = p + 1
    output = dip(adv, 'complex', 0.01, 301, save=False, plot=False, name=image_name)
    _, ranks = classification(output * 255, sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        q = q + 1
    print(q)
print("\n\n#Results: Adversary - " + p/20.0 + "   Recovered - "  + q/20.0)
z.append([q / 20.0, p / 20.0])
print(z)

q=0.0
p=0.0
for i in range(len(image_dataset)):
    image_path = image_dataset[i]
    image_name = '{}'.format(image_path.split('.')[0])
    print(image_name)
    orig = cv2.imread("data/" + image_path)[..., ::-1]
    _, ranks = classification(orig, sort=True, show=False, model_name='resnet18', cuda=True)
    orig_rank = ranks[0,0]
    adv = cv2.imread("results/adversarial_examples/Examples/LLCI_eps1/" + image_name + "_LLCI_eps1.png")[..., ::-1]
    _, ranks = classification(adv , sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        p = p + 1
    output = dip(adv, 'complex', 0.01, 301, save=False, plot=False, name=image_name)
    _, ranks = classification(output * 255, sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        q = q + 1
    print(q)
print("\n\n#Results: Adversary - " + p/20.0 + "   Recovered - "  + q/20.0)
z.append([q / 20.0, p / 20.0])
print(z)

q=0.0
p=0.0
for i in range(len(image_dataset)):
    image_path = image_dataset[i]
    image_name = '{}'.format(image_path.split('.')[0])
    print(image_name)
    orig = cv2.imread("data/" + image_path)[..., ::-1]
    _, ranks = classification(orig, sort=True, show=False, model_name='resnet18', cuda=True)
    orig_rank = ranks[0,0]
    adv = cv2.imread("results/adversarial_examples/Examples/LLCI_eps5/" + image_name + "_LLCI_eps5.png")[..., ::-1]
    _, ranks = classification(adv , sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        p = p + 1
    output = dip(adv, 'complex', 0.01, 301, save=False, plot=False, name=image_name)
    _, ranks = classification(output * 255, sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        q = q + 1
    print(q)
print("\n\n#Results: Adversary - " + p/20.0 + "   Recovered - "  + q/20.0)
z.append([q / 20.0, p / 20.0])
print(z)

q=0.0
p=0.0
for i in range(len(image_dataset)):
    image_path = image_dataset[i]
    image_name = '{}'.format(image_path.split('.')[0])
    print(image_name)
    orig = cv2.imread("data/" + image_path)[..., ::-1]
    _, ranks = classification(orig, sort=True, show=False, model_name='resnet18', cuda=True)
    orig_rank = ranks[0,0]
    adv = cv2.imread("results/adversarial_examples/Examples/LLCI_eps25/" + image_name + "_LLCI_eps25.png")[..., ::-1]
    _, ranks = classification(adv , sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        p = p + 1
    output = dip(adv, 'complex', 0.01, 301, save=False, plot=False, name=image_name)
    _, ranks = classification(output * 255, sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        q = q + 1
    print(q)
print("\n\n#Results: Adversary - " + p/20.0 + "   Recovered - "  + q/20.0)
z.append([q / 20.0, p / 20.0])
print(z)

q=0.0
p=0.0
for i in range(len(image_dataset)):
    image_path = image_dataset[i]
    image_name = '{}'.format(image_path.split('.')[0])
    print(image_name)
    orig = cv2.imread("data/" + image_path)[..., ::-1]
    _, ranks = classification(orig, sort=True, show=False, model_name='resnet18', cuda=True)
    orig_rank = ranks[0,0]
    adv = cv2.imread("results/adversarial_examples/Examples/LLCI_eps100/" + image_name + "_LLCI_eps100.png")[..., ::-1]
    _, ranks = classification(adv , sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        p = p + 1
    output = dip(adv, 'complex', 0.01, 301, save=False, plot=False, name=image_name)
    _, ranks = classification(output * 255, sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        q = q + 1
    print(q)
print("\n\n#Results: Adversary - " + p/20.0 + "   Recovered - "  + q/20.0)
z.append([q / 20.0, p / 20.0])
print(z)

q=0.0
p=0.0
for i in range(len(image_dataset)):
    image_path = image_dataset[i]
    image_name = '{}'.format(image_path.split('.')[0])
    print(image_name)
    orig = cv2.imread("data/" + image_path)[..., ::-1]
    _, ranks = classification(orig, sort=True, show=False, model_name='resnet18', cuda=True)
    orig_rank = ranks[0,0]
    adv = cv2.imread("results/adversarial_examples/Examples/JSMA_eps1/" + image_name + "_JSMA_eps1.png")[..., ::-1]
    _, ranks = classification(adv , sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        p = p + 1
    output = dip(adv, 'complex', 0.01, 301, save=False, plot=False, name=image_name)
    _, ranks = classification(output * 255, sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        q = q + 1
    print(q)
print("\n\n#Results: Adversary - " + p/20.0 + "   Recovered - "  + q/20.0)
z.append([q / 20.0, p / 20.0])
print(z)

q=0.0
p=0.0
for i in range(len(image_dataset)):
    image_path = image_dataset[i]
    image_name = '{}'.format(image_path.split('.')[0])
    print(image_name)
    orig = cv2.imread("data/" + image_path)[..., ::-1]
    _, ranks = classification(orig, sort=True, show=False, model_name='resnet18', cuda=True)
    orig_rank = ranks[0,0]
    adv = cv2.imread("results/adversarial_examples/Examples/JSMA_eps5/" + image_name + "_JSMA_eps5.png")[..., ::-1]
    _, ranks = classification(adv , sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        p = p + 1
    output = dip(adv, 'complex', 0.01, 301, save=False, plot=False, name=image_name)
    _, ranks = classification(output * 255, sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        q = q + 1
    print(q)
print("\n\n#Results: Adversary - " + p/20.0 + "   Recovered - "  + q/20.0)
z.append([q / 20.0, p / 20.0])
print(z)

q=0.0
p=0.0
for i in range(len(image_dataset)):
    image_path = image_dataset[i]
    image_name = '{}'.format(image_path.split('.')[0])
    print(image_name)
    orig = cv2.imread("data/" + image_path)[..., ::-1]
    _, ranks = classification(orig, sort=True, show=False, model_name='resnet18', cuda=True)
    orig_rank = ranks[0,0]
    adv = cv2.imread("results/adversarial_examples/Examples/JSMA_eps25/" + image_name + "_JSMA_eps25.png")[..., ::-1]
    _, ranks = classification(adv , sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        p = p + 1
    output = dip(adv, 'complex', 0.01, 301, save=False, plot=False, name=image_name)
    _, ranks = classification(output * 255, sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        q = q + 1
    print(q)
print("\n\n#Results: Adversary - " + p/20.0 + "   Recovered - "  + q/20.0)
z.append([q / 20.0, p / 20.0])
print(z)

q=0.0
p=0.0
for i in range(len(image_dataset)):
    image_path = image_dataset[i]
    image_name = '{}'.format(image_path.split('.')[0])
    print(image_name)
    orig = cv2.imread("data/" + image_path)[..., ::-1]
    _, ranks = classification(orig, sort=True, show=False, model_name='resnet18', cuda=True)
    orig_rank = ranks[0,0]
    adv = cv2.imread("results/adversarial_examples/Examples/JSMA_eps100/" + image_name + "_JSMA_eps100.png")[..., ::-1]
    _, ranks = classification(adv , sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        p = p + 1
    output = dip(adv, 'complex', 0.01, 301, save=False, plot=False, name=image_name)
    _, ranks = classification(output * 255, sort=True, show=False, model_name='resnet18', cuda=True)
    if ranks[0,0] == orig_rank:
        q = q + 1
    print(q)
print("\n\n#Results: Adversary - " + p/20.0 + "   Recovered - "  + q/20.0)
z.append([q / 20.0, p / 20.0])
print(z)
