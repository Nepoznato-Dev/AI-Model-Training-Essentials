# API Reference

## Overview

Quick reference for common APIs and interfaces used in AI engineering.

---

## PyTorch Essentials

### Tensor Operations

```python
import torch

# Create tensors
x = torch.tensor([1, 2, 3])                    # From list
x = torch.zeros(3, 4)                          # Zeros
x = torch.ones(3, 4)                           # Ones
x = torch.rand(3, 4)                           # Random [0,1)
x = torch.randn(3, 4)                          # Random normal
x = torch.arange(0, 10, 2)                     # Range

# Shape operations
x.shape                                        # Get shape
x.view(2, -1)                                  # Reshape
x.unsqueeze(0)                                 # Add dimension
x.squeeze()                                    # Remove dim of size 1
x.transpose(0, 1)                              # Transpose

# Math operations
x + y, x - y, x * y, x / y                     # Element-wise
x @ y                                          # Matrix multiply
torch.matmul(x, y)                             # Matrix multiply
x.sum(), x.mean(), x.max()                     # Reductions
```

### Model Building

```python
import torch.nn as nn

# Common layers
nn.Linear(in_features, out_features)           # Fully connected
nn.Conv2d(in_channels, out_channels, kernel_size)
nn.BatchNorm2d(num_features)
nn.Dropout(p=0.5)
nn.Embedding(num_embeddings, embedding_dim)

# Activations
nn.ReLU(), nn.Sigmoid(), nn.Tanh()
nn.Softmax(dim=-1), nn.GELU()

# Loss functions
nn.CrossEntropyLoss()                          # Classification
nn.MSELoss()                                   # Regression
nn.BCEWithLogitsLoss()                         # Binary classification

# Optimizers
torch.optim.Adam(model.parameters(), lr=0.001)
torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
```

### Training Loop Template

```python
model.train()
for epoch in range(num_epochs):
    for batch_x, batch_y in dataloader:
        optimizer.zero_grad()
        outputs = model(batch_x)
        loss = criterion(outputs, batch_y)
        loss.backward()
        optimizer.step()
```

---

## Transformers Library

### Loading Models

```python
from transformers import AutoModel, AutoTokenizer

# Load pretrained model
model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Tokenize
inputs = tokenizer("Hello world!", return_tensors="pt")
outputs = model(**inputs)
```

### Common Models

| Task | Model | Use Case |
|------|-------|----------|
| Text Classification | `bert-base-uncased` | General purpose |
| Question Answering | `distilbert-base-cased` | Fast QA |
| Text Generation | `gpt2`, `llama-7b` | Generation |
| Translation | `Helsinki-NLP/opus-mt-en-es` | EN→ES translation |
| Summarization | `facebook/bart-large-cnn` | News summarization |

### Pipeline API

```python
from transformers import pipeline

# Quick inference
classifier = pipeline("sentiment-analysis")
result = classifier("I love this!")

generator = pipeline("text-generation", model="gpt2")
result = generator("Once upon a time", max_length=50)

qa = pipeline("question-answering")
result = qa(question="What is AI?", context="AI stands for...")
```

---

## FastAPI

### Basic API

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    value: float

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/items/")
async def create_item(item: Item):
    return {"name": item.name, "value": item.value * 2}
```

### Running the Server

```bash
uvicorn main:app --reload          # Development
uvicorn main:app --host 0.0.0.0    # Production
```

---

## LangChain

### Chains

```python
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for {product}?",
)

chain = LLMChain(llm=OpenAI(), prompt=prompt)
result = chain.run("baby blankets")
```

### Agents

```python
from langchain.agents import load_tools, initialize_agent
from langchain.llms import OpenAI

llm = OpenAI(temperature=0)
tools = load_tools(["serpapi", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description")

result = agent.run("What is the population of France?")
```

---

## Scikit-learn

### Model Training

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
```

### Preprocessing

```python
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Handle missing values
imputer = SimpleImputer(strategy='mean')
X_imputed = imputer.fit_transform(X)

# Encode labels
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)
```

---

## Docker

### Basic Commands

```bash
# Build image
docker build -t my-model .

# Run container
docker run -p 8000:8000 my-model

# List containers
docker ps

# View logs
docker logs <container_id>
```

### Dockerfile Template

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Related Resources

- [PyTorch Documentation](https://pytorch.org/docs/)
- [Transformers Documentation](https://huggingface.co/docs/transformers/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [LangChain Documentation](https://python.langchain.com/)
- [Scikit-learn Documentation](https://scikit-learn.org/)

## See Also

- [Getting Started](../getting_started.md)
- [Deployment Guide](../deployment.md)
- [Troubleshooting](troubleshooting.md)
