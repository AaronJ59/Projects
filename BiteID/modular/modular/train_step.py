
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
    loss.backwards()

    # Optimizer step
    optimizer.step()

    # Turn prediction logits to prediction labels
    y_pred_labels = torch.argmax(y_pred_logits, dim=1)

    train_acc = train_acc + ((y_pred_labels == y).sum().item()/len(y_pred_logits))

  # Adjust metrics to get average loss and accuracy per batch
  train_loss = train_loss / len(dataloader)
  train_acc = train_acc / len(dataloader)

  return train_loss, train_acc



