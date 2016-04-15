sudo python3 -u /home/pi/pir2.py >> /home/pi/data.csv
tail -1440 /home/pi/data.csv > /home/pi/data24.csv
rsync -avzL /var/www/sensor/* $PUBLIC_FOLDER
