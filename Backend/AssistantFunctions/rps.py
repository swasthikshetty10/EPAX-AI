from random import choice

choices = ["rock","paper","scissor"]
def rps(user):
  user=user.lower()
  if user=="scissors":user="scissor"
  bot = choice(choices)
  # user wins
  if (bot=="rock" and user=="paper") or (bot=="paper" and user=="scissor") or (bot=="scissor" and user=="stone"):
    winner = "user"
  else:
    winner = "bot"
    
  return {"user_choice":user,"bot_choice":bot,"winner":winner}
  

  
