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
load("data/psychopy_dataset.RData") 

# data blocco italiano
ITA <- dataset %>%
  group_by(participant, congruent) %>%
  summarise(
    sum_acc = sum(trial_ita_kb.corr, na.rm = TRUE),
    n = n(),
    mean_acc = (sum_acc / n) * 100,
    mean_rt = mean(trial_ita_kb.rt[trial_ita_kb.corr == 1], na.rm = TRUE)
  ) %>% drop_na(congruent) %>%
  mutate(stroop = "ita")


# data blocco inglese
ENG<-dataset %>%
  group_by(participant, congruent) %>%
  summarise(
    sum_acc = sum(trial_eng_kb.corr, na.rm = TRUE),
    n = n(),
    mean_acc = (sum_acc / n) * 100,
    mean_rt = mean(trial_eng_kb.rt[trial_eng_kb.corr == 1], na.rm = TRUE)
  ) %>% drop_na(congruent) %>%
  mutate(stroop = "eng")

# unico dataset intaliano inglese
data<- rbind(ITA,ENG)

# plots  ------------------------------------------------------------

# Reaction Time
data %>%
  mutate(
    congruent = factor(congruent, 
                       levels = c(0, 1), 
                       labels = c("Incongruent", "Congruent"))
  ) %>%
  ggplot(aes(x = congruent, y = mean_rt, fill = stroop)) +
  geom_bar(stat = "identity", position = position_dodge(width = 0.8)) +
  labs(
    x = "Condition",
    y = "Mean Reaction Time (s)",
    fill = "Language Block"
  ) +
  theme_minimal(base_size = 14) +
  theme(
    legend.position = "top",
    panel.grid.major.x = element_blank()
  )

# Accuracy
data %>%
  mutate(
    congruent = factor(
      congruent,
      levels = c(0, 1),
      labels = c("Incongruent", "Congruent")
    )
  ) %>%
  ggplot(aes(x = congruent, y = mean_acc, fill = stroop)) +
  geom_bar(stat = "identity", position = position_dodge(width = 0.8)) +
  labs(
    x = "Condition",
    y = "Mean Accuracy (%)",
    fill = "Language Block"
  ) +
  theme_minimal(base_size = 14) +
  theme(
    legend.position = "top",
    panel.grid.major.x = element_blank()
  )

#################################################
# 
# END
#
#################################################
