#################################################
# 
# Name:           data exploration
# Programmer:     Thomas Quettier
# Date:           21/10/2022
# Description:    check stroop data
#
#################################################

rm(list=ls()) # remove all objects

# Packages ----------------------------------------------------------------

library(tidyverse)
library(ggplot2)

# Functions ---------------------------------------------------------------

devtools::load_all()

# loading data ------------------------------------------------------------
dataset_concatenation("dataset")
load("data/dataset.RData") 

# data blocco italiano
ITA<-dataset%>%
  filter(resp.corr == 1)%>%
  group_by(participant)%>%
  summarise_at(vars(resp.corr,resp.rt), list(sum,mean))%>%
  select(participant, resp.corr_fn1,resp.rt_fn2)%>%
  'colnames<-'(c("Pt","Acc","mean.rt"))%>%
  mutate(Acc = (Acc/12)*100 ,
         blocco = "ITA")# 12 trials, acc in % 

# data blocco inglese
ENG<-dataset%>%
  filter(resp.corr == 1)%>%
  group_by(participant)%>%
  summarise_at(vars(resp.corr,resp.rt), list(sum,mean))%>%
  select(participant, resp.corr_fn1,resp.rt_fn2)%>%
  'colnames<-'(c("Pt","Acc","mean.rt"))%>%
  mutate(Acc = (Acc/12)*100  ,
         blocco = "ENG")# 12 trials, acc in % 

# unico dataset intaliano inglese
data<- rbind(ITA,ENG)

# plots  ------------------------------------------------------------

# Reaction Time
data%>%
  select(-Acc)%>%
  #group_by(blocco)%>%
  ggplot(aes(x=blocco, y=mean.rt, fill= blocco)) +
  geom_bar(  stat="identity", position = position_dodge(width = 0.9))

# Accuracy
data%>%
  select(-mean.rt)%>%
  group_by(blocco)%>%
  ggplot(aes(x=blocco, y=Acc, fill = blocco)) +
  geom_bar(  stat="identity", position = position_dodge(width = 0.9))

#################################################
# 
# END
#
#################################################
