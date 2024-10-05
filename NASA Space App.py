import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Set a dark theme for plots
plt.style.use('dark_background')

# Sample data for OSD-379 and OSD-665
data_osd_379 = {
    'Group': ['Mice in Space', 'Control Mice'],
    'Liver Size (cm^2)': [2.5, 3.0],
}

data_osd_665 = {
    'Group': ['Mice in Space', 'Control Mice'],
    'Muscle Mass (g)': [1.2, 1.5],
}

# Additional NASA experiments
additional_experiments = {
    'Experiment': [
        'A Microgravity Investigation of Cement Solidification (OSD-705)',
        'Effects of Microgravity on Stem Cell Behavior (OSD-782)',
        'Tissue Regeneration in Microgravity (OSD-689)',
    ],
    'Group Size': [6, 8, 5],
    'Duration (days)': [30, 28, 25],
}

# Initialize session state for storing user-added experiments
if 'experiments' not in st.session_state:
    st.session_state.experiments = []


# Function to add a new experiment
def add_experiment(name, group_size, duration, description, date):
    new_experiment = {
        'Name': name,
        'Group Size': group_size,
        'Duration (days)': duration,
        'Description': description,
        'Date Conducted': date
    }
    st.session_state.experiments.append(new_experiment)
    st.success(f"Experiment '{name}' added successfully!")


# Function to display the sidebar
def display_sidebar():
    st.sidebar.title("Space Experiment Visualization")

    # Input fields for adding an experiment
    experiment_name = st.sidebar.text_input("Add Your Experiment Name:")
    group_size = st.sidebar.number_input("Group Size", min_value=1, max_value=20, value=5)
    duration = st.sidebar.number_input("Duration (days)", min_value=1, max_value=100, value=30)
    experiment_description = st.sidebar.text_area("Experiment Description:")
    experiment_date = st.sidebar.date_input("Date Conducted:")

    if st.sidebar.button("Add Experiment"):
        if experiment_name:
            add_experiment(experiment_name, group_size, duration, experiment_description, experiment_date)
        else:
            st.error("Please enter a valid experiment name.")

    # Download added experiments as CSV
    if st.sidebar.button("Download Experiments as CSV"):
        if st.session_state.experiments:
            exp_df = pd.DataFrame(st.session_state.experiments)
            csv = exp_df.to_csv(index=False).encode('utf-8')
            st.sidebar.download_button(
                label="Download CSV",
                data=csv,
                file_name='user_experiments.csv',
                mime='text/csv'
            )
        else:
            st.sidebar.error("No experiments available to download.")

    # Display existing experiments
    st.sidebar.subheader("Existing Experiments")
    st.sidebar.write("OSD-379: Rodent Research Reference Mission-1")
    st.sidebar.write("OSD-665: Rodent Research-23")
    st.sidebar.write("Other NASA Experiments:")
    for exp in additional_experiments['Experiment']:
        st.sidebar.write(exp)

    # Show user-added experiments
    st.sidebar.subheader("Your Added Experiments")
    if st.session_state.experiments:
        exp_df = pd.DataFrame(st.session_state.experiments)
        st.sidebar.dataframe(exp_df)

        # Option to delete selected experiment
        selected_exp = st.sidebar.selectbox("Select Experiment to Delete",
                                            list(range(len(st.session_state.experiments))), index=-1)
        if st.sidebar.button("Delete Selected Experiment"):
            if selected_exp != -1:
                del st.session_state.experiments[selected_exp]
                st.sidebar.success("Experiment deleted successfully!")
    else:
        st.sidebar.write("No experiments added yet.")


# Function to display summary statistics
def display_summary_stats(data, label):
    st.subheader(f"{label} Summary Statistics")
    df = pd.DataFrame(data)
    st.write(df.describe())


# Function to create interactive plots using Plotly
def create_interactive_plots():
    st.title("Biological Experiments in Space")
    st.write(
        "This tool visualizes biological experiments performed in space, "
        "providing insights into the effects of microgravity on various biological systems."
    )

    # OSD-379 plot
    st.subheader("OSD-379: Rodent Research Reference Mission-1")
    st.write(
        "Mice flew on the International Space Station for 22-40 days, "
        "with liver changes compared to similar mice that remained on Earth."
    )
    df_osd_379 = pd.DataFrame(data_osd_379)
    fig_379 = px.bar(df_osd_379, x='Group', y='Liver Size (cm^2)', title='Liver Size Comparison in OSD-379')
    st.plotly_chart(fig_379)

    # OSD-665 plot
    st.subheader("OSD-665: Rodent Research-23")
    st.write(
        "Mice flew on the International Space Station for 38 days, "
        "with leg muscle changes compared to similar mice that remained on Earth."
    )
    df_osd_665 = pd.DataFrame(data_osd_665)
    fig_665 = px.bar(df_osd_665, x='Group', y='Muscle Mass (g)', title='Muscle Mass Comparison in OSD-665')
    st.plotly_chart(fig_665)

    # Additional NASA experiments plot
    st.subheader("Additional NASA Experiments")
    st.write("This graph displays the group sizes of additional NASA experiments.")
    exp_df = pd.DataFrame(additional_experiments)
    fig_additional = px.bar(exp_df, x='Experiment', y='Group Size', title='Group Sizes of Additional NASA Experiments')
    st.plotly_chart(fig_additional)

    # Display summary statistics for additional experiments
    display_summary_stats(additional_experiments, "Additional NASA Experiments")


# Main application flow
def main():
    display_sidebar()
    create_interactive_plots()


# Run the application
if __name__ == "__main__":
    main()
