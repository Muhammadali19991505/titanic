import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Sahifa konfiguratsiyasi
st.set_page_config(
    page_title="Titanik: Xavfsizlik va Omon Qolish Tahlili",
    layout="wide",
    initial_sidebar_state="expanded"
)


# 2. Ma'lumotlarni yuklash va qayta ishlash
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    df = pd.read_csv(url)

    # Yosh ustunidagi bo'sh qiymatlarni to'ldirish va yaxlitlash
    df['Age'] = df['Age'].fillna(df['Age'].mean()).round()

    # Yosh toifalarini yaratish
    def classify_age(age):
        if pd.isna(age):
            return "Unknown"
        elif age <= 14:
            return "Children"
        elif 15 <= age <= 64:
            return "Youth&Adults"
        else:
            return "Seniors"

    df['age_category'] = df['Age'].apply(classify_age)

    # Matnli qulay nomlar berish
    df['Class_Name'] = df['Pclass'].map({1: '1-sinf (Yuqori)', 2: '2-sinf (O\'rta)', 3: '3-sinf (Quyi)'})
    df['Status'] = df['Survived'].map({1: 'Omon qolgan', 0: 'Vafot etgan'})
    return df


try:
    df = load_data()
except Exception as e:
    st.error("Ma'lumotlar to'plamini yuklashda xatolik yuz berdi. Iltimos internet aloqasini tekshiring.")
    st.stop()

# 3. Yon panel (Sidebar) - Interaktiv filtrlar
st.sidebar.title("🔍 Tahlil filtrlari")

selected_classes = st.sidebar.multiselect(
    "Yo'lovchi sinfini tanlang:",
    options=df['Class_Name'].unique(),
    default=df['Class_Name'].unique()
)

selected_categories = st.sidebar.multiselect(
    "Yosh toifasini tanlang:",
    options=['Children', 'Youth&Adults', 'Seniors'],
    default=['Children', 'Youth&Adults', 'Seniors']
)

# Filtrlash
filtered_df = df[
    (df['Class_Name'].isin(selected_classes)) &
    (df['age_category'].isin(selected_categories))
    ]

# 4. Asosiy sahifa sarlavhasi va kirish
st.title("🚢 Titanik Halokati: Kema Arxitekturasi va Evakuatsiya Tahlili")
st.markdown("""
Ushbu boshqaruv paneli favqulodda vaziyatlarda barcha sinf va yoshdagi yo'lovchilar uchun 
qutqaruv vositalaridan teng foydalanish imkoniyatini ta'minlash maqsadida tayyorlangan.
""")
st.divider()

# 5. KPI Kartalari
total_passengers = len(filtered_df)
total_survivors = filtered_df['Survived'].sum()
survival_rate = (total_survivors / total_passengers * 100) if total_passengers > 0 else 0

col1, col2, col3 = st.columns(3)
col1.metric("Jami yo'lovchilar", f"{total_passengers:,}")
col2.metric("Omon qolganlar soni", f"{total_survivors:,}")
col3.metric("Omon qolish darajasi", f"{survival_rate:.1f}%")

st.divider()

# 6. Diagrammalar bloki
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("1. Sinf kesimida qutqarilganlar soni")
    count_data = filtered_df.groupby(['Class_Name', 'Status']).size().reset_index(name='Soni')

    fig_count = px.bar(
        count_data,
        x='Class_Name',
        y='Soni',
        color='Status',
        barmode='group',
        color_discrete_map={'Omon qolgan': '#2ecc71', 'Vafot etgan': '#e74c3c'},
        text='Soni',
        labels={'Class_Name': 'Yo\'lovchi sinfi', 'Soni': 'Odamlar soni'}
    )
    fig_count.update_traces(textposition='outside')
    st.plotly_chart(fig_count, use_container_width=True)

with col_right:
    st.subheader("2. Har bir sinfning omon qolish foizi (%)")
    rate_data = filtered_df.groupby('Class_Name').agg(
        Jami=('PassengerId', 'count'),
        Qutqarilgan=('Survived', 'sum')
    ).reset_index()
    rate_data['Omon_Qolish_Foizi'] = (rate_data['Qutqarilgan'] / rate_data['Jami']) * 100

    fig_rate = px.bar(
        rate_data,
        x='Class_Name',
        y='Omon_Qolish_Foizi',
        color='Class_Name',
        text=rate_data['Omon_Qolish_Foizi'].apply(lambda x: f"{x:.1f}%"),
        labels={'Class_Name': 'Yo\'lovchi sinfi', 'Omon_Qolish_Foizi': 'Omon qolish foizi (%)'}
    )
    fig_rate.update_traces(textposition='outside')
    fig_rate.update_yaxes(range=[0, 100])
    st.plotly_chart(fig_rate, use_container_width=True)

# 7. Yosh toifalari bo'yicha chuqur tahlil
st.subheader("3. Yosh toifalari va sinflar kesimidagi omon qolish foizi")

pivot_data = filtered_df.groupby(['Class_Name', 'age_category'])['Survived'].mean().reset_index()
pivot_data['Survived_Pct'] = (pivot_data['Survived'] * 100).round(1)

fig_age = px.bar(
    pivot_data,
    x='age_category',
    y='Survived_Pct',
    color='Class_Name',
    barmode='group',
    text=pivot_data['Survived_Pct'].apply(lambda x: f"{x:.1f}%"),
    labels={'age_category': 'Yosh toifasi', 'Survived_Pct': 'Omon qolish darajasi (%)'},
    title="Yosh toifalari bo'yicha tenglik tahlili"
)
fig_age.update_traces(textposition='outside')
fig_age.update_yaxes(range=[0, 100])
st.plotly_chart(fig_age, use_container_width=True)

# 8. Xulosa jadvali
with st.expander("📊 Filtrlangan xom ma'lumotlar jadvalini ko'rish"):
    st.dataframe(filtered_df[['PassengerId', 'Name', 'Class_Name', 'Age', 'age_category', 'Status']],
                 use_container_width=True)