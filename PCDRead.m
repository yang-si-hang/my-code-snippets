% In Matlab 2022a
% 读取 pcd 文件，并取出 xyz 坐标
ptcloud = pcread('cloud.pcd');
pos = ptcloud.Location;

% 读取pcd文件中的颜色量
color = ptcloudcolor;
red = bitshift(bitand(color, hex2dec('FF0000')), -16);
green = bitshift(bitand(color, hex2dec('00FF00')), -8);
blue = bitand(color, hex2dec('0000FF'));
rgb = [red, green, blue];

scatter3(pos(:,1), pos(:,2), pos(:,3), 50, double(rgb) / 255, 'filled');
