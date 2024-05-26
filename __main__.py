"""
This is the main file where the program is start 
"""

def getUser(request: http.request) -> http.response:
  try: 
    request.getUser();
  except ValueError:
    print("What kinda error that was")
  else:
    print("user fetched")

def main() -> None:
  getUser(request)
  
