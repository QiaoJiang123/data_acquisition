library(edgar)

setwd("D:/")


getMasterIndex(2014)
getFilings(2014,cik.no = "ALL",form.type = "S-1")

getMasterIndex(2002)
getFilings(2002,cik.no = "ALL",form.type = "10-Q")

load("D:/Master Index/2012master.rda")



https://www.sec.gov/Archives/edgar/data/907471/0001140361-12-052474.txt
https://www.sec.gov/Archives/edgar/data/907471/000114036112052474/form10k.htm

url("https://www.sec.gov/Archives/edgar/data/907471/000114036112052474/form10k.htm")

try<-download.file("https://www.sec.gov/Archives/edgar/data/907471/000114036112052474/form10k.htm","D:/try.html")


#========================================================
# Download 10K in html
#========================================================

year<-2012
file_name<-"10-K"

load(paste0("D:/Master Index/",year,"master.rda"))
year.master_wanted<-year.master[year.master$FORM_TYPE==file_name,c("CIK","FORM_TYPE","EDGAR_LINK")]

file_link<-gsub("-","",year.master_wanted$EDGAR_LINK)

# This is for 10K specifically
file_link<-as.character(paste0("https://www.sec.gov/Archives/",substr(file_link,1,nchar(file_link)-4),"/form10k.htm"))

year.master_for_download<-data.frame(year.master_wanted,file_link)

for(i in 1:dim(year.master_for_download)[1]){
  download.file(year.master_for_download[i,"file_link"],paste0("D:/",year,"_",file_name,"/",year.master_for_download[i,"CIK"],"_",file_name,".html"))
}



https://www.sec.gov/Archives/edgar/data/1000180/0001000180-12-000003-index.htm
https://www.sec.gov/Archives/edgar/data/907471/0001140361-12-052474-index.htm



