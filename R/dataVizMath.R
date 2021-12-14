#install library
library(dplyr)
library(ggplot2)

#import data dari CSV yang sudah ditarik
mathAllGrades_data <- read.csv("allGrades.csv")
mathNonAllGrades_data <- read.csv("nonAllGrades.csv")

mathAllData <- rbind(mathAllGrades_data,mathNonAllGrades_data)

ggplot(mathAllData, aes(x=Number.Tested)) + 
  geom_boxplot()+
  ggtitle('Boxplot Jumlah Seluruh Peserta Tes')+
  xlab('Jumlah Peserta (dalam ribu)')

str(mathAllGrades_data)

#ganti menjadi factor
mathAllGrades_data$Year <- as.factor(mathAllGrades_data$Year)

#membuat jumlah tes per tahunnya untuk seluruh grade
ggplot(mathAllGrades_data, aes(fill=Category,x=Year,y=Number.Tested)) +
  geom_bar(position="dodge", stat="identity")+
  ggtitle('Jumlah Tes Per Tahun bedasarkan Kategori Ras')+
  xlab('Tahun')+
  ylab('Jumlah Tes')

#membuat detail data all grades data bedasarkan rasial
dataAsian = filter(mathAllGrades_data, mathAllGrades_data$Category == 'Asian')
dataBlack = filter(mathAllGrades_data, mathAllGrades_data$Category == 'Black')
dataHispanic = filter(mathAllGrades_data, mathAllGrades_data$Category == 'Hispanic')
dataWhite = filter(mathAllGrades_data, mathAllGrades_data$Category == 'White')

#Filter data per tahunnya
data2006 = filter(mathAllGrades_data, mathAllGrades_data$Year == '2006')
data2007 = filter(mathAllGrades_data, mathAllGrades_data$Year == '2007')
data2008 = filter(mathAllGrades_data, mathAllGrades_data$Year == '2008')
data2009 = filter(mathAllGrades_data, mathAllGrades_data$Year == '2009')
data2010 = filter(mathAllGrades_data, mathAllGrades_data$Year == '2010')
data2011 = filter(mathAllGrades_data, mathAllGrades_data$Year == '2011')

ggplot(mathAllGrades_data, aes(x=Category,y=Number.Tested)) + 
  geom_boxplot(fill="orange")+
  ggtitle('Boxplot Jumlah Seluruh Peserta Tes Untuk Tiap Kategori')+
  xlab('Kategori')+
  ylab("Jumlah Peserta")

ggplot(filter(mathNonAllGrades_data, mathNonAllGrades_data$Grade == '3'), aes(x=Category,y=Number.Tested)) + 
  geom_boxplot(fill="orange")+
  ggtitle('Boxplot Jumlah Seluruh Peserta Tes Untuk Grade 3')+
  xlab('Kategori')+
  ylab("Jumlah Peserta")

ggplot(filter(mathNonAllGrades_data, mathNonAllGrades_data$Grade == '4'), aes(x=Category,y=Number.Tested)) + 
  geom_boxplot(fill="orange")+
  ggtitle('Boxplot Jumlah Seluruh Peserta Tes Untuk Grade 4')+
  xlab('Kategori')+
  ylab("Jumlah Peserta")

ggplot(filter(mathNonAllGrades_data, mathNonAllGrades_data$Grade == '5'), aes(x=Category,y=Number.Tested)) + 
  geom_boxplot(fill="orange")+
  ggtitle('Boxplot Jumlah Seluruh Peserta Tes Untuk Grade 5')+
  xlab('Kategori')+
  ylab("Jumlah Peserta")

ggplot(filter(mathNonAllGrades_data, mathNonAllGrades_data$Grade == '6'), aes(x=Category,y=Number.Tested)) + 
  geom_boxplot(fill="orange")+
  ggtitle('Boxplot Jumlah Seluruh Peserta Tes Untuk Grade 6')+
  xlab('Kategori')+
  ylab("Jumlah Peserta")

ggplot(filter(mathNonAllGrades_data, mathNonAllGrades_data$Grade == '7'), aes(x=Category,y=Number.Tested)) + 
  geom_boxplot(fill="orange")+
  ggtitle('Boxplot Jumlah Seluruh Peserta Tes Untuk Grade 7')+
  xlab('Kategori')+
  ylab("Jumlah Peserta")

ggplot(filter(mathNonAllGrades_data, mathNonAllGrades_data$Grade == '8'), aes(x=Category,y=Number.Tested)) + 
  geom_boxplot(fill="orange")+
  ggtitle('Boxplot Jumlah Seluruh Peserta Tes Untuk Grade 8')+
  xlab('Kategori')+
  ylab("Jumlah Peserta")

#remove outliers
remove_outliers <- function(x, na.rm = TRUE, ...) {
  qnt <- quantile(x, probs=c(.25, .75), na.rm = na.rm, ...)
  H <- 1.5 * IQR(x, na.rm = na.rm)
  y <- x
  y[x < (qnt[1] - H)] <- NA
  y[x > (qnt[2] + H)] <- NA
  y
}

#data khusus
grade5 <- filter(mathNonAllGrades_data, mathNonAllGrades_data$Grade == '5')
grade6 <- filter(mathNonAllGrades_data, mathNonAllGrades_data$Grade == '6')
grade8 <- filter(mathNonAllGrades_data, mathNonAllGrades_data$Grade == '8')

cleanedData_grade5 <- as.data.frame(remove_outliers(grade5$Number.Tested))
cleanedData_grade6 <- as.data.frame(remove_outliers(grade6$Number.Tested))
cleanedData_grade8 <- as.data.frame(remove_outliers(grade8$Number.Tested))
#==================================================================================================================#

#melihat statical count untuk kategori rasial
summary(dataAsian$Number.Tested)
summary(dataBlack$Number.Tested)
summary(dataHispanic$Number.Tested)
summary(dataWhite$Number.Tested)

#seluruh data
ggplot(mathAllGrades_data, aes(x = Category,y = Number.Tested))+
  geom_boxplot(fill="#fcba03")+
  xlab("Kategori Rasial")+
  ylab("Jumlah Pendaftar")+
  ggtitle("Boxplot Jumlah Pendaftar Tes Matematika Bedasarkan Kategori Ras")+
  scale_fill_brewer(palette="Set2")

#data hanya asian dan white
ggplot(rbind(dataAsian,dataWhite), aes(x = Category,y = Number.Tested))+
  geom_boxplot(fill="#fcba03")+
  xlab("Kategori Rasial")+
  ylab("Jumlah Pendaftar")+
  ggtitle("Boxplot Jumlah Pendaftar Tes Matematika Bedasarkan Kategori Ras (Asian dan White)")+
  scale_fill_brewer(palette="Set2")

#melihat statical count untuk tiap tahun
summary(data2006$Number.Tested)
summary(data2007$Number.Tested)
summary(data2008$Number.Tested)
summary(data2009$Number.Tested)
summary(data2010$Number.Tested)
summary(data2011$Number.Tested)

#melihat data yang berhasil (level 1)
summary(dataAsian$Level.1..)
summary(dataBlack$Level.1..)
summary(dataHispanic$Level.1..)
summary(dataWhite$Level.1..)

#melihat data yang berhasil (level 2)
summary(dataAsian$Level.2..)
summary(dataBlack$Level.2..)
summary(dataHispanic$Level.2..)
summary(dataWhite$Level.2..)

#melihat data yang berhasil (level 3)
summary(dataAsian$Level.3..)
summary(dataBlack$Level.3..)
summary(dataHispanic$Level.3..)
summary(dataWhite$Level.3..)

#melihat data yang berhasil (level 4)
summary(dataAsian$Level.4..)
summary(dataBlack$Level.4..)
summary(dataHispanic$Level.4..)
summary(dataWhite$Level.4..)

#melihat data yang berhasil (level 1) PERSENTASE
summary(dataAsian$Level.1...1)
summary(dataBlack$Level.1...1)
summary(dataHispanic$Level.1...1)
summary(dataWhite$Level.1...1)

#melihat data yang berhasil (level 2) PERSENTASE
summary(dataAsian$Level.2...1)
summary(dataBlack$Level.2...1)
summary(dataHispanic$Level.2...1)
summary(dataWhite$Level.2...1)

#melihat data yang berhasil (level 3) PERSENTASE
summary(dataAsian$Level.3...1)
summary(dataBlack$Level.3...1)
summary(dataHispanic$Level.3...1)
summary(dataWhite$Level.3...1)

#melihat data yang berhasil (level 4) PERSENTASE
summary(dataAsian$Level.4...1)
summary(dataBlack$Level.4...1)
summary(dataHispanic$Level.4...1)
summary(dataWhite$Level.4...1)

#kumpulkan data untuk per levelnya
data_labelLevel <- c("Asian","Black","Hispanic","White")
data_Level1 <- as.data.frame(rbind(mean(dataAsian$Level.1..)
                                   ,mean(dataBlack$Level.1..)
                                   ,mean(dataHispanic$Level.1..)
                                   ,mean(dataWhite$Level.1..))) 

data_Level2 <- as.data.frame(rbind(mean(dataAsian$Level.2..)
                                   ,mean(dataBlack$Level.2..)
                                   ,mean(dataHispanic$Level.2..)
                                   ,mean(dataWhite$Level.2..)))  

data_Level3 <-as.data.frame(rbind(mean(dataAsian$Level.3..)
                                  ,mean(dataBlack$Level.3..)
                                  ,mean(dataHispanic$Level.3..)
                                  ,mean(dataWhite$Level.3..)))  

data_Level4 <- as.data.frame(rbind(mean(dataAsian$Level.4..)
                                   ,mean(dataBlack$Level.4..)
                                   ,mean(dataHispanic$Level.4..)
                                   ,mean(dataWhite$Level.4..)))

#data level per kategori ras
data_labelLevel2 <- c("Level 1","Level 2","Level 3","Level 4")
data_AllLevelAsia <- as.data.frame(rbind(mean(dataAsian$Level.1..)
                                              ,mean(dataAsian$Level.2..)
                                              ,mean(dataAsian$Level.3..)
                                              ,mean(dataAsian$Level.4..)))

data_AllLevelBlack <- as.data.frame(rbind(mean(dataBlack$Level.1..)
                                         ,mean(dataBlack$Level.2..)
                                         ,mean(dataBlack$Level.3..)
                                         ,mean(dataBlack$Level.4..)))

data_AllLevelHispanic <- as.data.frame(rbind(mean(dataHispanic$Level.1..)
                                         ,mean(dataHispanic$Level.2..)
                                         ,mean(dataHispanic$Level.3..)
                                         ,mean(dataHispanic$Level.4..)))

data_AllLevelWhite <- as.data.frame(rbind(mean(dataWhite$Level.1..)
                                         ,mean(dataWhite$Level.2..)
                                         ,mean(dataWhite$Level.3..)
                                         ,mean(dataWhite$Level.4..)))

ggplot(data_AllLevelAsia, aes(x = "", y = V1,fill=data_labelLevel2))+
  geom_bar(stat = "identity", width = 1)+
  ggtitle("Pie Chart Hasil Tes Matematika Kategori Asian")+
  guides(fill=guide_legend("Level"))+
  coord_polar("y",start=0)+
  theme_void()+
  scale_fill_brewer(palette="Set1")

ggplot(data_AllLevelBlack, aes(x = "", y = V1,fill=data_labelLevel2))+
  geom_bar(stat = "identity", width = 1)+
  ggtitle("Pie Chart Hasil Tes Matematika Kategori Black")+
  guides(fill=guide_legend("Level"))+
  coord_polar("y",start=0)+
  theme_void()+
  scale_fill_brewer(palette="Set1")

ggplot(data_AllLevelHispanic, aes(x = "", y = V1,fill=data_labelLevel2))+
  geom_bar(stat = "identity", width = 1)+
  ggtitle("Pie Chart Hasil Tes Matematika Kategori Hispanic")+
  guides(fill=guide_legend("Level"))+
  coord_polar("y",start=0)+
  theme_void()+
  scale_fill_brewer(palette="Set1")

ggplot(data_AllLevelWhite, aes(x = "", y = V1,fill=data_labelLevel2))+
  geom_bar(stat = "identity", width = 1)+
  ggtitle("Pie Chart Hasil Tes Matematika Kategori White")+
  guides(fill=guide_legend("Level"))+
  coord_polar("y",start=0)+
  theme_void()+
  scale_fill_brewer(palette="Set1")

#merge all data Category AVG
df_mergedCategoryAVG <- do.call("rbind", list(df_allAsianAverage,df_allBlackAverage,df_allHispanicAverage,df_allWhiteAverage))
df_mergedYearAVG <- do.call("rbind", list(df_all2006Average,df_all2007Average,df_all2008Average,df_all2009Average,df_all2010Average,df_all2011Average))

#buat barplot masing-masing kategori
ggplot(dataAsian, aes(x=Year,y=Number.Tested)) +
  geom_bar(position="dodge", stat="identity", fill="orange")+
  ggtitle('Jumlah Tes Per Tahun bedasarkan Kategori Asian')+
  xlab('Tahun')+
  ylab('Jumlah Tes')+
  coord_cartesian(ylim=c(50000,65000))

ggplot(dataBlack, aes(x=Year,y=Number.Tested)) +
  geom_bar(position="dodge", stat="identity", fill="orange")+
  ggtitle('Jumlah Tes Per Tahun bedasarkan Kategori Black')+
  xlab('Tahun')+
  ylab('Jumlah Tes')+
  coord_cartesian(ylim=c(110000,150000))

ggplot(dataHispanic, aes(x=Year,y=Number.Tested)) +
  geom_bar(position="dodge", stat="identity", fill="orange")+
  ggtitle('Jumlah Tes Per Tahun bedasarkan Kategori Hispanic')+
  xlab('Tahun')+
  ylab('Jumlah Tes')+
  coord_cartesian(ylim=c(160000,180000))

ggplot(dataWhite, aes(x=Year,y=Number.Tested)) +
  geom_bar(position="dodge", stat="identity", fill="orange")+
  ggtitle('Jumlah Tes Per Tahun bedasarkan Kategori White')+
  xlab('Tahun')+
  ylab('Jumlah Tes')+
  coord_cartesian(ylim=c(55000,65000))

#=======================================================================================#
# Bagian analisis data Level per kategori

library(reshape2)

#ASIAN
df_asianMeltedAll <- melt(dataAsian[,c('Year','Level.1...1','Level.2...1','Level.3...1','Level.4...1')],id.vars = 1)
ggplot(df_asianMeltedAll, aes(fill=Year, y=value, x=variable)) + 
  geom_bar(position="dodge", stat="identity")+
  ggtitle('Jumlah Hasil Tes Per Tahun bedasarkan Kategori Asian')+
  xlab('Level yang Didapatkan')+
  ylab('Persentase (%)')+
  ylim(0,70)

#Black
df_blackMeltedAll <- melt(dataBlack[,c('Year','Level.1...1','Level.2...1','Level.3...1','Level.4...1')],id.vars = 1)
ggplot(df_blackMeltedAll, aes(fill=Year, y=value, x=variable)) + 
  geom_bar(position="dodge", stat="identity")+
  ggtitle('Jumlah Hasil Tes Per Tahun bedasarkan Kategori Black')+
  xlab('Level yang Didapatkan')+
  ylab('Persentase (%)')+
  ylim(0,70)

#Hispanic
df_hispanicMeltedAll <- melt(dataHispanic[,c('Year','Level.1...1','Level.2...1','Level.3...1','Level.4...1')],id.vars = 1)
ggplot(df_hispanicMeltedAll, aes(fill=Year, y=value, x=variable)) + 
  geom_bar(position="dodge", stat="identity")+
  ggtitle('Jumlah Hasil Tes Per Tahun bedasarkan Kategori Hispanic')+
  xlab('Level yang Didapatkan')+
  ylab('Persentase (%)')+
  ylim(0,70)

#White
df_whiteicMeltedAll <- melt(dataWhite[,c('Year','Level.1...1','Level.2...1','Level.3...1','Level.4...1')],id.vars = 1)
ggplot(df_whiteicMeltedAll, aes(fill=Year, y=value, x=variable)) + 
  geom_bar(position="dodge", stat="identity")+
  ggtitle('Jumlah Hasil Tes Per Tahun bedasarkan Kategori White')+
  xlab('Level yang Didapatkan')+
  ylab('Persentase (%)')+
  ylim(0,70)

#=======================================================================================#
# Bagian analisis tingkat keberhasilan tes per ras seluruh grade

#melt data into per racial
df_copyMathAll <- mathAllGrades_data
df_copyMathAll <- aggregate(df_copyMathAll['Level.3.4..'], by=df_copyMathAll['Category'], sum)

df_allParticipated <- mathAllGrades_data
df_allParticipated <- aggregate(df_allParticipated['Number.Tested'], by=df_allParticipated['Category'], sum)

#merge data
df_allParticipatedMerged = merge(x = df_copyMathAll, y = df_allParticipated, by = "Category")

#fungsi untuk menyederhanakan nilai y axis
multi_format_1000 <- function() {
  function(x) format(x/1000,digits = 4) 
}

#fungsi untuk rename kolom
PesertaLabs <- c("Level 3 dan 4 (Melampaui)", "Peserta Mengikuti Tes")

ggplot(df_copyMathAll, aes(y=Level.3.4.., x=Category)) + 
  geom_bar(position="dodge", stat="identity", fill="orange")+
  ggtitle('Jumlah Peserta Tes Dengan Hasil Melampaui Standar Tahun 2006 - 2011')+
  xlab('Kategori')+
  ylab('Jumlah Peserta (dalam ribu)')+
  scale_y_continuous(labels = multi_format_1000(), breaks = seq(0,700000,by=100000))

#ggplot untuk semua data
df_allParticipatedMergedMelted <- melt(df_allParticipatedMerged[,c('Category','Level.3.4..','Number.Tested')],id.vars = 1)
ggplot(df_allParticipatedMergedMelted, aes(fill=Category, y=value, x=variable)) + 
  geom_bar(position="dodge", stat="identity")+
  ggtitle('Jumlah Peserta Tes Dengan Hasil Melampaui VS Jumlah Peserta Total Tahun 2006 - 2011')+
  xlab('')+
  ylab('Jumlah Peserta (dalam ribu)')+
  scale_y_continuous(labels = multi_format_1000(), breaks = seq(0,12000000,by=100000))+
  scale_x_discrete(labels = PesertaLabs )

#=======================================================================================#
# Bagian predictive analysis

