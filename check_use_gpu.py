# Pytorchを用いてGPUが使えるのか確認するだけのプログラム

# PyTorchを宣言する
import torch

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print(f'この環境は{device}が利用されます。')