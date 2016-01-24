## NEWS ANALYTICS ## FORBES ##

## PennApps XIII, Jeremy & Raghav (& Gus)

#rm(list=ls())

dir <- "C:\\Users\\jtcohen6\\Documents\\buckfitches\\news data"
setwd(dir)

forbes1220 <- readLines("buckfitches\\sentiment_analysis\\news_data\\forbes1220.ansi.txt") # dataset

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

keywords <- function(string.vec) { for (i in 1:n) { keyword(string.vec[i]) } }

View(forbes.tbl)

forbes_2006 <- read.csv("buckfitches\\sentiment_analysis\\news_data\\sentiment_output\\forbes_sentiment.csv", stringsAsFactors = F)
forbes_random <- read.csv("buckfitches\\sentiment_analysis\\news_data\\sentiment_output\\random_forbes_sentiment.csv", stringsAsFactors = F)
basic_data <- read.csv("buckfitches\\emerg_countries_basic_data.csv", stringsAsFactors = F)

# re-add dates
dates_2006 <- forbes.tbl[forbes_2006$ART_NUM,"DATE"]
forbes_2006$DATE <- dates_2006

# initialize new operation
findings.100 <- rep(0,times=100) # alternative temp vector

# do keyword for said operation
keyword_2006 <- function(string) {
  for (i in 1:100) { findings.100[i] <- sum(grepl(string, forbes_art(i))) }
  new.col <- ncol(forbes_2006)+1
  forbes_2006[,new.col] <<- findings.100
  names(forbes_2006)[new.col] <<- string
  str(forbes_2006) }

for (i in 1:length(basic_data$Name)) { keyword_2006(basic_data$Name[i]) }

## SAME basic principle, for random vector (instead of 2006 one)

# re-add dates
dates_random <- forbes.tbl[forbes_random$ART_NUM,"DATE"]
forbes_random$DATE <- dates_random

# do keyword for said operation
keyword_random <- function(string) {
  for (i in 1:100) { findings.100[i] <- sum(grepl(string, forbes_art(i))) }
  new.col <- ncol(forbes_random)+1
  forbes_random[,new.col] <<- findings.100
  names(forbes_random)[new.col] <<- string
  str(forbes_random) }

for (i in 1:length(basic_data$Name)) { keyword_random(basic_data$Name[i]) }

str(forbes_2006)
str(forbes_random)

write.csv(forbes_2006, "buckfitches\\sentiment_analysis\\news_data\\sentiment_output\\complete\\forbes_2006_complete.csv")
write.csv(forbes_random, "buckfitches\\sentiment_analysis\\news_data\\sentiment_output\\complete\\forbes_random_complete.csv")

# forbes.tbl <- forbes.tbl.basic # reset as needed
