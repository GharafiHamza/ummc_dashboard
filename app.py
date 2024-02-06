import streamlit as st
import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

consults = []
filling = []
max_cslt = 60

for i in range(5):
    consults.append(random.randint(0, max_cslt))
    filling.append(random.randint(0, consults[i])) 

df = pd.DataFrame({
    'Consultation': consults,
    'Taux de saisie': filling
})

def main():
    st.title("UMMC Dashboard App")
    st.write("consults : ", consults)
    st.write("filling : ", filling)
    # Bar chart
    st.bar_chart(df, use_container_width=True)
    # # Create an index array for the x-axis
    # x = np.arange(len(consults))

    # # Plot the bars
    # fig, ax = plt.subplots()
    # ax.bar(x - 0.2, consults, width=0.4, label='Consultation')
    # ax.bar(x + 0.2, filling, width=0.4, label='Taux de saisie')

    # # Customize the chart
    # ax.set_xlabel('Record')
    # ax.set_ylabel('Count')
    # ax.set_title('Vertical Bar Graph with Overlapping Bars')
    # ax.set_xticks(x)
    # ax.set_xticklabels([f'Record {i+1}' for i in range(len(consults))])
    # ax.legend()

    # # Show the chart in Streamlit
    # st.pyplot(fig)

    st.area_chart(data=df)

if __name__ == "__main__":
    main()