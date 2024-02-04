max_year = 10000;
% 1=lampery, 2=others
x1 = linspace(1,5,max_year);
y1 = sin(x1);
%plot(x1,y1);
rate1 = zeros(max_year);
rate2 = zeros(max_year);
disp(y1(1));
% for year = 1:max_year-1
%     rate1 = N1(year)/K1(year);
%     rate2 = N2(year)/K2(year);
% end
%float rate1=N1[year ]/K1[ year ]float rate2=N2[year ]/K2[year ]float rate_sex =Rf[year+1]-Rf[ year ]float rate=1-rate1-alpha *rate2 -rate seXN1[year +1]=N1[year ]+N1[year ]*r1[ year ]* rater1[year+1]=N1[year +1]/N1[ year ]