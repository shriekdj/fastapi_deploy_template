# FastAPI Deploy Template

**A plug‑and‑play template for deploying FastAPI projects with multiple options: ASGI, WSGI, and cloud platforms.**  
Perfect for quickly getting your FastAPI app production‑ready without worrying about boilerplate deployment scripts.

## Features

- **Standardized Structure:** Place your FastAPI app in `app/main.py` with your instance named `app`.
- **ASGI Support:** `asgi.py` ready for Uvicorn or any ASGI server.
- **WSGI Adapter:** `wsgi.py` allows running with WSGI providers using `a2wsgi`.
- **Uvicorn Runner:** Easily start your server via `uvicorn_runner.py`.
- **Cloud Examples:** Templates for deploying on [Render](https://render.com/) (`render.yaml`) and [Railway](https://railway.app/) (`railway.json`).
- **Requirements:** `requirements.txt` includes fastapi, uvicorn, and optionally `a2wsgi` for WSGI compatibility.

## Structure

```text
root_project/
│
├── app/
│   └── main.py         # FastAPI app instance must be named 'app'
├── asgi.py             # ASGI entry point
├── wsgi.py             # WSGI adapter (requires a2wsgi)
├── uvicorn_runner.py   # Uvicorn runner script
├── requirements.txt    # Main dependencies
├── render.yaml         # Render cloud deployment config example
├── railway.json        # Railway deployment config example
```

## Usage

### Basic Run (Local, ASGI)

```bash
# Install requirements
pip install -r requirements.txt

# Run using uvicorn
uvicorn app.main:app --reload
```

### ASGI Entrypoint (Production)

Use included `asgi.py` for deployment scripts:
```bash
uvicorn asgi:app
```

### WSGI Entrypoint (Legacy Platforms)

If your platform only supports WSGI:
```bash
pip install a2wsgi
gunicorn wsgi:application
```
- `wsgi.py` uses a2wsgi to wrap FastAPI for WSGI servers.

### Cloud Platforms

#### Render

- Deploy using the example `render.yaml` file, which sets up your build and run commands.

#### Railway

- Use `railway.json` to configure deployment pipeline for Railway.

### Custom Runner

Start with included script:
```bash
python uvicorn_runner.py
```

## Requirements

- Python 3.8+
- All packages listed in `requirements.txt`
    - `fastapi`
    - `uvicorn`
    - `a2wsgi` (required only for WSGI deployment)

## Customizing

- Place your FastAPI routes, logic, and extensions inside `app/main.py`, ensuring the instance is named `app`.
- Modify `render.yaml` or `railway.json` with your repo details, environment variables, etc.

## License

MIT License

***

You can copy-paste this directly to your `README.md`! It’s structured to be beginner-friendly but covers all the technical detail a deployer needs.

[1](https://github.com/shriekdj/fastapi_deploy_template)
