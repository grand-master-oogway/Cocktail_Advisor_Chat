Hi there

This is a simple cocktail chat bot. It will help you to choose cocktail what you want, taking into account your wishes. 

Setup:
1. Firstly you need to install requirements and cocktail dataset:
   - they are located in requirements.txt
   - just use the following command: "_pip install -r requirements.txt_ "

2. Then you need to create indexes for you data:
   - create directory with name "storage_indexes"
   - and run "_create_indexes.py_" file with a command: "_python create_indexes.py_"
   - it will create indexes for cocktail dataset
  
3. Finally you can run chat:
   - use the following command:  "fastapi dev chat.py"
   - these comand will run the local server, it will start at "_http://127.0.0.1:8000_"
   - after passing this link to your browser, you can get access to the chat-bot
  
![image](https://github.com/user-attachments/assets/413fcef9-7fe2-476e-9fc8-a823bc42975e)
