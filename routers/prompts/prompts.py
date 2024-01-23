from fastapi import APIRouter, HTTPException

from schema.models import PlayerPromptBase
from services.laminiLMM.lamini import LaminiService

router = APIRouter(prefix="/prompts", tags=["players"])


@router.post("/prompt_player")
def prompt_player(player_prompt: PlayerPromptBase):
    prompt = player_prompt.prompt
    lamini = LaminiService()
    try:
        if 'nba' in prompt.lower():
            return lamini.generate_answer_from_prompt(prompt)
        else:
            return 'Cannot prompt this request.'
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
