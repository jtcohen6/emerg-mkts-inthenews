## NEWS ANALYTICS ## FINANCIAL TIMES ##

## PennApps XIII, Jeremy & Raghav (& Gus)

rm(list=ls())

dir <- "C:\\Users\\jtcohen6\\Documents\\buckfitches\\news data"
setwd(dir)

ftimes21494 <- readLines("buckfitches\\sentiment_analysis\\news_data\\ftimes21494.txt") # dataset

n <- 21494 # number of articles

search_ftimes <- function(start,end) { ftimes21494[start:end] } # search function

art_end <- grep("Document FT|Document EP|Document AI",ftimes21494) # ending line
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

keywords <- function(string.vec) { for (i in 1:n) { keyword(string.vec[i]) } }

basic_data <- read.csv("buckfitches\\emerg_countries_basic_data.csv", stringsAsFactors = F)

View(ftimes.tbl)

ftimes_2006 <- read.csv("buckfitches\\sentiment_analysis\\news_data\\sentiment_output\\ftimes_sentiment.csv", stringsAsFactors = F)
ftimes_random <- read.csv("buckfitches\\sentiment_analysis\\news_data\\sentiment_output\\random_ftimes_sentiment.csv", stringsAsFactors = F)
basic_data <- read.csv("buckfitches\\emerg_countries_basic_data.csv", stringsAsFactors = F)

# re-add dates
dates_2006 <- ftimes.tbl[ftimes_2006$ART_NUM,"DATE"]
ftimes_2006$DATE <- dates_2006

# initialize new operation
findings.100 <- rep(0,times=100) # alternative temp vector

# do keyword for said operation
keyword_2006 <- function(string) {
  for (i in 1:100) { findings.100[i] <- sum(grepl(string, ftimes_art(i))) }
  new.col <- ncol(ftimes_2006)+1
  ftimes_2006[,new.col] <<- findings.100
  names(ftimes_2006)[new.col] <<- string
  str(ftimes_2006) }

for (i in 1:length(basic_data$Name)) { keyword_2006(basic_data$Name[i]) }

## SAME basic principle, for random vector (instead of 2006 one)

# re-add dates
dates_random <- ftimes.tbl[ftimes_random$ART_NUM,"DATE"]
ftimes_random$DATE <- dates_random

# do keyword for said operation
keyword_random <- function(string) {
  for (i in 1:100) { findings.100[i] <- sum(grepl(string, ftimes_art(i))) }
  new.col <- ncol(ftimes_random)+1
  ftimes_random[,new.col] <<- findings.100
  names(ftimes_random)[new.col] <<- string
  str(ftimes_random) }

for (i in 1:length(basic_data$Name)) { keyword_random(basic_data$Name[i]) }

str(ftimes_2006)
str(ftimes_random)

write.csv(ftimes_2006, "buckfitches\\sentiment_analysis\\news_data\\sentiment_output\\complete\\ftimes_2006_complete.csv")
write.csv(ftimes_random, "buckfitches\\sentiment_analysis\\news_data\\sentiment_output\\complete\\ftimes_random_complete.csv")

#ftimes.tbl <- ftimes.tbl.basic # reset as needed
