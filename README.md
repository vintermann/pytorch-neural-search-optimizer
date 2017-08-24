# Neural Optimizer Search - Optimizer_1

PyTorch implementation of Neural Optimizer Search's Optimizer_1. Based loosely on the implementation by David Dao, torch.optim.adam and one by Deepblue129. 

<p align="center"><img src="imgs/optimizer_1.png" /></p>

## Usage

Import _Optimizer_1_ like any torch.optim Optimizer:

```python
from optimizer_1 import Optimizer_1

optimizer = Optimizer_1(model.parameters(), lr=1e-3, momentum=0.99)
loss.backward()
optimizer.step()
```
