import torch.nn as nn
import torchvision


def get_resnet():
    model = torchvision.models.resnet50()
    num_ftrs = model.fc.in_features
    model.fc = nn.Linear(num_ftrs, 1)

    return model


class MyNet(nn.Module):
    def __init__(self):
        super(MyNet, self).__init__()
        self.pretrained = get_resnet()

    def forward(self, input):
        features = self.pretrained(input)
        return features
