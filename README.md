# ABNORMAL EVENT DETECTION IN VIDEOS USING GENERATIVE ADVERSARIAL NETS

This project is the Pytorch implementation of the paper ["ABNORMAL EVENT DETECTION IN VIDEOS USING GENERATIVE ADVERSARIAL NETS"](https://arxiv.org/pdf/1708.09644.pdf).

As described in the paper, this method applies [Pixel2Pixel](https://phillipi.github.io/pix2pix/) architecture. Using two same architecture as Pixel2Pixel, the model learns to map frames to optical flows and vice versa. To compute the optical flow, ["High accuracy optical flow estimation based on a theory for warping"](https://www.mia.uni-saarland.de/Publications/brox-eccv04-of.pdf) is used. Its implementation can be found [here](https://lmb.informatik.uni-freiburg.de/resources/binaries/). In addition, [AlexNet](https://stackoverflow.com/questions/13242382/resampling-a-numpy-array-representing-an-image) is used as feature extractor to provide a compact representation for frames. 

TO DO LIST:

- [x] Make optical flow for the dataset using the folder optical. The implementation is found [here](https://lmb.informatik.uni-freiburg.de/resources/binaries/)
  - [x] Implement for one video
  - [x] Extend for whole dataset and compute optical flow for all videos
- [x] Using the orginal implementation of Pixel2Pixel, two network is implemented, one to translate frames to optical flow and the other to translate optical flow to frames.
  - [x] To resample the last Conv layer of AlexNet use this [link](https://www.pydoc.io/pypi/torch-raspi-0.4.0/autoapi/nn/modules/upsampling/index.html)
  - [x] The output of optical flow to frame needs to be processed by last AlexNet ConvLeyer. Follow this [link](https://pytorch.org/docs/0.4.0/_modules/torchvision/models/alexnet.html). 
- [x] Error computing
  - [x] Semantic error: Let `h(F)` be the conv5 representation befoe MaxPooling of `F` in AlexNet: p_F : ∆_S = h(F) − h(p_F)
  - [x] Optical error: a simple pixel-by-pixel difference, : ∆_O = O − p_o
  - [x] we first upsample ∆_S in order to obtain ∆'_S with the same resolution as ∆_O.
  - [x] Normalizing optical test videos: the maximum value m_O of all the elements of ∆_O over all the input frames of V: N_O(i, j) = 1/m_O∆_O(i, j).
  - [x] Normalizing frame test videos: N_S(i, j) = 1/m_S∆'_S(i, j)
- [ ] Prepare frame-opticalFlow pairs from UCF Crime dataset
- [ ] Train Pix2Pix model on new dataset


  
  
