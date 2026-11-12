"""
ML Service – placeholder for image recognition and deep learning inference.
Replace with actual model loading when ready.
"""
from pathlib import Path
from app.config import settings


class MLService:
    """Wrapper for loading and running deep learning models."""

    def __init__(self):
        self.model = None
        self.model_dir: Path = settings.model_dir

    def load_model(self, model_name: str):
        """Load a trained model from disk."""
        model_path = self.model_dir / model_name
        if not model_path.exists():
            raise FileNotFoundError(f"Model not found: {model_path}")
        # TODO: torch.load(model_path) or similar
        pass

    def predict_image(self, image_path: Path) -> dict:
        """Run inference on a single image and return predictions."""
        if self.model is None:
            return {"error": "Model not loaded"}
        # TODO: preprocess → inference → postprocess
        return {"predictions": []}


ml_service = MLService()
