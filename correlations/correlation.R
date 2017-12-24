library(lubridate);

cat('Loading data...\n');
data = read.csv('../data/samples/311_sample_3.csv');
# data = read.csv('../data/samples/311_sample_3.csv', nrows = 100000);


cat('Transforming data...\n');
data$Date = mdy_hms(data$Created.Date);


weeklyFrequenciesOf = function (substr){
	tempFrame = as.data.frame(table(week(data$Date[sapply(data$Complaint.Type, function (type){
		grepl(substr, type, ignore.case = TRUE)
	})])));
	freq = rep(0, 52);
	for(i in 1:length(tempFrame$Freq)){
		freq[as.numeric(levels(tempFrame$Var1[i])[tempFrame$Var1[i]])] = tempFrame$Freq[i];
	}
	freq
};
weeklyFrequencies = weeklyFrequenciesOf('');
weeklyProportionsOf = function (substr){
	freq = weeklyFrequenciesOf(substr);
	prop = rep(0, 52);
	for(i in 1:length(freq)){
		prop[i] = freq[i] / weeklyFrequencies[i];
	}
	prop
};


rodents = weeklyProportionsOf('Rodent');
noise = weeklyProportionsOf('Noise');
food = weeklyProportionsOf('Food');
parking = weeklyProportionsOf('Parking');
heat = weeklyProportionsOf('Heat');
derelict = weeklyProportionsOf('Derelict');
construction = weeklyProportionsOf('Construction');



cat('Creating plots...\n');

# png('frequency_by_yearday.png');
# plot(table(yday(data$Date)), type = 'l', xlab = 'Day of Year', ylab = 'Frequency', main = 'Frequency of Calls by Day of Year');

# png('frequency_by_weekday.png');
# plot(table(wday(data$Date)), type = 'l', xlab = 'Day of Week', ylab = 'Frequency', main = 'Frequency of Calls by Day of Week');

# png('frequency_by_month.png');
# plot(table(month(data$Date)), type = 'l', xlab = 'Day of Month', ylab = 'Frequency', main = 'Frequency of Calls by Month of Year');

# png('frequency_by_2_weeks.png');
# plot(table(week(data$Date) / 2), type = 'l', xlab = '2-Week Period of Year', ylab = 'Frequency', main = 'Frequency of Calls by 2-week Periods');

# png('frequency_by_week.png');
# plot(table(week(data$Date)), type = 'l', xlab = 'Week of Year', ylab = 'Frequency', main = 'Frequency of Calls by Week of Year');


# png('noise_v_rodents.png');
# plot(noise, rodents, xlab = 'Noise Complaints in a Week', ylab = 'Rodent Reports in a Week', type = 'p');
# model = lm(rodents ~ noise);
# summary(model);

# png('food_v_rodent.png');
# plot(food, rodents, xlab = 'Food-Related Calls in a Week', ylab = 'Rodent Reports in a Week', type = 'p');
# model = lm(rodents ~ food);
# summary(model);

# png('heating_v_parking.png')
# plot(heat, parking, xlab = 'Heating-Related Calls in a Week', ylab = 'Parking Violation Calls in a Week', type = 'p');
# model = lm(heat ~ parking);
# summary(model);


png('noise.png');
plot(noise, type = 'l');

png('parking.png');
plot(parking, type = 'l');

png('derelict.png');
plot(derelict, type = 'l');

png('construction.png');
plot(construction, type = 'l');

png('heating.png');
plot(heat, type = 'l');