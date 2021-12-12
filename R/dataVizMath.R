#install library
library(dplyr)
library(ggplot2)

#import data dari CSV yang sudah ditarik
mathAllGrades_data <- read.csv("allGrades.csv")
mathNonAllGrades_data <- read.csv("nonAllGrades.csv")

str(mathAllGrades_data)

#ganti menjadi factor
mathAllGrades_data$Year <- as.factor(mathAllGrades_data$Year)

#memberikan urutan data dengan dplyr
#ordered_wl <- word_list_data %>% arrange(desc(word_list_data$freq))
#ordered_wlc <- word_list_cleaned %>% arrange(desc(word_list_cleaned$freq))
#ordered_wlp <- word_list_planet %>% arrange(desc(word_list_planet$freq))

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
  coord_cartesian(ylim=c(160000,175000))

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