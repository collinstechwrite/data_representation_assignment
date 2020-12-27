Use your command prompt to go to a directory that you want to save the github project

At the command prompt type git clone and copy paste the github url of the project<br>
git clone https://github.com/g00387822/data_representation_assignment

Open a new command prompt
Navigate to the folder called 'flask_web_project_for_data_representation'

and run the following commands

python -m venv venv<br>
.\venv\scripts\activate.bat<br>
pip install -r requirements.txt<br>
set FLASK_APP=app.py<br>
flask run<br>

Open your browser and go to your browser to load this url<br>
http://127.0.0.1:5000

You will be able to 

1. Search news headlines by keyword and view analysed results in a Matplotlib graph
2. The program will generate a file call analysis.xlsx to your local folder flask_web_project_for_data_representation
3. The program will update a table stored at a remote MySql database
4. You will be able to view and delete all the rows at the remote MySql database

