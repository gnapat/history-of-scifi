# History of Sci-Fi movies
รวบรวมข้อมูลเกี่ยวกับ Sci-Fi Movies ตั้งแต่ ปี 1965 จนถึงปัจจุบัน
โดยนำ dataset ที่เกียวข้องมาวิเคราะห์ว่า ภาพยนตร์ Sci-Fi มีการได้รับความนิยมหรือมีอิทธิพลอย่างไรในวงการภาพยนตร์

# Author
Napat Phongvichian

# Dataset

### IMDb Datasets https://www.imdb.com/interfaces/
+ file title.basics.tsv.gz and title.rating.tsv.gz 9,267,898 Row

#### Layout
|  | Field Name |	Type	| Info |
|--|------------|----------|------|
|1 |tconst|string|unique|identifier of the title|
|2 |titleType|string|	the type/format of the title|
|3 |primaryTitle|string|	popular title|
|4 |originalTitle|string|	original title|
|5 |isAdult|bool|	0: non-adult title; 1: adult title|
|6 |startYear|string date|	release year|
|7 |endYear|string date|	end year|
|8 |runtimeMinutes|int|	primary runtime of the title, in minutes|
|9 |genres|string array|includes up to three genres associated with the title|


### Boxofficemojo https://www.kaggle.com/datasets/eliasdabbas/boxofficemojo-alltime-domestic-data
+ file boxoffice_2.csv 16543 Row


#### Layout
|  |	Field Name|	Type|	Info|
|--|------------|----------|------|
|1|	rank|	string|	unique identifier of the title|
|2|	title|	string|	the type/format of the title|
|3|	studio| 	string|	Company|
|4|	lifetime_gross| 	int|	Life Time Value.|
|5|	year|	string date|	release year|

# Movies 1900 - 2022
![image](https://user-images.githubusercontent.com/22583786/195967646-dc9cda0e-cb16-42ec-8cf7-2329e5843838.png)

# The Star Wars franchise kicked off in 1977
![image](https://user-images.githubusercontent.com/22583786/195967776-d8f32c46-422e-420a-a0d6-33c496506b0d.png)
