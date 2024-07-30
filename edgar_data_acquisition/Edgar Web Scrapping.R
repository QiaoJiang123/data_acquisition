library(edgar)
library(downloader)
library(RCurl)
library(XML)
library(httr)


# This function does not work for year:
# 1993
#
YEAR<-2010
FORM.TYPE<-"10-K"

edgar_file_download<-function(YEAR,FORM.TYPE){
  year<-YEAR
  directory_set<-"D:/"
  load(paste0(directory_set,"Master Index/",year,"master.Rda"))
  form_type<-FORM.TYPE

  for(i in 1:5){
    year.master[,i]<-as.character(year.master[,i])
  }
  
  year.master$INDEX_LINK<-as.character(paste0("https://www.sec.gov/Archives/",
                                              as.character(substr(year.master$EDGAR_LINK,1,nchar(year.master$EDGAR_LINK)-4)),"-index.htm"))

  DownloadFile <- function(link, filename) {
    tryCatch({
      downloader::download(link, filename,quiet = T)
      return(TRUE)
    }, error = function(e) {
      return(FALSE)
    })
  }
  
  year.master.form<-year.master[year.master$FORM_TYPE==form_type,]
  
if(dim(year.master.form)[1]==0){
  return('No File Is Found')
}else{
  dir.create(paste0(directory_set,year,"_",form_type,"_","Index"))
  index_dir<-paste0(directory_set,year,"_",form_type,"_","Index")

  index_success<-vector()
for(i in 1:dim(year.master.form)[1]){
    index_success[i]<-DownloadFile(year.master.form[i,"INDEX_LINK"],paste0(index_dir,"/",year.master.form[i,"CIK"],
                                                                           "_",year.master.form[i,"FORM_TYPE"],"_",
                                                                           year.master.form[i,"DATE_FILED"],"_index.htm"))
} # resulting 8333 files
  
  ###########To be continued
  
  year.master.form<-data.frame(year.master.form,INDEX_SUCCESS = index_success)
  
  index_files<-list.files(index_dir)
  
  index_files_id<-as.character(substr(index_files,1,nchar(index_files)-10))
  
  index_files_id_split_list<-list()
  
  for(i in 1:length(index_files_id)){
    # print(index_files_id[i])
    suffix_temp<-readHTMLTable(paste0(index_dir,"/",index_files[i]))
    
    suffix_temp<-as.character(suffix_temp[[1]][suffix_temp[[1]]$Type == form_type,3])
    id_temp<-unlist(strsplit(index_files_id[i],"_"))
    if(length(suffix_temp)!=0){
      file_type_temp<-as.character(substr(suffix_temp,nchar(suffix_temp)-2,nchar(suffix_temp)))
      index_files_id_split_list[[i]]<-data.frame(CIK = id_temp[1],FORM_TYPE = id_temp[2],DATE_FILED = id_temp[3],SUFFIX = suffix_temp,FILE_TYPE = file_type_temp)
    }else if(length(suffix_temp)==0){
      index_files_id_split_list[[i]]<-data.frame(CIK = id_temp[1],FORM_TYPE = id_temp[2],DATE_FILED = id_temp[3],SUFFIX = "re/download",FILE_TYPE = "re/download")
    }
    #suffix_temp<-as.character(suffix_temp[[1]][1,3])
}
  
  index_files_id_df<-Reduce(function(x,y) rbind(x,y),index_files_id_split_list)
  
  year.master.form.link<-merge(year.master.form,index_files_id_df,by = c("CIK","FORM_TYPE","DATE_FILED"),all.x = T)
  year.master.form.link$SUFFIX<-as.character(year.master.form.link$SUFFIX)
  
  
  year.master.form.link$PREFIX<-as.character(substr(year.master.form.link$INDEX_LINK,1,nchar(year.master.form.link$INDEX_LINK)-10))
  year.master.form.link$PREFIX<-as.character(gsub("-","",year.master.form.link$PREFIX))
  year.master.form.link$FORM_LINK<-as.character(paste0(year.master.form.link$PREFIX,"/",year.master.form.link$SUFFIX))
  
  dir.create(paste0(directory_set,year,"_",form_type))
  file_dir<-paste0(directory_set,year,"_",form_type)
  
  file_success<-vector()
  for(i in 1:dim(year.master.form.link)[1]){
    file_success[i]<-DownloadFile(year.master.form.link[i,"FORM_LINK"],paste0(file_dir,"/",year.master.form.link[i,"CIK"],
                                                                              "_",year.master.form.link[i,"FORM_TYPE"],"_",
                                                                              year.master.form.link[i,"DATE_FILED"],".htm"))
  } # resulting 8333 files - surprise
  
  year.master.form.link<-data.frame(year.master.form.link,FILE_SUCCESS = file_success)
  
  save(year.master.form.link,file = paste0(directory_set,"year.master.form.link","_",year,"_",form_type,".RData"))
  write.csv(year.master.form.link, file = paste0(directory_set,"year.master.form.link","_",year,"_",form_type,".csv"), row.names = F)
  return('The Download Is Complete')
}
}

#edgar_file_download(2011,"10-K")

for(i in 2010:2010){
  edgar_file_download(i,"10-Q")
}

#edgar_file_download(2010,"10-K")

download("https://www.sec.gov/Archives/edgar/data/840886/000091431705001140/form10ksb-66774_fl.txt",destfile = "D:/FAILED_DOWNLOAD.htm")
#=============================================================================================================================
setwd("D:/")
getMasterIndex(2007)
getFilings(2011,cik.no = "ALL",form.type = "8-K")

# check this for 2010
https://www.sec.gov/Archives/edgar/data/1422221/0001144204-10-028326-index.htm

# 2005

https://www.sec.gov/Archives/edgar/data/840886/000091431705001140/form10ksb-66774_fl.txt

