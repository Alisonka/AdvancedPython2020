while true
do
  files=$(find ./custom_tmp -maxdepth 1 -type f | wc -l)
  dirs=$(find ./custom_tmp -maxdepth 1 -type d | wc -l)
  printf "Contents of custom_tmp: %d files, %d folders\n" $files $(($dirs-1))
  sleep 10s
done