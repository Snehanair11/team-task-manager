from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth, project, task, dashboard   # 👈 add dashboard here

app = FastAPI(
    title="Team Task Manager API",
    version="1.0.0"
)

# 🔥 CORS (needed for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(project.router, prefix="/api/projects", tags=["Projects"])
app.include_router(task.router, prefix="/api/tasks", tags=["Tasks"])
app.include_router(dashboard.router, prefix="/api/dashboard", tags=["Dashboard"])  # 👈 THIS LINE

# Health check
@app.get("/")
def root():
    return {"message": "API running 🚀"}