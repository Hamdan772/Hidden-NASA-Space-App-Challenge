Here’s a step-by-step guide to opening and running the Python-based visualization tool for space biological experiments using **Thonny**:

### Step 1: Install Thonny
1. Download and install Thonny IDE from [thonny.org](https://thonny.org/).
2. Open the Thonny IDE after installation is complete.

### Step 2: Install Python Libraries
Before running the code, you need to install several libraries. These can be installed directly within Thonny:
1. Open **Thonny**.
2. Go to **Tools** > **Manage Packages...**.
3. In the "Package name" field, type the following libraries one at a time and click **Install**:
   - `pandas`
   - `seaborn`
   - `matplotlib`
   - `streamlit`

You can also install all libraries at once via Thonny’s terminal:
1. Open Thonny.
2. Go to **View** > **Show Shell**.
3. Type the following command into the shell and press **Enter**:

   ```bash
   pip install pandas seaborn matplotlib streamlit
   ```

### Step 3: Add Data Files
1. Download the cleaned CSV files (`cleaned_osd_379.csv` and `cleaned_osd_665.csv`).
2. Place these files in a folder called `data` inside the same directory where your Python script resides.

### Step 4: Open and Run the Code in Thonny
1. Download or write the Python code for the tool in Thonny.
2. Save the script with the name `space_experiment_visualization.py` (or any preferred name).
3. Press **F5** or click on the green **Run** button at the top to run the script.
4. **Streamlit** will prompt you with a message like:

   ```
   Warning: to view this Streamlit app on a browser, run it with the following
   command:
   
   streamlit run <script_name>.py
   ```

### Step 5: Run Streamlit in a Web Browser
To run the Streamlit app and view the visualizations in a web browser:
1. Open **Thonny’s Shell** (located at the bottom).
2. In the **Shell**, type:

   ```bash
   streamlit run space_experiment_visualization.py
   ```

3. Press **Enter**.
4. A web browser window will open automatically with your visualizations, or a link will appear. Click the link or copy-paste it into a web browser to view your app.

Now you can view and interact with the space experiment visualization tool!
