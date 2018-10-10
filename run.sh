timer=$SECONDS
cat ~/Desktop/weather-2017/*.txt | python map.py | python reduce.py 
elapsedseconds=$(( SECONDS - timer ))
echo "exercise took $elapsedseconds seconds"