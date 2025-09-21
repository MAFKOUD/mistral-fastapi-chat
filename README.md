

Petit projet de démonstration utilisant **FastAPI** et le SDK Python de **Mistral AI**.  
Ce projet fait partie de ma candidature pour le stage chez **Mistral AI**.

---

## Installation

Cloner le repo et installer les dépendances :

```bash
git clone https://github.com/MAFKOUD/mistral-fastapi-chat.git
cd mistral-fastapi-chat
python -m venv venv
venv\Scripts\activate   
```

---

## Configuration

Définir la variable d’environnement avec votre clé API Mistral :

### Windows (CMD)

```cmd
set MISTRAL_API_KEY=ta_clef_api
```

---

## Lancement du serveur

```bash
uvicorn main:app --reload
```

Une fois lancé, ouvrir Swagger UI :
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

##  Exemple d’appel avec `curl`

```bash
curl -X POST "http://127.0.0.1:8000/chat" ^
  -H "Content-Type: application/json" ^
  -d "{\"message\": \"Bonjour Mistral\"}"
```

Réponse attendue :

```json
{"reply": "Bonjour! Comment ça va? ..."}
```

---

##  Tests

Exécuter les tests avec :

```bash
pytest -v
```

---

##  Technologies utilisées

* [FastAPI](https://fastapi.tiangolo.com/)
* [Uvicorn](https://www.uvicorn.org/)
* [Mistral AI Python SDK](https://github.com/mistralai/client-python)
* [Pytest](https://pytest.org/)





