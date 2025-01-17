
import torch

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

      test_acc = test_acc + ((y_pred_labels == y).sum().item()/len(y_pred_logits))

  test_loss = test_loss / len(dataloader)
  test_acc = test_acc / len(dataloader)

  return test_loss, test_acc
