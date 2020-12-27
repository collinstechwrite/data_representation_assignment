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




Original Mockup Idea Can be found in the Jupyter Notebook and within py files in the folder called draft_files
https://github.com/g00387822/data_representation_assignment/blob/main/Data_Representation_Assignment_Notebook.ipynb

This programs extract brand names that sell food from the openfoodfacts api<br>
This program then searches newsapi for newspaper headlines using a brand name chosen by the user<br>
This program then translates the newspaper headlines into a language chosen by the user - API key was required<br>
This program then saves the translated results to a spreadsheet called analysis.xlsx<br>
This program then saves the translated results to a MySQL database called news - It is requirement that user has database news setup on their local host and same passwords as within code.<br>
This program will then attempt to convert the spreadsheet results into a webpage called Output.html and load the webbrowser<br>

I ran into some issues and ran out of time trying to move all the moving parts over to FLASK. Instability in one api could have a knock on affect on functionality across other api calls.
