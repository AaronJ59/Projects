"""
This file is all for training and testing a model.
"""

from tqdm import tqdm
import torch

def train_step(model: torch.nn.Module,
               dataloader: torch.utils.data.DataLoader,
               optimizer: torch.optim.Optimizer,
               loss_fn: torch.nn.Module,
               device: torch.device):

  model.train()

  train_loss, train_acc = 0, 0


  for batch, (X, y) in enumerate(dataloader):
    # Send data to target device
    X, y = X.to(device), y.to(device)

    # Do the forward pass
    y_pred_logits = model(X)

    # Calculate the loss
    loss = loss_fn(y_pred_logits, y)
    train_loss = train_loss + loss.item()

    # Optimize the gradient
    optimizer.zero_grad()

    # Loss backwards
    loss.backward()

    # Optimizer step
    optimizer.step()

    # Turn prediction logits to prediction labels
    y_pred_labels = torch.argmax(y_pred_logits, dim=1)

    train_acc = train_acc + ((y_pred_labels == y).sum().item()/len(y_pred_logits))

  # Adjust metrics to get average loss and accuracy per batch
  train_loss = train_loss / len(dataloader)
  train_acc = train_acc / len(dataloader)

  return train_loss, train_acc

def test_step(model: torch.nn.Module,
              dataloader: torch.utils.data.DataLoader,
              loss_fn: torch.nn.Module,
              device: torch.device):

  model.eval()

  test_loss, test_acc = 0, 0

  with torch.inference_mode():
    for batch, (X, y) in enumerate(dataloader):
      X, y = X.to(device), y.to(device)

      y_pred_logits = model(X)

      loss = loss_fn(y_pred_logits, y)
      test_loss = test_loss + loss.item()

      y_pred_labels = torch.argmax(y_pred_logits, dim=1)

      test_acc = test_acc + ((y_pred_labels == y).sum().item()/len(y_pred_labels))

  test_loss = test_loss / len(dataloader)
  test_acc = test_acc / len(dataloader)

  return test_loss, test_acc



def train(model: torch.nn.Module,
          train_dataloader: torch.utils.data.DataLoader,
          test_dataloader: torch.utils.data.DataLoader,
          loss_fn:torch.nn.Module,
          optimizer:torch.optim.Optimizer,
          device: torch.device,
          epochs: int):
  
  results = {"train_loss": [],
             "train_acc" : [],
             "test_loss" : [],
             "test_acc" : []}

  model.to(device)
  print(f"Training the model for {epochs} epochs")
  for epoch in tqdm(range(epochs)):
    train_loss, train_acc = train_step(model=model,
                                       dataloader=train_dataloader,
                                       optimizer=optimizer,
                                       loss_fn=loss_fn,
                                       device=device)
    
    test_loss, test_acc = test_step(model=model,
                                    dataloader=test_dataloader,
                                    loss_fn=loss_fn,
                                    device=device)
    
    print(f"\nEpoch: {epoch + 1} | train_loss: {train_loss:.4f} | train_acc: {train_acc:.4f} | test_loss: {test_loss:.4f} | test_acc: {test_acc:.4f}")

    results["train_loss"].append(train_loss)
    results["train_acc"].append(train_acc)
    results["test_loss"].append(test_loss)
    results["test_acc"].append(test_acc)
  
  return results
