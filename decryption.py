import cv2

c = {i: chr(i) for i in range(255)}

def decrypt(filepath, msg_length):
    img = cv2.imread(filepath)
    message = ""
    n = m = z = 0
    for i in range(msg_length):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3
    return message
