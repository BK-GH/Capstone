import plotly.express as px  # Be sure to import express
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#state_df = pd.read_csv('CBECS_climate_zones_by_county.csv')

#fig = px.choropleth(state_df,  # Input Pandas DataFrame
     #               locations="State",  # DataFrame column with locations
      #              color="CBECS Climate Zone",  # DataFrame column with color values
      #              hover_name="State", # DataFrame column hover info
      #              locationmode = 'USA-states') # Set to plot as US States
#fig.update_layout(
   # title_text = 'State Rankings', # Create a Title
   # geo_scope='usa',  # Plot only the USA instead of globe
#)
#fig.show()


df = pd.read_csv('Five_states.csv')

Totalc = df.loc[:4]


ax =Totalc.plot(x="Energy Source", y=["Maine", 'Nebraska', 'Maryland',"North Carolina", 'Florida',"National Average"], kind="bar",figsize=(9,10))
ax.set_xticklabels(ax.get_xticklabels(),rotation = 0)
ax.set(xlabel='Total Energy Consumption', ylabel='Billion BTU')
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
plt.savefig('Total Energy Production .png', bbox_extra_artists=(ax,), bbox_inches='tight')
plt.show()

Totalp = df.loc[15:18]


ax =Totalp.plot(x="Energy Source", y=["Maine", 'Nebraska', 'Maryland',"North Carolina", 'Florida',"National Average"], kind="bar",figsize=(9,10))
ax.set_xticklabels(ax.get_xticklabels(),rotation = 0)
ax.set(xlabel='Total energy average price', ylabel='Billion BTU')
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
plt.savefig('Total energy average price.png', bbox_extra_artists=(ax,), bbox_inches='tight')
plt.show()


HydroC = df.loc[92:95]

ax =HydroC.plot(x="Energy Source", y=["Maine", 'Nebraska', 'Maryland',"North Carolina", 'Florida',"National Average"], kind="bar",figsize=(9,10))
ax.set_xticklabels(ax.get_xticklabels(),rotation = 0)
ax.set(xlabel='Total Hydropower Consumption', ylabel='Billion BTU')
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
plt.savefig('Total Hydropower Consumption .png', bbox_extra_artists=(ax,), bbox_inches='tight')
plt.show()


ElecE = df.loc[62:65]
ax =ElecE.plot(x="Energy Source", y=["Maine", 'Nebraska', 'Maryland',"North Carolina", 'Florida',"National Average"], kind="bar",figsize=(9,10))
ax.set_xticklabels(ax.get_xticklabels(),rotation = 0)
ax.set(xlabel='Total Electricity Consumption', ylabel='Billion BTU')
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
plt.savefig('Total Electricity Consumption .png', bbox_extra_artists=(ax,), bbox_inches='tight')
plt.show()




