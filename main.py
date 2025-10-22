import uvicorn

PROJECT_ENVIRONMENT = "development"

if __name__ == "__main__":
    # print(settings.environment)
    if PROJECT_ENVIRONMENT == "production":
        uvicorn.run("app.main:app", host="127.0.0.1", port=8000, workers=4)
    else:
        uvicorn.run(
            "app.main:app",
            host="127.0.0.1",
            port=8000,
            log_level="info",
            reload=True,
        )
