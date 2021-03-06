from functions.adversarial import *
# from functions.generate_results import *
import matplotlib.pyplot as plt

image_dataset = ['panda.jpg', 'peacock.jpg', 'F16_GT.png', 'monkey.jpg', 'zebra_GT.png', 'goldfish.jpg', 'whale.jpg',
                 'dolphin.jpg', 'spider.jpg', 'labrador.jpg', 'snake.jpg', 'flamingo_animal.JPG', 'canoe.jpg',
                 'car_wheel.jpg', 'fountain.jpg', 'football_helmet.jpg', 'hourglass.jpg', 'refrigirator.jpg',
                 'rope.jpeg', 'knife.jpg']

for i in range(len(image_dataset)):
    image_path = image_dataset[i]
    image_name = '{}'.format(image_path.split('.')[0])

    save_path_common = 'results/adversarial_examples/{}'

    print("#############\n\nWorking on image: {}".format(image_name))

    for eps in [100]:
        adv, _, _ = adversarial_examples("data/{}".format(image_path), method="JSMA", eps=eps, show=True, cuda=True)
        plt.imsave(save_path_common.format('JSMA_eps{}/{}_JSMA_eps{}.png'.format(eps, image_name, eps)), adv, format='png')

        # adv, _, _ = adversarial_examples("data/{}".format(image_path), method="BI", eps=eps, show=False)
        # plt.imsave(save_path_common.format('BI_eps{}/{}_BI_eps{}.png'.format(eps, image_name, eps)), adv, format='png')
        #
        # adv, _, _ = adversarial_examples("data/{}".format(image_path), method="FGSM", eps=eps, show=False)
        # plt.imsave(save_path_common.format('FGSM_eps{}/{}_FGSM_eps{}.png'.format(eps, image_name, eps)), adv, format='png')


