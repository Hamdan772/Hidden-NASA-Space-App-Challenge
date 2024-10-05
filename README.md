

### **Step 1: Install Thonny**

1. Go to the official Thonny website: [https://thonny.org](https://thonny.org)
2. Download and install the version appropriate for your operating system (Windows, macOS, or Linux).
3. Follow the prompts to complete the installation process.

---

### **Step 2: Open Thonny**

1. Once installed, open Thonny from your desktop or start menu.
2. Thonny’s interface should now be visible.

---

### **Step 3: Install Required Libraries**

To run the project, we need to install several Python libraries. We’ll be doing this through Thonny.

1. **Open the terminal in Thonny:**
   - In Thonny, click on **Tools** in the top menu.
   - Select **Manage Packages** from the dropdown.

2. **Install the Required Libraries:**
   In the "Manage packages" window, you will need to install all the necessary libraries:
   
   Type in the following libraries one by one and click **Install** for each:
   
   - **streamlit**
   - **pandas**
   - **matplotlib**
   - **plotly**
   - **numpy**
   - **seaborn**
   
   Example:
   - Search for `streamlit` in the search box, select it from the list, and then click **Install**.
   - Repeat this process for each library until all are installed.

---

### **Step 4: Set Up a Virtual Environment (Optional but Recommended)**

For better management of dependencies, we recommend setting up a virtual environment (though not necessary for beginners):

1. **Create a virtual environment:**
   - Open the terminal in Thonny by clicking on **View > Show Shell**.
   - In the terminal, type the following command to create a virtual environment:

     ```bash
     python -m venv venv
     ```

2. **Activate the virtual environment:**
   - For **Windows**, type:

     ```bash
     venv\Scripts\activate
     ```

   - For **Mac/Linux**, type:

     ```bash
     source venv/bin/activate
     ```

3. **Install libraries inside the virtual environment:**
   - Once the environment is activated, install the libraries again (only inside the environment) using:

     ```bash
     pip install streamlit pandas matplotlib plotly numpy seaborn
     ```

---

### **Step 5: Open the Project in Thonny**

1. **Open the Project File:**
   - Click on **File** > **Open**.
   - Navigate to the folder where the project file (e.g., `space_experiment_visualization.py`) is located.
   - Select the file and click **Open**.

---

### **Step 6: Run the Streamlit App**

1. **Open the Thonny Shell** (if it’s not already open):
   - Click on **View > Show Shell** if the shell is hidden.

2. **Run the App:**
   - In the **Thonny Shell**, type the following command to run the Streamlit app:

     ```bash
     streamlit run space_experiment_visualization.py
     ```

3. **Open in Browser:**
   - Once the app is running, Thonny will display a link in the shell.
   - Copy that link (it usually looks like `http://localhost:8501`), paste it into your web browser’s address bar, and press Enter.

   Your app should now open and display the visualizations!

---

### **Step 7: Interact with the App**

Now that the app is running, you can:

- Interact with the sidebar to switch between datasets, themes, and experiment options.
- Visualize the space experiment data through interactive charts and graphs.

---

### **Step 8: (Optional) Add Your Own Experiment**

To add your own experiment to the app:

1. Open the **Add Experiment** feature in the sidebar.
2. Input the experiment data, including the number of samples, groups, and treatments.
3. Submit the data to visualize it alongside existing NASA experiments.

---

### **Summary of Key Steps**

1. Install Thonny.
2. Install necessary libraries (e.g., `streamlit`, `pandas`, etc.) through Thonny’s package manager.
3. Optionally set up a virtual environment for managing dependencies.
4. Open your project file in Thonny.
5. Run the app using the command: `streamlit run space_experiment_visualization.py`.
6. Interact with the app via your web browser.

---

