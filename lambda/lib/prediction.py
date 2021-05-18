import io
from typing import Any, Dict, List

from PIL import Image
import torch
import torch.nn as nn
import torchvision

from lib import models


def predict(data: Dict[str, List[Any]]) -> float:
    byte_img: bytes = data["image"][0]
    img: torch.Tensor = get_img_tensor(byte_img)

    model: nn.Module = models.MyNet()
    # 重みの読み込み
    # weight_path = os.path.join("lib", "model.pth")
    # model.load_state_dict(torch.load(weight_path, map_location=torch.device("cpu")))
    model.eval()

    output: torch.Tensor = model(img)

    return output.item()


def get_transform():
    transforms = []
    transforms.append(torchvision.transforms.Resize((224, 224)))

    transforms.append(torchvision.transforms.ToTensor())
    transforms.append(
        torchvision.transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    )
    compose = torchvision.transforms.Compose(transforms)

    return compose


def get_img_tensor(byte_img: bytes) -> torch.Tensor:
    transform = get_transform()
    pil_img = Image.open(io.BytesIO(byte_img)).convert("RGB")
    img: torch.Tensor = transform(pil_img).unsqueeze(0)
    return img
