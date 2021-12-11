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