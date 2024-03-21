### Need to install Petlib, Numpy and Matplotlib --- use requirements.txt --- see below ####

To install all dependencies (preferably on virtual env):
-- pip install -r requirements.txt

Files:
1. sampleNormalDist.py -- Outputs a bar graph representing a normal distribution where mean=0, y-axis is bounded by (-ksd,ksd) and the number of samples (b) is 100,000

2. normalDist.py -- Function to generate b samples from a normal distribution where the function takes input (ksd,b).

2. lweScheme.py -- Outputs a LWE instance (A,b).

3. regevEnc.py -- Encryption and Decryption function of Regev's LWE encryption.