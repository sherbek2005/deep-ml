import torch

def calculate_eigenvalues(matrix: torch.Tensor) -> torch.Tensor:
    """
    Compute eigenvalues of a 2x2 matrix using PyTorch.
    Input: 2x2 tensor; Output: 1-D tensor with the two eigenvalues in descending order (highest to lowest).
    """
    # Your implementation here
    a = 1
    b = -(matrix[0][0] + matrix[1][1])
    c = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    
    d = b*b - 4*a*c
    #if(d < 0)  raise ValueError("Eigenvalues are complex")

    root1 = (-b + torch.sqrt(d)) / (2*a)
    root2 = (-b - torch.sqrt(d)) / (2*a)

    if(root1 < root2): root1,root2 = root2,root1
    return torch.tensor([root1,root2])

    
