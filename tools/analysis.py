import execute_mysql
import my_tools
import pandas as pd

pull_query = "SELECT * FROM location"
location = execute_mysql.run_query(pull_query, fetch=True, fetch_option='fetchall')
location = pd.DataFrame(location)
location.head()


for i in range(1,11): # for location_id in location['id'] <---- use this
    location_id = i # <---- remove this
    city = location.loc[(location['id']== location_id).idxmax(),'city']
    state = location.loc[(location['id']== location_id).idxmax(),'state']

    # make graphs and perform analysis
    vals = my_tools.get_graph_values(location_id, city, state)
    graph = my_tools.get_url(location_id)

    # create a dataframe containing all cities 
    if location_id == 1:
        graph_df = graph.copy()
        vals_df = vals.copy()
    else:    
        graph_df = graph_df.append(graph, ignore_index=True)
        vals_df = vals_df.append(vals, ignore_index=True)  


# insert into database
my_tools.insert_analysis(graph_df, "figure")
my_tools.insert_analysis(vals_df, "value")        