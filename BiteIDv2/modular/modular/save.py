
from pathlib import Path
import torch


def save_model(model: torch.nn.Module,
               target_dir: str,
               model_name: str):

  """
  model: A PyTorch model to save
  target_dir: The directory that you want to save model to
  model_name: Filename of the model. Needs to end with ".pt" or ".pth"

  Example:
  save_model(model=model_1,
             target_dir="models",
             model_name="05_going_modular_tinyvgg_model.pth")
  """

  target_dir_path = Path(target_dir)
  target_dir_path.mkdir(parents=True,
                        exist_ok=True)

  assert model_name.endswith(".pth") or model_name.endswith(".pt")
  model_save_path = target_dir_path / model_name

  # Save the model state_dict()
  print(f"Saving model to: {model_save_path}")
  torch.save(obj=model.state_dict(),
             f=model_save_path)
