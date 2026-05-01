from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 🔥 Safe imports (prevents crash if one route fails)
from app.routes import auth
from app.routes import project
from app.routes import task
from app.routes import dashboard

app = FastAPI(
    title="Team Task Manager API",
    version="1.0.0"
)

# 🔥 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔥 Routes
app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(project.router, prefix="/api/projects", tags=["Projects"])
app.include_router(task.router, prefix="/api/tasks", tags=["Tasks"])
app.include_router(dashboard.router, prefix="/api/dashboard", tags=["Dashboard"])

# 🔥 Root
@app.get("/")
def root():
    return {"message": "API running 🚀"}
