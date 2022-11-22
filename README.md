# PATAGI-
Ini adalah file untuk memenuhi tugas besar dari mata kuliah EL-5006 Desain Aplikasi Interaktif dari kami kelompok 1 project IoT dari opsi teknik kendali.
kelompok kami beranggotakan :
  1. Ardian Budi Kusuma Atmaja	NIM 23220360
  2. Hardi Kurnianto		        NIM 23220343
  3. Muhammad Fijar Aswad		    NIM 23220356

Introduction 
Berawal dari kebutuhan pokok sehari-hari kami, yang hidup dalam kosan bersama untuk memonitoring tabung gas LPG yang sering tiba-tiba habis tanpa disadari. Kemudian kami memutuskan untuk membuat tempat tabung LPG kami menjadi lebih berteknologi yang dapat kami pantau isi dari tabung LPG dan karena kesibukan kami mengerjakan tugas kuliah kami untuk itu kami juga melengkapi tampat tabung LPG kami dengan fitur yang bisa mengirimkan pesan ke penjual kepercayaan kami untuk mengantarkan tabung LPG yang baru.

Komponen:
kami menggunakan sensor loadcell dan HX711 sebagai alat pengukur isi tabung LPG. sebelumnya kami berencana untuk menggunakan sensor tekanan namun karena faktor keselamatan akhirnya kami memutuskan untuk memontoring isi dengan variable berat. Variable berat yang terbaca kami konversikan dalam bentuk persentase dengan vol% = (data terbaca/3)x100. Kemudian untuk microkontroller kami menggunakan NODEMCU karena sudah terintegrasi dengan modul wifi yang sangat memudahkan kami. Kami juga melengkapinya dengan sensor MQ6 sebagai pendeteksi kebocoran gas. Ini akan menjadi sistem keselamatan kami juga kami lalai atau salah dalam memasang tabung gas.


