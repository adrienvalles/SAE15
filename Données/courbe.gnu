set terminal png size 800,600
set output 'image.png'
set key inside bottom right
set autoscale
set xlabel 'temps (en heure)' 
set xdata time
set timefmt "%H:%M:%S"
set format x "%H:%M"
set ylabel 'Taux d occupation des parkings voitures'
set title 'Evolution du taux d occupation des parkings de Montpellier'
plot "Data_voitures.txt" using 1:2 with linepoints