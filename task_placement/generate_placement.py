import task_placement.Taneja_iot_placement as algo
# import task_placement.simple_app as app
# import task_placement.stats as app
# import task_placement.etl_stats as app
import task_placement.simple as app

mapped_modules = algo.module_map(app.network_nodes, app.app_modules)

for k, v in mapped_modules.items():
    for m in v:
        print(f'{k.node_id} {m.module_id}')
