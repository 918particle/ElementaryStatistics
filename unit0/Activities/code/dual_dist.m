clear;
home;
close;
n = 1e4;
m = 1e2;
f1 = 0.6;
f2 = 0.4;
gpa_all_pop_1 = randn(n*f1,1)*0.25+3.0;
gpa_all_pop_2 = randn(n*f2,1)*0.25+2.0;
gpa_all = [gpa_all_pop_1; gpa_all_pop_2];
sample_indices = sort(floor(rand(m,1)*1e4));
gpa_sample = gpa_all(sample_indices);
csvwrite("gpa_data.csv",gpa_sample);
clear;
