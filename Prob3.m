clc;
clear all;
format longE;
syms x;
f = exp(0.5*x+2)+exp(-0.5*x-0.5)+4*x;
fx = matlabFunction(f);
df = diff(f);
disp( "Analytic Result")

dfx = matlabFunction(df);
dfx_5 = dfx(5);
disp(dfx_5);

x_h = 5;
h = [1e-3,1e-4,1e-5,1e-6];

for i = 1:1:length(h)
    df5(i) = (fx(x_h+h(i))-fx(x_h-h(i)))/2/h(i);
    diff(i) = dfx_5-df5(i);
end

disp("h");
disp(h);
disp("df x=5");
disp(df5);
disp("diff from analytical");
disp(diff);