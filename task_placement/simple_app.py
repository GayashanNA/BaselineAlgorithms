from task_placement.Taneja_iot_placement import NetworkNode, AppModule

# , NetworkNode('N3', 5, 15, 50)
network_nodes = [NetworkNode('N1', 200, 1100, 100), NetworkNode('N2', 5, 15, 5)]
app_modules = [AppModule('M1', 50, 900, 5), AppModule('M2', 50, 100, 5), AppModule('M3', 5, 15, 5),
               AppModule('M4', 5, 15, 50)]
