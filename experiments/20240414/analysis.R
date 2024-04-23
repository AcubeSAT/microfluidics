# Load libraries
library(tidyverse)
library(ggplot2)
library(ggthemr)
library(viridis)

# Set paths
data_path <-
data_filename <-

# Set wd
setwd(data_path)

# Load data
data <- read.csv(file.path(data_path, file.path(data_filename, "csv", fsep = ".")), header = TRUE, stringsAsFactors = FALSE)

# Calculate statistics
data_summary <- function(data, varname, groupnames){
  require(plyr)
  summary_func <- function(x, col){
    c(mean = mean(x[[col]], na.rm = TRUE),
      sd = sd(x[[col]], na.rm = TRUE))
  }
  data_sum <- ddply(data, groupnames, .fun = summary_func,
                  varname)
  data_sum <- rename(data_sum, c("mean" = varname))
  return(data_sum)
}

# Factorize
data$Minutes <- factor(data$Minutes, levels = c("Before", "0", "45", "75", "120"))

# Plotting
ggthemr('fresh')

ggplot(data, aes(x = Minutes, y = Angle, group = Section)) +
    geom_point(size = 3) +
    geom_line() +
    facet_grid(~Section) +
    labs(x = "Date", y = "Contact angle (°)") +
    theme(
        strip.text = element_text(face = "bold", color = viridis(1, begin = 0.5, end = 0.9, option = "D")[1]),
        legend.position = "bottom",
        legend.text = element_text(size = 12),  
        legend.title = element_text(size = 14),
        axis.text.x = element_text(angle = 60, hjust = 1, size = 14),
        axis.text.y = element_text(size = 14),
        axis.title.x = element_text(size = 20),
        axis.title.y = element_text(size = 20),
        panel.border = element_rect(color = "black", fill=NA, size=1),
        strip.text.x = element_text(face = "bold", size = 16, margin = margin(2, 2, 2, 2), hjust = 0.5, color = "azure4"),
        strip.text.y = element_text(face = "bold", size = 16, margin = margin(2, 2, 2, 2), hjust = 0.5, angle = -90, color = "azure4"),
        strip.background = element_rect(fill = '#FFFFFF',)
    ) +
    scale_fill_viridis(discrete = TRUE) +
    scale_color_viridis(discrete = TRUE)

# ggsave("20240414_MITOMI_contact_angle.pdf", width = 12, height = 10)