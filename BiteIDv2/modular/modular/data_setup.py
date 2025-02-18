
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import os

NUM_WORKERS = os.cpu_count()

def create_dataloaders(
    train_dir: str,
    test_dir: str,
    transform: transforms.Compose,
    num_workers: int=NUM_WORKERS,
    batch_size=32):

  """
  Creates training and testing dataloaders
  """

  # Create datasets
  train_data = datasets.ImageFolder(train_dir, transform=transform)
  test_data = datasets.ImageFolder(train_dir, transform=transform)

  class_names = train_data.classes

  # Create dataloaders
  train_dataloader = DataLoader(train_data, batch_size=batch_size, shuffle=True, num_workers=num_workers, pin_memory=True)
  test_dataloader = DataLoader(test_data, batch_size=batch_size, shuffle=False, pin_memory=True)

  return train_dataloader, test_dataloader, class_names
