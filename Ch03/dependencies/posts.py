from fastapi import Request, HTTPException

def check_feedback_length(request: Request):
    feedback = request.query_params["feedback"]
    if len(feedback) < 20:
        raise HTTPException(status_code=403, detail="Feedback must be at least 20 characters long")