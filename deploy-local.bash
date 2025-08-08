#!/bin/bash
# Obtener el entorno desde el primer argumento, por defecto 'dev' si no se pasa
ENVIRONMENT="${1:-dev}"

# Validar que ENVIRONMENT sea 'dev' o 'prod'
if [[ "$ENVIRONMENT" != "dev" && "$ENVIRONMENT" != "prod" ]]; then
  echo "Error: ENVIRONMENT debe ser 'dev' o 'prod'. Valor recibido: '$ENVIRONMENT'"
  exit 1
fi


PROJECT_ID="mangosphere"
REGION="us-central1"
REPO="tottus"
SERVICE_NAME="tottus-${ENVIRONMENT}"
IMAGE_NAME="${SERVICE_NAME}"
IMAGE_URI="${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO}/${IMAGE_NAME}:latest"

# Paso 1: build and push # cambiar por docker en vez de podman
docker build . -t $IMAGE_URI
docker push $IMAGE_URI

# Paso 2: deploy
gcloud run deploy $SERVICE_NAME \
  --image=$IMAGE_URI \
  --region=$REGION \
  --platform=managed \
  --allow-unauthenticated \
  --cpu=1 \
  --memory=2Gi \
  --port=8000

