import streamlit as st
import pandas as pd
import plotly.express as px
import pickle as pl
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title="Plotting Demo")
st.title("Analytics")



new_df = pd.read_csv("datasets/data_viz1.csv")
feature_text = pl.load(open('datasets/feature_text.pkl','rb'))
st.dataframe(new_df)

# Goup the dataset based on critical features
group_df = new_df.groupby("sector")[['price','price_per_sqft','built_up_area',
                                            'latitude','longitude']].mean()


# Use plotly to plot the plot loactions and do a size map based on built-up
# area and colour map based on price per sqft to show the largest and most
# expensive plots
st.title(" 1. Location of sectors")
fig = px.scatter_mapbox(group_df, lat='latitude', lon='longitude',
                        size='built_up_area',color='price_per_sqft',
                        color_continuous_scale=px.colors.cyclical.IceFire,
                        zoom=10,size_max=35,
                        mapbox_style='open-street-map',
                        width=1200,height=700,
                        hover_name=group_df.index)
st.plotly_chart(fig,use_container_width=True)

# Plotting the most common features as a wordcloud
st.title(" 2.  Features Wordcloud")
wordcloud = WordCloud(width=800,height=800,
                      background_color='white',
                      stopwords=set(['s']),
                      min_font_size=10).generate(feature_text)

plt.figure(figsize=(8,8),facecolor=None)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad=0)
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)

# Scatter plot between area and price

st.title(" 3.  Variation of Price with Property Type and Age of Property ")
property_type = st.selectbox("Select Property",['Flat','House'])
age_property = st.selectbox(" Select Property Age",['Under Construction','New Property','Relatively New', 'Moderately Old', 'Old'])
if property_type == 'House':
    if age_property=='Under Construction':
        fig1 = px.scatter(new_df[(new_df['property_type']=='house')&(new_df['agePossession']=="Under Construction")],x = 'built_up_area',y ='price',color='bedRoom',title='Built Up Area vs Price')
        st.plotly_chart(fig1,use_container_width=True)
    elif age_property=='New Property':
        fig1 = px.scatter(new_df[(new_df['property_type']=='house')& (new_df['agePossession']=="New Property")],x = 'built_up_area',y ='price',color='bedRoom',title='Built Up Area vs Price')
        st.plotly_chart(fig1,use_container_width=True)
    elif age_property=='Relatively New':
        fig1 = px.scatter(new_df[(new_df['property_type']=='house')& (new_df['agePossession']=="Relatively New")],x = 'built_up_area',y ='price',color='bedRoom',title='Built Up Area vs Price')
        st.plotly_chart(fig1,use_container_width=True)
    elif age_property=='Moderately Old':
        fig1 = px.scatter(new_df[(new_df['property_type']=='house')& (new_df['agePossession']=="Moderately Old")],x = 'built_up_area',y ='price',color='bedRoom',title='Built Up Area vs Price')
        st.plotly_chart(fig1,use_container_width=True)
    else:
        fig1 = px.scatter(new_df[(new_df['property_type']=='house')& (new_df['agePossession']=="Old")],x = 'built_up_area',y ='price',color='bedRoom',title='Built Up Area vs Price')
        st.plotly_chart(fig1,use_container_width=True)
    
else:
    if age_property=='Under Construction':
        fig1 = px.scatter(new_df[(new_df['property_type']=='flat')& (new_df['agePossession']=="Under Construction")],x = 'built_up_area',y ='price',color='bedRoom',title='Built Up Area vs Price')
        st.plotly_chart(fig1,use_container_width=True)
    elif age_property=='New Property':
        fig1 = px.scatter(new_df[(new_df['property_type']=='flat')& (new_df['agePossession']=="New Property")],x = 'built_up_area',y ='price',color='bedRoom',title='Built Up Area vs Price')
        st.plotly_chart(fig1,use_container_width=True)
    elif age_property=='Relatively New':
        fig1 = px.scatter(new_df[(new_df['property_type']=='flat')& (new_df['agePossession']=="Relatively New")],x = 'built_up_area',y ='price',color='bedRoom',title='Built Up Area vs Price')
        st.plotly_chart(fig1,use_container_width=True)
    elif age_property=='Moderately Old':
        fig1 = px.scatter(new_df[(new_df['property_type']=='flat')& (new_df['agePossession']=="Moderately Old")],x = 'built_up_area',y ='price',color='bedRoom',title='Built Up Area vs Price')
        st.plotly_chart(fig1,use_container_width=True)
    else:
        fig1 = px.scatter(new_df[(new_df['property_type']=='flat')& (new_df['agePossession']=="Old")],x = 'built_up_area',y ='price',color='bedRoom',title='Built Up Area vs Price')
        st.plotly_chart(fig1,use_container_width=True)


#  4. Pie chart on number of bedrooms based on sectors

st.title(' 4.  BHK PIE CHART BASED ON SECTORS')
sector_options= new_df['sector'].unique().tolist()
sector_options.insert(0,'overall')
selected_sector = st.selectbox("Select Sector", sector_options)

if selected_sector == "overall":
    # if choice is overall select the entire dataset
    fig2 = px.pie(new_df,names='bedRoom',width=300,height=500,
              hole=0.3,
              labels={'bedroom':'bedroom count'},
              template='plotly_dark',
              color_discrete_sequence=px.colors.sequential.Plasma_r)

    # Adjust layout to mimic a 3D effect
    fig2.update_traces(textposition='inside', textinfo='percent+label', 
                   hoverinfo='label+percent+name', pull=[0.05]*len(new_df),
                   marker=dict(line=dict(color='#000000', width=1)))
    #px.pie(new_df,names='bedRoom') 
    st.plotly_chart(fig2,use_container_width=True)

else:
    fig2 = px.pie(new_df[new_df['sector']==selected_sector],names='bedRoom',width=300,height=500,
              hole=0.3,
              labels={'bedroom':'bedroom count'},
              template='plotly_dark',
              color_discrete_sequence=px.colors.sequential.Plasma_r)

    # Adjust layout to mimic a 3D effect
    fig2.update_traces(textposition='inside', textinfo='percent+label', 
                   hoverinfo='label+percent+name', pull=[0.05]*len(new_df[new_df['sector']==selected_sector]),
                   marker=dict(line=dict(color='#000000', width=1)))
    #px.pie(new_df,names='bedRoom') 
    st.plotly_chart(fig2,use_container_width=True)

# 5. Side by side box plots of price based on BHK

st.title(' 5.  PRICE VS BHK COMPARISON')
temp_df = new_df[new_df['bedRoom']<=4]
fig3 = px.box(temp_df,x='bedRoom',y='price',title='BHK Price Range')

# Customizing the layout
fig3.update_layout(
    title='Price Range by Number of Bedrooms',
    xaxis_title='Number of Bedrooms',
    yaxis_title='Price',
    font=dict(
        family="Arial, sans-serif",
        size=12,
        color="RebeccaPurple"
    ),
    plot_bgcolor='rgba(0, 0, 0, 0)'
)

# Customizing the boxplot itself
fig3.update_traces(
    boxmean=True,  # Display mean in boxplot
    jitter=0.3,  # Add a bit of jitter for better visualization of individual points
    marker=dict(
        color='rgb(158,202,225)',  # Customizing box color
        line=dict(
            color='rgb(8,48,107)',  # Customizing box outline color
            width=1.5
        )
    ),
    line=dict(
        color='rgb(8,48,107)',  # Customizing whiskers color
        width=2
    )
)
st.plotly_chart(fig3,use_container_width=True)

# 6. Price distribution of flats and houses

st.title(' 6. Property Price Distribution')

fig4 = plt.figure(figsize=(10,4))
sns.distplot(new_df[new_df['property_type']=='house']['price'],label='house')
sns.distplot(new_df[new_df['property_type']=='flat']['price'],label='flat')
plt.legend()
st.pyplot(fig4)





