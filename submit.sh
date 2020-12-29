 #!/bin/bash                                                  

# rm python/txt/out.txt
# 
# python python/sel_fit.py  root/testbeam_merged_101.root event/101.root
# mv python/txt/out.txt python/txt/101.txt
# 
# python python/sel_fit.py  root/testbeam_merged_102.root event/102.root
# mv python/txt/out.txt python/txt/102.txt
# 
# python python/sel_fit.py  root/testbeam_merged_103.root event/103.root
# mv python/txt/out.txt python/txt/103.txt
# 
# sed '1d' -i python/txt/101.txt 
# sed '1d' -i python/txt/102.txt 
# sed '1d' -i python/txt/103.txt 
# 
# 
python python/sel_events.py  root/testbeam_merged_101.root event/event_10mV_101.root
python python/sel_events.py  root/testbeam_merged_102.root event/event_10mV_102.root
python python/sel_events.py  root/testbeam_merged_103.root event/event_10mV_103.root
# 
# 

