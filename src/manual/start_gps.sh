FILENAME="/dev/barcode_reader"
if [ -e ${FILENAME} ] ; then
    echo "GPS Device Found!"
    foxtrotgps &
    sleep 3
    gpsd gps_ascen
fi