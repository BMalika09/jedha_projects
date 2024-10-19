import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def run_page():
    st.markdown("""## *Threshold*""")

    consecutive_df = pd.read_csv(r"C:\Users\Malika\Desktop\JEDHA\jedha_formation\fullstack\Deployment\get_around_project\dashboard\consecutive.csv")
    consecutive_df.drop(columns="Unnamed: 0", axis=1, inplace=True)

    st.write(consecutive_df.head())

    # percentages
    def calculate_percentages(consecutive_df):
        ended_rentals = consecutive_df[(consecutive_df['state'] == 'ended')]
        canceled_due_to_delay = consecutive_df[(consecutive_df['state'] == 'canceled') & (consecutive_df['previous_delay_at_checkout_in_minutes'] > 0)]

        total_ended = len(ended_rentals)
        total_canceled_due_to_delay = len(canceled_due_to_delay)

        thresholds = range(0, 720, 5)
        lost_ended_percentage = []
        reduced_canceled_percentage = []

        for threshold in thresholds:
            count_lost_ended = len(ended_rentals[ended_rentals['time_delta_with_previous_rental_in_minutes'] < threshold])
            lost_ended_percentage.append((count_lost_ended / total_ended) * 100)

            count_reduced_canceled = len(canceled_due_to_delay[canceled_due_to_delay['time_delta_with_previous_rental_in_minutes'] < threshold])
            reduced_canceled_percentage.append((count_reduced_canceled / total_canceled_due_to_delay) * 100)
        
        return thresholds, lost_ended_percentage, reduced_canceled_percentage

    # cursor
    def display_threshold_info(thresholds, lost_ended_percentage, reduced_canceled_percentage):
        selected_threshold = st.slider('Please set up a threshold (in minutes)', min(thresholds), max(thresholds), step=5)
        index = thresholds.index(selected_threshold)

        st.write(f"Percentage of lost 'ended' rents with threshold **{selected_threshold}** minutes: {lost_ended_percentage[index]:.2f}%")
        st.write(f"Percentage of avoided 'canceled' rents with threshold  **{selected_threshold}** minutes: {reduced_canceled_percentage[index]:.2f}%")

    # Pourcentage
    def plot_threshold_impact(thresholds, lost_ended_percentage, reduced_canceled_percentage):
        plt.figure(figsize=(10, 6))
        plt.plot(thresholds, lost_ended_percentage, marker='o', linestyle='-', color='purple', label="Lost'ended' rents (%)")
        plt.plot(thresholds, reduced_canceled_percentage, marker='o', linestyle='-', color='green', label="Avoided 'canceled' rents(%)")

        plt.title("Threshold impact on rents 'ended' & 'canceled'")
        plt.xlabel("Threshold (minutes)")
        plt.ylabel("Percentage (%)")
        plt.legend()

        plt.minorticks_on()
        plt.grid(True, which='both', axis='both', linestyle='-', color='gray', alpha=0.5)
        plt.grid(True, which='major', linestyle='-', linewidth=1, color='gray')
        plt.grid(True, which='minor', linestyle=':', linewidth=0.5, color='lightgray')

        st.pyplot(plt)

    # Raw data
    def plot_counts_impact(consecutive_df):
        ended_rentals = consecutive_df[consecutive_df['state'] == 'ended']
        canceled_due_to_delay = consecutive_df[(consecutive_df['state'] == 'canceled') & (consecutive_df['previous_delay_at_checkout_in_minutes'] > 0)]

        thresholds = range(0, 720, 10) 
        count_lost_ended = []
        count_reduced_canceled = []

        for threshold in thresholds: #########################
            count_lost_ended_count = len(ended_rentals[ended_rentals['time_delta_with_previous_rental_in_minutes'] < threshold])
            count_lost_ended.append(count_lost_ended_count)

            count_reduced_canceled_count = len(canceled_due_to_delay[canceled_due_to_delay['time_delta_with_previous_rental_in_minutes'] < threshold])
            count_reduced_canceled.append(count_reduced_canceled_count)

        plt.figure(figsize=(10, 6))
        plt.plot(thresholds, count_lost_ended, marker='o', linestyle='-', color='purple', label="Lost'ended' rents (count)")
        plt.plot(thresholds, count_reduced_canceled, marker='o', linestyle='-', color='green', label="Avoided 'canceled' rents (%)")

        plt.title("Threshold impact on rents 'ended' & 'canceled' (Counts)")
        plt.xlabel("Threshold (minutes)")
        plt.ylabel("Count rent")
        plt.legend()
        plt.grid(True)

        st.pyplot(plt)

    # mobile
    def plot_impact_mobile(consecutive_df):
        ended_rentals = consecutive_df[(consecutive_df['state'] == 'ended')  & (consecutive_df['checkin_type']== 'mobile')]
        canceled_due_to_delay = consecutive_df[(consecutive_df['state'] == 'canceled') & (consecutive_df['previous_delay_at_checkout_in_minutes'] > 0)& (consecutive_df['checkin_type']== 'mobile')]
        
        total_ended = len(ended_rentals)
        total_canceled_due_to_delay = len(canceled_due_to_delay)

        thresholds = range(0, 720, 10) 
        count_lost_ended = []
        count_reduced_canceled = []

        for threshold in thresholds:
            count_lost_ended_count = len(ended_rentals[ended_rentals['time_delta_with_previous_rental_in_minutes'] < threshold])
            count_lost_ended.append((count_lost_ended_count / total_ended) * 100)

            count_reduced_canceled_count = len(canceled_due_to_delay[canceled_due_to_delay['time_delta_with_previous_rental_in_minutes'] < threshold])
            count_reduced_canceled.append((count_reduced_canceled_count/ total_canceled_due_to_delay) * 100)


        plt.figure(figsize=(10, 6))
        plt.plot(thresholds, count_lost_ended, marker='o', linestyle='-', color='purple', label="Lost'ended' rents (count)")
        plt.plot(thresholds, count_reduced_canceled, marker='o', linestyle='-', color='green', label="Avoided 'canceled' rents (count)")

        plt.title("Threshold impact on MOBILE rents 'ended' & 'canceled'")
        plt.xlabel("Threshold (minutes)")
        plt.ylabel("Percentage (%)")
        plt.legend()
        plt.grid(True)

        st.pyplot(plt)

    #connect
    def plot_impact_connect(consecutive_df):
        ended_rentals = consecutive_df[(consecutive_df['state'] == 'ended')  & (consecutive_df['checkin_type']== 'connect')]
        canceled_due_to_delay = consecutive_df[(consecutive_df['state'] == 'canceled') & (consecutive_df['previous_delay_at_checkout_in_minutes'] > 0)& (consecutive_df['checkin_type']== 'connect')]

        total_ended = len(ended_rentals)
        total_canceled_due_to_delay = len(canceled_due_to_delay)

        thresholds = range(0, 720, 10) 
        count_lost_ended = []
        count_reduced_canceled = []

        for threshold in thresholds:
            count_lost_ended_count = len(ended_rentals[ended_rentals['time_delta_with_previous_rental_in_minutes'] < threshold])
            count_lost_ended.append((count_lost_ended_count / total_ended) * 100)

            count_reduced_canceled_count = len(canceled_due_to_delay[canceled_due_to_delay['time_delta_with_previous_rental_in_minutes'] < threshold])
            count_reduced_canceled.append((count_reduced_canceled_count/ total_canceled_due_to_delay) * 100)

        plt.figure(figsize=(10, 6))
        plt.plot(thresholds, count_lost_ended, marker='o', linestyle='-', color='purple', label="Lost'ended' rents (%)")
        plt.plot(thresholds, count_reduced_canceled, marker='o', linestyle='-', color='green', label="Avoided 'canceled' rents (%)")

        plt.title("Threshold impact on CONNECT rents 'ended' & 'canceled'")
        plt.xlabel("Threshold (minutes)")
        plt.ylabel("Percentage (%)")
        plt.legend()
        plt.grid(True)

        st.pyplot(plt)


    #simulation
    df = consecutive_df
    def simulation(df):
        ended_rentals = df[df['state'] == 'ended']
        canceled_due_to_delay = df[(df['state'] == 'canceled') & (df['previous_delay_at_checkout_in_minutes'] > 0)]
        delta_threshold = st.slider("Please choose a threshold (in minutes)", min_value=1, max_value=720, value=40)

        results = {
            'checkin_type': [],
            'lost_ended_percentage': [],
            'reduced_canceled_percentage': []
        }
        for checkin in df['checkin_type'].unique():
            
            ended_rentals_type = ended_rentals[ended_rentals['checkin_type'] == checkin]
            canceled_due_to_delay_type = canceled_due_to_delay[canceled_due_to_delay['checkin_type'] == checkin]

            count_lost_ended = len(ended_rentals_type[ended_rentals_type['time_delta_with_previous_rental_in_minutes'] < delta_threshold])
            count_reduced_canceled = len(canceled_due_to_delay_type[canceled_due_to_delay_type['time_delta_with_previous_rental_in_minutes'] < delta_threshold])

            total_ended = len(ended_rentals_type)
            total_canceled = len(canceled_due_to_delay_type)

            lost_ended_percentage = (count_lost_ended / total_ended * 100) 
            reduced_canceled_percentage = (count_reduced_canceled / total_canceled * 100) 

            results['checkin_type'].append(checkin)
            results['lost_ended_percentage'].append(lost_ended_percentage)
            results['reduced_canceled_percentage'].append(reduced_canceled_percentage)

        results_df = pd.DataFrame(results)
        st.write("### Results :")
        st.dataframe(results_df)

        st.write("### Impact on connect Vs mobile in (%) :")
        plt.figure(figsize=(10, 6))
        bar_width = 0.35  
        index = range(len(results_df['checkin_type']))
        plt.bar(index, results_df['lost_ended_percentage'], width=bar_width, alpha=0.7, color='purple', label="Lost'ended' rents (%)")
        plt.bar([i + bar_width for i in index], results_df['reduced_canceled_percentage'], width=bar_width, alpha=0.7, color='green', label="Avoided 'canceled' rents (%)")

        plt.title("Impact of threshold on 'ended' et 'canceled' by type of check-in")
        plt.xlabel("Type of check-in")
        plt.ylabel("Percentage (%)")
        plt.xticks([i + bar_width / 2 for i in index], results_df['checkin_type']) 
        plt.legend()
        plt.grid(axis='y')

        st.pyplot(plt)

    


    thresholds, lost_ended_percentage, reduced_canceled_percentage = calculate_percentages(consecutive_df)

    # display cursorr
    display_threshold_info(thresholds, lost_ended_percentage, reduced_canceled_percentage)

    st.markdown(""" 
    ## *Threshhold impact in percentage (%)*
    """)
    # plot percentages
    plot_threshold_impact(thresholds, lost_ended_percentage, reduced_canceled_percentage)

    st.markdown(""" 
    ## *Threshhold impact in real number*
    """)
    # plot raw data
    plot_counts_impact(consecutive_df)

    st.markdown(""" 
    ## *Connect Vs Mobile*
    """)

    col1, col2 = st.columns(2)
    with col1:
        plot_impact_mobile(consecutive_df)
    with col2:
        plot_impact_connect(consecutive_df)

    st.markdown(""" 
    ## *Simulation*
    """)

    simulation(df)


if __name__ == "__main__":
    run_page()
