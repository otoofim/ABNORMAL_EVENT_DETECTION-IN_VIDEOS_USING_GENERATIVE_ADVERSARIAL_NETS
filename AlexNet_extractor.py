import torch.nn as nn
import torch.utils.model_zoo as model_zoo
import cv2
import torch
from PIL import Image
from torchvision import transforms
from torchvision import models


__all__ = ['AlexNet', 'alexnet']


model_urls = {
    'alexnet': 'https://download.pytorch.org/models/alexnet-owt-4df8aa71.pth',
    'alexnet_local': './alexnet-owt-4df8aa71.pth'
}


class AlexNet(nn.Module):

    def __init__(self, num_classes=1000):
        super(AlexNet, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=11, stride=4, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(64, 192, kernel_size=5, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(192, 384, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(384, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
        )
        self.classifier = nn.Sequential(
            nn.Dropout(),
            nn.Linear(256 * 6 * 6, 4096),
            nn.ReLU(inplace=True),
            nn.Dropout(),
            nn.Linear(4096, 4096),
            nn.ReLU(inplace=True),
            nn.Linear(4096, num_classes),
        )


    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), 256 * 6 * 6)
        x = self.classifier(x)
        return x

class AlexNetConv5(nn.Module):
	def __init__(self, original_model):
	    super(AlexNetConv5, self).__init__()
		# stop at conv5
	    self.features = nn.Sequential(*list(original_model.features.children())[:-1])
        self.preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])


	def forward(self, x):
	    if not(self.training):
	        x = self.preprocess(x)
	        x = x.unsqueeze(0) # create a mini-batch as expected by the model
	    x = self.features(x)
	    return x





def alexnet(pretrained=False, **kwargs):
    r"""AlexNet model architecture from the
    `"One weird trick..." <https://arxiv.org/abs/1404.5997>`_ paper.

    Args:
        pretrained (bool): If True, returns a model pre-trained on ImageNet
    """
    model = AlexNet(**kwargs)
    if pretrained:
        model.load_state_dict(model_zoo.load_url(model_urls['alexnet_local']))
    return model



def AlexNetConv5_getFeatures():
	original_model = alexnet(True)
	model = AlexNetConv5(original_model)

	input_image = Image.open("./test.jpeg")
	model.eval()
	if torch.cuda.is_available():
	    input_batch = input_batch.to('cuda')
	    model.to('cuda')
	model(input_image)
