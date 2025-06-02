from email.policy import default

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Soccer API!"}

@app.get("/player_goals")
async def player_goals(name: str, goals: int):
    return f"Player name: {name} | Goals this season: {goals}"


@app.get("/team_info/{team_name}")
async def team_info(team_name: str):
    return f"{team_name} is a legendary football club!"


@app.get("/match_score")
async def match_score(home: int, away: int):
    return f"The final score is Home {home} - Away {away}"

class Player(BaseModel):
    name: str
    position: str

@app.post("/register_player")
async def register_player(player: Player):
    return f"Player {player.name} registered as a {player.position}"

@app.get("/stadium/{stadium_name}")
async def stadium_info(stadium_name: str):
    return f"{stadium_name} is a world-class stadium!"

@app.get("/matchday/{match_num}")
async def matchday(match_num: int):
    return f"Matchday Number: {match_num} "

@app.get("/standings")
async def standings(league: str, top: int):
    return f"Showing top {top} teams in the {league} league"

@app.get("/goal/{player}/{number}")
async def goal_info(player: str, number: int):
    return f"{player} has scored {number} goals this season"

class MatchResult(BaseModel):
    home_team: str
    away_team: str
    home_score: int
    away_score: int

@app.post("/submit_match")
async def submit_match(result: MatchResult):
    return f"{result.home_team} {result.home_score} - {result.away_score} {result.away_team}"
