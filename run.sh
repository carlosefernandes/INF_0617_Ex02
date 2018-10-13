PATH_DATA='/Users/kobinae/Desktop/MDC_data/weather-2017'
timer=$SECONDS
cat $PATH_DATA/*.txt | python map.py | python reduce.py 
elapsedseconds=$(( SECONDS - timer ))
echo "exercise imp1 took $elapsedseconds seconds"

timer=$SECONDS
cat $PATH_DATA/*.txt | python map_CARLOS.py | python reduce_CARLOS.py 
elapsedseconds=$(( SECONDS - timer ))
echo "exercise imp2 took $elapsedseconds seconds"