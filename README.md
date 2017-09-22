# PowerSign

PyTorch implementation of the PowerSign optimizer, as described in the paper

Neural Optimizer Search with Reinforcement Learning
https://arxiv.org/abs/1709.07417

by Google Brain researchers Irwan Bello, Barret Zoph, Vijay Vasudevan and Quoc V. Le.

This is an independent pytorch implementation, based loosely on the implementation by David Dao, torch.optim.adam and 
one by Deepblue129. 

## Usage

Import _PowerSign_ like any torch.optim Optimizer:

```python
from powersign import PowerSign

optimizer = Optimizer_1(model.parameters(), lr=1e-3, momentum=0.99)
loss.backward()
optimizer.step()
```
