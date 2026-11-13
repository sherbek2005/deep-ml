import torch

def matrixmul(a, b) -> torch.Tensor:
    """
    Multiply two matrices using PyTorch.
    Inputs can be Python lists, NumPy arrays, or torch Tensors.
    Returns a 2D tensor of shape (m, n) or a scalar tensor -1 if dimensions mismatch.
    """
    A = torch.tensor(a)
    B = torch.tensor(b)
    if len(A[0]) != len(B):
        return -1
    return A @ B
