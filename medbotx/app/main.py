from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router  # Ensure this import is correct
from fastapi.responses import HTMLResponse

app = FastAPI()

# Add this CORS config 👇
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def root():
    return "<h2>Welcome to MedBotX Backend!</h2><p>Go to <a href='/docs'>/docs</a> to test the API.</p>"

# Include your API router
app.include_router(router)



#npm start
#npm run build
