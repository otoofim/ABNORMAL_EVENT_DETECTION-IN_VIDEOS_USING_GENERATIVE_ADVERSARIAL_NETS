64bit Linux binaries for ECCV 2004 optical flow method

Copyright (c) 2009 Thomas Brox

------------------------------
Terms of use
------------------------------

This program is provided for research purposes only. Any commercial
use is prohibited. If you are interested in a commercial use, please 
contact the copyright holder. 

This program is distributed WITHOUT ANY WARRANTY. 

If you used this program in your research work, you must cite the 
following publication:

T. Brox, A. Bruhn, N. Papenberg, J. Weickert: 
High accuracy optical flow estimation based on a theory for warping, 
European Conference on Computer Vision (ECCV), Springer, LNCS, Vol. 3024, 
25-36, May 2004. 

------------------------------
Usage
------------------------------

Run with default parameters sigma = 0.9, alpha = 80, gamma = 5 by calling:
./of image1 image2
This will compute the flow between image1.ppm and image2.ppm (do not write 
the extension .ppm). The input images must be images in the binary PPM 
format (P6). Please convert any other image formats into PPM using convert 
or mogrify. 

To specifiy other parameters use one of these:
./of image1 image2 sigma
./of image1 image2 sigma alpha
./of image1 image2 sigma alpha gamma

There is one small change to the ECCV method: a separate robust function 
is used for the color and gradient constancy term, as noted in 
A. Bruhn, J. Weickert: Towards Ultimate Motion Estimation: Combining Highest 
Accuracy with Real-Time Performance, ICCV 2005. 

See Middlebury flow page: 
http://vision.middlebury.edu/flow/submit/
for description of the flo-format.

The ppm result is for checking the result visually. Depending on the size
of the flow vectors, the visualization might not show all details. In this
case you should use your own visualization method. 

------------------------------
Bugs
------------------------------

Please report bugs to Thomas Brox
