import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns


def run_page():
    st.header("Rent Analysis")

    delay_df = pd.read_csv("delay_df.csv")
    consecutive_df = pd.read_csv("consecutive.csv")
    delay_df.drop(columns="Unnamed: 0", axis=1, inplace=True)
    consecutive_df.drop(columns="Unnamed: 0", axis=1, inplace=True)

    st.write(delay_df.head())

    checking_counts = delay_df['checkin_type'].value_counts()

    def plot_checkin_distribution(checking_counts):
        plt.figure(figsize=(6, 6), facecolor="white") 
        patches, texts, autotexts = plt.pie(
            checking_counts, 
            labels=checking_counts.index, 
            autopct='%1.1f%%', 
            startangle=150, 
            colors=["#6a0dad", "orange"], 
            explode=(0.1, 0), 
            shadow=True
        )
        autotexts[1].set_color('#6a0dad')
        plt.title('Distribution of Type of Check-in', fontsize=14)  
        plt.axis('equal')  
        st.pyplot(plt)  

    col1, col2 = st.columns(2)
    with col1:
        st.write("Checkin Distribution", checking_counts)
    with col2:
        state_counts = delay_df['state'].value_counts()
        st.write("State Distribution", state_counts)

    def plot_state_distribution(state_counts):
        plt.figure(figsize=(6, 6), facecolor="white") 
        patches, texts, autotexts = plt.pie(
            state_counts, 
            labels=state_counts.index, 
            autopct='%1.1f%%', 
            startangle=150, 
            colors=["#6a0dad", "orange"],
            explode=(0.1, 0), 
            shadow=True
        )
        autotexts[1].set_color('#6a0dad')
        plt.title('Distribution of State', fontsize=14)  
        plt.axis('equal')
        st.pyplot(plt)

    col1, col2 = st.columns(2) 
    with col1:
        plot_checkin_distribution(checking_counts) 
    with col2:
        plot_state_distribution(state_counts)

    effect_df = delay_df[['state', 'previous_ended_rental_id']].copy()
    effect_df.columns = ['state', 'rent']

    effect_df['rent'] = effect_df['rent'].apply(lambda x: 'not consecutive' if pd.isna(x) else 'consecutive')

    rent_counts = effect_df['rent'].value_counts()

    def plot_consecutive_distribution(rent_counts):
        plt.figure(figsize=(3, 3), facecolor="white") 
        patches, texts, autotexts = plt.pie(
            rent_counts, 
            labels=rent_counts.index, 
            autopct='%1.1f%%', 
            startangle=150, 
            colors=["#6a0dad", "orange"], 
            explode=(0.1, 0), 
            shadow=True
        )
        autotexts[1].set_color('#6a0dad')
        plt.title('Consecutive vs Not Consecutive Rentals', fontsize=14)  
        plt.axis('equal')
        st.pyplot(plt)

    st.header(" ")
    st.header("**Consecutive rents**")
    plot_consecutive_distribution(rent_counts)

    ###############################################################################
    st.header("*Data*")
    st.write(consecutive_df.head())
    st.markdown("""### How many canceled? How many lates Vs. on time?""")

    state_counts = consecutive_df['state'].value_counts()

    def plot_state_distribution(state_counts):
        plt.figure(figsize=(4, 4), facecolor="white")  
        patches, texts, autotexts = plt.pie(
            state_counts, 
            labels=state_counts.index, 
            autopct='%1.1f%%', 
            startangle=150, 
            colors=["purple", "orange"], 
            explode=(0.1, 0), 
            shadow=True
        )
        autotexts[1].set_color('purple')
        plt.title('Proportion of State of Rent that is Followed by One', fontsize=12) 
        plt.axis('equal')
        st.pyplot(plt)

    consecutive_df['delay_status'] = consecutive_df['previous_delay_at_checkout_in_minutes'].apply(lambda x: 'Late' if x > 0 else 'On Time')
    status_counts = consecutive_df['delay_status'].value_counts()

    def plot_delay_status_distribution(status_counts):
        plt.figure(figsize=(4, 4), facecolor="white") 
        plt.pie(
            status_counts, 
            labels=status_counts.index, 
            autopct='%1.1f%%', 
            colors=['green', 'purple'], 
            startangle=90
        )
        plt.title('Late vs On Time', fontsize=12) 
        plt.axis('equal')
        st.pyplot(plt)

    col1, col2 = st.columns(2)

    with col1:
        plot_state_distribution(state_counts)

    with col2:
        plot_delay_status_distribution(status_counts)


    ###############################################################
    st.header(" ")
    st.markdown("""### Among the late cases how many following rents were cancelled?""")
    late = consecutive_df[consecutive_df['previous_delay_at_checkout_in_minutes'] > 0]
    state_counts = late['state'].value_counts()

    # state
    def plot_late_state_distribution(state_counts):
        plt.figure(figsize=(6, 6)) 
        plt.pie(
            state_counts, 
            labels=state_counts.index, 
            autopct='%1.1f%%', 
            colors=['green', 'purple'], 
            startangle=90
        )
        plt.title('Percentage of State in "Late Checkout" Scenario', fontsize=14) 
        plt.axis('equal')
        st.pyplot(plt)

    col1, col2 = st.columns([2, 1]) 

    with col1:
        plot_late_state_distribution(state_counts) 

    with col2:
        st.markdown("""
        This pie chart represents the distribution of states for rentals that experienced a late checkout.
        **12%** canceled due to delay.
        """)    

    ######################################################################################
    #delay distribution
    st.markdown("""
    ## Delays distribution """)

    df_cleaned = consecutive_df.dropna(subset=['previous_delay_at_checkout_in_minutes'])
    bins = [0, 30, 60, 120, 180, 240, 300, 360]
    labels = ['0-30', '30-60', '60-120', '120-180', '180-240', '240-300', '300-360']
    df_cleaned['delay_bins'] = pd.cut(df_cleaned['previous_delay_at_checkout_in_minutes'], bins=bins, labels=labels, right=False)

    count_data = df_cleaned['delay_bins'].value_counts().sort_index()

    # delay distribution
    def plot_delay_distribution(count_data):
        plt.figure(figsize=(10, 6)) 
        sns.barplot(x=count_data.index, y=count_data.values, color="purple")
        plt.title('Delay Distribution', fontsize=14)
        plt.xlabel('Delays', fontsize=12)
        plt.ylabel('Count', fontsize=12)
        plt.xticks(rotation=45) 
        st.pyplot(plt)

    plot_delay_distribution(count_data)

    st.markdown("""
    ### Delays distribution
    This bar plot shows the distribution of delays at checkout
    - **52%** of checkouts have at least **0 mn** of delay
    - **42%** of checkouts have at least **15 mn** of delay
    - **36%** of checkouts have at least **30 mn** of delay
    - **23%** of checkoutshave at least **60 mn** of delay
    - **8%** of checkouts have at least **180** mn of delay
    - **4%** checkouts have at least **360 mn** of delay
    """)

if __name__ == "__main__":
    run_page()