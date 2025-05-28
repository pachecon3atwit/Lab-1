from email.policy import default

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Soccer API"}

@app.get("/player_goals")
async def player_goals(name: str, goals: int):
    return f"Player name: {name} | Goals this season: {goals}"



@app.get("/team_info/{team_name}")
async def team_info(team_name: str):
    return f"{team_name} is a legendary football club!"




















