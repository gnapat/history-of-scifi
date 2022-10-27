# History of Sci-Fi movies
รวบรวมข้อมูลเกี่ยวกับ Sci-Fi Movies ตั้งแต่ ปี 1965 จนถึงปัจจุบัน
โดยนำ dataset ที่เกียวข้องมาวิเคราะห์ว่า ภาพยนตร์ Sci-Fi มีการได้รับความนิยมหรือมีอิทธิพลอย่างไรในวงการภาพยนตร์

# Author
Napat Phongvichian (นพัต พงษ์วิเชียร)
ID: 6420422022
graduate student in Applied Statistics at National Institute of Development Administration.


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

# New Dataset
File: movies_sheet1.csv
|Field Name|	Type	|description|
|----|------------|-------------|
|year|	string|	release year|
|All|	int|	All genres|
|Romance|int|	Romance genres|
|Action|	int|	Action genres|
|Adventure|	int|	Adventure genres|
|Biography|	int|	Biography genres|
|Drama|	int|	Drama genres|
|Fantasy|	int|	Fantasy genres|
|Comedy|	int|	Comedy genres|
|War|	int|	War genres|
|Documentary|	int|	Documentary genres|
|Crime|	int|	Crime genres|
|Family|	int|	Family genres|
|History|	int|	History genres|
|Sci-Fi|	int|	Sci-Fi genres|
|Thriller|	int|	Thriller genres|
|Western|	int|	Western genres|
|Sport|	int|	Sport genres|
|Mystery|	int|	Mystery genres|
|Horror|	int|	Horror genres|
|Music|	int|	Music genres|
|Animation|	int|	Animation genres|
|Musical|	int|	Musical genres|
|Film-Noir|	int|	Film-Noir genres|
|News|	int|	News genres|
|Short|	int|	Short genres|
|Adult|	int|	Adult genres|
|Reality-TV|	int|	Reality-TV genres|
|Talk-Show|	int|	Talk-Show genres|
|Game-Show|	int|	Game-Show genres|

File: movies_sheet2.csv
|Field Name|	Type|	description|
|----|------------|-------------|
|tconst|	string|	unique identifier of the title.|
|titleType|	string|	the type/format of the title.|
|primaryTitle|	string|	popular title.|
|originalTitle|	string|	original title.|
|isAdult|	bool|	0: non-adult title; 1: adult title.|
|startYear|	string date|	release year.|
|endYear|	string date|	end year.|
|runtimeMinutes|	int|	primary runtime of the title, in minutes.|
|genres|	string array|	includes up to three genres associated with the title.|
|averageRating|	int|	calculator takes a number of votes for each rating .|
|numVotes|	int|	total number of votes.|
|lifetime_gross|	int|	Life Time Value.|

# Movies 1900 - 2022
![image](https://user-images.githubusercontent.com/22583786/195967646-dc9cda0e-cb16-42ec-8cf7-2329e5843838.png)

# The Star Wars franchise kicked off in 1977
![image](https://user-images.githubusercontent.com/22583786/195967776-d8f32c46-422e-420a-a0d6-33c496506b0d.png)
