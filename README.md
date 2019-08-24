# ABNORMAL EVENT DETECTION IN VIDEOS USING GENERATIVE ADVERSARIAL NETS

This project is the Pytorch implementation of the paper ["ABNORMAL EVENT DETECTION IN VIDEOS USING GENERATIVE ADVERSARIAL NETS"](https://arxiv.org/pdf/1708.09644.pdf).

As described in the paper, this method applies [Pixel2Pixel](https://phillipi.github.io/pix2pix/) architecture. Using two same architecture as Pixel2Pixel, the model learns to map frames to optical flows and vice versa. To compute the optical flow, ["High accuracy optical flow estimation based on a theory for warping"](https://www.mia.uni-saarland.de/Publications/brox-eccv04-of.pdf) is used. Its implementation can be found [here](https://lmb.informatik.uni-freiburg.de/resources/binaries/). In addition, [AlexNet](https://stackoverflow.com/questions/13242382/resampling-a-numpy-array-representing-an-image) is used as feature extractor to provide a compact representation for frames. 

TO DO LIST:

- [ ] Make optical flow for the dataset using the folder optical. The implementation is found [here](https://lmb.informatik.uni-freiburg.de/resources/binaries/)
  - [x] Implement for one video
  - [ ] Extend for whole dataset and compute optical flow for all videos
- [ ] Using the orginal implementation of Pixel2Pixel, two network is implemented, one to translate frames to optical flow and the other to translate optical flow to frames.
  - [ ] To resample the last Conv layer of AlexNet use this [link](https://stackoverflow.com/questions/13242382/resampling-a-numpy-array-representing-an-image)
