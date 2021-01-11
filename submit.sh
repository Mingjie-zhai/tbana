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

python python/sel_events.py  /publicfs/atlas/atlasnew/SUSY/users/zhaimingjie/testbeam/testbeamanalysis/Data/1.root /publicfs/atlas/atlasnew/SUSY/users/zhaimingjie/testbeam/code/suyu/tbana/output/1.root
# 

