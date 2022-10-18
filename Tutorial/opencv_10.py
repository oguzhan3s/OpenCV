import cv2
import matplotlib.pyplot as plt
import numpy as np

"""
BULANIKLAŞTIRMA
- Görüntü bulanıklığı, görüntünün düşük geçişli bir filtre uygulamasıyla elde edilir.
- Gürültüyü gidermek için kullanışlıdır. Aslında görüntüden yüksek frekanslı içeriği(örn. parazir, kenarlar) kaldırır.
- Opencv, üç ana tür bulanıklaştırma tekniği sağlar.
-- Ortalama bulanıklaştırma 
-- Gauss bulanıklaştırma
-- Medyan bulanıklaştırma

Ortalama Bulanıklaştrıma:
Bir görüntünün normalleştirilmiş bir kutu filtresiyle sarılmasıyla yapılır.
Çekirdek alanı altındaki tüm piksellerin ortalamasını alır ve bu ortalamayı merkezi öğe ile yer değiştirir.

Gauss Bulanıklaştırma:
Bu yöntemde kutu filtresi yerine Gauss çekirdeği kullanılır.
Pozitif ve tek olması gereken çekirdeğin genişliğini ve yüksekliğini belirtir.
SigmaX ve sigmaY, X ve Y yönlerindeki standart sapmayı belirtmeliyiz.

Medyan Bulanıklaştırma:
Çekirdek alanı altındaki tüm piksellerin medyanını alır ve merkezi öğe bu medyan değerle değiştirilir.
Tuz ve biber gürültüsüne karşı olduça etkilidir.


"""
#blurring (detayı azaltır, gürültüyü engeller)
img = cv2.imread("pictures/kule.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("orjinal")

#Ortalama bulanıklaştırma

dst2 = cv2.blur(img, ksize= (3,3))
plt.figure(), plt.imshow(dst2), plt.axis("off"),plt.title("ortalama blur")

#gauss blur

gb = cv2.GaussianBlur(img, ksize = (3,3), sigmaX=7)
plt.figure(), plt.imshow(gb), plt.axis("off"),plt.title("gauss blur")

#medyan blur
mb = cv2.medianBlur(img, ksize=3)
plt.figure(), plt.imshow(mb), plt.axis("off"),plt.title("medyan blur")

def gaussianNoise(image):
    row, col, ch = image.shape
    mean = 0
    var = 0.05
    sigma = var**0.5

    gauss = np.random.normal(mean, sigma, (row,col, ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    return noisy
# içe aktar normalize et
img = cv2.imread("pictures/kule.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255
plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("orjinal")

gaussianNoisyImage = gaussianNoise(img)
plt.figure(),plt.imshow(gaussianNoisyImage ),plt.axis("off"),plt.title("gauss noisy")

#gauss blur
gb2 = cv2.GaussianBlur(gaussianNoisyImage, ksize = (3,3), sigmaX=7)
plt.figure(), plt.imshow(gb2), plt.axis("off"),plt.title("with gauss blur")


#tuz ve karabiber gürültüsü resme siyah ve beyaz noktaların resme rastgele yerleştirilmesi
def saltPapperNoise(image):

    row, col, ch= image.shape
    s_vs_p = 0.5

    amount = 0.004

    noisy = np.copy(image)

    #salt beyaz noktacık ekleme
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape ]
    noisy[coords] = 1

    # papper siyah
    num_papper = np.ceil(amount * image.size *  (1 -  s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_papper)) for i in image.shape ]
    noisy[coords] = 0

    return noisy


spImage = saltPapperNoise(img)
plt.figure(), plt.imshow(spImage), plt.axis("off"),plt.title("sp ımage")

mb2 = cv2.medianBlur(spImage.astype(np.float32), ksize=3)
plt.figure(), plt.imshow(mb2), plt.axis("off"),plt.title("with medyan blur"), plt.show()


