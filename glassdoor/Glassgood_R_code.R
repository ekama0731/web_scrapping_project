library(ggplot2)
library(plotly)

Sys.setenv("plotly_username"="ekama0731")
Sys.setenv("plotly_api_key"="WgvibePNVAQAgzJAntMR")
glass = read.csv('/Users/emanuelkamali/Desktop/glassdoor/glassdoor_industry_clean.csv')

# Industry Count ####
industry_count = glass %>%
  group_by(industry) %>%
  summarise(count=n()) %>%
  filter(industry != '' & count>25)

#industry_Count = ggplot(industry_count, aes(x=reorder(industry, count), y=count, fill = count)) + 
 # geom_bar(stat = 'identity', colour = 'black') + 
  #geom_text(aes(label = industry_count$count, vjust=-.25)) +
  #theme(plot.subtitle = element_text(vjust = 1), plot.caption = element_text(vjust = 1), panel.grid.major = element_line(size = 1), panel.grid.minor = element_line(size = 1), 
   # axis.title = element_text(size = 13, face = "bold"), axis.text = element_text(size = 15), 
    #axis.text.x = element_text(size = 12, vjust = 0.5, angle = -90), axis.text.y = element_text(size = 15), 
    #plot.title = element_text(size = 19, face = "bold", hjust = 0.5), legend.text = element_text(face = "bold"), 
    #legend.title = element_text(size = 15, face = "bold"), panel.background = element_rect(fill = "white", size = 1), plot.background = element_rect(fill = "white", size = 1)) +
  #labs(title = "Number of Job Postings in each Industry", x = "Industry", y = "Count", fill = "Count")

industry_Count = plot_ly(industry_count, x=~reorder(industry,count),y=~count, color = ~industry, hoverinfo = 'text',
        text = ~paste('Industry: ', industry,
                      '<br> Count: ', count)) %>%
  layout(yaxis = list(title = 'Count'), xaxis = list(title = 'Industry'), title = 'Count per Industry', autosize = T , plot_ly(width = 1000), plot_ly(height = 400), 
         margin = list(l = 50, r = 75, b = 150, t = 50, pad = 1))
industry_Count

# Looking at salary vs industry ####
glass_industry_14 = glass %>%
  group_by(industry) %>%
  filter(industry != '' & n() >50)

industrySalaryEstimate <- plot_ly(glass_industry_14, x=~reorder(industry, salary_estimate), y = ~salary_estimate, color = ~industry, type = "box") %>%
  layout(yaxis = list(title = 'Salary'), xaxis = list(title = 'Industry'), title = 'Salary per Industry', autosize = T , plot_ly(width = 1000), plot_ly(height = 400), 
         margin = list(l = 50, r = 75, b = 150, t = 50, pad = 1))
industrySalaryEstimate
chart_link = api_create(industrySalaryEstimate, filename = "Industry Salary")

# Looking at rating vs industry ####
industry_rating = glass %>%
  group_by(industry) %>%
  summarise(rating = mean(rating), count=n()) %>%
  filter(industry != '' & count >50)

industry_Rating = plot_ly(industry_rating, x=~reorder(industry,rating), y=~rating, color = ~industry ,type = 'bar',hoverinfo = 'text',
                          text = ~paste('Industry: ', industry,
                                        '<br> Rating: ', rating)) %>%
  layout(xaxis = list(title = 'Industry'), yaxis = list(title = 'Average Rating'), title = 'Average Rating per Industry',
         margin = list(l = 50, r = 75, b = 150, t = 50, pad = 1))

industry_Rating
chart_link = api_create(industry_Rating, filename = "Industry Rating")



# Loo king at the number of job posting per city ####
city_count = glass %>%
  group_by(city)%>%
  summarise(count=n(), salary = mean(salary_estimate)) %>%
  filter(count>20)

city_Count=plot_ly(city_count, x = ~reorder(city,count), y = ~count, type = 'bar', color = ~city,hoverinfo = 'text',
                   text = ~paste('City: ', city,
                                 '<br> Count: ', count)) %>%
  layout(xaxis = list(title = 'Cities'), yaxis = list(title = 'Number of Job Postings'), title = 'Job Postings in Each City',
         margin = list(l = 50, r = 75, b = 150, t = 50, pad = 1))

city_Count
chart_link = api_create(city_Count, filename = "City Count")

# Looking at salary vs city ####
city_salary = plot_ly(city_count, x=~reorder(city,salary), y=~salary, color=~city, type = 'bar',hoverinfo = 'text',
                      text = ~paste('City: ', city,
                                    '<br> Salary: ', salary)) %>%
  layout(xaxis = list(title = 'Cities'), yaxis = list(title = 'Average Salary'), title = 'Average Salary in Each City',
         margin = list(l = 50, r = 75, b = 150, t = 50, pad = 1))

city_salary
chart_link = api_create(city_salary, filename = "City salary")



# Looking at the number of job posting per state ####

State_count = glass %>%
  group_by(state)%>%
  summarise(count=n()) %>%
  filter(count>20)

State_Count=plot_ly(State_count, x = ~reorder(state,count), y = ~count, type = 'bar', color = ~state,hoverinfo = 'text',
                   text = ~paste('State: ', state,
                                 '<br> Count: ', count)) %>%
  layout(xaxis = list(title = 'States'), yaxis = list(title = 'Number of Job Postings'), title = 'Job Postings in Each State',
         margin = list(l = 50, r = 75, b = 150, t = 50, pad = 1))

State_Count
chart_link = api_create(city_Count, filename = "State Count")

#state_count = glass %>%
 # group_by(state) %>%
  #summarise(count = n()) %>%
  #filter(count>2)

#state_Count = ggplot(state_count, aes(x= reorder(state, count),y= count, fill=count)) +
 # geom_bar(stat='identity', colour = 'black')+
  #geom_text(aes(label=count, vjust=-.25)) + 
  #theme(plot.subtitle = element_text(size = 15, hjust = 0.5, vjust = 1), 
   #     plot.caption = element_text(vjust = 1),
     #   axis.text.x = element_text(size = 12, vjust = 0.5, angle = -90),
    #    axis.title = element_text(size = 15, face = "bold"), axis.text = element_text(face = "bold"), 
      #  plot.title = element_text(size = 19, face = "bold", hjust = 0.5), legend.title = element_text(size = 15, face = "bold"), panel.background = element_rect(fill = "white"), 
       # plot.background = element_rect(fill = "white")) +
  #labs(title = "Job posting in each state", x = "State", y = "Count", fill = "Count", subtitle = "Last 30 days")

#state_Count
# looking at the average price salary per state ####
state_salary = plot_ly(glass,x =~reorder(state, salary_estimate), y=~salary_estimate, color=~state, type='box') %>%
  layout(xaxis = list(title = 'State'), yaxis = list(title='Salary'), title = 'Salary Per State')
state_salary
chart_link = api_create(state_salary, filename = "Salary Per State")


# Looking at state vs rating ####
state_vs_rating = glass %>%
  group_by(state)

state_vs_Rating = plot_ly(state_vs_rating, x=~reorder(state,rating), y=~ rating, color = ~state, sort = FALSE,type = 'box') %>%
  layout(xaxis = list(title='State', size = 20), yaxis = list(title = 'Rating', size = 20 ), title = 'Rating Per State', size= 30)

state_vs_Rating
chart_link = api_create(state_vs_Rating, filename = "Difference-state-ratings")


# Looking at texas with the most job postings ####

city_tex = glass %>%
  group_by(city) %>%
  filter(state == ' TX') %>%
  summarise( salary = mean(salary_estimate), count = n()) %>%
  filter(count>2)
city_Tex = plot_ly(city_tex, x = ~reorder(city,salary), y = ~count, type = 'bar', color = ~city,hoverinfo = 'text',
                   text = ~paste('City: ', city,
                                 '<br> Count: ', count,
                                 '<br> Salary Average: ', salary)) %>%
  layout(xaxis = list(title = 'Cities in Texas'), yaxis = list(title = 'Number of Job Postings'), title = 'Job Postings in Each City of Texas',
         margin = list(l = 50, r = 75, b = 150, t = 50, pad = 1))

city_Tex
chart_link = api_create(city_Tex, filename = "Job Postings in Texas")





# Looking at rating vs salary.  ####
fit <- lm(salary_estimate ~ rating, data = glass)
ratingSalaryEstimate = plot_ly(glass, x = ~rating, y= ~salary_estimate, color = ~salary_estimate,type = 'scatter',hoverinfo = 'text',
  text = ~paste('Rating: ', rating,
                '<br> Salary: ', salary_estimate)) %>%
  layout(xaxis = list(title = "Rating"), yaxis = list(title= "Salary"), title = "Salary based on Ratings", showlegend = F)%>%
  add_lines(x =~rating,y = fitted(fit)) 
ratingSalaryEstimate
chart_link = api_create(ratingSalaryEstiate, filename = "Salary based on Ratings")






