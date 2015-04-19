close all;clear all;clc;
load hw5db1.txt;
htsdata = hw5db1;
actdata(1:1347,1:16)=htsdata(1:1347,4:19);
nondata(1:42000,1:16)=htsdata(1348:43347,4:19);
active_mean = mean(actdata(:,1:16));
non_active_mean = mean(nondata(:,1:16));


for i = 1:1347
    dAN(i,1)=sqrt(sum((actdata(i,:)-active_mean(:)').^2));
    dAN(i,2)=sqrt(sum((actdata(i,:)-non_active_mean(:)').^2));
    dANM(i,1)=sqrt(sum(((actdata(i,:)-active_mean(:)')/std(actdata(:,1:16))).^2));
    dANM(i,2)=sqrt(sum(((actdata(i,:)-non_active_mean(:)')/std(actdata(:,1:16))).^2));
end
for  i = 1:1347
    if dAN(i,1)<dAN(i,2)
        act_nonact(i) = 'A';
    else
        act_nonact(i) = 'N';
    end
        if dAN(i,1)<dAN(i,2)
        maha_act_nonact(i) = 'A';
    else
        maha_act_nonact(i) = 'N';
    end
end
        