import io
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from database import engine

# Load student data from the database
def get_student_data():
    query = "SELECT id, firstname, lastname, dob, gender, department, regNumber FROM students"
    df = pd.read_sql(query, engine)
    df['dob'] = pd.to_datetime(df['dob'])
    return df

# Generate Pie Chart (Birth Month Distribution)
def plot_pie_chart():
    df = get_student_data()
    df['birth_month'] = df['dob'].dt.month_name()
    birth_counts = df['birth_month'].value_counts()

    plt.figure(figsize=(8, 8))
    plt.pie(
        birth_counts, labels=birth_counts.index, autopct='%1.1f%%', startangle=90, 
        colors=sns.color_palette("pastel")
    )
    plt.title('Student Birth Month Distribution', fontsize=14, fontweight='bold')

    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    return buf

# Generate Line Chart (Birth Year Trend)
def plot_birth_year_trend():
    df = get_student_data()
    
    # Extract birth year
    df['birth_year'] = df['dob'].dt.year
    year_counts = df['birth_year'].value_counts().sort_index()

    # Plot
    plt.figure(figsize=(8, 8))
    plt.plot(year_counts.index, year_counts.values, marker='o', color='blue', linestyle='-', linewidth=2)
    plt.title('Student Birth Year Trend', fontsize=14, fontweight='bold')
    plt.xlabel('Birth Year', fontsize=12)
    plt.ylabel('Number of Students', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)

    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    return buf

# Generate Bar Chart (Students per Department)
def plot_column_chart():
    df = get_student_data()
    dept_counts = df['department'].value_counts()

    plt.figure(figsize=(13, 8))
    sns.barplot(x=dept_counts.index, y=dept_counts.values, palette='Set2')
    plt.title('Student Count by Department', fontsize=14, fontweight='bold')
    plt.xlabel('Department', fontsize=12)
    plt.ylabel('Number of Students', fontsize=12)

    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    return buf
