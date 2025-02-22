import cv2

d = {chr(i): i for i in range(255)}

def encrypt(filepath, msg):
    img = cv2.imread(filepath)
    n = m = z = 0
    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n += 1
        m += 1
        z = (z + 1) % 3
    cv2.imwrite("encryptedImage.png", img)
