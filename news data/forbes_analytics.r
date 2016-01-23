## NEWS ANALYTICS ## FORBES ##

## PennApps XIII, Jeremy & Raghav (& Gus)

rm(list=ls())

dir <- "C:\\Users\\jtcohen6\\Documents\\buckfitches\\news data"
setwd(dir)

forbes1220 <- readLines("forbes1220.ansi.txt") # dataset

n <- 1220 # number of articles

search_forbes <- function(start,end) { forbes1220[start:end] } # search function

art_end <- grep("Document FB|Document NA|Document FF",forbes1220) # ending line
art_start <- c(15,art_end[-n]+1) # starting line, based on ending line

forbes_art <- function(art_num) { search_forbes( art_start[art_num], art_end[art_num] ) }

## instantiate table, with article number (ID), starting line, ending line

forbes.tbl <- data.frame("ART_NUM"=c(1:n),"ART_START"=art_start[1:n],
                         "ART_END"=art_end[1:n],"WORDS"=0,"DATE"=0)

## get word count and date (next line) for each article and add to table

for (i in 1:n) {
  art <- forbes_art(i)
  WC_line <- grep("words$", art)
  forbes.tbl[i,"WORDS"] <- as.numeric(gsub("[^[:digit:]]","",art[WC_line]))
  date <- strsplit(gsub("PD \t","",art[WC_line + 1])," ")[[1]]
  forbes.tbl[i,"DATE"] <- as.Date(
    paste(grep(date[2],month.name),"/",date[1],"/",date[3],sep=""),"%m/%d/%y")
}

str(forbes.tbl) # check my work
forbes.tbl.basic <- forbes.tbl # backup basic table (just in case!)

## the search engine

findings <- rep(0,times=n) # initialize temp vector

keyword <- function(string) {
  for (i in 1:n) { findings[i] <- sum(grepl(string, forbes_art(i))) }
  new.col <- ncol(forbes.tbl)+1
  forbes.tbl[,new.col] <<- findings
  names(forbes.tbl)[new.col] <<- string
  str(forbes.tbl) }

View(forbes.tbl)

forbes.tbl <- forbes.tbl.basic # reset as needed

write.csv(forbes.tbl, "forbes.csv")
