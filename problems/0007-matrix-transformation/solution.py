import torch

def transform_matrix(A, T, S) -> torch.Tensor:
    """
    Perform the change-of-basis transform T⁻¹ A S and round to 3 decimals using PyTorch.
    Inputs A, T, S can be Python lists, NumPy arrays, or torch Tensors.
    Returns a 2×2 tensor or tensor(-1.) if T or S is singular.
    """
   
    if torch.linalg.det(T) == 0 or torch.linalg.det(S) == 0:
        return torch.tensor([[-1,-1],[-1,-1]])

    T_inverse = torch.linalg.inv(T)
    return T_inverse @ torch.tensor(A)
