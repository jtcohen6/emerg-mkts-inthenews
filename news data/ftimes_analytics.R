## NEWS ANALYTICS ## FINANCIAL TIMES ##

## PennApps XIII, Jeremy & Raghav (& Gus)

rm(list=ls())

dir <- "C:\\Users\\jtcohen6\\Documents\\buckfitches\\news data"
setwd(dir)

ftimes20189 <- readLines("ftimes20189.txt") # dataset

n <- 21494 # number of articles

search_ftimes <- function(start,end) { ftimes20189[start:end] } # search function

art_end <- grep("Document FT|Document EP|Document AI",ftimes20189) # ending line
art_start <- c(15,art_end[-n]+1) # starting line, based on ending line

ftimes_art <- function(art_num) { search_ftimes( art_start[art_num], art_end[art_num] ) }

## instantiate table, with article number (ID), starting line, ending line

ftimes.tbl <- data.frame("ART_NUM"=c(1:n),"ART_START"=art_start[1:n],
                         "ART_END"=art_end[1:n],"WORDS"=0,"DATE"=0)

## get word count and date (next line) for each article and add to table

for (i in 1:n) {
  art <- ftimes_art(i)
  WC_line <- grep("^WC \t", art)
  ftimes.tbl[i,"WORDS"] <- as.numeric(gsub("[^[:digit:]]","",art[WC_line]))
  date <- strsplit(gsub("PD \t","",art[WC_line + 1])," ")[[1]]
  ftimes.tbl[i,"DATE"] <- as.Date(
    paste(grep(date[2],month.name),"/",date[1],"/",date[3],sep=""),"%m/%d/%y")
}

str(ftimes.tbl) # check my work
ftimes.tbl.basic <- ftimes.tbl # backup basic table (just in case!)

## the search engine

findings <- rep(0,times=n) # initialize temp vector

keyword <- function(string) {
  for (i in 1:n) { findings[i] <- sum(grepl(string, ftimes_art(i))) }
  new.col <- ncol(ftimes.tbl)+1
  ftimes.tbl[,new.col] <<- findings
  names(ftimes.tbl)[new.col] <<- string
  str(ftimes.tbl) }

View(ftimes.tbl)

keyword("Russia")
keyword("China")
keyword("South Korea")
keyword("oil")
keyword("Middle East")
keyword("Bangladesh")

ftimes.tbl <- ftimes.tbl.basic # reset as needed

y <- ftimes.tbl$Russia/sqrt(ftimes.tbl$WORDS)
