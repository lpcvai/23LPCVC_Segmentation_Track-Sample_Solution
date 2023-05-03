import torch

def clear_gpu_memory():
    torch.cuda.empty_cache()

if __name__ == "__main__":
    clear_gpu_memory()