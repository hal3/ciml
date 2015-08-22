D = load('2vs3.tr');
IM = ones(290,290);
for xx=1:10,
  for yy=1:10,
    x = (xx-1)*29 + 1;
    y = (yy-1)*29 + 1;
    n = (xx-1)*10 + yy;
    thisIM = reshape( D(n,2:end),28,28 )';
    IM(x:(x+27),y:(y+27)) = thisIM/255;
  end;
end;
imshow(IM)
