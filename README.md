# iris-classifier-api

A FastAPI service to predict iris flower species (setosa, versicolour, virginica). Trained on an SVM model, and containerized with Docker.

##Installation

Cloning the repository and building the Docker image:

```bash
git clone https://github.com/yourname/iris-classifier-api.git
cd iris-classifier-api
docker build -t iris-species-prediction-api .
```

Usuage

Start the container: 

```bash
docker run -d -p 80:80 iris-species-prediction-api

Prediction request (PowerShell):

```powershell
$body = @{
    sepal_length = 4.9
    sepal_width  = 3.0
    petal_length = 3.2
    petal_width  = 1.4
} | ConvertTo-Json

Invoke-RestMethod -Uri http://127.0.0.1:80/predict -Method Post -ContentType "application/json" -Body $body
```

Or with curl (bash):

```bash
curl -X POST http://127.0.0.1:80/predict \
  -H "Content-Type: application/json" \
  -d '{"sepal_length": 4.9, "sepal_width": 3.0, "petal_length": 3.2, "petal_width": 1.4}'
```

Interactive API docs are available at `http://127.0.0.1:80/docs`.

## Example Output

```json
{
  "predicted_iris_species": "versicolor"
}
```