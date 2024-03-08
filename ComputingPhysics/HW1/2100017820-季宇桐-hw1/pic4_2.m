%% 椭圆柱面
% 参数方程
a=2^0.5;
b=1.5^0.5;
theta=0:0.1:2*pi+0.1;
x=a*cos(theta);
y=b*sin(theta);
z=-2:0.5:2;
X=ones(length(z),1)*x;
Y=ones(length(z),1)*y;
Z=z'*ones(1,length(x));

figure
hold on
surf(X,Y,Z)
quiver3(0,0,0,1,0,0,1,"LineWidth",3.0,"ShowArrowHead","on")
quiver3(0,0,0,0,1,0,1,"LineWidth",3.0,"ShowArrowHead","on")
quiver3(0,0,0,0,0,1,1,"LineWidth",3.0,"ShowArrowHead","on")

alpha(0.5)
shading interp
line([0,0],[0,0],[2.5,-2.5],'linewidth',1);
line([0,0],[2.5,-2.5],[0,0],'linewidth',1);
line([2.5,-2.5],[0,0],[0,0],'linewidth',1)
axis on
axis equal
view(120,15)