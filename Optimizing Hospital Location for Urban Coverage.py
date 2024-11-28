import networkx as nx
from matplotlib import pyplot as plt
# creation of the graph of the city
city_graph=nx.Graph()
# adding edges and weights for the graph city
city_graph.add_weighted_edges_from([("Kouba","Bachdjarah",3.9),
                                    ("Kouba","Hussein dey",2.7),
                                    ("Bachdjarah","Hussein dey",4.3),
                                    ("Bachdjarah","Birkhadem",8),
                                    ("Bachdjarah","Ain naedja",5.4),
                                    ("Hussein dey","Ain naedja",9.4),
                                    ("Birkhadem","Ain naedja",4.2),
                                    ("Birkhadem","Birmourad-Rais",2.8),
                                    ("Ain naedja","Birmourad-Rais",9.4),
                                    ("Birkhadem","Kouba",5.8),
                                    ("Birkhadem","Hussein dey",9.1),
                                    ("Ain naedja","Kouba",4.2),
                                    ("Kouba","Birmourad-Rais",4.8),
                                    ("Hussein dey","Birmourad-Rais",5.4),
                                    ("Bachdjarah","Birmourad-Rais",12.1),])
# creating D: matrix of short paths between each city
cities=["Kouba","Bachdjarah","Hussein dey","Birkhadem","Ain naedja","Birmourad-Rais"]
D=[]
for i in cities:
    line=[]
    for j in cities:
        if i==j:
            line.append(0)
        else:
            line.append(nx.shortest_path_length(city_graph,source=i,target=j,weight='weight'))
    D.append(line)
# creating a function to return a list of maximum values of each column in the matrix D
# it represents the maximal distance between a city j and the other cities the list called dj
def maximum_of_each_column(D):
    max_values_columns=[]
    for j in range(len(D[1])):
        line=[]
        for i in range(len(D[1])):
            line.append(D[i][j])
        max_values_columns.append(max(line))
    return max_values_columns
dj=maximum_of_each_column(D)
# optimal coverage distance
optimal_coverage_distance=min(dj)
# which city will be the hospital position
hospital_position=cities[dj.index(optimal_coverage_distance)]
print(f"the hospital position on the city {hospital_position} with a coverage distance of {optimal_coverage_distance} Km.")
# visualizing the graphe and the hospital position
pos=nx.spring_layout(city_graph)
nx.draw(city_graph,pos,with_labels=True,node_size=3000,node_color="lightblue",font_size=8,edge_color="grey")
nx.draw_networkx_nodes(city_graph,pos,nodelist=[hospital_position],node_size=4000,node_color="orange")
edge_labels=nx.get_edge_attributes(city_graph,"weight")
nx.draw_networkx_edge_labels(city_graph,pos,edge_labels=edge_labels)
plt.title("the optimal positioning of a hospital in the city")
plt.show()