import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Adm_pro3.csv") 

st.set_page_config(
    page_title="Student Admission Data Analysis",
    layout="wide",
    initial_sidebar_state="expanded"
)

with st.sidebar:
    st.title("Filters")
    student_type = st.selectbox("Select Student Type:", ['AllotedCategory', 'Gender', 'Scholarship', 'District', 'Caste'])
    selected_value = st.selectbox(f"Select {student_type}:", df[student_type].dropna().unique())

filtered_df = df[df[student_type] == selected_value]


tabs = st.tabs([
    "Alloted Category vs Caste",
    "Student Distribution Across Districts",
    "Gender Distribution",
    "Scholarship Status",
    "Rank by Caste",
    "Filtered Data"
])

with tabs[0]:  
    st.subheader("Students from Different Castes in Each Category")
    if "AllotedCategory" in df.columns and "Caste" in df.columns:
        caste_counts = df.groupby(["AllotedCategory", "Caste"]).size().unstack(fill_value=0)
        fig, ax = plt.subplots(figsize=(12, 6))
        caste_counts.plot(kind="bar", ax=ax, colormap="tab20")
        plt.xlabel("Alloted Category")
        plt.ylabel("Number of Students")
        plt.xticks(rotation=0)
        st.pyplot(fig)
    else:
        st.error("Missing columns: 'AllotedCategory' or 'Caste'")

with tabs[1]:  
    st.subheader("Student Distribution Across Districts")
    if "District" in df.columns:
        district_counts = df["District"].value_counts()
        fig, ax = plt.subplots(figsize=(10, 6))
        district_counts.plot(kind="bar", ax=ax, color="skyblue")
        plt.xlabel("District")
        plt.ylabel("Number of Students")
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.error("Missing column: 'District'")

with tabs[2]:  
    st.subheader("Gender Distribution")
    if "Gender" in df.columns:
        gender_counts = df["Gender"].value_counts()
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.pie(gender_counts, labels=gender_counts.index, autopct ="%1.1f%%", colors=["lightblue", "pink"])
        st.pyplot(fig)
    else:
        st.error("Missing column: 'Gender'")

with tabs[3]:  
    st.subheader("Scholarship Status Distribution")
    if "Scholarship" in df.columns:
        scholarship_counts = df["Scholarship"].value_counts()
        fig, ax = plt.subplots(figsize=(8, 6))
        scholarship_counts.plot(kind="bar", ax=ax, color=["green", "red"])
        plt.xlabel("Scholarship Status")
        plt.ylabel("Number of Students")
        st.pyplot(fig)
    else:
        st.error("Missing column: 'Scholarship'")

with tabs[4]:  
    st.subheader("Rank Distribution Across Castes")
    if "Caste" in df.columns and "Rank" in df.columns:
        fig, ax = plt.subplots(figsize=(10, 6))
        df.boxplot(column="Rank", by="Caste", ax=ax)
        plt.xlabel("Caste")
        plt.ylabel("Rank")
        plt.title("Rank Distribution Across Castes")
        st.pyplot(fig)
    else:
        st.error("Missing columns: 'Caste' or 'Rank'")
with tabs[5]:  
    st.subheader(f"Students with {student_type}: {selected_value}")
    st.dataframe(filtered_df)


st.write("Analysis Completed")