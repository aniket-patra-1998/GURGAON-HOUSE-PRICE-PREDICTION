import streamlit as st
import pickle
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="Recommended Apartments")

location_df = pickle.load(open('datasets\location_distance.pkl','rb'))
cosine_sim1 =   pickle.load(open('datasets\cosine_sim1.pkl','rb'))
cosine_sim2 =   pickle.load(open('datasets\cosine_sim2.pkl','rb'))
cosine_sim3 =   pickle.load(open('datasets\cosine_sim3.pkl','rb'))
apart_df = pd.read_pickle(('datasets\df.pkl'))
# Recommender system function

def recommend_properties_with_scores(property_name, top_n=5):
    
    cosine_sim_matrix = 30*cosine_sim1 + 20*cosine_sim2 + 8*cosine_sim3
    # cosine_sim_matrix = cosine_sim3
    
    # Get the similarity scores for the property using its name as the index
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))
    
    # Sort properties based on the similarity scores
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the indices and scores of the top_n most similar properties
    top_indices = [i[0] for i in sorted_scores[1:top_n+1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n+1]]
    
    # Retrieve the names of the top properties using the indices
    top_properties = location_df.index[top_indices].tolist()
    
    # Create a dataframe with the results
    recommendations_df = pd.DataFrame({
        'PropertyName': top_properties,
        'SimilarityScore': top_scores
    })
    
    return recommendations_df

#Function to generate links
def property_with_link(rec_df,apart_df):
    for value in rec_df['PropertyName'].to_list():
    # Find the corresponding 'Link' value in df
        link_value = apart_df[apart_df['PropertyName'] == value]['Link'].values
    # If a link value is found, assign it to rec_df
        if len(link_value) > 0:
            rec_df.loc[rec_df['PropertyName'] == value, 'Link'] = link_value[0]
    return rec_df


#st.dataframe(location_df)
st.title("Select Location and Radius")

location = st.selectbox("Location", sorted(location_df.columns.to_list()))

kms = st.number_input("Radius in Kms")

if st.button('Search'):
    result_ser= location_df[location_df[location]<kms*1000][location].sort_values().to_dict()

    apartment = []
    distance= []

    if len(result_ser)==0:
        st.text("No property nearby")
    else:
        st.text('Property Name   Property Distance' )
        for key,value in result_ser.items(): 
            
            #distance.append(value)
            st.text(str(key)+"        "+str(round(value/1000,2))+" kms")
        
st.title("Recommended Apartments")       
selected_apartment = st.selectbox("Select an apartment",sorted(location_df.index.to_list()))

if st.button('Recommend'):
    recommendation_df = recommend_properties_with_scores(selected_apartment)
    rec_df = property_with_link(recommendation_df,apart_df)
    st.dataframe(rec_df)
    for value in rec_df['PropertyName'].to_list():
    # Find the corresponding 'Link' value in df
        link_value = apart_df[apart_df['PropertyName'] == value]['Link'].values
    # If a link value is found, display it as a clickable link
        if len(link_value) > 0:
            st.markdown(f" **Property Name** : {value} --> 99 Acres Property Link : [Link]({link_value[0]})")
            # Web scraping to extract image URL from the property webpage
            try:
                response = requests.get(link_value[0], timeout=10)  # Set a timeout of 10 seconds
                soup = BeautifulSoup(response.content, 'html.parser')
                img_url = soup.find('meta', property='og:image')['content']
                st.image(img_url, caption='Property Image', use_column_width=True)
            except Exception as e:
                st.error(f"Error fetching image for {value}: {e}")