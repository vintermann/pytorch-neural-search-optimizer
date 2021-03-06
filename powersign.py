import torch
from torch.optim import Optimizer

required = object()

class PowerSign(Optimizer):
    """Implements PowerSign for PyTorch
    
    Proposed in 'Neural Optimizer Search with Reinforcement Learning' by 
    Irwan Bello, Barret Zoph, Vijay Vasudevan and Quoc Le
    
    https://arxiv.org/abs/1709.07417
    
    Arguments:
      params (iterable): iterable of parameters to optimize or dicts defining
         parameter groups
      lr (float, optional): learning rate (default: 1e-3)
      beta (float, optional): decay for the running exponential average
         (momentum) range (0,1) (default: 0.9)
      weight_decay (float, optional): weight decay (L2 penalty) (default: 0)
    """

    def __init__(self, params, lr=1e-3, beta=0.9, weight_decay=0):
        defaults = dict(lr=lr, beta=beta, weight_decay=weight_decay)
        super(PowerSign, self).__init__(params, defaults)

    def __setstate__(self, state):
        super(PowerSign, self).__setstate__(state)

    def step(self, closure=None):
        """Performs a single optimization step.
        Arguments:
            closure (callable, optional): A closure that reevaluates the model
                and returns the loss.
        """
        loss = None
        if closure is not None:
            loss = closure()

        for group in self.param_groups:
            for p in group['params']:
                if p.grad is None:
                    continue
                grad = p.grad.data
                state = self.state[p]
                
                # State initialization
                if len(state) == 0:
                    # Exponential moving average of gradient values
                    state['exp_avg'] = grad.new().resize_as_(grad).zero_()
                
                exp_avg = state['exp_avg']
                beta = group['beta']
                                
                # Apply weight decay (L2 penalty)
                if group['weight_decay'] != 0:
                    grad = grad.add(group['weight_decay'], p.data)
                
                # Decay the momentum running average coefficient
                exp_avg.mul_(beta).add_(1 - beta, grad)
                
                update = grad.mul(torch.exp(torch.sign(grad) * torch.sign(exp_avg)))
                
                p.data.add_(-group['lr'], update)
        return loss