import numpy as np

def Thresholding(Image):
    I = Image
    Im = np.asarray(I, dtype = np.uint8)
    [r, c] = I.shape
    H = np.zeros((256, 1))
    
    #/// Build the image histogram
    for i in range (0, r):
        for j in range (0, c):
            k = Im[i, j]
            H[k] = H[k] + 1
    
    Hist = H
    #/// Total number of pixels
    N = r*c
    #/// Initial values
    Thsd = 0 
    Vmax = 0
    #/ Variable of the total sum
    t = 0
    for q in range(0, 256):
        t += q * Hist[q]
    
    sumB = 0
    mB = 0
    mF = 0
    wB = 0
    wF = 0
    varBetween = 0
    
    for w in range(0, 256):
        wB += Hist[w]
        wF = t - wB
        if (wF == 0):
            break
        sumB += float(w * Hist[w])
        mB = sumB/wB
        mF = (t - sumB)/wF
        #// Calculate Between Class Variance
        varBetween = wB*wF
        varBetween *= (mB - mF)*(mB - mF)
        #// Check if new maximum found
        if (varBetween > Vmax):
            Vmax = varBetween
            Thsd = w
            
    return Thsd
