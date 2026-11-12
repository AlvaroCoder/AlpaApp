# ALPA

Aplicación web MonoLito FastAPI MVC para registro de cultivos agrícolas con soporte de Deep Learning.

## Stack
- **FastAPI** + Jinja2 (MVC server-side rendering)
- **Leaflet.js** + OpenStreetMap (mapa gratuito, sin API key)
- **Leaflet.draw** – delimitación de parcelas en el mapa
- **SQLAlchemy** + SQLite (swappable a PostgreSQL)
- **PyTorch** + OpenCV – reconocimiento de imágenes (placeholder)

## Estructura
```
AlpaApp/
├── app/
│   ├── controllers/     # Rutas FastAPI (MVC – Controller)
│   ├── models/          # Modelos de datos Pydantic
│   ├── schemas/         # Schemas de validación
│   ├── services/        # Lógica de negocio
│   ├── views/templates/ # Templates Jinja2 (MVC – View)
│   ├── static/          # CSS, JS, imágenes
│   └── ml/              # Deep Learning: modelos, preprocesado, inferencia
├── data/
│   ├── uploads/         # Imágenes subidas
│   └── processed/       # Imágenes procesadas
├── tests/
└── requirements.txt
```

## Instalación
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```
Abrir http://localhost:8000

## Flujo de registro
1. **Home** → elegir tipo (transitorio / historial)
2. **Ubicación** → buscar distrito o GPS → dibujar parcela en el mapa
3. **Cultivo** → elegir cultivo transitorio
4. **Rotación** → responder rotación y cultivo anterior → guardar
