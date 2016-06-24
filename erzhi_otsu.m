
%二值化图像：大律算法
x = imread('1.jpg');
a = rgb2gray(x);
%[count s]=imhist(a);%获取灰度级及点数
[m,n] = size(a);
N = m*n;
L = 256;
count=zeros(256,1);%灰度级为0,1,2,...的点数
for i=1:L  
    count(i)=length(find(a==(i-1)));  
    f(i)=count(i)/N;  
end
s=(0:L-1)';
Total = sum(count.*s);%总灰度
for i=0:L-1
    c=0;
    total =0;
    for j=0:i
     total = total+count(j+1)*j;
     c = c +count(j+1);
    end
    
     w0 = c/N;
     w1 = 1-w0;
     miu0 = total/c;
     miu1 = (Total-total)/(N-c);
     g(i+1) = w0*w1*(miu0-miu1)^2;    
end
threhold = find(g>=max(g))-1%根据最大类间方差求最佳阈值

for i=1:m   
    for j=1:n   
        if a(i,j)>threhold  
            a(i,j)=0;   
        else   
            a(i,j)=255;   
        end   
    end   
end    
figure
imshow(a);  