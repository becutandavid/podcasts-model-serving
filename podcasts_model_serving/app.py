from fastapi import FastAPI
from ray import serve
from sentence_transformers import SentenceTransformer

app = FastAPI()


@serve.deployment(route_prefix="/model")
@serve.ingress(app)
class SentenceTransformerModel:
    def __init__(self) -> None:
        self.model = SentenceTransformer("all-mpnet-base-v2")

    @app.post("/embeddings", response_model=list[list[float]])
    def root(self, texts: list[str]) -> list[list[float]]:
        """get embeddings for a list of episode descriptions

        Args:
            descriptions (list[str]): list of episode descriptions

        Returns:
            list[float]: list of descriptions
        """
        embeddings = self.model.encode(texts, convert_to_numpy=True)
        return embeddings.tolist()  # type: ignore


model = SentenceTransformerModel.bind()  # type: ignore
