function burningship

% ouput image resolution, WIDTHxHEIGHT
WIDTH = 1000; %number of points in x axis
HEIGHT = 1000; %number of points in y axis
% maximum number of iterations
MAX_ITERATION = 256;
% Burning ship fractal x y range
X_MIN = -5.7;
X_MAX = 10.1;
Y_MIN = -3.5;
Y_MAX = 7.4;
%Generate linearly spaced points from X_MIN to X_MAX
x = linspace(X_MIN, X_MAX, WIDTH);
%Generate linearly spaced points from Y_MIN to Y_MAX
y = linspace(Y_MIN, Y_MAX, HEIGHT);
% Create a linear 2d grid
% X is 2d a array, column value are varying and row values are constant
% Y is 2d a array, row value are varying and column values are constant
[X Y] = meshgrid(x,y);
% Allocate space for output
zval = zeros(HEIGHT, WIDTH);
nPoints = WIDTH * HEIGHT;
xnew = 0;
ynew = 0;
a = 0;
b = 0;
xn = 0;
yn = 0;
h_msg = msgbox('Please  wait...','');
tic %start timer
for n = 1:nPoints
    a = X(n);
    b = Y(n);
    xn = 0;
    yn = 0;
    k  = 1;
    while (k < MAX_ITERATION) && ((xn^2+yn^2) < 4)
        xnew = xn^2 - yn^2 + a;
        ynew = 2*abs(xn*yn)+ b;
        xn = xnew;
        yn = ynew;
        k = k+1;
    end
    zval(n) = k;
end
toc %stop timer
close(h_msg);
cmap = fliplr(flipud(colormap(bone(MAX_ITERATION))));
colormap(cmap);
image(zval);
axis equal
box on
axis([0 WIDTH 0 HEIGHT]);
imwrite(zval, cmap , 'burningShip.png','png');
end