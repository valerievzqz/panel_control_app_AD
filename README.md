# panel_control_app_AD
Create and deploy a control panel for a web application using cloud services while implementing software practices such as the creation and management of virtual environments(Python) and application developement
---------------------------------------------------------------
## Project Structure
-'notebooks':directoy with jupyter notebook files
-'panel_control_app_AD':main directory with the app code, readme,gitingore,requirements.txt and datasets (using only vehicles_us.csv(demo version is not used))

## Setup and Usage
To set up and use the project, follow these steps:
1. Clone the repository to your local machine. Git:Clone the repo
2. Virtual Environment with its packages (provided in requirements.txt)
    2.1 conda create --name <env_name> python streamlit pandas
    2.2 conda activate <env_name>
    2.3 conda install -n <env_name> nbformats
    2.4 conda install -n <env_name plotly::plotly_express>
3. practice plotly-express in notebook to create histogram and scatter plot
    3.1 pandas(read_csv) and plotly-express(px.histogram,px.scatter) are used

4. app.py (pandas,streamlit,plotly-express)