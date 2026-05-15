import time as t
import uuid
from Backend.Services.modelLlama import Jarvis
from Backend.Core.Features.LLmModelCore.greetFunc import greet
from Frontend.F_Main import style3_MAIN, animation
from DB.MySQL.wake_db import insert_wake
from DB.MongoDB.MainDB import insert_into_user

style3_MAIN()
animation()

j = Jarvis()

if __name__ == "__main__":
    
    userID = str(uuid.uuid4())
    
    greet()

    while True:
        # Listen only for wake word
        wake_word = j.listen_wake_word()

        if wake_word:
            # Insert wake word in DB (if needed)
            insert_wake(wake_word)

            
            j.speak("Yes sir, i am listening")

            # Run main Jarvis conversation
            query = j.take_command()
            insert_into_user(user_id=userID,query_user=query)

            if query != "none":
                result = j.JarvisRun(query)

                if result == "exit":
            # After finishing, loop continues to listen again
                    break

        t.sleep(0.2)