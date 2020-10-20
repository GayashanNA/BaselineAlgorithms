from task_placement.Taneja_iot_placement import NetworkNode, AppModule

network_nodes = [NetworkNode('C1', cpu=2300000000, ram=256000 * 8 * 1024, bandwidth=10000000000),
                 NetworkNode('Pi1', cpu=1200000000 - 100450063 - 564421, ram=1024 * 8 * 1024, bandwidth=11534336),
                 NetworkNode('Pi2', cpu=1200000000, ram=1024 * 8 * 1024, bandwidth=11534336)]
_lambda = 10
_beta = 4096
_bw = _lambda * _beta
# AppModule('so', cpu=100450063, ram=100, bandwidth=_bw * 1),AppModule('pa', cpu=564421, ram=32, bandwidth=_bw * 1.65),
# TASK = {so, pa1, rf, bf, ip, jo, an, csv, si1, pa2, lr, bwa, dac, mlp, fcsv};
app_modules = [AppModule('rf', cpu=1939, ram=256, bandwidth=_bw * 1.65),
               AppModule('bf', cpu=35, ram=256, bandwidth=_bw * 1.65),
               AppModule('ip', cpu=5363, ram=256, bandwidth=_bw * 1.65),
               AppModule('jo', cpu=1627, ram=256, bandwidth=_bw * 1.65*0.2*1.3),
               AppModule('an', cpu=11851, ram=256, bandwidth=_bw * 1.65*0.2*1.3),
               AppModule('csv', cpu=63426, ram=256, bandwidth=_bw * 1.65*0.2*1.3*2),
               AppModule('lr', cpu=153280, ram=256, bandwidth=_bw * 3.3),
               AppModule('bwa', cpu=4488, ram=256, bandwidth=_bw * 1.65),
               AppModule('dac', cpu=42153, ram=32, bandwidth=_bw * 3.3),
               AppModule('mlp', cpu=114831399, ram=32, bandwidth=_bw * 0.00165 * 0.2),
               AppModule('fcsv', cpu=306645, ram=512, bandwidth=_bw * 1)]
