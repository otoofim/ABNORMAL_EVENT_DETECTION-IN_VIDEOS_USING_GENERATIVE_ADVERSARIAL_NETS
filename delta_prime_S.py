from AlexNet_extractor.py import *



def computing_delta_prime_S(img1, img2):

	sampler = nn.Upsample(size = (3,256,256))

	output1 = AlexNetConv5_getFeatures(img1)
	output2 = AlexNetConv5_getFeatures(img2)
	dif = output1 - output2
	dif = dif.unsqueeze(0)
	return sampler(dif).squeeze().squeeze()

