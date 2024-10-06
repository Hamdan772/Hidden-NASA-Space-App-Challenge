YOUTUBE VIDEO - 

### STEP 0: INSTALL PYTHON

### **Step 1: Install PyCharm Community Edition**

1. Go to the official PyCharm website: [https://www.jetbrains.com/pycharm/download](https://www.jetbrains.com/pycharm/download).
2. Download the **Community Edition** (which is free).
3. Follow the prompts to install PyCharm on your operating system (Windows, macOS, or Linux).

---

### **Step 2: Open PyCharm and Create a New Project**

1. **Open PyCharm** after installation.
2. **Create space_experiment_visualization.py**:
   - Click on **space_experiment_visualization.py** on the welcome screen.
   - Choose a location for your project.
   - For the **Environment**, select **New environment using Virtualenv**.
   - Check if the base interpreter is set to the correct Python version installed on your system.
   - Click **Create**.

---

### **Step 3: Install Required Libraries**

Once your project is created, you'll need to install several libraries required to run the app.

1. **Open the Terminal in PyCharm**:
   - At the bottom of PyCharm, click on **Terminal** to open a command-line interface inside PyCharm.

2. **Install the Required Libraries**:
   Run the following command in the terminal to install all the required Python packages:

   ```bash
   pip install streamlit pandas matplotlib plotly numpy seaborn
   ```

This command installs the necessary libraries:

- `streamlit` for running the web app.
- `pandas` for data manipulation.
- `matplotlib` and `seaborn` for plotting.
- `plotly` for interactive plots.
- `numpy` for numerical computations.

---

### **Step 4: Open the Python File**

1. Once the project is set up, **OPEN THE NASA SPACE APP.PY IN GITHUB AND COPY THE TEXT** (e.g., `space_experiment_visualization.py`) into the project folder you created.
   
2. **Open the Python file**:
   - In PyCharm’s left-hand **Project** pane, find and double-click on the file (e.g., `space_experiment_visualization.py`) to open it in the editor.

---

### **Step 5: Run the Streamlit App**

To run the app using **Streamlit**, we need to execute a command in the terminal.

1. **Open the Terminal** (if it's not already open):
   - At the bottom of PyCharm, click on the **Terminal** tab.

2. **Run Streamlit**:
   In the terminal, type the following command to start the Streamlit server:

   ```bash
   streamlit run space_experiment_visualization.py
   ```

3. **Open in Browser**:
   - Once the app starts, you will see a link in the terminal that looks something like `http://localhost:8501`.
   - Copy this link, paste it into your browser’s address bar, and hit **Enter**.
   - Your Streamlit app will now open in the browser.

---

### **Step 6: Interact with the App**

Now that the app is running, you can interact with it as follows:

1. **Use the Sidebar**:
   - The sidebar provides options to switch between datasets (e.g., OSD-379, OSD-665) and visualizations.
   
2. **Visualize Data**:
   - View different data visualizations like bar charts, interactive plots, and more.
   
3. **Add New Experiment**:
   - In the sidebar, use the **Add Experiment** feature to input custom data for new experiments and visualize them.

---

### **Step 7: (Optional) Create and Activate a Virtual Environment**

Although this step is optional, it’s highly recommended for managing dependencies in Python projects.

1. **Create a virtual environment**:
   - If you didn’t create one during project setup, open the **Terminal** and run:

     ```bash
     python -m venv venv
     ```

2. **Activate the virtual environment**:
   - For **Windows**, run:

     ```bash
     venv\Scripts\activate
     ```

   - For **macOS/Linux**, run:

     ```bash
     source venv/bin/activate
     ```

3. **Reinstall the libraries in the virtual environment** (if needed):

   ```bash
   pip install streamlit pandas matplotlib plotly numpy seaborn
   ```

4. After activating the virtual environment, run the app again by typing:

   ```bash
   streamlit run space_experiment_visualization.py
   ```

---

### **Step 8: Troubleshooting Common Issues**

1. **Error: ModuleNotFoundError: No module named 'streamlit'**:
   - If you encounter this error, it means Streamlit is not installed. Make sure you have installed all the necessary libraries using `pip install streamlit`.

2. **Python Interpreter**:
   - If PyCharm can’t find Python, make sure your project’s interpreter is correctly set up by going to **File** > **Settings** > **Project: YourProject** > **Python Interpreter** and selecting the correct interpreter.

---

### **Summary of Key Steps**

1. Install PyCharm.
2. Create a new project with a virtual environment (optional but recommended).
3. Install required libraries (`streamlit`, `pandas`, etc.).
4. Open the project file in PyCharm.
5. Run the app using `streamlit run space_experiment_visualization.py`.
6. Open the Streamlit app in a browser.
7. Interact with the app and add new experiments.

---
